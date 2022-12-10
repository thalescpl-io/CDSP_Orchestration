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
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_dpg_client_profile

DOCUMENTATION = '''
---
module: dpg_client_profile_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create DPG Client Profile API
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
        description: Unique name for the protection policy.
        required: true
        type: str
    app_connector_type:
        description: App connector type for which the client profile is created.
        options:
            - DPG
        required: true
        type: str
    ca_id:
        description: Local CA mapped with client profile.
        required: false
        type: str
        default: null
    cert_duration:
        description: Duration for which client credentials are valid.
        required: false
        type: int
    configurations:
        description: Parameters required to initialize connector.
        type: dict
        required: false
    csr_parameters:
        description: Client certificate parameters to be updated.
        type: dict
        required: false
    heartbeat_threshold:
        description: The Threshold by which client's connectivity_status will be moved to Error if not herabeat is received
        required: false
        type: int
    lifetime:
        description: Validity of registration token.
        required: false
        type: str
        default: null
    max_clients:
        description: Number of clients that can register using a registration token.
        required: false
        type: int
    nae_iface_port:
        description: Nae interface mapped with client profile.
        required: false
        type: int
    policy_id:
        description: Policy mapped with client profile.
        required: false
        type: str
        default: null
'''

EXAMPLES = '''
- name: "Create Client Profile"
    thales.ciphertrust.dpg_client_profile_create:
      localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
      name: "Ansible-Client-profile"
      nae_iface_port: "9005"
      app_connector_type: "DPG"
      csr_parameters: 
        csr_cn: "admin"
      configurations: 
        verify_ssl_certificate: False
        use_persistent_connections: True
        log_level: "DEBUG"
        tls_to_appserver:
          tls_skip_verify: True
          tls_enabled: True
        auth_method_used:
          scheme_name: 'Basic'
      policy_id: "DPG-POLICY-ID"
'''

RETURN = '''

'''

def main():
    csr_params = dict(
            csr_cn=dict(type='str', required=False, default=""),
            csr_country=dict(type='str', required=False, default=""),
            csr_state=dict(type='str', required=False, default=""),
            csr_city=dict(type='str', required=False, default=""),
            csr_org_name=dict(type='str', required=False, default=""),
            csr_org_unit=dict(type='str', required=False, default=""),
            csr_email=dict(type='str', required=False, default=""),
        )
    tlsToAppServer = dict(
            tls_skip_verify=dict(type='bool', required=False, default=True),
            tls_enabled=dict(type='bool', required=False, default=True),
        )
    authMethod = dict(
            scheme_name=dict(type='str', required=False, default="Basic"),
        )
    configuration = dict(
            symmetric_key_cache_enabled=dict(type='bool', required=False, default=True),
            symmetric_key_cache_expiry=dict(type='int', required=False, default=43200),
            verify_ssl_certificate=dict(type='bool', required=False, default=False),
            syslog_server_ip=dict(type='str', required=False),
            syslog_server_port=dict(type='int', required=False),
            syslog_server_protocol=dict(type='str', required=False),
            #syslog_no_of_retries
            #syslog_retry_interval
            #syslog_retry_limit
            use_persistent_connections=dict(type='bool', required=False, default=True),
            size_of_connection_pool=dict(type='int', required=False, default=300),
            load_balancing_algorithm=dict(type='str', required=False, default="round-robin"),
            connection_idle_timeout=dict(type='int', required=False, default=600000),
            connection_retry_interval=dict(type='int', required=False, default=600000),
            cluster_synchronization_delay=dict(type='int', required=False, default=170),
            #cert_file_location
            #credentials_encrypted
            #asymmetric_key_cache_enabled
            #persistent_cache_enabled
            #persistent_cache_directory
            #persistent_cache_expiry_keys
            #persistent_cache_max_size
            log_level=dict(type='str', required=False, default="WARN"),
            #log_file
            #log_rotation
            #log_size_limit
            log_type=dict(type='str', required=False, default="Console"),
            key_non_exportable_policy=dict(type='bool', required=False, default=False),
            connection_timeout=dict(type='int', required=False, default=60000),
            connection_read_timeout=dict(type='int', required=False, default=7000),
            heartbeat_interval=dict(type='int', required=False, default=300),
            heartbeat_timeout_count=dict(type='int', required=False),
            tls_to_appserver=dict(type='dict', options=tlsToAppServer, required=False),
            dial_timeout=dict(type='int', required=False),
            dial_keep_alive=dict(type='int', required=False),
            auth_method_used=dict(type='dict', options=authMethod, required=False),
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
                name=dict(type='str', required=True),
                app_connector_type=dict(type='str', required=True),
                ca_id=dict(type='str', required=False, default=""),
                cert_duration=dict(type='int', required=False, default=0),
                configurations=dict(type='dict', options=configuration, required=False),
                csr_parameters=dict(type='dict', options=csr_params, required=False),
                heartbeat_threshold=dict(type='int', required=False, default=0),
                lifetime=dict(type='str', required=False, default=""),
                max_clients=dict(type='int', required=False, default=0),
                nae_iface_port=dict(type='int', required=False, default=0),
                policy_id=dict(type='str', required=False, default=""),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    app_connector_type =  module.params.get('app_connector_type');
    ca_id =  module.params.get('ca_id');
    cert_duration = module.params.get('cert_duration');
    configurations = module.params.get('configurations');
    csr_parameters = module.params.get('csr_parameters');
    heartbeat_threshold = module.params.get('heartbeat_threshold');
    lifetime = module.params.get('lifetime');
    max_clients = module.params.get('max_clients');
    nae_iface_port = module.params.get('nae_iface_port');
    policy_id = module.params.get('policy_id');

    result = dict(
        changed=False,
    )

    response = create_dpg_client_profile(
        node=localNode,
        name=name,
        app_connector_type=app_connector_type,
        ca_id=ca_id,
        cert_duration=cert_duration,
        configurations=configurations,
        csr_parameters=csr_parameters,
        heartbeat_threshold=heartbeat_threshold,
        lifetime=lifetime,
        max_clients=max_clients,
        nae_iface_port=nae_iface_port,
        policy_id=policy_id
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
