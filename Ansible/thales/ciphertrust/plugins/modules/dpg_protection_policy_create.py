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
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_protection_policy

DOCUMENTATION = '''
---
module: dpg_protection_policy_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create DPG Protection Policy API
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
        description: Unique name for the protection policy.
        required: true
        type: str
    algorithm:
        description: Algorithm to be used during crypto operations.
        required: true
        type: str
    key:
        description: Name of the key
        required: true
        type: str
    allow_single_char_input:
        description: If true, null or single-character inputs are passed untransformed. If false, row transformation fails.
        required: false
        type: bool
        default: False
    character_set_id:
        description: ID of the Characterset.
        required: false
        type: str
        default: null
    iv:
        description: IV to be used during crypto operations.
        required: false
        type: str
        default: null
    tweak:
        description: Tweak data to be used during crypto operations.
        required: false
        type: str
        default: null
    tweak_algorithm:
        description: Tweak algorithm to be used during crypto operations. 
        type: str
        required: false
        default: null
        options:
            - SHA1
            - SHA256
            - None
'''

EXAMPLES = '''
- name: "Create DPG Protection Policy"
  thales.ciphertrust.dpg_protection_policy_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "UNICODE-PROT-POLICY"
    key: "KEY-NAME"
    tweak: "1628462495815733"
    tweak_algorithm: "SHA1"
    algorithm: "FPE/FF1v2/UNICODE"
    character_set_id: "CHARACTER-SET-ID"
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
                algorithm=dict(type='str', required=True),
                key=dict(type='str', required=True),
                name=dict(type='str', required=True),
                allow_single_char_input=dict(type='bool', required=False, default=False),
                character_set_id=dict(type='str', required=False, default=""),
                iv=dict(type='str', required=False, default=""),
                tweak=dict(type='str', required=False, default=""),
                tweak_algorithm=dict(type='str', choices=['SHA1', 'SHA256', 'None'], required=False, default=""),
            ),
        )

    localNode = module.params.get('localNode');
    algorithm = module.params.get('algorithm');
    key = module.params.get('key');
    name = module.params.get('name');
    allow_single_char_input = module.params.get('allow_single_char_input');
    character_set_id = module.params.get('character_set_id');
    iv = module.params.get('iv');
    tweak = module.params.get('tweak');
    tweak_algorithm = module.params.get('tweak_algorithm');
    
    result = dict(
        changed=False,
    )

    response = create_protection_policy(
        node=localNode,
        algorithm=algorithm,
        key=key,
        name=name,
        allow_single_char_input=allow_single_char_input,
        character_set_id=character_set_id,
        iv=iv,
        tweak=tweak,
        tweak_algorithm=tweak_algorithm
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()

