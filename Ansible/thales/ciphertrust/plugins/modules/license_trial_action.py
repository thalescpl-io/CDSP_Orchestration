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
from ansible_collections.thales.ciphertrust.plugins.module_utils.licensing import activateTrial, deactivateTrial

DOCUMENTATION = '''
---
module: license_trial_action
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with Licensing API
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
    action_type:
        description: Can be activate or deactivate
        required: true
        type: str
        choices:
            - activate
            - deactivate
    trialId:
        description: Trial license ID
        required: true
        type: str
'''

EXAMPLES = '''
- name: "Create License"
  thales.ciphertrust.license_trial_action:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
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
                action_type=dict(type='str', options=['activate', 'deactivate'], required=True),
                trialId=dict(type='str', required=True),
            ),
        )

    localNode = module.params.get('localNode');
    action_type =  module.params.get('action_type');
    trialId =  module.params.get('trialId');

    result = dict(
        changed=False,
    )
    response = dict()

    if action_type == "activate":
        respone = activateTrial(
            node=localNode,
            trialId=trialId
        )
    else:
        respone = deactivateTrial(
            node=localNode,
            trialId=trialId
        )

    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()