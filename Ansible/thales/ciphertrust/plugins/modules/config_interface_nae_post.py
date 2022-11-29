#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.interfaces import new

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
                cert_user_field=dict(type='str', required=False, default=""),
                custom_uid_size=dict(type='int', required=False, default=None),
                custom_uid_v2=dict(type='bool', required=False, default=True),
                default_connection=dict(type='str', required=False, default="local_account"),
                interface_type=dict(type='str', required=False, choices=['web', 'kmip', 'nae', 'snmp'], default="nae"),
                kmip_enable_hard_delete=dict(type='int', required=False, default=None),
                maximum_tls_version=dict(type='str', required=False, choices=['tls_1_0', 'tls_1_1', 'tls_1_2', 'tls_1_3'], default="tls_1_2"),
                minimum_tls_version=dict(type='str', required=False, choices=['tls_1_0', 'tls_1_1', 'tls_1_2', 'tls_1_3'], default="tls_1_2"),
                mode=dict(type='str', required=False, default=""),
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
