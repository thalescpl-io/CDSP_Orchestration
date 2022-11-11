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
    usersetObj = dict(
            name=dict(type='str', required=True),
            users=dict(type='list', elements='str', required=True),
        )
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
                usersets=dict(type='list', elements='dict', options=usersetObj, required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    usersets =  module.params.get('usersets');

    result = dict(
        changed=False,
    )

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/user-sets",
            verify=False,
        )

    for userset in usersets:
        name = userset.get("name")
        users = userset.get("users")

        requestObj = {}
        requestObj['name'] = name
        requestObj['description'] = 'Userset created by Ansible ' + name
        requestObj['users'] = users

        payload_json = json.dumps(requestObj)
        try:
          response = requests.post(cmSessionObject["url"], 
                  headers=cmSessionObject["headers"], 
                  json = json.loads(payload_json), 
                  verify=False)
          result['resp'] = response.json()
          result['success'] = 'Usersets creation successfull!'
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
