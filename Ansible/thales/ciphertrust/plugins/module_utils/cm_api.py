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
import ast

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def getJwt(host, username, password):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    auth_url='https://'+host+'/api/v1/auth/tokens'
    auth_payload = {
        "grant_type":"password",
        "username":username,
        "password":password,
    }
    response = requests.post(auth_url, json=auth_payload, verify=False)
    return response.json()["jwt"]

# This will never return the ID
# There will be a separate call to be made to get the ID
def POSTData(payload=None, cm_node=None, cm_api_endpoint=None):
    # Create the session object
    # cm_node_json = cm_node.replace("\'", "\"")
    node = ast.literal_eval(json.dumps(cm_node))
    # node = json.loads(cm_node_json)
    cmSessionObject = CMAPIObject(
            cm_api_user=node["user"],
            cm_api_pwd=node["password"],
            cm_url=node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the post API call to create the resource on CM 
    try:
      response = requests.post(
        cmSessionObject["url"], 
        headers=cmSessionObject["headers"], 
        json = json.loads(payload), 
        verify=False)
      if "codeDesc" in response.json():
          codeDesc=response.json()["codeDesc"]
          if 'NCERRKeyAlreadyExists' in codeDesc:
              return '4xx'
          if 'NCERRConflict' in codeDesc:
              return '4xx'
      else:
          return response.json()
    except requests.exceptions.RequestException as err:
        raise

# This will never return the ID
# There will be a separate call to be made to get the ID
def POSTWithoutData(cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the post API call to create the resource on CM 
    try:
      response = requests.post(
        cmSessionObject["url"], 
        headers=cmSessionObject["headers"], 
        verify=False)
      if "codeDesc" in response.json():
          codeDesc=response.json()["codeDesc"]
          if 'NCERRKeyAlreadyExists' in codeDesc:
              return '4xx'
          if 'NCERRConflict' in codeDesc:
              return '4xx'
      else:
          return response.json()
    except requests.exceptions.RequestException as err:
        raise

def PATCHData(payload=None, cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the patch API call to update the resource on CM 
    try:
      response = requests.patch(
        cmSessionObject["url"], 
        headers=cmSessionObject["headers"], 
        json = json.loads(payload), 
        verify=False)
      if "codeDesc" in response.json():
          codeDesc=response.json()["codeDesc"]
          if 'NCERRKeyAlreadyExists' in codeDesc:
              return '4xx'
          if 'NCERRConflict' in codeDesc:
              return '4xx'
      else:
          return response.json()
    except requests.exceptions.RequestException as err:
        raise

def DELETEByNameOrId(name=None, cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the delete API call to delete the resource on CM
    try:
      response = requests.delete(cmSessionObject["url"] + "/" + name, headers=cmSessionObject["headers"], verify=False)
      if is_json(str(response)):
          if "codeDesc" in response.json():
              codeDesc=response.json()["codeDesc"]
              if 'NCERRResourceNotFound' in codeDesc:
                  return 'no matching resource found'
          else:
              return 'resource deletion succesful'
      else:
          if '204' in str(response):
              return 'resource deletion succesful'
          if '405' in str(response):
              return 'resource ID/Name is a required parameter'
    except requests.exceptions.RequestException as err:
        raise
    except json.decoder.JSONDecodeError as jsonErr:
        return jsonErr

def DeleteWithoutData(cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the delete API call to delete the resource on CM
    try:
      response = requests.delete(cmSessionObject["url"], headers=cmSessionObject["headers"], verify=False)
      if is_json(str(response)):
          if "codeDesc" in response.json():
              codeDesc=response.json()["codeDesc"]
              if 'NCERRResourceNotFound' in codeDesc:
                  return 'no matching resource found'
          else:
              return 'resource deletion succesful'
      else:
          if '204' in str(response):
              return 'resource deletion succesful'
          if '405' in str(response):
              return 'resource ID/Name is a required parameter'
    except requests.exceptions.RequestException as err:
        raise
    except json.decoder.JSONDecodeError as jsonErr:
        return jsonErr

def GETData(cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the delete API call to delete the resource on CM
    try:
        response = requests.get(cmSessionObject["url"], headers=cmSessionObject["headers"], verify=False)
        if is_json(str(response)):
            return response
        else:
            return '4xx'
    except requests.exceptions.RequestException as err:
        raise

# Below method is outdated...need to be cleaned up later
def GETIdByName(name=None, cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    # execute the delete API call to delete the resource on CM
    ret=dict()
    try:
        response = requests.get(cmSessionObject["url"] + "/?skip=0&limit=1&name=" + name, headers=cmSessionObject["headers"], verify=False)
        if len(response.json()["resources"]) > 0:
            ret["id"]=response.json()["resources"][0]["id"]
            ret["status"]='2xx'
            return ret
        else:
            ret["status"]='4xx'
            ret["id"]=''
            return ret
    except requests.exceptions.RequestException as err:
        raise

def GETIdByQueryParam(param=None, value=None, cm_node=None, cm_api_endpoint=None):
    # Create the session object
    cmSessionObject = CMAPIObject(
            cm_api_user=cm_node["user"],
            cm_api_pwd=cm_node["password"],
            cm_url=cm_node["server_ip"],
            cm_api_endpoint=cm_api_endpoint,
            verify=False,
        )
    ret=dict()
    try:
        response = requests.get(
                cmSessionObject["url"] + "/?skip=0&limit=1&" + param + "=" + value, 
                headers=cmSessionObject["headers"], 
                verify=False)
        if response.json()["resources"] == None:
            ret["status"]='4xx'
            ret["id"]=''
            return ret
        if len(response.json()["resources"]) > 0:
            if cm_api_endpoint == "usermgmt/users":
                ret["id"]=response.json()["resources"][0]["user_id"]
            else:
                ret["id"]=response.json()["resources"][0]["id"]
            ret["status"]='2xx'
            return ret
        else:
            ret["status"]='4xx'
            ret["id"]=''
            return ret
    except requests.exceptions.RequestException as err:
        raise

def CMAPIObject(cm_api_user=None, cm_api_pwd=None, cm_url=None, cm_api_endpoint=None, verify=None):
    """Create a Ciphertrust Manager (CM) client"""
    session=dict()
    session["url"] = 'https://' + cm_url + '/api/v1/' + cm_api_endpoint
    session["headers"] = {"Content-Type": "application/json; charset=utf-8","Authorization": "Bearer " + getJwt(cm_url, cm_api_user, cm_api_pwd),}
    return session

