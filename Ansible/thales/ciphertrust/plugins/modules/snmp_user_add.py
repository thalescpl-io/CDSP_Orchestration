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
from ansible_collections.thales.ciphertrust.plugins.module_utils.snmp import addUser

DOCUMENTATION = '''
---
module: snmp_user_add
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with SNMP APIs
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
        description: Name of the user. It is also called as security name. Max 32.
        required: true
        type: str
    security_level:
        description: Security level. Valid values are noAuthNoPriv, authNoPriv and authPriv.
        required: true
        type: str
        choices:
            - noAuthNoPriv
            - authNoPriv
            - authPriv
    auth_password:
        description: Authentication password. Required with authentication protocol. Size must be 8 - 32
        required: false
        type: str
    auth_protocol:
        description: Authentication protocol. MD5, SHA, SHA-224, SHA-256, SHA-384, SHA-512 are supported. Required for authNoPriv and authPriv security levels.
        required: false
        type: str
        choices:
            - MD5
            - SHA
            - SHA-224
            - SHA-256
            - SHA-384
            - SHA-512
    engine_id:
        description: Engine ID of the notification receiver for inform and it is optional. It will be discovered for inform if not set.
        required: false
        type: str
    mib_accesses:
        description: Access to MIB object groups 'standard', 'enterprise', or both. Default is 'standard' only.
        required: false
        type: list
        element: str
    priv_password:
        description: Privacy password. Required with privacy protcol. Size must be 8 - 32.
        required: false
        type: str
    priv_protocol:
        description: Privacy protocol. DES, AES, AES-192, AES-192-C, AES-256, AES-256-C are supported. Algorithms AES, AES-192 and AES-256 use the Blumenthal Internet-Draft. Algorithms AES-192-C and AES-256-C (Cisco) use the key localization procedure for 3DES (Reeder Internet-Draft).
        required: false
        type: str
        choices:
            - DES
            - AES
            - AES-192
            - AES-192-C
            - AES-256
            - AES-256-C
    read_write:
        description: Read-write or read-only access to the MIB objects. Default is read-only.
        required: false
        type: str
'''

EXAMPLES = '''
- name: "Create SNMP User"
  thales.ciphertrust.snmp_user_add:
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
                security_level=dict(type='str', options=['noAuthNoPriv', 'authNoPriv', 'authPriv'], required=True),
                auth_password=dict(type='str', required=False),
                auth_protocol=dict(type='str', options=['MD5', 'SHA', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512'], required=False),
                engine_id=dict(type='str', required=False),
                mib_accesses=dict(type='list', element='str', required=False, default=[]),
                priv_password=dict(type='str', required=False),
                priv_protocol=dict(type='str', options=['DES', 'AES', 'AES-192', 'AES-192-C', 'AES-256', 'AES-256-C'] required=False),
                read_write=dict(type='bool', required=False, default=False),
            ),
        )

    localNode = module.params.get('localNode');
    name = module.params.get('name');
    mib_accesses = module.params.get('mib_accesses');
    read_write = module.params.get('read_write');
    security_level = module.params.get('security_level');
    auth_password = module.params.get('auth_password');
    auth_protocol = module.params.get('auth_protocol');
    engine_id = module.params.get('engine_id');
    priv_password = module.params.get('priv_password');
    priv_protocol = module.params.get('priv_protocol');

    result = dict(
        changed=False,
    )

    response = addUser(
        node=localNode,
        name=name,
        mib_accesses=mib_accesses,
        read_write=read_write,
        security_level=security_level,
        auth_password=auth_password,
        auth_protocol=auth_protocol,
        engine_id=engine_id,
        priv_password=priv_password,
        priv_protocol=priv_protocol
    )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()