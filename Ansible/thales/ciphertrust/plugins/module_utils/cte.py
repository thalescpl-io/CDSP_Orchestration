#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a utility file for interacting with the Thales CipherTrust Manager APIs for CipheTrust Transparent Encryption

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import json
import ast

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, PATCHData
from ansible_collections.thales.ciphertrust.plugins.module_utils.exceptions import CMApiException, AnsibleCMException

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def createCTEPolicy(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/policies",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateCTEPolicy(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "policy_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/policies/" + kwargs['policy_id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add new rules to the CTE Policy
def ctePolicyAddRule(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "policy_id", "rule_name"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/policies/" + kwargs['policy_id'] + "/" + kwargs["rule_name"],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def ctePolicyPatchRule(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "policy_id", "rule_name", "rule_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/policies/" + kwargs['policy_id'] + "/" + kwargs["rule_name"] + "/" + kwargs["rule_id"],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End of add new rules to the CTE Policy

def createCSIStorageGroup(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add Clients to Storage Group
def csiGroupAddClient(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "group_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups/" + kwargs['group_id'] + "/clients",
      )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add GuardPolicy to Storage Group
def csiGroupAddGuardPoint(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "group_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups/" + kwargs['group_id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Create Client Group
def createClientGroup(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add Client to ClientGroup
def clientGroupAddClient(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "group_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups/" + kwargs['group_id'] + "/clients",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add GuardPoint to ClientGroup
def clientGroupAddGuardPoint(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "group_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups/" + kwargs['group_id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Creates a CTE client on the CipherTrust Manager. The client need not necessarily have the CTE Agent installed on it.
def create_client(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clients",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add GuardPoint to Client
def clientAddGuardPoint(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "client_id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clients/" + kwargs['client_id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise