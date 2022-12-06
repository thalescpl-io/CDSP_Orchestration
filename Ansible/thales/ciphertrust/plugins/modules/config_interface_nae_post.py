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
from ansible_collections.thales.ciphertrust.plugins.module_utils.interfaces import new

DOCUMENTATION = '''
---
module: config_interface_nae_post
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create Interface API
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
    port:
        description:
            - The new interface will listen on the specified port. The port number should not be negative, 0 or the one already in-use.
        required: true
        type: int
    auto_gen_ca_id:
        description:
            - Auto-generate a new server certificate on server startup using the identifier (URI) of a Local CA resource if the current server certificate is issued by a different Local CA. This is especially useful when a new node joins the cluster. In this case, the existing data of the joining node is overwritten by the data in the cluster. A new server certificate is generated on the joining node using the existing Local CA of the cluster. Auto-generation of the server certificate can be disabled by setting auto_gen_ca_id to an empty string ("") to allow full control over the server certificate.
        required: false
        default: none
        type: str
    auto_registration:
        description:
            - Set auto registration to allow auto registration of kmip clients.
        required: false
        default: False
        type: bool
    cert_user_field:
        description:
            - Specifies how the user name is extracted from the client certificate. Allowed values are: CN, SN, E, E_ND, UID and OU. Refer to the top level discussion of the Interfaces section for more details.
        required: false
        default: CN
        choices:
            - CN
            - SN
            - E
            - E_ND
            - UID
            - OU
        type: str
    custom_uid_size:
        description: This flag is used to define the custom uid size of managed object over the KMIP interface.
        required: false
        default: none
        type: int
    custom_uid_v2:
        description: This flag specifies which version of custom uid feature is to be used for KMIP interface. If it is set to true, new implementation i.e. Custom uid version 2 will be used.
        required: false
        default: true
        type: bool
    default_connection:
        description: The default connection may be "local_account" for local authentication or the LDAP domain for LDAP authentication. This value is applied when the username does not embed the connection name (e.g. "jdoe" effectively becomes "local_account|jdoe"). This value only applies to NAE only and is ignored if set for web and KMIP interfaces.
        required: false
        default: local_account
        type: str
    interface_type:
        description: This parameter is used to identify the type of interface, what service to run on the interface.
        required: false
        default nae
        choices:
            - web
            - kmip
            - nae
            - snmp
        type: str
    kmip_enable_hard_delete:
        description: Enables hard delete of keys on KMIP Destroy operation, that is both meta-data and material will be removed from CipherTrust Manager for the key being deleted. By default, only key material is removed and meta-data is preserved with the updated key state. This setting applies only to KMIP interface. Should be set to 1 for enabling the feature or 0 for returning to default behavior.
        required: false
        default: 0
        choices:
            - 0
            - 1
        type: int
    maximum_tls_version:
        description: Maximum TLS version to be configured for NAE or KMIP interface, default is latest maximum supported protocol.
        required: false
        default: tls_1_2
        choices:
            - tls_1_0
            - tls_1_1
            - tls_1_2
            - tls_1_3
        type: str
    minimum_tls_version:
        description: Minimum TLS version to be configured for NAE or KMIP interface, default is v1.2 (tls_1_2).
        required: false
        default: tls_1_2
        choices:
            - tls_1_0
            - tls_1_1
            - tls_1_2
            - tls_1_3
        type: str
    mode:
        description: The interface mode can be one of the following: no-tls-pw-opt, no-tls-pw-req, unauth-tls-pw-opt, tls-cert-opt-pw-opt, tls-pw-opt, tls-pw-req, tls-cert-pw-opt, or tls-cert-and-pw. Default mode is no-tls-pw-opt. Refer to the top level discussion of the Interface section for further details.
        required: false
        default: no-tls-pw-opt
        choices:
            - no-tls-pw-opt
            - no-tls-pw-req
            - unauth-tls-pw-opt
            - tls-cert-opt-pw-opt
            - tls-pw-opt
            - tls-pw-req
            - tls-cert-pw-opt
            - tls-cert-and-pw
        type: str
    name:
        description: The name of the interface. Not valid for interface_type nae.
        required: false
        default: none
        type: str
    network_interface:
        description: Defines what ethernet adapter the interface should listen to, use "all" for all.
        default: all
        required: false
        type: str
    registration_token:
        description: Registration token in case auto registration is true.
        default: none
        required: false
        type: str
    external_trusted_cas:
        description: Collection of external CA IDs to trust for client authentication.
        default: empty arr
        required: false
        type: arr
    local_trusted_cas:
        description: Collection of local CA IDs to trust for client authentication.
        default: empty arr
        required: false
        type: arr
'''

