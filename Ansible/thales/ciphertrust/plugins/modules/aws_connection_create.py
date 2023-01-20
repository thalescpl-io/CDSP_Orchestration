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
from ansible_collections.thales.ciphertrust.plugins.module_utils.connections import createAWSConnection

DOCUMENTATION = '''
---
module: aws_connection_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create AWS Connection API
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
    access_key_id:
        description: Key ID of the AWS user
        required: true
        type: str
    secret_access_key:
        description: Secret associated with the access key ID of the AWS user
        required: true
        type: str
    assume_role_arn:
        description: AWS IAM role ARN
        required: false
        type: str
    assume_role_external_id:
        description: AWS role external ID
        required: false
        type: str
    aws_region:
        description: AWS region. only used when aws_sts_regional_endpoints is equal to regional otherwise, it takes default values according to Cloud Name given.
        required: false
        type: str
    aws_sts_regional_endpoints:
        description: By default, AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com. Global requests map to the US East (N. Virginia) Region. AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity.
        required: false
        type: str
    cloud_name:
        description: Name of the cloud
        required: false
        type: str
    products:
        description: Array of the CipherTrust products associated with the connection
        required: false
        type: str
'''

EXAMPLES = '''
- name: "Create AWS Connection"
  thales.ciphertrust.aws_connection_create:
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
                access_key_id=dict(type='str', required=True),
                secret_access_key=dict(type='str', required=True),
                assume_role_arn=dict(type='str', required=False),
                assume_role_external_id=dict(type='str', required=False),
                aws_region=dict(type='str', required=False),
                aws_sts_regional_endpoints=dict(type='str', options=['legacy', 'regional'], default='legacy', required=False),
                cloud_name=dict(type='str', options=['aws', 'aws-us-gov', 'aws-cn'], default='aws', required=False),
                description=dict(type='str', required=False),
                products=dict(type='list', element='str', required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    description =  module.params.get('description');
    access_key_id =  module.params.get('access_key_id');
    secret_access_key =  module.params.get('secret_access_key');
    assume_role_arn =  module.params.get('assume_role_arn');
    assume_role_external_id =  module.params.get('assume_role_external_id');
    aws_region =  module.params.get('aws_region');
    aws_sts_regional_endpoints =  module.params.get('aws_sts_regional_endpoints');
    cloud_name =  module.params.get('cloud_name');
    products =  module.params.get('products');

    result = dict(
        changed=False,
    )

    response = createAWSConnection(
            node=localNode,
            name=name,
            description=description,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            assume_role_arn=assume_role_arn,
            assume_role_external_id=assume_role_external_id,
            aws_region=aws_region,
            aws_sts_regional_endpoints=aws_sts_regional_endpoints,
            cloud_name=cloud_name,
            products=products
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()