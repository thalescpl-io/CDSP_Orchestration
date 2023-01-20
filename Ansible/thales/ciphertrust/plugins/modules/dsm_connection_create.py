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
from ansible_collections.thales.ciphertrust.plugins.module_utils.connections import createDSMConnection

DOCUMENTATION = '''
---
module: azure_connection_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create Azure Connection API
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
        description: Unique connection name
        required: true
        type: str
    description:
        description: Description about the connection
        required: false
        type: str
    products:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    client_id:
        description: Unique Identifier (client ID) for the Azure application
        required: false
        type: str
    tenant_id:
        description: Tenant ID of the Azure application.
        required: false
        type: str
    active_directory_endpoint:
        description: Azure stack active directory authority URL
        required: false
        type: str
    azure_stack_connection_type:
        description: Azure stack connection type
        required: false
        type: str
        choices:
            - AAD
            - ADFS
    azure_stack_server_cert:
        description: Azure stack server certificate
        required: false
        type: str
    cert_duration:
        description: Duration in days for which the azure certificate is valid, default (730 i.e. 2 Years).
        required: false
        type: int
        default: 730
    client_secret:
        description: Secret key for the Azure application. Required in Azure Stack connection.
        required: false
        type: str
    cloud_name:
        description: Name of the cloud.
        required: false
        type: str
        choices:
            - AzureCloud
            - AzureChinaCloud
            - AzureUSGovernment
            - AzureStack
    is_certificate_used:
        description: User has the option to choose the Certificate Authentication method instead of Client Secret for Azure Cloud connection. In order to use the Certificate, set it to true. Once the connection is created, in the response user will get a certificate. By default, the certificate is valid for 2 Years. User can update the certificate in the existing connection by setting it to true in Update (PATCH) API call.
        required: false
        type: bool
    key_vault_dns_suffix:
        description: Azure stack key vault dns suffix
        required: false
        type: str
    management_url:
        description: Azure stack management URL
        required: false
        type: str
    resource_manager_url:
        description: Azure stack resource manager URL
        required: false
        type: str
    vault_resource_url:
        description: Azure stack vault service resource URL
        required: false
        type: str
'''

EXAMPLES = '''
- name: "Create Azure Connection"
  thales.ciphertrust.azure_connection_create:
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
    node = dict(
        hostname=dict(type='str', required=True),
        server_certificate=dict(type='str', required=True),
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
                description=dict(type='str', required=False),
                products=dict(type='list', element='str', required=False),
                nodes=dict(type='list', element='dict', options=node, required=True),
                password=dict(type='str', required=True),
                username=dict(type='str', required=True),
                domain_id=dict(type='str', required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    description =  module.params.get('description');
    products =  module.params.get('products');
    nodes =  module.params.get('nodes');
    password =  module.params.get('password');
    username =  module.params.get('username');
    domain_id =  module.params.get('domain_id');
    
    result = dict(
        changed=False,
    )

    response = createDSMConnection(
            node=localNode,
            name=name,
            description=description,
            products=products,
            nodes=nodes,
            password=password,
            username=username,
            domain_id=domain_id
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()