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

# ProcessSet
def createProcessSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/processsets",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateProcessSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/processsets/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def addProcessToSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/processsets/" + kwargs['id'] + "/addprocesses",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateProcessInSetByIndex(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id", "processIndex"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/processsets/" + kwargs['id'] + "/updateprocess/" + kwargs['processIndex'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End ProcessSet

# ResourceSet
def createResourceSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/resourcesets",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateResourceSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/resourcesets/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def addResourceToSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/resourcesets/" + kwargs['id'] + "/addresources",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateResourceInSetByIndex(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id", "resourceIndex"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/resourcesets/" + kwargs['id'] + "/updateresource/" + kwargs['resourceIndex'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End ResourceSet

# SignatureSet
def createSignatureSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateSignatureSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def addSignatureToSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets/" + kwargs['id'] + "/addsignatures",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def sendSignAppRequest(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets/" + kwargs['id'] + "/signapp",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def querySignAppRequest(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets/" + kwargs['id'] + "/querysignapp",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def cancelSignAppRequest(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/signaturesets/" + kwargs['id'] + "/cancelsignapp",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End SignatureSet

# UserSet
def createUserSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/usersets",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateUserSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/usersets/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def addUserToSet(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/usersets/" + kwargs['id'] + "/addusers",
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def updateUserInSetByIndex(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id", "userIndex"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/usersets/" + kwargs['id'] + "/updateuser/" + kwargs['userIndex'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End UserSet

# CSI Storage Group
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

def updateCSIStorageGroup(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def csiGroupAddClient(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups/" + kwargs['id'] + "/clients",
      )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

def csiGroupAddGuardPoint(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/csigroups/" + kwargs['id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End CSI Storage Group

# CTE Client Group
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

def updateClientGroup(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
        response = PATCHData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups/" + kwargs['id'],
        )
        return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise

# Add Client to ClientGroup
def clientGroupAddClients(**kwargs):
    request = {}

    for key, value in kwargs.items():
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups/" + kwargs['id'] + "/clients",
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
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clientgroups/" + kwargs['id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End CTE Client Group

# CTE Client
# Creates a CTE client on the CipherTrust Manager. The client need not necessarily have the CTE Agent installed on it.
def createClient(**kwargs):
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
        if key not in ["node", "id"] and value != None:
            request[key] = value

    payload = json.dumps(request)

    try:
      response = POSTData(
            payload=payload,
            cm_node=kwargs['node'],
            cm_api_endpoint="transparent-encryption/clients/" + kwargs['id'] + "/guardpoints",
        )
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
        raise
    except AnsibleCMException as custom_e:
        raise
# End CTE Client