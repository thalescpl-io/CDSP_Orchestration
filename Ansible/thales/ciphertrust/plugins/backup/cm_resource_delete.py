#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import CMAPIObject

def main():
    resource = dict(
            resource_type=dict(type='str', required=True),
            names=dict(type='list', elements='str', required=True),
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
                resources=dict(type='list', elements='dict', options=resource, required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    resources =  module.params.get('resources');

    result = dict(
        changed=False,
    )

    for resourceNode in resources:
        cm_api_endpoint_category = ''
        if "dpg-policies" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/dpg-policies"
        if "client-profiles" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/client-profiles"
        if "access-policies" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/access-policies"
        if "masking-formats" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/masking-formats"
        if "user-sets" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/user-sets"
        if "users" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "usermgmt/users"
        if "protection-policies" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "data-protection/protection-policies"
        if "character-sets" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "character-sets"
        if "interfaces" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "configs/interfaces"
        if "keys2" in resourceNode["resource_type"]:
            cm_api_endpoint_category = "vault/keys2"

        cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint=cm_api_endpoint_category,
            verify=False,
        )
        #result['data'] = resourceNode["names"]
        try:
            getResources = requests.get(cmSessionObject["url"],
                headers=cmSessionObject["headers"],
                verify=False)
            result['api_resp']=getResources.json()["resources"]
              #for item in listResources:
              #    if name in item["name"]:
              #        resourceId = item["id"]
        except requests.exceptions.RequestException as err:
            result['failed'] = True
            result['error'] = err

        for name in resourceNode["names"]:
            result['name']=name
            #result['output']=resResource
            #result['resourceId'] = resourceId
            #Delete resource by ID
            #try:
            #  response = requests.delete(cmSessionObject["url"] + '/' + resourceId, 
            #          headers=cmSessionObject["headers"], 
            #          verify=False
            #      )
            #  result['response'] = response.json()
            #  result['success'] = 'Delete of resource successful'
            #except requests.exceptions.RequestException as err:
            #  result['failed'] = True
            #  result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
