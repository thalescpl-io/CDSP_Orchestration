#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_character_set

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
                charsetRange=dict(type='list', element='str', required=True),
                encoding=dict(type='str', required=False, default=""),
            ),
        )

    localNode = module.params.get('localNode');
    name = module.params.get('name');
    charsetRange = module.params.get('charsetRange');
    encoding = module.params.get('encoding');
    
    result = dict(
        changed=False,
    )

    response = create_character_set(
        node=localNode,
        name=name,
        charsetRange=charsetRange,
        encoding=encoding
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()

