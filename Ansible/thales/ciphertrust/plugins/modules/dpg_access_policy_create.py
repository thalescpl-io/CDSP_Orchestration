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
    user_set_policy = dict(
            user_set_name=dict(type='str', required=True),
            reveal_type=dict(type='str', required=True),
            masking_format_name=dict(type='str', required=False),
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
                userSetPolicies=dict(type='list', elements='dict', options=user_set_policy, required=True),
                name=dict(type='str', required=True),
                default_reveal_type=dict(type='str', required=True),
                default_error_replacement_value=dict(type='str', required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    default_reveal_type = module.params.get('default_reveal_type');
    default_error_replacement_value = module.params.get('default_error_replacement_value');
    userSetPolicies = module.params.get('userSetPolicies');

    result = dict(
        changed=False,
    )

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/access-policies",
            verify=False,
        )

    requestObj=dict(
        )

    requestObj['name'] = name
    requestObj['default_reveal_type'] = default_reveal_type
    #requestObj['default_error_replacement_value'] = default_error_replacement_value
    arrUsersetPolicies = []

    #Creating the user_set_policy json object
    for userSetPolicy in userSetPolicies:
        dictUsersetPolicy=dict()
        dictUsersetPolicy["reveal_type"] = userSetPolicy["reveal_type"]
        
        #Convert userset name to userset ID to attach to the access policy
        cmSessionObject_getUsersetId = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/user-sets",
            verify=False,
        )
        
        response = requests.get(cmSessionObject_getUsersetId["url"],
              headers=cmSessionObject_getUsersetId["headers"],
              verify=False)
        
        resources = response.json()["resources"]
        
        for resource in resources:
            #we found the user set with name provided in the task params
            if userSetPolicy["user_set_name"] in resource["name"]:
                user_set_id = resource["id"]
                dictUsersetPolicy["user_set_id"] = user_set_id

        #For the Masked Value reveal_type, add the masking format
        #Fetch the masking_format ID from the name provided in the playbook vars
        if "Masked Value" in userSetPolicy["reveal_type"]:
            cmSessionObject_getMaskFormatId = CMAPIObject(
                    cm_api_user=localNode["user"],
                    cm_api_pwd=localNode["password"],
                    cm_url=localNode["server_ip"],
                    cm_api_endpoint="data-protection/masking-formats",
                    verify=False,
                )

            response = requests.get(cmSessionObject_getMaskFormatId["url"],
                    headers=cmSessionObject_getMaskFormatId["headers"],
                    verify=False)

            resources = response.json()["resources"]

            for resource in resources:
                #we found the masking format with name provided in the task params
                if userSetPolicy["masking_format_name"] in resource["name"]:
                    masking_format_id = resource["id"]
                    dictUsersetPolicy["masking_format_id"] = masking_format_id

        arrUsersetPolicies.append(dictUsersetPolicy)

    requestObj["user_set_policy"] = arrUsersetPolicies

    payload_json = json.dumps(requestObj)
    result['payload'] = payload_json
    try:
      response = requests.post(cmSessionObject["url"], 
              headers=cmSessionObject["headers"], 
              json = json.loads(payload_json), 
              verify=False)
      result['resp'] = response.json()
      result['success'] = 'Protection policy creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
