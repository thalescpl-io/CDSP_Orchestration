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

def create_policy(node,
        name,
        policyDescription,
        policy_type,
        data_transform_rules,
        idt_key_rules,
        key_rules,
        ldt_key_rules,
        metadata,
        never_deny,
        security_rules
    ):

    result = dict()
    request = {}

    request['name'] = name
    request['policy_type'] = policy_type
    request['description'] = policyDescription
    request['data_transform_rules'] = data_transform_rules
    request['idt_key_rules'] = idt_key_rules
    request['key_rules'] = key_rules
    request['ldt_key_rules'] = ldt_key_rules
    request['metadata'] = metadata
    request['never_deny'] = never_deny
    request['security_rules'] = security_rules

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/policies",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Create Process Set
def createProcessSet(node,
        name,
        processSetDescription,
        processes
    ):

    result = dict()
    request = {}
    arrProcess = []

    for p in processes:
        process["directory"] = p["directory"]
        process["file"] = p["processSetFile"]
        process["signature"] = p["directory"]
        arrProcess.append(process)

    request['name'] = name
    request['description'] = processSetDescription
    request['processes'] = arrProcess

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/processsets",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Create Resource Set
def createResourceSet(node,
        name,
        description,
        classification_tags,
        resources,
        resourceType
    ):
    result = dict()
    request = {}

    request['name'] = name
    request['description'] = description
    request['classification_tags'] = classification_tags
    request['resources'] = resources
    request['resourceType'] = resourceType

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/resourcesets",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

# Create CTE Profile
def create_cte_profile(node,
        name,
        profileDescription,
        cache_settings,
        concise_logging,
        connect_timeout,
        duplicate_settings,
        file_settings,
        ldt_qos_cap_cpu_allocation,
        ldt_qos_cpu_percent,
        ldt_qos_rekey_option,
        ldt_qos_rekey_rate,
        ldt_qos_schedule,
        management_service_logger,
        metadata_scan_interval,
        mfa_exempt_user_set_id,
        oidc_connection_id,
        policy_evaluation_logger,
        qos_schedules,
        security_admin_logger,
        server_settings,
        syslog_settings,
        system_admin_logger,
        upload_settings
    ):

    result = dict()
    request = {}

    request['name'] = name
    request['description'] = profileDescription
    request['cache_settings'] = cache_settings
    request['concise_logging'] = concise_logging
    request['connect_timeout'] = connect_timeout
    request['duplicate_settings'] = duplicate_settings
    request['file_settings'] = file_settings
    request['ldt_qos_cap_cpu_allocation'] = ldt_qos_cap_cpu_allocation
    request['ldt_qos_cpu_percent'] = ldt_qos_cpu_percent
    request['ldt_qos_rekey_option'] = ldt_qos_rekey_option
    request['ldt_qos_rekey_rate'] = ldt_qos_rekey_rate
    request['ldt_qos_schedule'] = ldt_qos_schedule
    request['management_service_logger'] = management_service_logger
    request['metadata_scan_interval'] = metadata_scan_interval
    request['mfa_exempt_user_set_id'] = mfa_exempt_user_set_id
    request['oidc_connection_id'] = oidc_connection_id
    request['policy_evaluation_logger'] = policy_evaluation_logger
    request['qos_schedules'] = qos_schedules
    request['security_admin_logger'] = security_admin_logger
    request['server_settings'] = server_settings
    request['syslog_settings'] = syslog_settings
    request['system_admin_logger'] = system_admin_logger
    request['upload_settings'] = upload_settings

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="transparent-encryption/profiles",
          )
      if response == '4xx':
          result['success'] = 'Error'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True