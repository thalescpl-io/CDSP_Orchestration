#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2023 Thales Group. All rights reserved.
# Author: Anurag Jain, Developer Advocate, Thales
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

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData
#from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, POSTWithoutData, DeleteWithoutData, PUTData
from ansible_collections.thales.ciphertrust.plugins.module_utils.exceptions import CMApiException, AnsibleCMException

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def new(node):
    result = dict()
    
    request = {
        "localNodeHost":node["server_private_ip"],
        "localNodePort":node["server_port"],
        "publicAddress":node["server_ip"],
    }
    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=node,
            cm_api_endpoint="cluster/new",
        )
      return 'Cluster creation success!'
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise

def csr(master, node):
    request = {
        "localNodeHost":node["server_private_ip"],
        "publicAddress":master["server_ip"],
    }
    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=node,
            cm_api_endpoint="cluster/csr"
        )
        return response["csr"]
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise

def sign(master, node, csr):
    result=dict()
    request = {
        "csr":csr,
        "shared_hsm_partition":False,
        "newNodeHost":node["server_private_ip"],
        "publicAddress":master["server_ip"],
    }
    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=master,
            cm_api_endpoint="nodes"
        )
        return response
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise

def join(master, node, cert, caChain, mkek_blob):
    result = dict()
    request = {
        "cert":cert,
        "cachain":caChain,
        "localNodeHost":node["server_private_ip"],
        "localNodePort":5432,
        "localNodePublicAddress":node["server_ip"],
        "memberNodeHost":master["server_private_ip"],
        "memberNodePort":5432,
        "mkek_blob":mkek_blob,
        "blocking":False,
    }
    payload = json.dumps(request)

    try:
        response = POSTData(
                payload=payload,
                cm_node=node,
                cm_api_endpoint="cluster/join"
            )
        return response
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise