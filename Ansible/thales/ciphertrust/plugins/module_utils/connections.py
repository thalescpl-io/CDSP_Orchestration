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

# AWS Connection Creation
def createAWSConnection(node,
           access_key_id,
           name,
           secret_access_key,
           assume_role_arn,
           assume_role_external_id,
           aws_region,
           aws_sts_regional_endpoints,
           cloud_name,
           description,
           products):
    result = dict()
    meta = dict()
    request = {
            "name": name,
            "access_key_id": access_key_id,
            "secret_access_key": secret_access_key,
            "assume_role_arn": assume_role_arn,
            "assume_role_external_id": assume_role_external_id,
            "aws_region": aws_region,
            "aws_sts_regional_endpoints": aws_sts_regional_endpoints,
            "cloud_name": cloud_name,
            "description": description,
            "products": products,
            "meta": meta,
        }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="connectionmgmt/services/aws/connections",
          )
      if response == '4xx':
          result['success'] = 'Connection already exists with same name'
      else:
          result['success'] = 'Connection Created Succesfully'

      return response
    except:
      result['failed'] = True

# Azure Connection Creation
def createAzureConnection(node,
      name,
      description,
      client_id,
      tenant_id,
      active_directory_endpoint,
      azure_stack_connection_type,
      azure_stack_server_cert,
      cert_duration,
      client_secret,
      cloud_name,
      products,
      is_certificate_used,
      key_vault_dns_suffix,
      management_url,
      resource_manager_url,
      vault_resource_url):
    result = dict()
    meta = dict()
    request = {
        "name": name,
        "description": description,
        "products": products,
        "meta": meta,
        "client_id": client_id,
        "tenant_id": tenant_id,
        "active_directory_endpoint": active_directory_endpoint,
        "azure_stack_connection_type": azure_stack_connection_type,
        "azure_stack_server_cert": azure_stack_server_cert,
        "cert_duration": cert_duration,
        "client_secret": client_secret,
        "cloud_name": cloud_name,
        "is_certificate_used": is_certificate_used,
        "key_vault_dns_suffix": key_vault_dns_suffix,
        "management_url": management_url,
        "resource_manager_url": resource_manager_url,
        "vault_resource_url": vault_resource_url,
      }

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="connectionmgmt/services/azure/connections",
          )
      if response == '4xx':
          result['success'] = 'Connection already exists with same name'
      else:
          result['success'] = 'Connection Created Succesfully'

      return response
    except:
      result['failed'] = True