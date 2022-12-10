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
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_access_policy

DOCUMENTATION = '''
---
module: dpg_access_policy_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create DPG Access Policy API
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
        description: name of the DPG policy
        required: false
        type: str
        default: null
    user_set_policies:
        description: List of policies to be added to the access policy.
        required: false
        type: list
        default: empty
    default_error_replacement_value:
        description: Value to be revealed if the type is 'Error Replacement Value'.
        required: true, if default_reveal_type is 'Error Replacement Value
        type: str
        default: null
    default_masking_format_id:
        description: Masking format used to reveal if the type is 'Masked Value'.
        required: true, if default_reveal_type is 'Masked Value'
        type: str
        default: null
    default_reveal_type:
        description: Value using which data should be revealed.
        options:
            - Error Replacement Value
            - Masked Value
            - Ciphertext
            - Plaintext
        required: false
        type: str
        default: null
    access_policy_description:
        description: Description of the Access Policy
        required: false
        type: str
        default: null
'''

EXAMPLES = '''
- name: "Create DPG Access Policy"
  thales.ciphertrust.dpg_access_policy_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "ACCESS-POLICY"
    default_reveal_type: "Ciphertext"
    user_set_policies:
        - user_set_id: "USERSET-ID"
          reveal_type: "Plaintext"
        - user_set_id: "USERSET-ID"
          reveal_type: "Masked Value"
          masking_format_id: "MASKING-FORMAT-ID"
        - user_set_id: "USERSET-ID"
          reveal_type: "Ciphertext"
'''

RETURN = '''

'''

def main():
    user_set_policy = dict(
            user_set_id=dict(type='str', required=False, default=""),
            error_replacement_value=dict(type='str', required=False),
            reveal_type=dict(type='str', choices=['Error Replacement Value', 'Masked Value', 'Ciphertext', 'Plaintext'], required=False, default=""),
            masking_format_id=dict(type='str', required=False),
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
                user_set_policies=dict(type='list', elements='dict', options=user_set_policy, required=False, default=[]),
                default_error_replacement_value=dict(type='str', required=False, default=""),
                default_masking_format_id=dict(type='str', required=False, default=""),
                default_reveal_type=dict(type='str', choices=['Error Replacement Value', 'Masked Value', 'Ciphertext', 'Plaintext'], required=False, default=""),
                access_policy_description=dict(type='str', required=False, default=""),
                name=dict(type='str', required=False, default=""),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    default_reveal_type = module.params.get('default_reveal_type');
    default_error_replacement_value = module.params.get('default_error_replacement_value');
    user_set_policies = module.params.get('user_set_policies');
    default_masking_format_id = module.params.get('default_masking_format_id');
    access_policy_description = module.params.get('access_policy_description');

    policies=[]
    for policy in user_set_policies:
        userset_policy = dict()
        if policy['reveal_type'] == 'Ciphertext':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
        if policy['reveal_type'] == 'Masked Value':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
            userset_policy['masking_format_id'] = policy['masking_format_id'];
        if policy['reveal_type'] == 'Error Replacement Value':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
            userset_policy['error_replacement_value'] = policy['error_replacement_value'];
        if policy['reveal_type'] == 'Plaintext':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
        policies.append(userset_policy)

    result = dict(
        changed=False,
    )

    response = create_access_policy(
            node=localNode,
            name=name,
            default_reveal_type=default_reveal_type,
            default_error_replacement_value=default_error_replacement_value,
            user_set_policies=policies,
            default_masking_format_id=default_masking_format_id,
            access_policy_description=access_policy_description
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
