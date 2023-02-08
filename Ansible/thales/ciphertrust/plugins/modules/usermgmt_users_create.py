#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.users import new

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
            ),
        )

    localNode = module.params.get('localNode');
    certificate_subject_dn = module.params.get('certificate_subject_dn');
    connection = module.params.get('connection');
    email = module.params.get('email');
    enable_cert_auth = module.params.get('enable_cert_auth');
    is_domain_user = module.params.get('is_domain_user');
    prevent_ui_login = module.params.get('prevent_ui_login');
    name = module.params.get('name');
    password = module.params.get('password');
    password_change_required = module.params.get('password_change_required');
    user_id = module.params.get('user_id');
    username = module.params.get('username');

    result = dict(
        changed=False,
    )

    response = new(
        node=localNode,
        cert_sub_dn=certificate_subject_dn,
        conn=connection,
        email=email,
        enable_cert_auth_bool=enable_cert_auth,
        is_domain_user_bool=is_domain_user,
        prevent_ui_login_bool=prevent_ui_login,
        name=name,
        pwd=password,
        pwd_change_reqd_bool=password_change_required,
        user_id=user_id,
        username=username,
    )

    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
