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
                keyName=dict(type='str', required=True),
                usageMask=dict(type=int, required=False),
                keyAlgo=dict(type='str', required=False),
                keySize=dict(type=int, required=False),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    keyName = module.params.get('keyName');
    usageMask = module.params.get('usageMask');
    keyAlgo = module.params.get('keyAlgo');
    keySize = module.params.get('keySize');
    localNode = module.params.get('localNode');

    result = dict(
        changed=False,
    )

    #Validating playbook inputs
    if keyName is None:
        module.fail_json(msg='Key Name is mandatory parameter in create new key task')
    if localNode is None:
        module.fail_json(msg='Ciphertrust Manager connection details are not optional')
    #Set default values if missing
    if usageMask is None:
        usageMask = 3145740
    if keyAlgo is None:
        keyAlgo = 'aes'
    if keySize is None:
        keySize = 256

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    cmSessionObject_user = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="auth/self/user",
            verify=False,
        )

    cmSessionObject_key = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="vault/keys2",
            verify=False,
        )

    #Make CM API call to get the user ID for this user
    userId = ''
    try:
      getUserResponse = requests.get(cmSessionObject_user["url"], headers=cmSessionObject_user["headers"], verify=False)
      result['response'] = getUserResponse.json()
      #userId = getUserResponse.json()["user_id"]
    except requests.exceptions.RequestException as err:
      result['getUserQueryFailed'] = True
      result['getUserQueryError'] = err

    metaObj = dict(
            ownerId=userId,
            versionedKey=True,
        )

    requestObj = dict(
            name=keyName,
            usageMask=usageMask,
            algorithm=keyAlgo,
            size=keySize,
            unexportable=False,
            undeletable=False,
            meta=metaObj
        )

    keyRequestPayload = json.dumps(requestObj)

    try:
      response = requests.post(cmSessionObject_key["url"], headers=cmSessionObject_key["headers"], json = json.loads(keyRequestPayload), verify=False)
      result['success'] = 'Key creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
