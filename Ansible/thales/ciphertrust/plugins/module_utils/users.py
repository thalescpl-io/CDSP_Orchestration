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

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, PATCHData

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def create(**kwargs):
    result = dict()
    request = {}

    for key, value in kwargs.items():
        if key != "node" and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=kwargs['node'],
              cm_api_endpoint="usermgmt/users",
          )
      return response

    #   if response["status_code"] == "201":
    #     __ret = {
    #       "user_id": response["data"]["user_id"],
    #       "created_at": response["data"]["created_at"],
    #       "message": "User created sucessfully"
    #     }
    #     return __ret
    #   else:
    #     if is_json(str(response["data"])):
    #       if "codeDesc" in response["data"].json():
    #         codeDesc=response["data"].json()["codeDesc"]
    #         __ret = {
    #           "message": "User creation failed",
    #           "err": codeDesc
    #         }
    #         return __ret
    #     else:
    #         __ret = {
    #           "message": "User creation failed",
    #           "err": str(response["data"])
    #         }
    #         return __ret
    except:
      raise

def patch(**kwargs):
    result = dict()
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "cm_user_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=kwargs['node'],
              cm_api_endpoint="usermgmt/users/" + kwargs['cm_user_id'],
          )
      if response == '4xx':
          return 'User update failed'
      else:
          return 'User updated succesfully'
    except:
      raise

def changepw(**kwargs):
    result = dict()
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=kwargs['node'],
              cm_api_endpoint="auth/changepw",
          )
      if response == '4xx':
        return 'Password update failed'
      else:
        return 'Password updated succesfully'
    except:
      raise

def patch_self(**kwargs):
    result = dict()
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=kwargs['node'],
              cm_api_endpoint="auth/self/user",
          )
      if response == '4xx':
          return 'User update failed'
      else:
          return 'User updated succesfully'
    except:
      raise