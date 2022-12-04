#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_access_policy

def main():
    user_set_policy = dict(
            user_set_id=dict(type='str', required=False, default=""),
            error_replacement_value=dict(type='str', required=False),
            reveal_type=dict(type='str', choices=['Error Replacement Value', 'Masked Value', 'Ciphertext', 'Plaintext'], required=False, default=""),
            masking_format_id=dict(type='str', required=False),
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
                user_set_policies=dict(type='list', elements='dict', options=user_set_policy, required=False, default=[]),
                default_error_replacement_value=dict(type='str', required=False, default=""),
                default_masking_format_id=dict(type='str', required=False, default=""),
                default_reveal_type=dict(type='str', choices=['Error Replacement Value', 'Masked Value', 'Ciphertext', 'Plaintext'], required=False, default=""),
                access_policy_description=dict(type='str', required=False, default=""),
                name=dict(type='str', required=False, default=""),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    default_reveal_type = module.params.get('default_reveal_type');
    default_error_replacement_value = module.params.get('default_error_replacement_value');
    user_set_policies = module.params.get('user_set_policies');
    default_masking_format_id = module.params.get('default_masking_format_id');
    access_policy_description = module.params.get('access_policy_description');

    policies=[]
    for policy in user_set_policies:
        userset_policy = dict()
        if policy['reveal_type'] == 'Ciphertext':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
        if policy['reveal_type'] == 'Masked Value':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
            userset_policy['masking_format_id'] = policy['masking_format_id'];
        if policy['reveal_type'] == 'Error Replacement Value':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
            userset_policy['error_replacement_value'] = policy['error_replacement_value'];
        if policy['reveal_type'] == 'Plaintext':
            userset_policy['reveal_type'] = policy['reveal_type'];
            userset_policy['user_set_id'] = policy['user_set_id'];
        policies.append(userset_policy)

    result = dict(
        changed=False,
    )

    response = create_access_policy(
            node=localNode,
            name=name,
            default_reveal_type=default_reveal_type,
            default_error_replacement_value=default_error_replacement_value,
            user_set_policies=policies,
            default_masking_format_id=default_masking_format_id,
            access_policy_description=access_policy_description
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
