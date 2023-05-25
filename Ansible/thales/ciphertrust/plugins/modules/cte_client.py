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
import json

from ansible_collections.thales.ciphertrust.plugins.module_utils.modules import ThalesCipherTrustModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import createClient, clientAddGuardPoint
from ansible_collections.thales.ciphertrust.plugins.module_utils.exceptions import CMApiException, AnsibleCMException

DOCUMENTATION = '''
---
module: cte_client
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with CTE Client management
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
    sg_id:
      description:
        - Identifier of the CTE CSI Storage Group to be patched
      type: str
'''

EXAMPLES = '''
- name: "Create CTE Policy"
  thales.ciphertrust.dpg_policy_save:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: create

- name: "Patch DPG Policy"
  thales.ciphertrust.dpg_policy_save:
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

_guard_point_params = dict(
  guard_point_type=dict(type='str', options=['directory_auto', 'directory_manual', 'rawdevice_manual', 'rawdevice_auto', 'cloudstorage_auto', 'cloudstorage_manual']),
  policy_id=dict(type='str'),
  automount_enabled=dict(type='bool'),
  cifs_enabled=dict(type='bool'),
  data_classification_enabled=dict(type='bool'),
  data_lineage_enabled=dict(type='bool'),
  disk_name=dict(type='str'),
  diskgroup_name=dict(type='str'),
  early_access=dict(type='bool'),
  intelligent_protection=dict(type='bool'),
  is_esg_capable_device=dict(type='bool'),
  is_idt_capable_device=dict(type='bool'),
  mfa_enabled=dict(type='bool'),
  network_share_credentials_id=dict(type='str'),
  preserve_sparse_regions=dict(type='bool'),
)

argument_spec = dict(
    op_type=dict(type='str', options=[
      'create', 
      'patch',
      'add_guard_point',
    ], required=True),
    id=dict(type='str'),
    name=dict(type='str'),
    client_type=dict(type='str', options=['CTE-U', 'FS']),
    client_locked=dict(type='bool'),
    communication_enabled=dict(type='bool'),    
    description=dict(type='str'),
    password=dict(type='str'),
    password_creation_method=dict(type='str', options=['GENERATE', 'MANUAL']),
    profile_identifier=dict(type='str'),
    registration_allowed=dict(type='bool'),
    system_locked=dict(type='bool'),
    user_space_client=dict(type='bool'),
    # Patch specific attributes
    client_mfa_enabled=dict(type='bool'),
    del_client=dict(type='bool'),
    disable_capability=dict(type='str'),
    dynamic_parameters=dict(type='str'),
    enable_domain_sharing=dict(type='bool'),
    enabled_capabilities=dict(type='str'),
    max_num_cache_log=dict(type='int'),
    max_space_cache_log=dict(type='int'),
    profile_id=dict(type='str'),
    shared_domain_list=dict(type='list', element='str'),
    # Params for adding guard paths to client
    guard_paths=dict(type='list', element='str'),
    guard_point_params=dict(type='dict', options=_guard_point_params),
)

def validate_parameters(cte_client_module):
    return True

def setup_module_object():
    module = ThalesCipherTrustModule(
        argument_spec=argument_spec,
        required_if=(
            ['op_type', 'create', ['name']],
            ['op_type', 'patch', ['id']],
            ['op_type', 'add_guard_point', ['id', 'guard_paths', 'guard_point_params']],
        ),
        mutually_exclusive=[],
        supports_check_mode=True,
    )
    return module

def main():

    global module
    
    module = setup_module_object()
    validate_parameters(
        cte_client_module=module,
    )

    result = dict(
        changed=False,
    )

    if module.params.get('op_type') == 'create':
      try:
        response = createClient(
          node=module.params.get('localNode'),
          name=module.params.get('name'),
          description=module.params.get('description'),
          client_locked=module.params.get('client_locked'),
          client_type=module.params.get('client_type'),
          communication_enabled=module.params.get('communication_enabled'),
          password=module.params.get('password'),
          password_creation_method=module.params.get('password_creation_method'),
          profile_identifier=module.params.get('profile_identifier'),
          registration_allowed=module.params.get('registration_allowed'),
          system_locked=module.params.get('system_locked'),
          user_space_client=module.params.get('user_space_client'),
        )
        result['response'] = response
      except CMApiException as api_e:
        if api_e.api_error_code:
          module.fail_json(msg="status code: " + str(api_e.api_error_code) + " message: " + api_e.message)
      except AnsibleCMException as custom_e:
        module.fail_json(msg=custom_e.message)

    # elif module.params.get('op_type') == 'patch':
    #   try:
    #     response = updateClientGroup    (
    #       node=module.params.get('localNode'),
    #       id=module.params.get('id'),
    #       client_locked=module.params.get('client_locked'),
    #       communication_enabled=module.params.get('communication_enabled'),
    #       description=module.params.get('description'),
    #       enable_domain_sharing=module.params.get('enable_domain_sharing'),
    #       enabled_capabilities=module.params.get('enabled_capabilities'),
    #       password=module.params.get('password'),
    #       password_creation_method=module.params.get('password_creation_method'),
    #       profile_id=module.params.get('profile_id'),
    #       shared_domain_list=module.params.get('shared_domain_list'),
    #       system_locked=module.params.get('system_locked'),
    #     )
    #     result['response'] = response
    #   except CMApiException as api_e:
    #     if api_e.api_error_code:
    #       module.fail_json(msg="status code: " + str(api_e.api_error_code) + " message: " + api_e.message)
    #   except AnsibleCMException as custom_e:
    #     module.fail_json(msg=custom_e.message)

    elif module.params.get('op_type') == 'add_guard_point':
      try:
        response = clientAddGuardPoint(
          node=module.params.get('localNode'),
          id=module.params.get('id'),
          guard_paths=module.params.get('guard_paths'),
          guard_point_params=module.params.get('guard_point_params'),
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