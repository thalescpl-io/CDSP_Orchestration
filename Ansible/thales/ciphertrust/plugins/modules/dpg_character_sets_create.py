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
                char_set_range=dict(type='list', elements='str', required=False),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    cs_name = module.params.get('name');
    cs_range = module.params.get('char_set_range');

    # Validation and default setting
    if cs_name is None:
        module.fail_json(msg='Character Set Name is a mandatory parameter!!!')
    if cs_range is None:
        cs_range = ['0030-0039','0041-005A','0061-007A']

    result = dict(
        changed=False,
    )

    #Create Character Set
    requestObj = {}
    requestObj['name'] = cs_name
    requestObj['range'] = cs_range
    requestObj['encoding'] = 'UTF-8'

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/character-sets",
            verify=False,
        )

    payload_json = json.dumps(requestObj)
    try:
      response = requests.post(cmSessionObject["url"], 
              headers=cmSessionObject["headers"], 
              json = json.loads(payload_json), 
              verify=False)
      result['charsetId'] = response.json()["id"]
      result['success'] = 'Character Set creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
