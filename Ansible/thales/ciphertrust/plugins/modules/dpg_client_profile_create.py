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
                name=dict(type='str', required=True),
                nae_iface_port=dict(type='int', required=True),
                policy_id=dict(type='str', required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    name = module.params.get('name');
    nae_iface_port = module.params.get('nae_iface_port');
    policy_id = module.params.get('policy_id');
    localNode = module.params.get('localNode');

    result = dict(
        changed=False,
    )
    

    #####GET CA ID First#####
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
      result['caId'] = caId
    except requests.exceptions.RequestException as err:
      result['getCAQueryFailed'] = True
      result['getCAQueryError'] = err

    #####Now create DPG policy#####
    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/client-profiles",
            verify=False,
        )

    requestObj=dict(
        )

    requestObj['name'] = name
    requestObj['nae_iface_port'] = nae_iface_port
    requestObj['app_connector_type'] = "DPG"
    requestObj['policy_id'] = policy_id
    requestObj['lifetime'] = "30d"
    requestObj['cert_duration'] = 730 
    requestObj['max_clients'] = 200
    requestObj['ca_id'] = caId
    requestObj['csr_parameters'] = dict(
            csr_cn='admin',
            csr_country='',
            csr_state='',
            csr_city='',
            csr_org_name='',
            csr_org_unit='',
            csr_email='',
        )
    requestObj['configurations'] = dict(
            verify_ssl_certificate=False,
            use_persistent_connections=True,
            log_level="DEBUG",
            tls_to_appserver=dict(
                tls_skip_verify=True,
                tls_enabled=True,
            ),
            auth_method_used=dict(
                scheme_name="Basic",
            ),
        )


    payload_json = json.dumps(requestObj)
    result['payload'] = payload_json
    try:
      response = requests.post(cmSessionObject["url"], 
              headers=cmSessionObject["headers"], 
              json = json.loads(payload_json), 
              verify=False)
      result['resp'] = response.json()
      result['success'] = 'DPG policy creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
