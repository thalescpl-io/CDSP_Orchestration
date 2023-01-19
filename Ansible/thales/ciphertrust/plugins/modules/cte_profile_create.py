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
from ansible_collections.thales.ciphertrust.plugins.module_utils.cte import create_cte_profile

DOCUMENTATION = '''
---
module: cte_profile_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create profile for CTE API
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
        description: Name of the CTE profile
        required: true
        type: str
    cache_settings:
        description: Cache settings for the server
        required: false
        type: dict
    concise_logging:
        description: Whether to allow concise logging
        required: false
        type: bool
    connect_timeout:
        description: Connect timeout in seconds. Valid values are 5 to 150
        required: false
        type: int
    profileDescription:
        description: Description of the profile resource
        required: false
        type: str
    duplicate_settings:
        description: Duplicate setting parameters
        required: false
        type: dict
    file_settings:
        description: File settings for the profile
        required: false
        type: dict
    ldt_qos_cap_cpu_allocation:
        description: Whether to allow CPU allocation for Quality of Service (QoS) capabilities
        required: false
        type: bool
    ldt_qos_cpu_percent:
        description: CPU application percentage if ldt_qos_cap_cpu_allocation is true. Valid values are 0 to 100
        required: false
        type: int
    ldt_qos_rekey_option:
        description: Rekey option and applicable options are RekeyRate and CPU
        required: false
        type: str
    ldt_qos_rekey_rate:
        description: Rekey rate in terms of MB/s. Valid values are 0 to 32767
        required: false
        type: int
    ldt_qos_schedule:
        description: Type of QoS schedule
        required: false
        type: str
        choices:
            - CUSTOM
            - CUSTOM_WITH_OVERWRITE
            - ANY_TIME
            - WEEKNIGHTS
            - WEEKENDS
    management_service_logger:
        description: Logger configurations for the management service
        required: false
        type: dict
    metadata_scan_interval:
        description: Time interval in seconds to scan files under guard point. Default value is 600
        required: false
        type: int
    mfa_exempt_user_set_id:
        description: ID of the user set to be exempted from MFA. MFA will not be enforced on the users of this set
        required: false
        type: str
    oidc_connection_id:
        description: ID of the OIDC connection
        required: false
        type: str
    policy_evaluation_logger:
        description: Logger configurations for policy evaluation
        required: false
        type: dict
    qos_schedules:
        description: Schedule of QoS capabilities
        required: false
        type: list
    security_admin_logger:
        description: Logger configurations for security administrators
        required: false
        type: str
    server_settings:
        description: Server configuration of cluster nodes. These settings are allowed only in cluster environment
        required: false
        type: list
    syslog_settings:
        description: Parameters to configure the Syslog server
        required: false
        type: dict
    system_admin_logger:
        description: Logger configurations for the System administrator
        required: false
        type: dict
    upload_settings:
        description: Configure log upload to the Syslog server
        required: false
        type: dict
'''

