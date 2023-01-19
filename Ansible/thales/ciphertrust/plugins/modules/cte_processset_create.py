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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import createProcessSet

DOCUMENTATION = '''
---
module: cte_processset_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create processset for CTE API
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
        description: Name of the process set.
        required: true
        type: str
    processSetDescription:
        description: Description of the process set.
        required: false
        type: str
    processes:
        description: List of processes to be added to the process set
        required: false
        type: list
        default: null
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_processset_create:
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
    process = dict(
        directory=dict(type='str', required=False),
        processSetFile=dict(type='str', required=False),
        signature=dict(type='str', required=False),
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
                processSetDescription=dict(type='str', required=False),
                processes=dict(type='list', element='dict', options=process, required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    processSetDescription =  module.params.get('processSetDescription');
    processes =  module.params.get('processes');

    result = dict(
        changed=False,
    )

    response = createProcessSet(
            node=localNode,
            name=name,
            processSetDescription=processSetDescription,
            processes=processes
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()