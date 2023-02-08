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

def new(node, 
        cert_sub_dn, 
        conn, 
        email, 
        enable_cert_auth_bool, 
        is_domain_user_bool, 
        prevent_ui_login_bool, 
        name, 
        pwd, 
        pwd_change_reqd_bool, 
        user_id, 
        username):
    result = dict()
    request = {
            "enable_cert_auth": enable_cert_auth_bool,
            "is_domain_user": is_domain_user_bool,
            "login_flags": {
                "prevent_ui_login": prevent_ui_login_bool
            },
            "password": pwd,
            "password_change_required": pwd_change_reqd_bool,
            "username": username,
        }
    
    request['app_metadata'] = dict()
    
    request['user_metadata'] = dict()

    if cert_sub_dn != "":
        request['certificate_subject_dn']=cert_sub_dn

    if conn != "":
        request['connection']=conn

    if email != "":
        request['email']=email
    else:
        request['email']=username + "@local"

    if name != "":
        request['name']=name

    if user_id != "":
        request['user_id']=user_id


    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="usermgmt/users",
          )
      if response == '4xx':
          result['success'] = 'User already exists with same username'
      else:
          result['success'] = 'User Created Succesfully'

      return response
    except:
      result['failed'] = True

