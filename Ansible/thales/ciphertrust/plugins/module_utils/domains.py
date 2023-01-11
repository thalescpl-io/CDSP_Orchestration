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

def create(node,
           name,
           admins,
           allow_user_management,
           hsm_connection_id,
           hsm_kek_label,
           parent_ca_id):
    result = dict()
    request = {
            "name": name,
            "admins": admins,
            "allow_user_management": allow_user_management,
            "hsm_connection_id": hsm_connection_id,
            "hsm_kek_label": hsm_kek_label,
            "parent_ca_id": parent_ca_id,
        }

    request['meta'] = dict()

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="domains",
          )
      if response == '4xx':
          result['success'] = 'Domain already exists with same name'
      else:
          result['success'] = 'Domain Created Succesfully'

      return response
    except:
      result['failed'] = True