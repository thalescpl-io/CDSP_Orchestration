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
                names=dict(type='list', element='str', required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    names =  module.params.get('names');

    result = dict(
        changed=False,
    )


    cmSessionObject = CMAPIObject(
        cm_api_user=localNode["user"],
        cm_api_pwd=localNode["password"],
        cm_url=localNode["server_ip"],
        cm_api_endpoint="configs/interfaces",
        verify=False,
    )

    for name in names:
        try:
            deleteResources = requests.delete(cmSessionObject["url"] + "/" + name,
                headers=cmSessionObject["headers"],
                verify=False)
        except requests.exceptions.RequestException as err:
            result['failed'] = True
            result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
