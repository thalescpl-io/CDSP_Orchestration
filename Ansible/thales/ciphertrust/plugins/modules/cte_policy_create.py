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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import create_policy

DOCUMENTATION = '''
---
module: cte_policy_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create policy for CTE API
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
        description: Name of the policy.
        required: true
        type: str
    policy_type:
        description: Type of the policy.
        required: true
        type: str
        choices:
            - Standard
            - LDT
            - IDT
            - Cloud_Object_Storage
            - CSI
    policyDescription:
        description: Description of the policy.
        required: false
        type: str
    data_transform_rules:
        description: Data transformation rules to link with the policy.
        required: false
        type: list
        default: null
    idt_key_rules:
        description: IDT rules to link with the policy.
        required: false
        type: list
        default: null
    key_rules:
        description: Key rules to link with the policy.
        required: false
        type: list
        default: null
    ldt_key_rules:
        description: LDT rules to link with the policy. Supported for LDT policies.
        required: false
        type: list
        default: null
    metadata:
        description: Restrict policy for modification
        required: false
        type: dict
        default: null
    never_deny:
        description: Whether to always allow operations in the policy. By default, it is disabled, that is, operations are not allowed. Supported for Standard, LDT, and Cloud_Object_Storage policies. For Learn Mode activations, never_deny is set to true, by default.
        required: false
        type: bool
        default: true
    security_rules:
        description: Security rules to link with the policy.
        required: false
        type: list
        default: null
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_policy_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "Ansible CSI Storage Group"
'''

RETURN = '''

'''

def main():
    data_transform_rule = dict(
        key_id=dict(type='str', required=False),
        key_type=dict(type='str', options=['name', 'id', 'slug', 'alias', 'uri', 'uuid', 'muid', 'key_id'], required=False),
        resource_set_id=dict(type='str', required=False)
    )
    idt_key_rule = dict(
        current_key=dict(type='str', required=False),
        current_key_type=dict(type='str', options=['name', 'id', 'slug', 'alias', 'uri', 'uuid', 'muid', 'key_id'], required=False),
        transformation_key=dict(type='str', required=False),
        transformation_key_type=dict(type='str', options=['name', 'id', 'slug', 'alias', 'uri', 'uuid', 'muid', 'key_id'], required=False)
    )
    key_rule = dict(
        key_id=dict(type='str', required=False),
        key_type=dict(type='str', options=['name', 'id', 'slug', 'alias', 'uri', 'uuid', 'muid', 'key_id'], required=False),
        resource_set_id=dict(type='str', required=False)
    )
    key = dict (
        key_id=dict(type='str', required=False),
        key_type=dict(type='str', options=['name', 'id', 'slug', 'alias', 'uri', 'uuid', 'muid', 'key_id'], required=False)
    )
    ldt_key_rule = dict(
        current_key=dict(type='dict', options=key, required=False),
        is_exclusion_rule=dict(type='bool', required=False),
        resource_set_id=dict(type='str', required=False),
        transformation_key=dict(type='dict', options=key, required=False)
    )
    metadata=dict(
        restrict_update=dict(type='bool', required=False)
    )
    security_rule = dict(
        action=dict(type='str', options=['read', 'write', 'all_ops', 'key_op'], required=False),
        effect=dict(type='str', options=['permit', 'deny', 'audit', 'applykey'], required=False),
        exclude_process_set=dict(type='bool', required=False),
        exclude_resource_set=dict(type='bool', required=False),
        exclude_user_set=dict(type='bool', required=False),
        partial_match=dict(type='bool', required=False),
        process_set_id=dict(type='str', required=False),
        resource_set_id=dict(type='str', required=False),
        user_set_id=dict(type='str', required=False)
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
                localNode=dict(type='dict', options=localNode, required=True),
                name=dict(type='str', required=True),
                policy_type=dict(type='str', options=['Standard', 'LDT', 'IDT', 'Cloud_Object_Storage', 'CSI'], required=True),
                policyDescription=dict(type='str', required=False),
                data_transform_rules=dict(type='list', element='dict', options=data_transform_rule, required=False),
                idt_key_rules=dict(type='list', element='dict', options=idt_key_rule, required=False),
                key_rules=dict(type='list', element='dict', options=key_rule, required=False),
                ldt_key_rules=dict(type='list', element='dict', options=ldt_key_rule, required=False),
                metadata=dict(type='dict', options=metadata, required=False),
                never_deny=dict(type='bool', required=False),
                security_rules=dict(type='list', element='dict', options=security_rule, required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    policy_type =  module.params.get('policy_type');
    policyDescription =  module.params.get('policyDescription');
    data_transform_rules =  module.params.get('data_transform_rules');
    idt_key_rules =  module.params.get('idt_key_rules');
    key_rules =  module.params.get('key_rules');
    ldt_key_rules =  module.params.get('ldt_key_rules');
    metadata =  module.params.get('metadata');
    never_deny =  module.params.get('never_deny');
    security_rules =  module.params.get('security_rules');

    result = dict(
        changed=False,
    )

    response = create_policy(
            node=localNode,
            name=name,
            policyDescription=policyDescription,
            policy_type=policy_type,
            data_transform_rules=data_transform_rules,
            idt_key_rules=idt_key_rules,
            key_rules=key_rules,
            ldt_key_rules=ldt_key_rules,
            metadata=metadata,
            never_deny=never_deny,
            security_rules=security_rules
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()