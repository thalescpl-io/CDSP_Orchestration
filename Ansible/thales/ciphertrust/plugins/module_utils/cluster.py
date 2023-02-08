#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a utility file for creating Thales Ciphertrust Manager REST API session
# Generating Token
# Generating Headers
# Preparing URL for REST operation

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData

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
      result['success'] = 'Cluster creation success!'
      return response
    except:
      result['failed'] = True

def csr(localNode, node):
    request = {
        "localNodeHost":node["server_private_ip"],
        "publicAddress":localNode["server_ip"],
    }
    payload = json.dumps(request)

    try:
        response = POSTData(
                payload=payload,
                cm_node=node,
                cm_api_endpoint="cluster/csr"
            )
        #if is_json(response):
        #    csr = response.json()["csr"]
        #    return csr
        #else:
        return response["csr"]
    except requests.exceptions.RequestException as err:
        raise

def sign(localNode, node, csr):
    result=dict()
    request = {
        "csr":csr,
        "shared_hsm_partition":False,
        "newNodeHost":node["server_private_ip"],
        "publicAddress":localNode["server_ip"],
    }
    payload = json.dumps(request)

    try:
        response = POSTData(
                payload=payload,
                cm_node=localNode,
                cm_api_endpoint="nodes"
            )
        #if is_json(response.json()):
        #    result["cert"] = response.json()["cert"]
        #    result["cachain"] = response.json()["cachain"]
        #    result["mkek_blob"] = response.json()["mkek_blob"]
        #    return result
        #else:
        return response
    except requests.exceptions.RequestException as err:
        raise

def join(localNode, node, cert, caChain, mkek_blob):
    result = dict()
    request = {
        "cert":cert,
        "cachain":caChain,
        "localNodeHost":node["server_private_ip"],
        "localNodePort":5432,
        "localNodePublicAddress":node["server_ip"],
        "memberNodeHost":localNode["server_private_ip"],
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
    except:
        raise
