#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import CMAPIObject

def main():
    localNode = dict(
            server_ip=dict(type='str', required=True),
            server_private_ip=dict(type='str', required=True),
            server_port=dict(type='int', required=True),
            user=dict(type='str', required=True),
            password=dict(type='str', required=True),
            verify=dict(type='bool', required=True),
        )
    module = AnsibleModule(
            argument_spec=dict(
                portNumber=dict(type='int', required = True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    portNumber = module.params.get('portNumber');

    result = dict(
        changed=False,
    )

    caId = ''

    # Get Local CA ID
    # https://$kms/api/v1/ca/local-cas?subject=/C=US/ST=TX/L=Austin/O=Thales/CN=CipherTrust Root CA
    cmSessionObject_get_ca_id = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="ca/local-cas",
            verify=False,
        )

    try:
      getUserResponse = requests.get(cmSessionObject_get_ca_id["url"] + "?subject=/C=US/ST=TX/L=Austin/O=Thales/CN=CipherTrust Root CA", 
              headers=cmSessionObject_get_ca_id["headers"], 
              verify=False)
      caId = getUserResponse.json()["resources"][0]["uri"]
    except requests.exceptions.RequestException as err:
      result['getCAQueryFailed'] = True
      result['getCAQueryError'] = err

    #Create NAE Interface
    requestObj = dict(
            cert_user_field='CN',
            mode='tls-cert-pw-opt',
            auto_gen_ca_id=caId,
            port=portNumber,
            network_interface='all',
            trusted_cas=dict(
                external=[],
                local=[caId],
            ),
        )

    cmSessionObject_create_interface = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="configs/interfaces",
            verify=False,
        )

    payload_json = json.dumps(requestObj)
    try:
      response = requests.post(cmSessionObject_create_interface["url"], 
              headers=cmSessionObject_create_interface["headers"], 
              json = json.loads(payload_json), 
              verify=False)
      if "codeDesc" in response.json():
          codeDesc=response.json()["codeDesc"]
          if 'NCERRConflict' in codeDesc:
              result['message'] = 'NAE interface already exists, ignoring task'
      else:
          result['success'] = 'NAE interface creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
