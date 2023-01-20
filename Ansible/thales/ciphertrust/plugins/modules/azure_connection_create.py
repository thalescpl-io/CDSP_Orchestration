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
from ansible_collections.thales.ciphertrust.plugins.module_utils.connections import createAzureConnection

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
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    tenant_id:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    active_directory_endpoint:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    azure_stack_connection_type:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    azure_stack_server_cert:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    cert_duration:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    client_secret:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    cloud_name:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    is_certificate_used:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    key_vault_dns_suffix:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    management_url:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    resource_manager_url:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
    vault_resource_url:
        description: Array of the CipherTrust products associated with the connection
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
                client_id=dict(type='str', required=True),
                tenant_id=dict(type='str', required=True),
                active_directory_endpoint=dict(type='str', required=False),
                azure_stack_connection_type=dict(type='str', options=['AAD', 'ADFS'], required=False),
                azure_stack_server_cert=dict(type='str', required=False),
                cert_duration=dict(type='int', default=730, required=False),
                client_secret=dict(type='str', required=False),
                cloud_name=dict(type='str', options=['AzureCloud', 'AzureChinaCloud', 'AzureUSGovernment', 'AzureStack'], required=False),
                description=dict(type='str', required=False),
                is_certificate_used=dict(type='bool', required=False),
                key_vault_dns_suffix=dict(type='str', required=False),
                management_url=dict(type='str', required=False),
                resource_manager_url=dict(type='str', required=False),
                vault_resource_url=dict(type='str', required=False),
                products=dict(type='list', element='str', required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    description =  module.params.get('description');
    client_id =  module.params.get('client_id');
    tenant_id =  module.params.get('tenant_id');
    active_directory_endpoint =  module.params.get('active_directory_endpoint');
    azure_stack_connection_type =  module.params.get('azure_stack_connection_type');
    azure_stack_server_cert =  module.params.get('azure_stack_server_cert');
    cert_duration =  module.params.get('cert_duration');
    client_secret =  module.params.get('client_secret');
    cloud_name =  module.params.get('cloud_name');
    is_certificate_used =  module.params.get('is_certificate_used');
    products =  module.params.get('products');
    key_vault_dns_suffix =  module.params.get('key_vault_dns_suffix');
    management_url =  module.params.get('management_url');
    resource_manager_url =  module.params.get('resource_manager_url');
    vault_resource_url =  module.params.get('vault_resource_url');

    result = dict(
        changed=False,
    )

    response = createAzureConnection(
            node=localNode,
            name=name,
            description=description,
            client_id=client_id,
            tenant_id=tenant_id,
            active_directory_endpoint=active_directory_endpoint,
            azure_stack_connection_type=azure_stack_connection_type,
            azure_stack_server_cert=azure_stack_server_cert,
            cert_duration=cert_duration,
            client_secret=client_secret,
            cloud_name=cloud_name,
            products=products,
            is_certificate_used=is_certificate_used,
            key_vault_dns_suffix=key_vault_dns_suffix,
            management_url=management_url,
            resource_manager_url=resource_manager_url,
            vault_resource_url=vault_resource_url
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()