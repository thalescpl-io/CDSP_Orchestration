#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.data_protection import create_dpg_policy

def main():
    token = dict(
            name=dict(type='str', required=True),
            operation=dict(type='str', required=True),
            protection_policy=dict(type='str', required=True),
            access_policy=dict(type='str', required=False),
        )
    endpoint = dict(
            rest_op_type=dict(type='str', required=True),
            api_url=dict(type='str', required=False),
            destination_url=dict(type='str', required=False),
            tokens=dict(type='list', elements='dict', options=token, required=False, default=[]),
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
                policyDescription=dict(type='str', required=False, default=""),
                proxy_config=dict(type='list', elements='dict', options=endpoint, required=False, default=[]),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    policyDescription =  module.params.get('policyDescription');
    proxy_config = module.params.get('proxy_config');

    result = dict(
        changed=False,
    )

    response = create_dpg_policy(
        node=localNode,
        name=name,
        policyDescription=policyDescription,
        proxy_config=proxy_config
    )

    result["response"] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
