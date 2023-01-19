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
from ansible_collections.thales.ciphertrust.plugins.module_utils.connections import patchSyslogConnection

DOCUMENTATION = '''
---
module: syslog_connection_patch
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with Syslog Connection API
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
    syslog_params:
        description: Params
        required: true
        type: dict
    conn_description:
        description: Description about the connection
        required: false
        type: str
    host:
        description: Host of the log-forwarder server
        required: false
        type: str
    port:
        description: The port to use for the connection. Defaults to 514 for udp, 601 for tcp and 6514 for tls
        required: false
        type: int
    products:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: list
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.syslog_connection_patch:
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
    syslogParams = dict(
        transport=dict(type='str', required=True),
        ca_cert=dict(type='str', required=False),
        message_format=dict(type='str', required=False),
    )
    module = AnsibleModule(
            argument_spec=dict(
                localNode=dict(type='dict', options=localNode, required=True),
                connectionId=dict(type='str', required=True),
                syslog_params=dict(type='dict', options=syslogParams, required=True),
                conn_description=dict(type='str', required=False),
                host=dict(type='str', required=False),
                port=dict(type='int', required=False),
                products=dict(type='list', element='str', required=False, default=[]),
            ),
        )

    localNode = module.params.get('localNode');
    connectionId =  module.params.get('connectionId');
    syslog_params =  module.params.get('syslog_params');
    conn_description =  module.params.get('conn_description');
    host =  module.params.get('host');
    port =  module.params.get('port');
    products =  module.params.get('products');

    result = dict(
        changed=False,
    )

    response = patchSyslogConnection(
        node=localNode,
        syslog_params=syslog_params,
        connectionId=connectionId,
        conn_description=conn_description,
        host=host,
        port=port,
        products=products
    )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()