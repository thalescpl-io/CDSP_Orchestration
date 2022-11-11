#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

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
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    
    result = dict(
        changed=False,
    )

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="cluster/new",
            verify=False,
        )

    payload = {
        "localNodeHost":localNode["server_private_ip"],
        "localNodePort":localNode["server_port"],
        "publicAddress":localNode["server_ip"],
    }
    try:
      response = requests.post(cmSessionObject["url"], headers=cmSessionObject["headers"], json = payload, verify=False)
      result['success'] = 'Cluster creation success!'
    except:
      result['failed'] = True
      result['error'] = response.json()["message"]

    module.exit_json(**result)

if __name__ == '__main__':
    main()

