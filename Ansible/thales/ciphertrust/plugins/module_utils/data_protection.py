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

def create_character_set(
        node,
        name,
        charsetRange,
        encoding=""
        ):
    result = dict()
    
    request = {}

    request['name'] = name;

    request['range'] = charsetRange;

    if encoding != "":
        request['encoding'] = encoding

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/character-sets",
          )
      result['success'] = 'Character Set creation success!'
      return result
    except:
      result['failed'] = True
      raise

def create_protection_policy(
        node,
        name,
        algorithm,
        key,
        allow_single_char_input=False,
        character_set_id="",
        iv="",
        tweak="",
        tweak_algorithm=""
        ):
    result = dict()
    request = {}
    request['name'] = name;
    request['algorithm'] = algorithm;
    request['key'] = key;
    request['allow_single_char_input'] = allow_single_char_input;
    if character_set_id != "":
        request['character_set_id'] = character_set_id;

    if iv != "":
        request['iv'] = iv;

    if tweak != "":
        request['tweak'] = tweak;

    if tweak_algorithm != "":
        request['tweak_algorithm'] = tweak_algorithm;

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/protection-policies",
          )
      result['success'] = 'Protection Policy creation success!'
      return result
    except:
      result['failed'] = True
      raise

def create_user_set(
        node,
        name,
        usersetDescription="",
        users=[]
        ):
    result = dict()
    request = {}
    request['name'] = name;
    request['users'] = users;

    if usersetDescription != "":
        request['description'] = usersetDescription;

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/user-sets",
          )
      result['success'] = 'Userset creation success!'
      return result
    except:
      result['failed'] = True
      raise

def create_access_policy(
        node,
        name="",
        default_reveal_type="",
        default_error_replacement_value="",
        user_set_policy=[],
        default_masking_format_id="",
        access_policy_description=""
        ):
    result = dict()
    request = {}
    request['user_set_policy']=user_set_policy;
    if name != "":
        request['name'] = name;

    if default_reveal_type != "":
        request['default_reveal_type'] = default_reveal_type;

    if default_error_replacement_value != "":
        request['default_error_replacement_value'] = default_error_replacement_value;

    if default_masking_format_id != "":
        request['default_masking_format_id'] = default_masking_format_id;

    if access_policy_description != "":
        request['access_policy_description'] = access_policy_description;

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/access-policies",
          )
      result['success'] = 'Access Policy creation success!'
      return result
    except:
      result['failed'] = True
      raise

def create_dpg_policy(
        node,
        name,
        policyDescription,
        proxy_config
    ):
    result = dict()
    request = {}
    if name != "":
        request['name'] = name;

    if policyDescription != "":
        request['description'] = policyDescription;

    proxyConfigs = []
    if len(proxy_config) > 0:
        for config in proxy_config:
            dictProxyConfig=dict()
            if config['api_url'] != '':
                dictProxyConfig["api_url"]=config['api_url'];

            if config['destination_url'] != "":
                dictProxyConfig["destination_url"]=config['destination_url'];

            proxyConfigTokens = []
            if len(config['tokens']) > 0:
                for token in config['tokens']:
                    dictToken = dict()
                    if token['name'] != "":
                        dictToken['name'] = token['name'];

                    if token['operation'] != "":
                        dictToken['operation'] = token['operation'];

                    if token['protection_policy'] != "":
                        dictToken['protection_policy'] = token['protection_policy'];

                    if token['access_policy'] != "":
                        dictToken['access_policy'] = token['access_policy'];

                    proxyConfigTokens.append(dictToken)
                
            dictProxyConfig["json_request_" + config['rest_op_type'] + "_tokens"] = proxyConfigTokens

            proxyConfigs.append(dictProxyConfig)

    request['proxy_config'] = proxyConfigs;

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/dpg-policies",
          )
      result['success'] = 'DPG Policy creation success!'
      result['payload'] = payload
      result['response'] = response
      return result
    except:
      result['failed'] = True
      raise

#below is new
def create_dpg_client_profile(
        node,
        name,
        app_connector_type,
        ca_id,
        cert_duration,
        configurations,
        csr_parameters,
        heartbeat_threshold,
        lifetime,
        max_clients,
        nae_iface_port,
        policy_id
        ):
    result = dict()
    request = {}
    request['name'] = name;
    request['app_connector_type'] = app_connector_type;
    request['configurations'] = configurations;
    request['csr_parameters'] = csr_parameters;

    if ca_id != "":
        request['ca_id'] = ca_id;

    if cert_duration != 0:
        request['cert_duration'] = cert_duration;

    if heartbeat_threshold != 0:
        request['heartbeat_threshold'] = heartbeat_threshold;

    if lifetime != "":
        request['lifetime'] = lifetime;

    if max_clients != 0:
        request['max_clients'] = max_clients;

    if nae_iface_port != 0:
        request['nae_iface_port'] = nae_iface_port;

    if policy_id != "":
        request['policy_id'] = policy_id;

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="data-protection/client-profiles",
          )
      result['success'] = 'Client Profile creation success!'
      result['payload'] = payload;
      result['response'] = response;
      return result
    except:
      result['failed'] = True
      raise
