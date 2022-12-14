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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import create_clientgroup

DOCUMENTATION = '''
---
module: cte_client_group_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create Client Group for CTE API
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
        description: Name of the ClientGroup.
        required: true
        type: str
    clientgroupDescription:
        description: Description of the ClientGroup.
        required: true
        type: str
    cluster_type:
        description: Cluster type of the ClientGroup, valid values are NON-CLUSTER and HDFS.
        required: true
        type: str
        choices:
          - NON-CLUSTER
          - HDFS
    profile_id:
        description: ID of the client group profile that is used to schedule custom configuration for logger, logging, and Quality of Service (QoS).
        required: false
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
                clientgroupDescription=dict(type='str', required=False, default=""),
                cluster_type=dict(type='str', options=['NON-CLUSTER','HDFS'], required=True),
                profile_id=dict(type='str', required=False, default="")
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    clientgroupDescription = module.params.get('clientgroupDescription');
    cluster_type = module.params.get('cluster_type');
    profile_id = module.params.get('profile_id');

    result = dict(
        changed=False,
    )

    response = create_clientgroup(
            node=localNode,
            name=name,
            clientgroupDescription=clientgroupDescription,
            cluster_type=cluster_type,
            profile_id=profile_id
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
