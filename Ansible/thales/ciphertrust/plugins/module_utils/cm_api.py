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

def CMAPIObject(cm_api_user=None, cm_api_pwd=None, cm_url=None, cm_api_endpoint=None, verify=None):
    """Create a Ciphertrust Manager (CM) client"""
    session=dict()
    session["url"] = 'https://' + cm_url + '/api/v1/' + cm_api_endpoint
    session["headers"] = {"Content-Type": "application/json; charset=utf-8","Authorization": "Bearer " + getJwt(cm_url, cm_api_user, cm_api_pwd),}
    return session

