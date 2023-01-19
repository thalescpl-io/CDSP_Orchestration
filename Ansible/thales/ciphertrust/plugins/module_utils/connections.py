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

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, PATCHData

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def create(node,
           name,
           strategy,
           ldap_options,
           oidc_options,
           options):
    result = dict()
    request = {
            "name": name,
            "strategy": strategy,
            "ldap_options": ldap_options,
            "oidc_options": oidc_options,
            "options": options,
        }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="usermgmt/connections",
          )
      if response == '4xx':
          result['success'] = 'Connection already exists with same name'
      else:
          result['success'] = 'Connection Created Succesfully'

      return response
    except:
      result['failed'] = True

def createSyslogConnection(node,
           name,
           syslog_params,
           conn_description,
           host,
           port,
           products):
    result = dict()
    meta = dict()
    request = {
            "name": name,
            "description": conn_description,
            "syslog_params": syslog_params,
            "host": host,
            "port": port,
            "meta": meta,
            "products": products,
        }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="connectionmgmt/services/log-forwarders/syslog/connections",
          )
      if response == '4xx':
          result['success'] = 'Connection already exists with same name'
      else:
          result['success'] = 'Connection Created Succesfully'

      return response
    except:
      result['failed'] = True

def patchSyslogConnection(node,
           connectionId,
           syslog_params,
           conn_description,
           host,
           port,
           products):
    result = dict()
    meta = dict()
    request = {
            "description": conn_description,
            "syslog_params": syslog_params,
            "host": host,
            "port": port,
            "meta": meta,
            "products": products,
        }

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="connectionmgmt/services/log-forwarders/syslog/connections/" + connectionId,
          )
      if response == '4xx':
          result['success'] = 'Connection already exists with same name'
      else:
          result['success'] = 'Connection Created Succesfully'

      return response
    except:
      result['failed'] = True