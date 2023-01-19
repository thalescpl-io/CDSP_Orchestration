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
from ansible_collections.thales.ciphertrust.plugins.module_utils.smtp import addServer

DOCUMENTATION = '''
---
module: smtp_server_add
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with SMTP Server API
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
    email_from:
        description: address to put in the email's "from" field
        required: true
        type: str
    port:
        description: SMTP server port
        required: true
        type: int
    server:
        description: SMTP server address
        required: true
        type: str
    allow_tcp:
        description: allow less secure tcp connection
        required: false
        type: bool
    password:
        description: SMTP server password
        required: false
        type: str
    username:
        description: SMTP server username
        required: false
        type: str
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.smtp_server_add:
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
                email_from=dict(type='str', required=True),
                port=dict(type='int', required=True),
                server=dict(type='str', required=True),
                allow_tcp=dict(type='bool', required=False),
                password=dict(type='str', required=False),
                username=dict(type='str', required=False),
            ),
        )

    localNode = module.params.get('localNode');
    email_from =  module.params.get('email_from');
    port =  module.params.get('port');
    server =  module.params.get('server');
    allow_tcp =  module.params.get('allow_tcp');
    password =  module.params.get('password');
    username =  module.params.get('username');

    result = dict(
        changed=False,
    )

    response = addServer(
        node=localNode,
        email_from=email_from,
        port=port,
        server=server,
        allow_tcp=allow_tcp,
        password=password,
        username=username
    )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()