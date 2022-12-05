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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import CMAPIObject, GETIdByQueryParam

DOCUMENTATION = '''
---
module: cm_resource_get_id_from_name
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically List API with name filter.
version_added: "1.0.0"
author: Anurag Jain, Developer Advocate Thales Group
options:
    localNode:
        description:
            - This is a dictionary type of object that contains CipherTrust Manager Instance FQDN and credentials
        default: null
        type: dict
        elements:
            - str
            - bool
    name:
        description:
            - This is a string type of option that holds the "name" filter value
        default: null
        type: str
    resource_type:
        description:
            - This is a string type of option that can hold the resource type. 
        default: null
        type: str
'''

EXAMPLES = '''
# Delete Resource at CipherTrust Manager
- name: "Get Key ID"
  thales.ciphertrust.cm_resource_get_id_from_name:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    name: "AnsibleKey"
    resource_type: "keys"
'''

RETURN = '''
id:
    description: String with the ID returned by the CipherTrust Manager
    returned: changed or success
    type: string
    sample: 123456789
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
                #name=dict(type='str', required=True),
                resource_type=dict(type='str', choices=['keys', 'protection-policies', 'access-policies', 'user-sets', 'interfaces', 'character-sets', 'users', 'dpg-policies', 'client-profiles', 'masking-formats'], required=True),
                query_param=dict(type='str', choices=['name', 'username', 'email', 'status'], required=False, default='name'),
                query_param_value=dict(type='str', required=False),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    #name =  module.params.get('name');
    resource_type = module.params.get('resource_type');
    query_param = module.params.get('query_param');
    query_param_value = module.params.get('query_param_value');

    result = dict(
        changed=False,
    )

    endpoint = '';
    #Create the API end point based on the resource_type
    if resource_type == "keys":
        endpoint = 'vault/keys2';
    elif resource_type == "protection-policies":
        endpoint = 'data-protection/protection-policies';
    elif resource_type == "access-policies":
        endpoint = 'data-protection/access-policies';
    elif resource_type == "user-sets":
        endpoint = 'data-protection/user-sets';
    elif resource_type == "interfaces":
        endpoint = 'configs/interfaces';
    elif resource_type == "character-sets":
        endpoint = 'data-protection/character-sets';
    elif resource_type == "users":
        endpoint = 'usermgmt/users';
    elif resource_type == "dpg-policies":
        endpoint = 'data-protection/dpg-policies';
    elif resource_type == "client-profiles":
        endpoint = 'data-protection/client-profiles';
    elif resource_type == "masking-formats":
        endpoint = 'data-protection/masking-formats';
    else:
        module.fail_json(msg='resource_type not supported yet')

    try:
        response = GETIdByQueryParam(
                param=query_param,
                value=query_param_value,
                cm_node=localNode,
                cm_api_endpoint=endpoint
            )
        result['response'] = response
    except requests.exceptions.RequestException as err:
        result['failed'] = True
        result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
