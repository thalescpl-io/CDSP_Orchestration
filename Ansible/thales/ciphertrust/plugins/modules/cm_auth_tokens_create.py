#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            cm_hostname=dict(type='str', required=True),
            cm_username=dict(type='str', required=True),
            cm_password=dict(type='str', required=True),
        ),
    )
    cm_hostname = module.params.get('cm_hostname');
    cm_username = module.params.get('cm_username');
    cm_password = module.params.get('cm_password');

    result = dict(
        changed=False,
    )

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    base_url = 'https://'+cm_hostname+'/api/v1/'
    auth_payload = {
            "grant_type":"password",
            "username":cm_username,
            "password":cm_password,
        }
    response_token_request = requests.post(base_url + 'auth/tokens', json = auth_payload, verify=False)
    result['token'] = response_token_request.json()["jwt"]

    module.exit_json(**result)

if __name__ == '__main__':
    main()

