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
from ansible_collections.thales.ciphertrust.plugins.module_utils.snmp import addManagementStation

DOCUMENTATION = '''
---
module: snmp_management_station_add
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
    host:
        description: Hostname or IPAddress of the SNMP trap receiver.
        required: true
        type: str
    version:
        description: SNMP version 1, 2c or 3
        required: true
        type: str
        choices:
            - 1
            - 2c
            - 3
    security_name:
        description: Security name is Community name for versions 1 / 2c, and User name for version 3. User must be already configured for version 3.
        required: true
        type: str
    notification_type:
        description: Notification type 'trap' or 'inform'. Default is 'trap'.
        required: false
        default: trap
        type: str
        choices:
            - trap
            - inform
    port:
        description: Port to receive the notification. Default is 162.
        required: false
        default: 162
        type: int
'''

EXAMPLES = '''
- name: "Create SNMP User"
  thales.ciphertrust.snmp_management_station_add:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
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
                host=dict(type='str', required=True),
                security_name=dict(type='str', required=True),
                version=dict(type='str', options=['1', '2c', '3'], required=True),
                notification_type=dict(type='str', options=['trap', 'inform'], required=False, default='trap'),
                port=dict(type='int', required=False, default=162),
            ),
        )

    localNode = module.params.get('localNode');
    host = module.params.get('host');
    security_name = module.params.get('security_name');
    version = module.params.get('version');
    notification_type = module.params.get('notification_type');
    port = module.params.get('port');

    result = dict(
        changed=False,
    )

    response = addManagementStation(
        node=localNode,
        host=host,
        security_name=security_name,
        version=version,
        notification_type=notification_type,
        port=port
    )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()