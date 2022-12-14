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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import clientgroup_add_guardpoint

DOCUMENTATION = '''
---
module: cte_client_group_add_guardpoint
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
    guard_paths:
        description:
            - List of GuardPaths to be created.
        type: list
        element: str
        required: true
        default: empty
    guard_point_params:
        description:
            - Parameters for creating a GuardPoint.
        type: dict
        required: true
        default: null
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_client_group_add_guardpoint:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    guard_paths: 
      -  "path"
'''

RETURN = '''

'''

def main():
    guardPointParams = dict(
        guard_point_type=dict(type='str', options=['directory_auto', 'directory_manual', 'rawdevice_manual', 'rawdevice_auto', 'cloudstorage_auto', 'cloudstorage_manual'], required=True),
        policy_id=dict(type='str', required=True),
        automount_enabled=dict(type='bool', required=False),
        cifs_enabled=dict(type='bool', required=False),
        data_classification_enabled=dict(type='bool', required=False),
        data_lineage_enabled=dict(type='bool', required=False),
        disk_name=dict(type='str', required=False),
        diskgroup_name=dict(type='str', required=False),
        early_access=dict(type='bool', required=False),
        intelligent_protection=dict(type='bool', required=False),
        is_esg_capable_device=dict(type='bool', required=False),
        is_idt_capable_device=dict(type='bool', required=False),
        mfa_enabled=dict(type='bool', required=False),
        preserve_sparse_regions=dict(type='bool', required=False),
        network_share_credentials_id=dict(type='str', required=False)
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
                group_id=dict(type='str', required=True),
                guard_point_params=dict(type='dict', options=guardPointParams, required=True),
                guard_paths=dict(type='list', elements='str', required=True)
            ),
        )

    localNode = module.params.get('localNode');
    guard_point_params = module.params.get('guard_point_params');
    guard_paths = module.params.get('guard_paths');
    group_id = module.params.get('group_id');

    result = dict(
        changed=False,
    )

    response = clientgroup_add_guardpoint(
            node=localNode,
            group_id=group_id,
            guard_point_params=guard_point_params,
            guard_paths=guard_paths
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
