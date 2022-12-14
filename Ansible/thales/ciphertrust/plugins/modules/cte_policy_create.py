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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import create_client

DOCUMENTATION = '''
---
module: cte_client_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create client for CTE API
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
        description: Name to uniquely identify the client. This name will be visible on the CipherTrust Manager.
        required: true
        type: str
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_client_create:
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
                data_transform_rules=dict(type='list')
                clientDescription=dict(type='str', required=False),
                client_locked=dict(type='bool', required=False),
                communication_enabled=dict(type='bool', required=False),
                password=dict(type='str', required=False),
                
                profile_identifier=dict(type='str', required=False),
                registration_allowed=dict(type='bool', required=False),
                system_locked=dict(type='bool', required=False)
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    

    result = dict(
        changed=False,
    )

    response = create_client(
            node=localNode,
            name=name,
            clientDescription=clientDescription,
            client_locked=client_locked,
            communication_enabled=communication_enabled,
            password=password,
            password_creation_method=password_creation_method,
            profile_identifier=profile_identifier,
            registration_allowed=registration_allowed,
            system_locked=system_locked
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
