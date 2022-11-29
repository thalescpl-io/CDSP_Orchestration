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