EXAMPLES = '''
- name: "Create Interface"
  thales.ciphertrust.config_interface_nae_post:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    port: 9005
    cert_user_field: "CN"
    mode: "tls-cert-pw-opt"
    auto_gen_ca_id: "kylo:kylo:naboo:localca:6a508c29-a385-440c-b4f4-787b91a4a883"
    auto_registration: True
    local_trusted_cas:
        - "kylo:kylo:naboo:localca:6a508c29-a385-440c-b4f4-787b91a4a883"
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
                port=dict(type='int', required=True),
                auto_gen_ca_id=dict(type='str', required=False, default=""),
                auto_registration=dict(type='bool', required=False, default=False),
                cert_user_field=dict(type='str', options=['CN','SN','E','E_ND','UID','OU'], required=False, default="CN"),
                custom_uid_size=dict(type='int', required=False, default=None),
                custom_uid_v2=dict(type='bool', required=False, default=True),
                default_connection=dict(type='str', required=False, default="local_account"),
                interface_type=dict(type='str', required=False, choices=['web', 'kmip', 'nae', 'snmp'], default="nae"),
                kmip_enable_hard_delete=dict(type='int', options=[0,1], required=False, default=0),
                maximum_tls_version=dict(type='str', required=False, choices=['tls_1_0', 'tls_1_1', 'tls_1_2', 'tls_1_3'], default="tls_1_2"),
                minimum_tls_version=dict(type='str', required=False, choices=['tls_1_0', 'tls_1_1', 'tls_1_2', 'tls_1_3'], default="tls_1_2"),
                mode=dict(type='str', choices=['no-tls-pw-opt','no-tls-pw-req','unauth-tls-pw-opt','unauth-tls-pw-req','tls-cert-opt-pw-opt','tls-pw-opt','tls-pw-req','tls-cert-pw-opt','tls-cert-and-pw'], required=False, default=""),
                name=dict(type='str', required=False, default=""),
                network_interface=dict(type='str', required=False, default="all"),
                registration_token=dict(type='str', required=False, default=""),
                external_trusted_cas=dict(type='list', element='str', required=False, default=[]),
                local_trusted_cas=dict(type='list', element='str', required=False, default=[]),
            ),
        )

    localNode = module.params.get('localNode');
    port = module.params.get('port');
    auto_gen_ca_id = module.params.get('auto_gen_ca_id');
    auto_registration = module.params.get('auto_registration');
    cert_user_field = module.params.get('cert_user_field');
    custom_uid_size = module.params.get('custom_uid_size');
    custom_uid_v2 = module.params.get('custom_uid_v2');
    default_connection = module.params.get('default_connection');
    interface_type = module.params.get('interface_type');
    kmip_enable_hard_delete = module.params.get('kmip_enable_hard_delete');
    maximum_tls_version = module.params.get('maximum_tls_version');
    minimum_tls_version = module.params.get('minimum_tls_version');
    mode = module.params.get('mode');
    name = module.params.get('name');
    network_interface = module.params.get('network_interface');
    registration_token = module.params.get('registration_token');
    external_trusted_cas = module.params.get('external_trusted_cas');
    local_trusted_cas = module.params.get('local_trusted_cas');

    if interface_type == 'web' and mode != 'tls-cert-opt-pw-opt':
        module.fail_json(msg="interface type web should have mode tls-cert-opt-pw-opt")

    if interface_type == 'kmip' and mode not in ['tls-pw-opt', 'tls-pw-req', 'tls-cert-pw-opt', 'tls-cert-and-pw']:
        module.fail_json(msg="interface type kmip should have mode tls-pw-opt, tls-pw-req, tls-cert-pw-opt or tls-cert-and-pw")

    if interface_type == 'snmp' and mode != '':
        mode = '';

    if interface_type == 'ssh' and mode != '':
        mode = '';

    if interface_type == 'nae' and name != '':
        name = '';

    result = dict(
        changed=False,
    )

    response = new(
        node=localNode,
        port=port,
        auto_gen_ca_id=auto_gen_ca_id,
        auto_registration=auto_registration,
        cert_user_field=cert_user_field,
        custom_uid_size=custom_uid_size,
        custom_uid_v2=custom_uid_v2,
        default_connection=default_connection,
        interface_type=interface_type,
        kmip_enable_hard_delete=kmip_enable_hard_delete,
        maximum_tls_version=maximum_tls_version,
        minimum_tls_version=minimum_tls_version,
        mode=mode,
        name=name,
        network_interface=network_interface,
        registration_token=registration_token,
        external_trusted_cas=external_trusted_cas,
        local_trusted_cas=local_trusted_cas,
    )

    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
