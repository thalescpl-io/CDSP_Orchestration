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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cluster import csr, sign, join

DOCUMENTATION = '''
---
module: cm_cluster_join
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically join cluster API.
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
    newNodes:
        description:
            - List of CipherTrust nodes that want to join an existing cluster. Existing cluster node is identified by the localNode attribute.
        required: false
        type: list of node type dict
        default: empty list
'''

EXAMPLES = '''
- name: "Join nodes to the cluster"
  thales.ciphertrust.cm_cluster_join:
      localNode:
          server_ip: "IP/FQDN of CipherTrust Manager"
          server_private_ip: "Privare IP in case that is different from above"
          server_port: 5432
          user: "CipherTrust Manager Username"
          password: "CipherTrust Manager Password"
          verify: false
      newNodes:
          - server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Privare IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
'''

RETURN = '''
'''

def main():
    newNode = dict(
            server_ip=dict(type='str', required=True),
            server_private_ip=dict(type='str', required=True),
            server_port=dict(type='int', required=True),
            user=dict(type='str', required=True),
            password=dict(type='str', required=True),
            verify=dict(type='bool', required=True),
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

    for node in newNodes:
        strCSR = ''
        # ------Section Begins-----"
        # Send request for CSR generation to the new node
        try:
            strCSR = csr(
                localNode=localNode,
                node=node,
            )
        except ValueError as err:
            result["failed"] = True
            result["err"]=err

        # ------Section Ends-----"

        # ------Section Begins-----"
        # Send request for CSR signing to member node
        cert=''
        caChain=''
        mkek_blob=''

        try:
          output = sign(
                  localNode=localNode,
                  node=node,
                  csr=strCSR,
              )
          cert = output["cert"]
          caChain = output["cachain"]
          mkek_blob = output["mkek_blob"]
        except requests.exceptions.RequestException as err:
          result['failed'] = True
        # ------Section Ends-----"

        # ------Section Begins-----"
        # Last but not least, send the join request to new node with signed certificate

        try:
          output = join(
                  localNode=localNode,
                  node=node,
                  cert=cert,
                  caChain=caChain,
                  mkek_blob=mkek_blob,
              )
          result["output"] = output
        except requests.exceptions.RequestException as err:
          result['failed'] = True
          result['error'] = err
          # ------Section Ends-----"

    module.exit_json(**result)

if __name__ == '__main__':
    main()

