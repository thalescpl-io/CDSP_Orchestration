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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import clientgroup_add_client

DOCUMENTATION = '''
---
module: cte_client_group_add_client
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create CSI Storage Group for CTE API
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
    group_id:
        description: 
            - ID of the CSI storage group to which the clients need to be added
        required: true
        type: str
        default: null
    client_list:
        description:
            - List of Client identifier which are to be associated with clientgroup. This identifier can be the Name, ID (a UUIDv4), URI, or slug of the client.
        type: list
        element: str
        required: true
        default: empty
    inherit_attributes:
        description:
            - Whether the client should inherit attributes from the ClientGroup.
        type: bool
        required: true
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_client_group_add_client:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    client_list: 
      -  "client"
    inherit_attributes: false
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
                group_id=dict(type='str', required=True),
                client_list=dict(type='list', elements='str', required=True),
                inherit_attributes=dict(type='bool', required=True),
            ),
        )

    localNode = module.params.get('localNode');
    group_id = module.params.get('group_id');
    client_list = module.params.get('client_list');
    inherit_attributes = module.params.get('inherit_attributes');

    result = dict(
        changed=False,
    )

    response = clientgroup_add_client(
            node=localNode,
            group_id=group_id,
            client_list=client_list,
            inherit_attributes=inherit_attributes
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
