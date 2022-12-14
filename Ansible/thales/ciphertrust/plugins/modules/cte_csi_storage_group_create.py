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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import create_csigroup

DOCUMENTATION = '''
---
module: cte_csi_storage_group_create
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
    name:
        description: Name to uniquely identify the CSI storage group. This name will be visible on the CipherTrust Manager.
        required: true
        type: str
    k8s_namespace:
        description: Name of the K8s namespace.
        required: true
        type: str
    k8s_storage_class:
        description: Name of the K8s StorageClass.
        required: true
        type: str
    client_profile:
        description: Optional Client Profile for the storage group. If not provided, the default profile will be used.
        required: false
        type: str
        default: null
    csigroupDescription:
        description: Optional description for the storage group.
        required: true
        type: str
        default: null
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_csi_storage_group_create:
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
                csigroupDescription=dict(type='str', required=False, default=""),
                k8s_namespace=dict(type='str', required=True),
                k8s_storage_class=dict(type='str', required=True),
                client_profile=dict(type='str', required=False, default="")
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    csigroupDescription = module.params.get('csigroupDescription');
    k8s_namespace = module.params.get('k8s_namespace');
    k8s_storage_class = module.params.get('k8s_storage_class');
    client_profile = module.params.get('client_profile');

    result = dict(
        changed=False,
    )

    response = create_csigroup(
            node=localNode,
            name=name,
            csigroupDescription=csigroupDescription,
            k8s_namespace=k8s_namespace,
            k8s_storage_class=k8s_storage_class,
            client_profile=client_profile
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
