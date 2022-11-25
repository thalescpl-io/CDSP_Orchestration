#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.keys2 import new

def main():
    localNode = dict(
            server_ip=dict(type='str', required=True),
            server_private_ip=dict(type='str', required=True),
            server_port=dict(type='int', required=True),
            user=dict(type='str', required=True),
            password=dict(type='str', required=True),
            verify=dict(type='bool', required=True),
        )
    hkdfCreateParams = dict()
    label=dict()
    module = AnsibleModule(
            argument_spec=dict(
                localNode=dict(type='dict', options=localNode, required=True),
                activationDate=dict(type='str', required=False, default=""),
                algorithm=dict(type='str', required=False, choices=['aes', 'tdes', 'rsa', 'ec', 'hmac-sha1', 'hmac-sha256', 'hmac-sha384', 'hmac-sha512', 'seed', 'aria', 'opaque'], default="aes"),
                aliases=dict(type='list', element='str' required=False, default=[]),
                archiveDate=dict(type='str', required=False, default=""),
                certType=dict(type='str', required=False, default=""),
                compromiseDate=dict(type='str', required=False, default=""),
                compromiseOccurrenceDate=dict(type='str', required=False, default=""),
                curveid=dict(type='str', required=False, default=""),
                deactivationDate=dict(type='str', required=False, default=""),
                defaultIV=dict(type='str', required=False, default=""),
                destroyDate=dict(type='str', required=False, default=""),
                encoding=dict(type='str', required=False, default=""),
                keyFormat=dict(type='str', required=False, default=""),
                generateKeyId=dict(type='bool', required=False, default=False),
                hkdfCreateParameters=dict(type='dict', options=hkdfCreateParams, required=False),
                Id=dict(type='str', required=False, default=""),
                idSize=dict(type='int', required=False, default=None),
                keyId=dict(type='str', required=False, default=""),
                labels=dict(type='dict', options=label, required=False),
                macSignBytes=dict(type='str', required=False, default=""),
                macSignKeyIdentifier=dict(type='str', required=False, default=""),
                macSignKeyIdentifierType=dict(type='str', required=False, default=""),
                material=dict(type='str', required=False, default=""),
                ownerId=dict(type='str', required=False, default=""),
                muid=dict(type='str', required=False, default=""),
                name=dict(type='str', required=False, default=""),
                objectType=dict(type='str', required=False, default=""),
                padded=dict(type='dict', options=label, required=False),
                processStartDate=dict(type='str', required=False, default=""),
                protectStopDate=dict(type='str', required=False, default=""),
                revocationMessage=dict(type='str', required=False, default=""),
                revocationReason=dict(type='str', required=False, default=""),
                rotationFrequencyDays=dict(type='str', required=False, default=""),
                secretDataEncoding=dict(type='str', required=False, default=""),
                secretDataLink=dict(type='str', required=False, default=""),
                signingAlgo=dict(type='str', required=False, default=""),
                size=dict(type='int', required=False, default=None),
                state=dict(type='str', required=False, default=""),
                undeletable=dict(type='bool', required=False, default=False),
                unexportable=dict(type='bool', required=False, default=False),
                usageMaske=dict(type='int', required=False, default=None),
                uuid=dict(type='str', required=False, default=""),
                xts=dict(type='bool', required=False, default=False),
            ),
        )

    localNode = module.params.get('localNode');
    activationDate = module.params.get('activationDate');
    algorithm = module.params.get('algorithm');
    aliases = module.params.get('aliases');
    archiveDate = module.params.get('archiveDate');
    certType = module.params.get('certType');
    compromiseDate = module.params.get('compromiseDate');
    compromiseOccurrenceDate = module.params.get('compromiseOccurrenceDate');
    curveid = module.params.get('curveid');
    deactivationDate = module.params.get('deactivationDate'); 
    defaultIV = module.params.get('defaultIV');
    destroyDate = module.params.get('destroyDate');
    encoding = module.params.get('encoding');
    keyFormat = module.params.get('format');
    generateKeyId = module.params.get('generateKeyId');
    hkdfCreateParameters = module.params.get('hkdfCreateParameters');
    Id = module.params.get('id');
    idSize = module.params.get('idSize');
    keyId = module.params.get('keyId');
    labels = module.params.get('labels');
    macSignBytes = module.params.get('macSignBytes');
    macSignKeyIdentifier = module.params.get('macSignKeyIdentifier');
    macSignKeyIdentifierType = module.params.get('macSignKeyIdentifierType');
    material = module.params.get('material');
    ownerId = module.params.get('ownerId');
    muid = module.params.get('muid');
    name = module.params.get('name');
    objectType = module.params.get('objectType');
    padded = module.params.get('padded');
    processStartDate = module.params.get('processStartDate');
    protectStopDate = module.params.get('protectStopDate');
    revocationMessage = module.params.get('revocationMessage');
    revocationReason = module.params.get('revocationReason');
    rotationFrequencyDays = module.params.get('rotationFrequencyDays');
    secretDataEncoding = module.params.get('secretDataEncoding');
    secretDataLink = module.params.get('secretDataLink');
    signingAlgo = module.params.get('signingAlgo');
    size = module.params.get('size');
    state = module.params.get('state');
    undeletable = module.params.get('undeletable');
    unexportable = module.params.get('unexportable');
    usageMaske = module.params.get('usageMask');
    uuid = module.params.get('uuid');
    xts = module.params.get('xts');

    result = dict(
        changed=False,
    )

    response = new(
        node=localNode,
		activationDate=activationDate,
        algorithm=algorithm,
        aliases=aliases,
        archiveDate=archiveDate,
        certType=certType,
        compromiseDate=compromiseDate,
        compromiseOccurrenceDate=compromiseOccurrenceDate,
        curveid=curveid,
        deactivationDate=deactivationDate,
        defaultIV=defaultIV,
        destroyDate=destroyDate,
        encoding=encoding,
        keyFormat=keyFormat,
        generateKeyId=generateKeyId,
        hkdfCreateParameters=hkdfCreateParameters,
        Id=Id,
        idSize=idSize,
        keyId=keyId,
        labels=labels,
        macSignBytes=macSignBytes,
        macSignKeyIdentifier=macSignKeyIdentifier,
        macSignKeyIdentifierType=macSignKeyIdentifierType,
        material=material,
        ownerId=ownerId,
        muid=muid,
        name=name,
        objectType=objectType,
        padded=padded,
        processStartDate=processStartDate,
        protectStopDate=protectStopDate,
        revocationMessage=revocationMessage,
        revocationReason=revocationReason,
        rotationFrequencyDays=rotationFrequencyDays,
        secretDataEncoding=secretDataEncoding,
        secretDataLink=secretDataLink,
        signingAlgo=signingAlgo,
        size=size,
        state=state,
        undeletable=undeletable,
        unexportable=unexportable,
        usageMask=usageMask,
		uuid=uuid,
        xts=xts,
    )

    result['response'] = response

    module.exit_json(**result)

if __name__ == '__main__':
    main()
