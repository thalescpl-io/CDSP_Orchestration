#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.cluster import csr, sign, join

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

