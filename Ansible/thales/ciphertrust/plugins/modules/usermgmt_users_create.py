#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2022 Thales Group. All rights reserved.
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
from ansible_collections.thales.ciphertrust.plugins.module_utils.users import new

module = None

DOCUMENTATION = '''
---
module: usermgmt_users_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create User API
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
        description: Full name of the user.
        required: false
        type: str
        default: null
    app_metadata:
        description: A schema-less object, which can be used by applications to store information about the resource. app_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles.
        required: false
        type: dict
        default: null
    certificate_subject_dn:
        description: The Distinguished Name of the user in certificate
        required: false
        type: str
        default: null
    connection:
        description: This attribute is required to create a user, but is not included in user resource responses. Can be the name of a connection or "local_account" for a local user, defaults to "local_account".
        required: false
        type: str
        default: null
    email:
        description: E-mail of the user
        required: false
        type: str
        default: null
    enable_cert_auth:
        description: Enable certificate based authentication flag. If set to true, the user will be able to login using certificate.
        required: false
        type: bool
        default: false
    is_domain_user:
        description: This flag can be used to create the user in a non-root domain where user management is allowed.
        required: false
        type: bool
        default: false
    prevent_ui_login:
        description: Part of login_flags for controlling user's login behavior.
        required: false
        type: bool
        default: false
    password:
        description: The password used to secure the users account. Allowed passwords are defined by the password policy. This attribute is required to create a local user, but is not included in user resource responses.
        required: false
        type: str
        default: null
    password_change_required:
        description: Password change required flag. If set to true, user will be required to change their password on next successful login.
        required: false
        type: bool
        default: false
    user_id:
        description: The user_id is the ID of an existing root domain user. This field is used only when adding an existing root domain user to a different domain.
        required: false
        type: str
        default: null
    user_metadata:
        description: A schema-less object, which can be used by applications to store information about the resource. user_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences.
        required: false
        type: dict
        default: null
    username:
        description: The login name of the user. This is the identifier used to login. This attribute is required to create a user, but is omitted when getting or listing user resources. It cannot be updated. This attribute may also be used (instead of the user_id) when adding an existing root domain user to a different domain.
        required: false
        type: str
        default: null
'''

EXAMPLES = '''
- name: "Create DPG Protection Policy"
  thales.ciphertrust.dpg_protection_policy_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    username: "john.doe"
    password: "cmPassw0rd!"
    email: "john.doe@example.com"
    name: "John Doe"
'''

RETURN = '''

'''

argument_spec = dict(
    # module function variables
    # localNode=dict(type='dict', options=localNode, required=True),
    certificate_subject_dn=dict(type='str', required=False, default=""),
    connection=dict(type='str', required=False, default=""),
    email=dict(type='str', required=False, default=""),
    enable_cert_auth=dict(type='bool', required=False, default=False),
    is_domain_user=dict(type='bool', required=False, default=False),
    prevent_ui_login=dict(type='bool', required=False, default=False),
    name=dict(type='str', required=False, default=""),
    password=dict(type='str', required=True),
    password_change_required=dict(type='bool', required=False, default=False),
    user_id=dict(type='str', required=False, default=""),
    username=dict(type='str', required=True),
)

def setup_module_object():
    module = ThalesCipherTrustModule(
        argument_spec=argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,

    )
    return module

def main():
    
    module = setup_module_object()

    result = dict(
        changed=False,
    )

    response = new(
        node=module.params.get('localNode'),
        cert_sub_dn=module.params.get('certificate_subject_dn'),
        conn=module.params.get('connection'),
        email=module.params.get('email'),
        enable_cert_auth_bool=module.params.get('enable_cert_auth'),
        is_domain_user_bool=module.params.get('is_domain_user'),
        prevent_ui_login_bool=module.params.get('prevent_ui_login'),
        name=module.params.get('name'),
        pwd=module.params.get('password'),
        pwd_change_reqd_bool=module.params.get('password_change_required'),
        user_id=module.params.get('user_id'),
        username=module.params.get('username'),
    )

    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
