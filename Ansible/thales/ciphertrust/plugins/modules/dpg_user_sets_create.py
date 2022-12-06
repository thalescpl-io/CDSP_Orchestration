#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_user_set

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
                name=dict(type='str', required=True),
                usersetDescription=dict(type='str', required=False, default=""),
                users=dict(type='list', element='str', required=False, default=[]),
            ),
        )

    localNode = module.params.get('localNode');
    name = module.params.get('name');
    usersetDescription = module.params.get('usersetDescription');
    users = module.params.get('users');
    
    result = dict(
        changed=False,
    )

    response = create_user_set(
        node=localNode,
        name=name,
        usersetDescription=usersetDescription,
        users=users
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()

