#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a utility file for interacting with the Thales CipherTrust Manager APIs for CipheTrust Transparent Encryption

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

def create_csigroup(node,
        k8s_namespace,
        k8s_storage_class,
        name,
        client_profile="",
        csigroupDescription=""
    ):
    result = dict()
    request = {}

    request['k8s_namespace']=k8s_namespace
    request['k8s_storage_class']=k8s_storage_class
    request['name']=name

    if client_profile != "":
        request['client_profile']=client_profile

    if csigroupDescription != "":
        request['description']=csigroupDescription

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/csigroups",
          )
      if response == '4xx':
          result['success'] = 'CSI Group already exists with same name'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Add Clients to Storage Group
def csigroup_add_client(node,
        group_id,
        client_list=[]
    ):
    result = dict()
    request = {}

    request['client_list']=client_list

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/csigroups/" + group_id + "/clients",
          )
      if response == '4xx':
          result['success'] = 'CSI Group already exists with same name'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Add GuardPolicy to Storage Group
def csigroup_add_guardpoint(node,
        group_id,
        policy_list=[]
    ):
    result = dict()
    request = {}

    request['policy_list']=policy_list

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/csigroups/" + group_id + "/guardpoints",
          )
      if response == '4xx':
          result['success'] = 'CSI Group already exists with same name'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Create Client Group
def create_clientgroup(node,
        cluster_type,
        name,
        profile_id="",
        clientgroupDescription=""
    ):
    result = dict()
    request = {}
    
    request['name']=name
    request['cluster_type']=cluster_type

    if client_profile != "":
        request['client_profile']=client_profile

    if csigroupDescription != "":
        request['description']=clientgroupDescription

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/csigroups",
          )
      if response == '4xx':
          result['success'] = 'Client Group already exists with same name'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Add Client to ClientGroup
def clientgroup_add_client(node,
        group_id,
        inherit_attributes,
        client_list=[]
    ):
    result = dict()
    request = {}

    request['client_list']=client_list
    request['inherit_attributes']=inherit_attributes

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/clientgroups/" + group_id + "/clients",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Add GuardPoint to ClientGroup
def clientgroup_add_guardpoint(node,
        group_id,
        guard_paths=[],
        guard_point_params
    ):
    result = dict()
    request = {}

    request['guard_paths']=guard_paths
    request['guard_point_params']=guard_point_params

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/clientgroups/" + group_id + "/guardpoints",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Creates a CTE client on the CipherTrust Manager. The client need not necessarily have the CTE Agent installed on it.
def create_client(node,
        name,
        client_locked=False,
        communication_enabled=False,
        password="",
        password_creation_method="",
        profile_identifier="",
        registration_allowed=False,
        system_locked=False,
        clientDescription=""
    ):
    result = dict()
    request = {}

    request['name']=k8s_namespace
    request['client_locked']=client_locked
    request['communication_enabled']=communication_enabled
    request['system_locked']=system_locked
    request['registration_allowed']=registration_allowed

    if password is not None:
        request['password']=password

    if password_creation_method is not None:
        request['password_creation_method']=password_creation_method

    if profile_identifier is not None:
        request['profile_identifier']=profile_identifier

    if clientDescription is not None:
        request['description']=clientDescription

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/clients",
          )
      if response == '4xx':
          result['success'] = 'CTE client already exists with same name'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Add GuardPoint to Client
def client_add_guardpoint(node,
        client_id,
        guard_paths=[],
        guard_point_params
    ):
    result = dict()
    request = {}

    request['guard_paths']=guard_paths
    request['guard_point_params']=guard_point_params

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/clients/" + client_id + "/guardpoints",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True