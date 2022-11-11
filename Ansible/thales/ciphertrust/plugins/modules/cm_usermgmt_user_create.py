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
    userObj = dict(
            username=dict(type='str', required=True),
            password=dict(type='str', required=True),
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
                users=dict(type='list', elements='dict', options=userObj, required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    users =  module.params.get('users');

    result = dict(
        changed=False,
    )

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="usermgmt/users",
            verify=False,
        )

    for user in users:
        username = user.get("username")
        password = user.get("password")

        requestObj = {}
        requestObj['email'] = username + '@local'
        requestObj['name'] = username
        requestObj['username'] = username
        requestObj['password'] = password
        requestObj['app_metadata'] = dict()
        requestObj['user_metadata'] = dict()

        payload_json = json.dumps(requestObj)
        try:
          response = requests.post(cmSessionObject["url"], 
                  headers=cmSessionObject["headers"], 
                  json = json.loads(payload_json), 
                  verify=False)
          result['resp'] = response.json()
          result['success'] = 'User creation successfull!'
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
