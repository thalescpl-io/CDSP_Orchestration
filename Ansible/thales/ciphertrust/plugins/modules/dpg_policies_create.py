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
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_dpg_policy

DOCUMENTATION = '''
---
module: dpg_policies_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create DPG Policy API
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
    policyDescription:
        description: name of the DPG policy
        required: false
        type: str
        default: null
    proxy_config:
        description: List of API urls to be added to the proxy configuration.
        required: false
        type: list
        default: empty array
'''

EXAMPLES = '''
- name: "Create DPG Policy"
  thales.ciphertrust.dpg_policies_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "DPG Policy"
    proxy_config:
        - rest_op_type: "post"
          api_url: "/post/url/resource/create"
          tokens:
            - name: "card.cardNumber"
              operation: "protect"
              protection_policy: "CARD-PROT-POLICY"
            - name: "card.cvv"
              operation: "protect"
              protection_policy: "UNICODE-PROT-POLICY"
        - rest_op_type: "get"
          api_url: "/post/url/resource/list"
          tokens:
            - name: "data.[*].card.cvv"
              operation: "reveal"
              protection_policy: "UNICODE-PROT-POLICY"
              access_policy: "ACCESS-POLICY"
            - name: "data.[*].card.cardNumber"
              operation: "reveal"
              protection_policy: "CARD-PROT-POLICY"
              access_policy: "ACCESS-POLICY"
'''

RETURN = '''

'''

def main():
    token = dict(
            name=dict(type='str', required=True),
            operation=dict(type='str', required=True),
            protection_policy=dict(type='str', required=True),
            access_policy=dict(type='str', required=False),
        )
    endpoint = dict(
            rest_op_type=dict(type='str', required=True),
            api_url=dict(type='str', required=False),
            destination_url=dict(type='str', required=False),
            tokens=dict(type='list', elements='dict', options=token, required=False, default=[]),
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
                name=dict(type='str', required=True),
                policyDescription=dict(type='str', required=False, default=""),
                proxy_config=dict(type='list', elements='dict', options=endpoint, required=False, default=[]),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    policyDescription =  module.params.get('policyDescription');
    proxy_config = module.params.get('proxy_config');

    result = dict(
        changed=False,
    )

    response = create_dpg_policy(
        node=localNode,
        name=name,
        policyDescription=policyDescription,
        proxy_config=proxy_config
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
