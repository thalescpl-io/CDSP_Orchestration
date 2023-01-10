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
from ansible_collections.thales.ciphertrust.plugins.module_utils.connections import create

DOCUMENTATION = '''
---
module: usermgmt_connection_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with creating LDAP type connections
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
        description: A friendly name for your connection which users will see when they login. It is ignored during a connection test.
        required: true
        type: str
    strategy:
        description: Strategy of connection (ldap or oidc)
        required: true
        choices:
            - ldap
            - oidc
        type: str
    ldap_options:
        description: Options for connecting to an LDAP server.
        required: false
        type: dict
    oidc_options:
        description: Options for connecting to an external OpenID Connect server
        required: false
        type: dict
    options:
        description: Deprecated, replaced by 'ldap_options'.
        required: false
        type: dict
'''

EXAMPLES = '''
- name: "Create Connection"
  thales.ciphertrust.usermgmt_connection_create:
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
    jwk = dict(
            alg=dict(type='str', required=False),
            e=dict(type='str', required=False),
            kid=dict(type='str', required=False),
            kty=dict(type='str', required=False),
            nameuse=dict(type='str', required=False)
        )
    ldapOptions = dict(
            root_dn=dict(type='str', required=True),
            server_url=dict(type='str', required=True),
            uid_field=dict(type='str', required=True),
            bind_dn=dict(type='str', required=False),
            bind_password=dict(type='str', required=False),
            group_base_dn=dict(type='str', required=False),
            group_filter=dict(type='str', required=False),
            group_id_field=dict(type='str', required=False),
            group_member_field=dict(type='str', required=False),
            guid_field=dict(type='str', required=False),
            insecure_skip_verify=dict(type='bool', required=False, default=False),
            root_cas=dict(type='list', element='str', required=False, default=[]),
            search_filter=dict(type='str', required=False),
            user_dn_field=dict(type='str', required=False)
        )
    oidcOptions = dict(
            client_id=dict(type='str', required=True),
            redirect_uris=dict(type='list', element='str', required=False, default=[]),
            authorization_uri=dict(type='str', required=True),
            discovery_uri=dict(type='str', required=True),
            jwks=dict(type='list', element='dict', options=jwk, required=False, default=[]),
            redirect_uri=dict(type='str', required=True)
        )
    optionsDeprecated = dict(
            root_dn=dict(type='str', required=True),
            server_url=dict(type='str', required=True),
            uid_field=dict(type='str', required=True),
            bind_dn=dict(type='str', required=False),
            bind_password=dict(type='str', required=False),
            group_base_dn=dict(type='str', required=False),
            group_filter=dict(type='str', required=False),
            group_id_field=dict(type='str', required=False),
            group_member_field=dict(type='str', required=False),
            guid_field=dict(type='str', required=False),
            insecure_skip_verify=dict(type='bool', required=False, default=False),
            root_cas=dict(type='list', element='str', required=False, default=[]),
            search_filter=dict(type='str', required=False),
            user_dn_field=dict(type='str', required=False)
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
                strategy=dict(type='str', options=['ldap', 'oidc'] required=True),
                ldap_options=dict(type='dict', options=ldapOptions, required=False),
                oidc_options=dict(type='dict', options=oidcOptions, required=False),
                options=dict(type='dict', options=optionsDeprecated, required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    strategy =  module.params.get('strategy');
    ldap_options =  module.params.get('ldap_options');
    oidc_options =  module.params.get('oidc_options');
    options =  module.params.get('options');

    result = dict(
        changed=False,
    )

    response = create(
            node=localNode,
            name=name,
            strategy=strategy,
            ldap_options=ldap_options,
            oidc_options=oidc_options,
            options=options
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()