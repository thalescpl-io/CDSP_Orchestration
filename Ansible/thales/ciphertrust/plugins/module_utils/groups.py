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
              cm_node=kwargs["node"],
              cm_api_endpoint="usermgmt/groups",
              id="name",
          )
          
      return ast.literal_eval(str(response))
    except:
      raise

def patch(**kwargs):
    result = dict()
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "old_name"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=kwargs['node'],
              cm_api_endpoint="usermgmt/groups/" + kwargs['old_name'],
          )
      return ast.literal_eval(str(response))
    except:
      raise

def addUserToGroup(**kwargs):
  url = "usermgmt/groups/" + kwargs['name'] + "/users/" + kwargs['object_id']

  try:
    response = POSTWithoutData(
      cm_node=node,
      cm_api_endpoint=url,
    )
    return ast.literal_eval(str(response))
  except:
    raise

def addClientToGroup(**kwargs):
  url = "usermgmt/groups/" + kwargs['name'] + "/clients/" + kwargs['object_id']

  try:
    response = POSTWithoutData(
      cm_node=node,
      cm_api_endpoint=url,
    )
    return ast.literal_eval(str(response))
  except:
    raise

def deleteUserFromGroup(**kwargs):
  url = "usermgmt/groups/" + kwargs['name'] + "/users/" + kwargs['object_id']

  try:
    response = DeleteWithoutData(
      cm_node=node,
      cm_api_endpoint=url,
    )
    return ast.literal_eval(str(response))
  except:
    raise

def deleteClientFromGroup(**kwargs):
    url = "usermgmt/groups/" + kwargs['name'] + "/clients/" + kwargs['object_id']

    try:
    response = DeleteWithoutData(
      cm_node=node,
      cm_api_endpoint=url,
    )
    return ast.literal_eval(str(response))
  except:
    raise