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
                key=dict(type='str', required=True),
                tweak=dict(type='str', required=False),
                tweak_algorithm=dict(type='str', required=False),
                algorithm=dict(type='str', required=True),
                character_set_id=dict(type='str', required=False),
                localNode=dict(type='dict', options=localNode, required=True),
            ),
        )

    localNode = module.params.get('localNode');
    name =  module.params.get('name');
    key =  module.params.get('key');
    tweak =  module.params.get('tweak');
    tweak_algorithm =  module.params.get('tweak_algorithm');
    algorithm =  module.params.get('algorithm');
    character_set_id =  module.params.get('character_set_id');

    # Validation and default setting
    if "CARD" in algorithm:
        if tweak is None or tweak_algorithm is None:
            module.fail_json(msg='tweak and tweak_algorithm are required for CARD algorithms!!!')
        if not character_set_id is None:
            module.fail_json(msg='character_set_id should not be there for CARD algorithms!!!')

    result = dict(
        changed=False,
    )

    #Create Character Set
    requestObj = {}
    requestObj['name'] = name
    requestObj['key'] = key
    requestObj['tweak']=tweak
    requestObj['tweak_algorithm']=tweak_algorithm
    requestObj['algorithm']=algorithm
    requestObj['allow_single_char_input']=False
    if not "CARD" in algorithm:
        requestObj['character_set_id']=character_set_id

    cmSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="data-protection/protection-policies",
            verify=False,
        )

    payload_json = json.dumps(requestObj)
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
