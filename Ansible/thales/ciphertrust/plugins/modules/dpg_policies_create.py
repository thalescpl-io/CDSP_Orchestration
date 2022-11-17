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
    token = dict(
            name=dict(type='str', required=True),
            operation=dict(type='str', required=True),
            protection_policy=dict(type='str', required=True),
            access_policy=dict(type='str', required=False),
        )
    endpoint = dict(
            rest_op_type=dict(type='str', required=True),
            api_url=dict(type='str', required=True),
            tokens=dict(type='list', elements='dict', options=token, required=True),
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
                proxy_config=dict(type='list', elements='dict', options=endpoint, required=True),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    name = module.params.get('name');
    localNode = module.params.get('localNode');
    proxy_config = module.params.get('proxy_config');

    result = dict(
        changed=False,
    )

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/dpg-policies",
            verify=False,
        )

    requestObj=dict(
        )

    requestObj['name'] = name
    proxyConfigs = []

    for proxy_config_unit in proxy_config:
        dictProxyConfig=dict()
        dictProxyConfig["api_url"]=proxy_config_unit["api_url"]
        if "POST" in proxy_config_unit["rest_op_type"]:
            tokens=proxy_config_unit["tokens"]
            arrTokens=[]
            for token in tokens:
                dictToken=dict(
                        name=token["name"],
                        operation=token["operation"],
                        protection_policy=token["protection_policy"],
                    )
                arrTokens.append(dictToken)

            dictProxyConfig["json_request_post_tokens"]=arrTokens
            proxyConfigs.append(dictProxyConfig)

        if "GET" in proxy_config_unit["rest_op_type"]:
            tokens=proxy_config_unit["tokens"]
            arrTokens=[]
            for token in tokens:
                dictToken=dict(
                        name=token["name"],
                        operation=token["operation"],
                        protection_policy=token["protection_policy"],
                        access_policy=token["access_policy"],
                    )
                arrTokens.append(dictToken)

            dictProxyConfig["json_request_get_tokens"]=arrTokens
            proxyConfigs.append(dictProxyConfig)

    requestObj["proxy_config"]=proxyConfigs

    payload_json = json.dumps(requestObj)
    try:
      response = requests.post(cmSessionObject["url"], 
              headers=cmSessionObject["headers"], 
              json = json.loads(payload_json), 
              verify=False)
      if "codeDesc" in response.json():
          codeDesc=response.json()["codeDesc"]
          if 'NCERRConflict' in codeDesc:
              policyId=''
              result['message'] = 'DPG Policy with same name already exists, fetching ID'
              getDPGProfiles = requests.get(cmSessionObject["url"],
                  headers=cmSessionObject["headers"],
                  verify=False)
              dpgProfiles=getDPGProfiles.json()["resources"]
              for dpgProfile in dpgProfiles:
                  if name in dpgProfile["name"]:
                      dpgProfileId=dpgProfile["id"]
              result['policyId'] = dpgProfileId
      else:
          result['policyId'] = response.json()["id"]
          result['success'] = 'DPG policy creation successfull!'
    except requests.exceptions.RequestException as err:
      result['failed'] = True
      result['error'] = err

    module.exit_json(**result)

if __name__ == '__main__':
    main()
