#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_protection_policy

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
                algorithm=dict(type='str', required=True),
                key=dict(type='str', required=True),
                name=dict(type='str', required=True),
                allow_single_char_input=dict(type='bool', required=False, default=False),
                character_set_id=dict(type='str', required=False, default=""),
                iv=dict(type='str', required=False, default=""),
                tweak=dict(type='str', required=False, default=""),
                tweak_algorithm=dict(type='str', choices=['SHA1', 'SHA256', 'None'], required=False, default=""),
            ),
        )

    localNode = module.params.get('localNode');
    algorithm = module.params.get('algorithm');
    key = module.params.get('key');
    name = module.params.get('name');
    allow_single_char_input = module.params.get('allow_single_char_input');
    character_set_id = module.params.get('character_set_id');
    iv = module.params.get('iv');
    tweak = module.params.get('tweak');
    tweak_algorithm = module.params.get('tweak_algorithm');
    
    result = dict(
        changed=False,
    )

    response = create_protection_policy(
        node=localNode,
        algorithm=algorithm,
        key=key,
        name=name,
        allow_single_char_input=allow_single_char_input,
        character_set_id=character_set_id,
        iv=iv,
        tweak=tweak,
        tweak_algorithm=tweak_algorithm
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()

