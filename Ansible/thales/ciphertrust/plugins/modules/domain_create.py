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
from ansible_collections.thales.ciphertrust.plugins.module_utils.domains import create

DOCUMENTATION = '''
---
module: domain_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create domain API
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
        description: Name of the domain.
        required: true
        type: str
    admins:
        description: List of administrators for the domain
        required: true
        type: list
        element: str
    allow_user_management:
        description: To allow user creation and management in the domain, set it to true. The default value is false.
        required: false
        type: str
    hsm_connection_id:
        description: The ID of the HSM connection. Required for HSM-anchored domains.
        required: false
        type: str
    hsm_kek_label:
        description: Optional name field for the domain KEK for an HSM-anchored domain. If not provided, a random UUID is assigned for KEK label.
        required: false
        type: str
    parent_ca_id:
        description: This optional parameter is the ID or URI of the parent domain's CA. This CA is used for signing the default CA of a newly created sub-domain. The oldest CA in the parent domain is used if this value is not supplied.
        required: false
        type: str
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.domain_create:
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
                admins=dict(type='list', element='str', required=True),
                allow_user_management=dict(type='bool', required=False, default=False),
                hsm_connection_id=dict(type='str', required=False),
                hsm_kek_label=dict(type='str', required=False),
                parent_ca_id=dict(type='str', required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');

    result = dict(
        changed=False,
    )

    response = create(
            node=localNode,
            name=name,
            admins=admins,
            allow_user_management=allow_user_management,
            hsm_connection_id=hsm_connection_id,
            hsm_kek_label=hsm_kek_label,
            parent_ca_id=parent_ca_id
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()