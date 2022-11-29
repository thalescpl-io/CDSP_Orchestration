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
        activationDate="",
        algorithm="",
        aliases=[],
        archiveDate="",
        certType="",
        compromiseDate="",
        compromiseOccurrenceDate="",
        curveid="",
        deactivationDate="",
        defaultIV="",
        destroyDate="",
        encoding="",
        keyFormat="",
        generateKeyId=False,
        hkdfCreateParameters={},
        Id="",
        idSize=None,
        keyId="",
        labels={},
        macSignBytes="",
        macSignKeyIdentifier="",
        macSignKeyIdentifierType="",
        material="",
        ownerId="",
        muid="",
        name="",
        objectType="",
        padded=False,
        processStartDate="",
        protectStopDate="",
        revocationMessage="",
        revocationReason="",
        rotationFrequencyDays="",
        secretDataEncoding="",
        secretDataLink="",
        signingAlgo="",
        size=None,
        state="",
        undeletable=False,
        unexportable=False,
        usageMask=None,
        uuid="",
        xts=False
    ):
    result = dict()
    request = {}

    if activationDate != "":
        request['activationDate']=activationDate

    if algorithm != "":
        request['algorithm']=algorithm
  
    if len(aliases) > 0:
        request['aliases']=aliases

    if archiveDate != "":
        request['archiveDate']=archiveDate

    if certType != "":
        request['certType']=certType

    if compromiseOccurrenceDate != "":
        request['compromiseOccurrenceDate']=compromiseOccurrenceDate

    if curveid != "":
        request['curveid']=curveid

    if deactivationDate != "":
        request['deactivationDate']=deactivationDate

    if defaultIV != "":
        request['defaultIV']=defaultIV

    if destroyDate != "":
        request['destroyDate']=destroyDate

    if encoding != "":
        request['encoding']=encoding

    if keyFormat != "":
        request['format']=keyFormat

    request['generateKeyId']=generateKeyId

    request['hkdfCreateParameters']=hkdfCreateParameters

    if Id != "":
        request['id']=Id

    if idSize is not None:
        request['idSize']=idSize

    if keyId != "":
        request['keyId']=keyId

    request['labels']=labels

    if macSignBytes != "":
        request['macSignBytes']=macSignBytes

    if macSignKeyIdentifier != "":
        request['macSignKeyIdentifier']=macSignKeyIdentifier

    if macSignKeyIdentifierType != "":
        request['macSignKeyIdentifierType']=macSignKeyIdentifierType

    if material != "":
        request['material']=material

    if ownerId != "":
        request['ownerId']={"ownerId": ownerId}

    if muid != "":
        request['muid']=muid

    if name != "":
        request['name']=name

    if objectType != "":
        request['objectType']=objectType

    request['padded']=padded

    if processStartDate != "":
        request['processStartDate']=processStartDate

    if protectStopDate != "":
        request['protectStopDate']=protectStopDate

    if revocationMessage != "":
        request['revocationMessage']=revocationMessage

    if revocationReason != "":
        request['revocationReason']=revocationReason

    if rotationFrequencyDays != "":
        request['rotationFrequencyDays']=rotationFrequencyDays

    if secretDataEncoding != "":
        request['secretDataEncoding']=secretDataEncoding

    if secretDataLink != "":
        request['secretDataLink']=secretDataLink

    if signingAlgo != "":
        request['signingAlgo']=signingAlgo

    if size is not None:
        request['size']=size

    if state != "":
        request['state']=state

    request['undeletable']=undeletable

    request['unexportable']=unexportable

    if usageMask is not None:
        request['usageMask']=usageMask

    if uuid != "":
        request['uuid']=uuid

    request['xts']=xts

    payload = json.dumps(request)

    try:
      response = POSTData(
              payload=payload,
              cm_node=node,
              cm_api_endpoint="vault/keys2",
          )
      if response == '4xx':
          result['success'] = 'User already exists with same username'
      else:
          result['success'] = response

      return response
    except:
      result['failed'] = True

