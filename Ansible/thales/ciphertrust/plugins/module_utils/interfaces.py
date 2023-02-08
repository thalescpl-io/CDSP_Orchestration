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

def new(
        node,
        port,
        auto_gen_ca_id="",
        auto_registration=False,
        cert_user_field="",
        custom_uid_size=None,
        custom_uid_v2=True,
        default_connection="",
        interface_type="nae",
        kmip_enable_hard_delete=None,
        maximum_tls_version="tls_1_2",
        minimum_tls_version="tls_1_2",
        mode="",
        name="",
        network_interface="all",
        registration_token="",
        external_trusted_cas=[],
        local_trusted_cas=[]
        ):
    result = dict()
    
    trusted_cas={}

    request = {}

    request['port']=port
   
    if auto_gen_ca_id != "":
        request['auto_gen_ca_id']=auto_gen_ca_id

    request['auto_registration']=auto_registration
    request['custom_uid_v2']=custom_uid_v2
    request['interface_type']=interface_type
    request['minimum_tls_version']=minimum_tls_version
    request['maximum_tls_version'] = maximum_tls_version
    request['network_interface']=network_interface

    if cert_user_field != "":
        request['cert_user_field']=cert_user_field

    if custom_uid_size is not None:
        request['custom_uid_size'] = custom_uid_size

    if default_connection != "":
        request['default_connection']=default_connection

    if kmip_enable_hard_delete is not None:
        request['kmip_enable_hard_delete'] = kmip_enable_hard_delete

    if mode != "":
        request['mode'] = mode

    if name != "":
        request['name'] = name

    if registration_token != "":
        request['registration_token'] = registration_token

    if len(external_trusted_cas) > 0:
        trusted_cas['external'] = external_trusted_cas

    if len(local_trusted_cas) > 0:
        trusted_cas['local'] = local_trusted_cas

    request['trusted_cas'] = trusted_cas

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="configs/interfaces",
          )
      result['success'] = 'Interface creation success!'
      result['payload'] = payload
      result['response'] = response
      return result
    except:
      result['failed'] = True
      raise

