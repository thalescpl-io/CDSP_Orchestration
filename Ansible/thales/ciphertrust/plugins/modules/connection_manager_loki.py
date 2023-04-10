#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2023 Thales Group. All rights reserved.
# Author: Anurag Jain, Developer Advocate, Thales
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

from ansible_collections.thales.ciphertrust.plugins.module_utils.modules import ThalesCipherTrustModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.connection_management import createConnection, patchConnection
from ansible_collections.thales.ciphertrust.plugins.module_utils.exceptions import CMApiException, AnsibleCMException

DOCUMENTATION = '''
---
module: connection_manager_aws
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with Connection Manager API for AWS
version_added: "1.0.0"
author: Anurag Jain, Developer Advocate Thales Group
options:
    localNode:
        description:
            - this holds the connection parameters required to communicate with an instance of CipherTrust Manager (CM)
            - holds IP/FQDN of the server, username, password, and port 
        required: true
        type: dict
        suboptions:
          server_ip:
            description: CM Server IP or FQDN
            type: str
            required: true
          server_private_ip:
            description: internal or private IP of the CM Server, if different from the server_ip
            type: str
            required: true
          server_port:
            description: Port on which CM server is listening
            type: int
            required: true
            default: 5432
          user:
            description: admin username of CM
            type: str
            required: true
          password:
            description: admin password of CM
            type: str
            required: true
          verify:
            description: if SSL verification is required
            type: bool
            required: true
            default: false     
    op_type:
        description: Operation to be performed
        choices: [create, patch]
        required: true
        type: str
    name:
        description: Unique connection name
        required: true
        default: none
        type: str
    access_key_id:
        description: Key ID of the AWS user
        required: true
        default: none
        type: str
    secret_access_key:
        description: Secret associated with the access key ID of the AWS user
        required: true
        default: none
        type: str
    assume_role_arn:
        description: AWS IAM role ARN
        required: false
        default: none
        type: str
    assume_role_external_id:
        description: AWS role external ID
        required: false
        default: none
        type: str
    aws_region:
        description: AWS region. only used when aws_sts_regional_endpoints is equal to regional otherwise, it takes default values according to Cloud Name given.
        required: false
        default: none
        type: str
    aws_sts_regional_endpoints:
        description: By default, AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com. Global requests map to the US East (N. Virginia) Region. AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity.
        required: false
        default: none
        type: str
    cloud_name:
        description: Name of the cloud
        required: false
        default: none
        type: str
    description:
        description: Description about the connection
        required: false
        default: none
        type: str
    meta:
        description: Optional end-user or service data stored with the connection
        required: false
        default: none
        type: dict
    products:
        description: Array of the CipherTrust products associated with the connection.
        required: false
        default: none
        type: list
        element: str
'''

EXAMPLES = '''
- name: "Create AWS Connection"
  thales.ciphertrust.connection_manager_aws:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: create

- name: "Update AWS Connection"
  thales.ciphertrust.connection_manager_aws:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: patch
'''

RETURN = '''

'''
_schema_less = dict()

_loki_param = dict(
    ca_cert=dict(type='str', required=False),
    http_password=dict(type='str', required=False),
    http_user=dict(type='str', required=False),
    insecure_tls_skip_verify=dict(type='bool', required=False),
    transport=dict(type='str', options=['tcp', 'tls'], required=False),
)

argument_spec = dict(
    op_type=dict(type='str', options=['create', 'patch'], required=True),
    connection_type=dict(type='str', options=['aws', 'azure', 'dsm', 'elasticsearch', 'google', 'hadoop', 'ldap', 'loki', 'luna_network_hsm_server', 'oidc', 'oracle', 'sap', 'scp', 'smb', 'salesforce', 'syslog'], required=True),
    connection_id=dict(type='str', required=False),    
    host=dict(type='str'),
    name=dict(type='str'),
    port=dict(type='int'),
    description=dict(type='str', required=False),
    loki_params=dict(type='dict', options=_loki_param, required=False),    
    meta=dict(type='dict', options=_schema_less, required=False),
    products=dict(type='list', element='str', required=False),
)

def validate_parameters(domain_module):
    return True

def setup_module_object():
    module = ThalesCipherTrustModule(
        argument_spec=argument_spec,
        required_if=(
            ['op_type', 'patch', ['connection_id']],
            ['op_type', 'create', ['name']],
        ),
        mutually_exclusive=[],
        supports_check_mode=True,
    )
    return module

def main():

    global module
    
    module = setup_module_object()
    validate_parameters(
        domain_module=module,
    )

    result = dict(
        changed=False,
    )

    if module.params.get('op_type') == 'create':
      try:
        response = createConnection(
          node=module.params.get('localNode'),
          connection_type=module.params.get('connection_type'),
          host=module.params.get('host'),
          name=module.params.get('name'),
          port=module.params.get('port'),
          description=module.params.get('description'),
          loki_params=module.params.get('elasticsearch_params'),
          meta=module.params.get('meta'),
          products=module.params.get('products'),
        )
        result['response'] = response
      except CMApiException as api_e:
        if api_e.api_error_code:
          module.fail_json(msg="status code: " + str(api_e.api_error_code) + " message: " + api_e.message)
      except AnsibleCMException as custom_e:
        module.fail_json(msg=custom_e.message)

    elif module.params.get('op_type') == 'patch':
      try:
        response = patchConnection(
          node=module.params.get('localNode'),
          connection_type=module.params.get('connection_type'),
          connection_id=module.params.get('connection_id'),
          host=module.params.get('host'),
          port=module.params.get('port'),
          description=module.params.get('description'),
          loki_params=module.params.get('elasticsearch_params'),
          meta=module.params.get('meta'),
          products=module.params.get('products'),
        )
        result['response'] = response
      except CMApiException as api_e:
        if api_e.api_error_code:
          module.fail_json(msg="status code: " + str(api_e.api_error_code) + " message: " + api_e.message)
      except AnsibleCMException as custom_e:
        module.fail_json(msg=custom_e.message)

    else:
        module.fail_json(msg="invalid op_type")
        
    module.exit_json(**result)

if __name__ == '__main__':
    main()