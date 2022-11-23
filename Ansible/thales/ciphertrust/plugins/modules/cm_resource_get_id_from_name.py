#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import CMAPIObject, GETIdByName

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
                name=dict(type='str', required=True),
                resource_type=dict(type='str', choices=['keys', 'protection-policies', 'access-policies', 'user-sets', 'interfaces', 'character-sets', 'users', 'dpg-policies', 'client-profiles'], required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    resource_type = module.params.get('resource_type');

    result = dict(
        changed=False,
    )

    endpoint = '';
    #Create the API end point based on the resource_type
    if resource_type == "keys":
        endpoint = 'vault/keys2';
    elif resource_type == "protection-policies":
        endpoint = 'data-protection/protection-policies';
    elif resource_type == "access-policies":
        endpoint = 'data-protection/access-policies';
    elif resource_type == "user-sets":
        endpoint = 'data-protection/user-sets';
    elif resource_type == "interfaces":
        endpoint = 'configs/interfaces';
    elif resource_type == "character-sets":
        endpoint = 'data-protection/character-sets';
    elif resource_type == "users":
        endpoint = 'usermgmt/users';
    elif resource_type == "dpg-policies":
        endpoint = 'data-protection/dpg-policies';
    elif resource_type == "client-profiles":
        endpoint = 'data-protection/client-profiles';
    else:
        module.fail_json(msg='resource_type not supported yet')

    try:
        response = GETIdByName(
                name=name,
                cm_node=localNode,
                cm_api_endpoint=endpoint
            )
        result['response'] = response
    except requests.exceptions.RequestException as err:
        result['failed'] = True
        result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
