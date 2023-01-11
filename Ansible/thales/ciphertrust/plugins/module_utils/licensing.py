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

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, GETData, POSTWithoutData

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def getLockdata(node):
    result = dict()

    try:
      response = GETData(
              cm_node=node,
              cm_api_endpoint="licensing/lockdata",
          )
      if response == '4xx':
          result['error'] = 'Failed to fetch data'
      else:
          result['data'] = response

      return result
    except:
      result['failed'] = True

def addLicense(node,
        license,
        bind_type
    ):
    result = dict()

    request = {
        "license": license,
        "bind_type": bind_type
      }

    payload = json.dumps(request)
    
    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="licensing/licenses",
          )
      if response == '4xx':
          result['success'] = 'Unable to add license'
      else:
          result['success'] = 'License Added Succesfully'

      return result
    except:
      result['failed'] = True

def activateTrial(node,
        trialId
    ):
    result = dict()
    
    try:
      response = POSTWithoutData(
            cm_node=node,
            cm_api_endpoint="licensing/trials/" + trialId + "/activate",
        )
      if response == '4xx':
          result['success'] = 'Unable to activate trial'
      else:
          result['success'] = 'Trial Activated Succesfully'

      return result
    except:
      result['failed'] = True

def deactivateTrial(node,
        trialId
    ):
    result = dict()
    
    try:
      response = POSTWithoutData(
            cm_node=node,
            cm_api_endpoint="licensing/trials/" + trialId + "/deactivate",
        )
      if response == '4xx':
          result['success'] = 'Unable to deactivate trial'
      else:
          result['success'] = 'Trial DeActivated Succesfully'

      return result
    except:
      result['failed'] = True