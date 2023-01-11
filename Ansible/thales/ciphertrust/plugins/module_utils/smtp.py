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

def addServer(node,
           server,
           port,
           username,
           email_from,
           password,
           allow_tcp):
    result = dict()
    request = {
        "server": server,
        "port": port,
        "username": username,
        "email_from": email_from,
        "password": password,
        "allow_tcp": allow_tcp,
    }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="notification/smtp-servers",
          )
      if response == '4xx':
          result['success'] = 'SMTP Server creation failed'
      else:
          result['success'] = 'SMTP Server Created Succesfully'

      return result
    except:
      result['failed'] = True