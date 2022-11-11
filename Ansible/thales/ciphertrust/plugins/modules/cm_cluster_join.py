#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import CMAPIObject

def main():
    newNode = dict(
            public_address=dict(type='str', required=True),
            private_address=dict(type='str', required=True),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True),
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
                newNodes=dict(type='list', elements='dict', options=newNode, required=False),
            ),
        )

    localNode = module.params.get('localNode');
    newNodes = module.params.get('newNodes');

    result = dict(
        changed=False,
    )

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #CM Session object for the member node and /nodes endpoint
    #/nodes endpoint will let the member node sign a CSR
    memberNodeCMSessionObject = CMAPIObject(
            cm_api_user=localNode["user"],
            cm_api_pwd=localNode["password"],
            cm_url=localNode["server_ip"],
            cm_api_endpoint="nodes",
            verify=False,
        )

    for node in newNodes:
        # ------Section Begins-----"
        # Send request for CSR generation to the new node
        csr=''
        newNodeCMSessionObject_csr = CMAPIObject(
            cm_api_user=node["username"],
            cm_api_pwd=node["password"],
            cm_url=node["public_address"],
            cm_api_endpoint="cluster/csr",
            verify=False,
        )

        csr_payload = {
            "localNodeHost":node["private_address"],
            "publicAddress":localNode["server_ip"],
        }

        try:
          csr_response = requests.post(newNodeCMSessionObject_csr["url"], headers=newNodeCMSessionObject_csr["headers"], json = csr_payload, verify=False)
          csr = csr_response.json()["csr"]
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err
        # ------Section Ends-----"

        # ------Section Begins-----"
        # Send request for CSR signing to member node
        cert=''
        caChain=''
        mkek_blob=''
        sign_csr_payload = {
            "csr":csr,
            "shared_hsm_partition":False,
            "newNodeHost":node["private_address"],
            "publicAddress":localNode["server_ip"],
        }

        try:
          sign_csr_response = requests.post(memberNodeCMSessionObject["url"], headers=memberNodeCMSessionObject["headers"], json = sign_csr_payload, verify=False)
          cert=sign_csr_response.json()["cert"]
          caChain=sign_csr_response.json()["cachain"]
          mkek_blob=sign_csr_response.json()["mkek_blob"]
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err
        # ------Section Ends-----"

        # ------Section Begins-----"
        # Last but not least, send the join request to new node with signed certificate

        newNodeCMSessionObject_join = CMAPIObject(
            cm_api_user=node["username"],
            cm_api_pwd=node["password"],
            cm_url=node["public_address"],
            cm_api_endpoint="cluster/join",
            verify=False,
        )

        join_payload = {
            "cert":cert,
            "cachain":caChain,
            "localNodeHost":node["private_address"],
            "localNodePort":5432,
            "localNodePublicAddress":node["public_address"],
            "memberNodeHost":localNode["server_private_ip"],
            "memberNodePort":5432,
            "mkek_blob":mkek_blob,
            "blocking":False,
        }

        try:
          join_response = requests.post(newNodeCMSessionObject_join["url"], headers=newNodeCMSessionObject_join["headers"], json = join_payload, verify=False)
          result["output"] = join_response.json()
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err
          # ------Section Ends-----"

    module.exit_json(**result)

if __name__ == '__main__':
    main()