EXAMPLES = '''
- name: "Create CTE CSI Storage Group"
  thales.ciphertrust.cte_profile_create:
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
    cache_setting = dict(
        max_files=dict(type='int', required=False),
        max_space=dict(type='int', required=False)
    )
    duplicate_setting = dict(
        suppress_interval=dict(type='int', required=False),
        suppress_threshold=dict(type='int', required=False)
    )
    file_setting = dict(
        allow_purge=dict(type='bool', required=False),
        file_threshold=dict(type='str', options=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'], required=False),
        max_file_size=dict(type='int', required=False),
        max_file_size=dict(type='int', required=False)
    )
    logger = dict (
        duplicates=dict(type='str', options=['ALLOW', 'SUPPRESS'], required=False),
        file_enabled=dict(type='bool', required=False),
        syslog_enabled=dict(type='bool', required=False),
        threshold=dict(type='str', options=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'], required=False),
        upload_enabled=dict(type='bool', required=False)
    )
    qos_schedule=dict(
        end_time_hour=dict(type='int', required=False),
        end_time_min=dict(type='int', required=False),
        end_weekday=dict(type='str', required=False, options=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']),
        start_time_hour=dict(type='int', required=False),
        start_time_min=dict(type='int', required=False),
        start_weekday=dict(type='str', required=False, options=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    )
    server_setting = dict(
        hostName=dict(type='str', required=False),
        priority=dict(type='int', required=False)
    )
    server = dict(
        caCertificate=dict(type='str', required=False),
        certificate=dict(type='str', required=False),
        message_format=dict(type='str', required=False, options=['CEF', 'LEEF', 'RFC5424', 'PLAIN']),
        name=dict(type='str', required=False),
        port=dict(type='int', required=False),
        privateKey=dict(type='str', required=False),
        protocol=dict(type='str', required=False, options=['TCP', 'UDP', 'TLS'])
    )
    syslog_setting = dict(
        local=dict(type='bool', required=False),
        servers=dict(type='list', element='dict', options=server, required=False),
        syslog_threshold=dict(type='str', required=False)
    )
    upload_setting = dict(
        connection_timeout=dict(type='int', required=False),
        drop_if_busy=dict(type='bool', required=False),
        job_completion_timeout=dict(type='int', required=False),
        max_interval=dict(type='int', required=False),
        max_messages=dict(type='int', required=False),
        min_interval=dict(type='int', required=False),
        upload_threshold=dict(type='str', options=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'], required=False)
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
                cache_settings=dict(type='dict', options=cache_setting, required=False),
                concise_logging=dict(type='bool', required=False),
                connect_timeout=dict(type='int', required=False),
                profileDescription=dict(type='str', required=False),
                duplicate_settings=dict(type='dict', options=duplicate_setting, required=False),
                file_settings=dict(type='dict', options=file_setting, required=False),
                ldt_qos_cap_cpu_allocation=dict(type='bool', required=False),
                ldt_qos_cpu_percent=dict(type='int', required=False),
                ldt_qos_rekey_option=dict(type='str', required=False),
                ldt_qos_rekey_rate=dict(type='int', required=False),
                ldt_qos_schedule=dict(type='str', options=['CUSTOM', 'CUSTOM_WITH_OVERWRITE', 'ANY_TIME', 'WEEKNIGHTS', 'WEEKENDS'], required=False),
                management_service_logger=dict(type='dict', options=logger, required=False),
                metadata_scan_interval=dict(type='int', default=600, required=False),
                mfa_exempt_user_set_id=dict(type='str', required=False),
                oidc_connection_id=dict(type='str', required=False),
                policy_evaluation_logger=dict(type='dict', options=logger, required=False),
                qos_schedules=dict(type='list', element='dict', options=qos_schedule, required=False),
                security_admin_logger=dict(type='dict', options=logger, required=False),
                server_settings=dict(type='list', element='dict', options=server_setting, required=False),
                syslog_settings=dict(type='list', element='dict', options=syslog_setting, required=False),
                system_admin_logger=dict(type='dict', options=logger, required=False),
                upload_settings=dict(type='dict', options=upload_setting, required=False),
            ),
        )

    localNode = module.params.get('localNode');
    name = module.params.get('name');
    profileDescription = module.params.get('profileDescription');
    cache_settings = module.params.get('cache_settings');
    concise_logging = module.params.get('concise_logging');
    connect_timeout = module.params.get('connect_timeout');
    duplicate_settings = module.params.get('duplicate_settings');
    file_settings = module.params.get('file_settings');
    ldt_qos_cap_cpu_allocation = module.params.get('ldt_qos_cap_cpu_allocation');
    ldt_qos_cpu_percent = module.params.get('ldt_qos_cpu_percent');
    ldt_qos_rekey_option = module.params.get('ldt_qos_rekey_option');
    ldt_qos_rekey_rate = module.params.get('ldt_qos_rekey_rate');
    ldt_qos_schedule = module.params.get('ldt_qos_schedule');
    management_service_logger = module.params.get('management_service_logger');
    metadata_scan_interval = module.params.get('metadata_scan_interval');
    mfa_exempt_user_set_id = module.params.get('mfa_exempt_user_set_id');
    oidc_connection_id = module.params.get('oidc_connection_id');
    policy_evaluation_logger = module.params.get('policy_evaluation_logger');
    qos_schedules = module.params.get('qos_schedules');
    security_admin_logger = module.params.get('security_admin_logger');
    server_settings = module.params.get('server_settings');
    syslog_settings = module.params.get('syslog_settings');
    system_admin_logger = module.params.get('system_admin_logger');
    upload_settings = module.params.get('upload_settings');

    result = dict(
        changed=False,
    )

    response = create_cte_profile(
            node=localNode,
            name=name,
            profileDescription=profileDescription,
            cache_settings=cache_settings,
            concise_logging=concise_logging,
            connect_timeout=connect_timeout,
            duplicate_settings=duplicate_settings,
            file_settings=file_settings,
            ldt_qos_cap_cpu_allocation=ldt_qos_cap_cpu_allocation,
            ldt_qos_cpu_percent=ldt_qos_cpu_percent,
            ldt_qos_rekey_option=ldt_qos_rekey_option,
            ldt_qos_rekey_rate=ldt_qos_rekey_rate,
            ldt_qos_schedule=ldt_qos_schedule,
            management_service_logger=management_service_logger,
            metadata_scan_interval=metadata_scan_interval,
            mfa_exempt_user_set_id=mfa_exempt_user_set_id,
            oidc_connection_id=oidc_connection_id,
            policy_evaluation_logger=policy_evaluation_logger,
            qos_schedules=qos_schedules,
            security_admin_logger=security_admin_logger,
            server_settings=server_settings,
            syslog_settings=syslog_settings,
            system_admin_logger=system_admin_logger,
            upload_settings=upload_settings
        )
    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()