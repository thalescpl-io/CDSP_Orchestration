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

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, POSTWithoutData, DeleteWithoutData

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def create(node,
           name):
    result = dict()
    request = {
        "name": name,
      }

    request['app_metadata'] = dict()
    request['client_metadata'] = dict()
    request['user_metadata'] = dict()

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="usermgmt/groups",
          )
      if response == '4xx':
          result['success'] = 'Group already exists with same name'
      else:
          result['success'] = 'Group Created Succesfully'

      return result
    except:
      result['failed'] = True

def addUserToGroup(node,
           groupName,
           userId):
    result = dict()

    try:
      response = POSTWithoutData(
              cm_node=node,
              cm_api_endpoint="usermgmt/groups/" + groupName + "/users/" + userId,
          )
      if response == '4xx':
          result['success'] = 'User Addition Failed'
      else:
          result['success'] = 'User Added Succesfully'

      return result
    except:
      result['failed'] = True

def addClientToGroup(node,
           groupName,
           clientId):
    result = dict()

    try:
      response = POSTWithoutData(
              cm_node=node,
              cm_api_endpoint="usermgmt/groups/" + groupName + "/clients/" + clientId,
          )
      if response == '4xx':
          result['success'] = 'Client Addition Failed'
      else:
          result['success'] = 'Client Added Succesfully'

      return result
    except:
      result['failed'] = True

def deleteUserFromGroup(node,
           groupName,
           userId):
    result = dict()

    try:
      response = DeleteWithoutData(
              cm_node=node,
              cm_api_endpoint="usermgmt/groups/" + groupName + "/users/" + userId,
          )
      if response == '4xx':
          result['success'] = 'User Deletion Failed'
      else:
          result['success'] = 'User Deleted Succesfully'

      return result
    except:
      result['failed'] = True

def deleteClientFromGroup(node,
           groupName,
           clientId):
    result = dict()

    try:
      response = DeleteWithoutData(
              cm_node=node,
              cm_api_endpoint="usermgmt/groups/" + groupName + "/clients/" + clientId,
          )
      if response == '4xx':
          result['success'] = 'Client Deletion Failed'
      else:
          result['success'] = 'Client Deleted Succesfully'

      return result
    except:
      result['failed'] = True