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
import ast

from ansible_collections.thales.ciphertrust.plugins.module_utils.cm_api import POSTData, PATCHData, POSTWithoutData
from ansible_collections.thales.ciphertrust.plugins.module_utils.exceptions import CMApiException, AnsibleCMException

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

# CCKM AWS CKS Management Functions
def createCustomKeyStore(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def editCustomKeyStore(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = PATCHData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'],
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def createAWSKeyCKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/create-aws-key",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def blockCKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/block",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def unblockCKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/unblock",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def connectCKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/connect",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def disconnectCKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/disconnect",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def linkLocalCKSWithAWS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/link",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def synchronize_AWS_CKS(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/synchronization-jobs",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def cancelSynchronizeJob(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/synchronization-jobs/" + kwargs['id'] + "/cancel",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def rotateCredential(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/custom-key-stores/" + kwargs['id'] + "/rotate-credential",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def createVirtualKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/virtual/keys",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def editVirtualKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = PATCHData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/virtual/keys/" + kwargs['id'],
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def createHYOKKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/create-hyok-key",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def blockHYOKKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/keys/" + kwargs['id'] + "/block",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def unblockHYOKKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/keys/" + kwargs['id'] + "/unblock",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def linkHYOKKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/keys/" + kwargs['id'] + "/link",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

# CCKM AWS Key Management Functions
def createAWSKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/keys",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def synchronizeAWSKey(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node'] and value != None:
      request[key] = value

  payload = json.dumps(request)

  try:
    response = POSTData(
      payload=payload,
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/synchronization-jobs",
      id="id",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def cancelSynchronizeAWSKeyJob(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id'] and value != None:
      request[key] = value

  try:
    response = POSTWithoutData(
      cm_node=kwargs["node"],
      cm_api_endpoint="cckm/aws/synchronization-jobs/" + kwargs['id'] + "/cancel",
    )          
    return ast.literal_eval(str(response))
  except CMApiException as api_e:
    raise
  except AnsibleCMException as custom_e:
    raise

def performKeyOperation(**kwargs):
  request = {}

  for key, value in kwargs.items():
    if key not in ['node', 'id', 'aws_key_action'] and value != None:
      request[key] = value

  if kwargs['aws_key_action'] == "disable-rotation-job" or kwargs['aws_key_action'] == "delete-key-material" or kwargs['aws_key_action'] == "enable-key" or kwargs['aws_key_action'] == "disable-key" or kwargs['aws_key_action'] == "cancel-deletion" or kwargs['aws_key_action'] == "enable-auto-rotation" or kwargs['aws_key_action'] == "disable-auto-rotation":
    try:
      response = POSTWithoutData(
        cm_node=kwargs["node"],
        cm_api_endpoint="cckm/aws/synchronization-jobs/" + kwargs['id'] + "/cancel",
      )          
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise
  elif kwargs['aws_key_action'] == "disable-rotation-job" or kwargs['aws_key_action'] == "delete-key-material" or kwargs['aws_key_action'] == "enable-key" or kwargs['aws_key_action'] == "disable-key" or kwargs['aws_key_action'] == "cancel-deletion" or kwargs['aws_key_action'] == "enable-auto-rotation" or kwargs['aws_key_action'] == "disable-auto-rotation":
    try:
      response = POSTWithoutData(
        cm_node=kwargs["node"],
        cm_api_endpoint="cckm/aws/synchronization-jobs/" + kwargs['id'] + "/cancel",
      )          
      return ast.literal_eval(str(response))
    except CMApiException as api_e:
      raise
    except AnsibleCMException as custom_e:
      raise