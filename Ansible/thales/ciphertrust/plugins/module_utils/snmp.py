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

def addCommunity(node,
           name,
           mib_accesses,
           read_write,
           source):
    result = dict()
    request = {
        "name": name,
        "mib_accesses": mib_accesses,
        "read_write": read_write,
        "source": source,
    }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/communities",
          )
      if response == '4xx':
          result['success'] = 'SNMP Community already exists with same name'
      else:
          result['success'] = 'SNMP Community Created Succesfully'

      return result
    except:
      result['failed'] = True

def addUser(node,
           name,
           security_level,
           auth_password,
           auth_protocol,
           engine_id,
           mib_accesses,
           priv_password,
           priv_protocol,
           read_write):
    result = dict()
    request = {
        "name": name,
        "security_level": security_level,
        "auth_password": auth_password,
        "auth_protocol": auth_protocol,
        "engine_id": engine_id,
        "mib_accesses": mib_accesses,
        "priv_password": priv_password,
        "priv_protocol": priv_protocol,
        "read_write": read_write,
    }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/users",
          )
      if response == '4xx':
          result['success'] = 'SNMP User already exists with same name'
      else:
          result['success'] = 'SNMP User Created Succesfully'

      return result
    except:
      result['failed'] = True

def addManagementStation(node,
           name,
           host,
           security_name,
           version,
           notification_type,
           port):
    result = dict()
    request = {
        "name": name,
        "host": host,
        "security_name": security_name,
        "version": version,
        "notification_type": notification_type,
        "port": port,
    }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/management-stations",
          )
      if response == '4xx':
          result['success'] = 'Management Station already exists with same name'
      else:
          result['success'] = 'Management Station Created Succesfully'

      return result
    except:
      result['failed'] = True

# Patch methods
def patchCommunity(node,
           communityId,
           name,
           mib_accesses,
           read_write,
           source):
    result = dict()
    request = {
        "name": name,
        "mib_accesses": mib_accesses,
        "read_write": read_write,
        "source": source,
    }

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/communities/" + communityId,
          )
      if response == '4xx':
          result['success'] = 'Patch operation failed'
      else:
          result['success'] = 'Patched Succesfully'

      return result
    except:
      result['failed'] = True

def patchUser(node,
           userId,
           security_level,
           auth_password,
           auth_protocol,
           mib_accesses,
           priv_password,
           priv_protocol,
           read_write):
    result = dict()
    request = {
        "security_level": security_level,
        "auth_password": auth_password,
        "auth_protocol": auth_protocol,
        "mib_accesses": mib_accesses,
        "priv_password": priv_password,
        "priv_protocol": priv_protocol,
        "read_write": read_write,
    }

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/users/" + userId,
          )
      if response == '4xx':
          result['success'] = 'Patch operation failed'
      else:
          result['success'] = 'Patched Succesfully'

      return result
    except:
      result['failed'] = True

def patchManagementStation(node,
           managementStationId,
           security_name):
    result = dict()
    request = {
        "security_name": security_name,
    }

    payload = json.dumps(request)

    try:
      response = PATCHData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="snmp/management-stations/" + managementStationId,
          )
      if response == '4xx':
          result['success'] = 'Patch operation failed'
      else:
          result['success'] = 'Patched Succesfully'

      return result
    except:
      result['failed'] = True