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
    client_locked:
        description: Whether the CTE client is locked. The default value is false. Enable this option to lock the configuration of the CTE Agent on the client. Set to true to lock the configuration, set to false to unlock. Locking the Agent configuration prevents updates to any policies on the client.
        required: false
        type: bool
        default: null
    communication_enabled:
        description: Whether communication with the client is enabled. The default value is false. Can be set to true only if registration_allowed is true.
        required: false
        type: bool
        default: null
    clientDescription:
        description: Description to identify the client.
        required: false
        type: str
        default: null
    password:
        description: Password for the client. Required when password_creation_method is MANUAL.
        required: false
        type: str
        default: null
    password_creation_method:
        description: Password creation method for the client. Valid values are MANUAL and GENERATE. The default value is GENERATE.
        choices:
          - MANUAL
          - GENERATE
        required: false
        type: str
        default: null
    profile_identifier:
        description: Identifier of the Client Profile to be associated with the client. If not provided, the default profile will be linked.
        required: false
        type: str
        default: null
    registration_allowed:
        description: Whether client's registration with the CipherTrust Manager is allowed. The default value is false. Set to true to allow registration.
        required: false
        type: bool
        default: null
    system_locked:
        description: Whether the system is locked. The default value is false. Enable this option to lock the important operating system files of the client. When enabled, patches to the operating system of the client will fail due to the protection of these files.
        required: false
        type: bool
        default: null
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
                clientDescription=dict(type='str', required=False),
                client_locked=dict(type='bool', required=False),
                communication_enabled=dict(type='bool', required=False),
                password=dict(type='str', required=False),
                password_creation_method=dict(type='str', options=['MANUAL', 'GENERATE'], required=False),
                profile_identifier=dict(type='str', required=False),
                registration_allowed=dict(type='bool', required=False),
                system_locked=dict(type='bool', required=False)
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    clientDescription = module.params.get('clientDescription');
    client_locked = module.params.get('client_locked');
    communication_enabled = module.params.get('communication_enabled');
    password = module.params.get('password');
    password_creation_method = module.params.get('password_creation_method');
    profile_identifier = module.params.get('profile_identifier');
    registration_allowed = module.params.get('registration_allowed');
    system_locked = module.params.get('system_locked');

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
