#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2022 Thales Group. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_user_set

DOCUMENTATION = '''
---
module: dpg_user_sets_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create DPG Userset API
version_added: "1.0.0"
author: Anurag Jain, Developer Advocate Thales Group
options:
    localNode:
        description:
            - This is a dictionary type of object that contains CipherTrust Manager Instance FQDN and credentials
        required: true
        type: dict
        elements:
            - str
            - bool
    name:
        description: Unique name for the user set.
        required: true
        type: str
    usersetDescription:
        description: The description of user-set.
        required: false
        default: null
        type: str
    users:
        description: List of users to be added in user set.
        type: list
        element:
            - str
        required: false
        default: empty list
'''

EXAMPLES = '''
- name: "Create User Set"
  thales.ciphertrust.dpg_user_sets_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "userset-ansible"
    usersetDescription: "created by ansible"
    users:
        - "user1"
'''

RETURN = '''

'''

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

