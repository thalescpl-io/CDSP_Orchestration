#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2022 Thales Group. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import requests
import urllib3
import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.thales.ciphertrust.plugins.module_utils.keys2 import new

DOCUMENTATION = '''
---
module: vault_keys2_create
short_description: This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
description:
    - This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with create User API
version_added: "1.0.0"
author: Anurag Jain, Developer Advocate Thales Group
options:
    localNode:
        description:
            - This is a dictionary type of object that contains CipherTrust Manager Instance FQDN and credentials
        required: true
        type: dict
        elements:
            - str
            - bool
    name:
        description: Full name of the user.
        required: false
        type: str
        default: null
    activationDate:
        description: Date/time the object becomes active
        required: false
        type: str
        default: null
    algorithm:
        description: Cryptographic algorithm this key is used with. Defaults to 'aes'
        type: str
        required: false
        choices:
          - aes
          - tdes
          - rsa
          - ec
          - hmac-sha1
          - hmac-sha256
          - hmac-sha384
          - hmac-sha512
          - seed
          - aria
          - opaque
        default: aes
    aliases:
        description: Aliases associated with the key. The alias and alias-type must be specified. The alias index is assigned by this operation, and need not be specified.
        type: list
        required: false
        default: null
    archiveDate:
        description: Date/time the object becomes archived
        required: false
        type: str
        default: null
    certType
        description: This specifies the type of certificate object that is being created. Valid values are 'x509-pem' and 'x509-der'. At present, we only support x.509 certificates. The cerfificate data is passed in via the 'material' field. The certificate type is infered from the material if it is left blank.
        type: str
        required: false
        default: null
    compromiseDate:
        description: Date/time the object entered into the compromised state.
        type: str
        required: false
        default: null
    compromiseOccurrenceDate:
        description: Date/time when the object was first believed to be compromised, if known. Only valid if the revocation reason is CACompromise or KeyCompromise, otherwise ignored.
        type: str
        required: false
        default: null
    curveid:
        description: Cryptographic curve id for elliptic key. Key algorithm must be 'EC'
        choices: 
          - secp224k1
          - secp224r1
          - secp256k1
          - secp384r1
          - secp521r1
          - prime256v1
          - brainpoolP224r1
          - brainpoolP224t1
          - brainpoolP256r1
          - brainpoolP256t1
          - brainpoolP384r1
          - brainpoolP384t1
          - brainpoolP512r1
          - brainpoolP512t1
        type: str
        required: false
        default: null
    deactivationDate:
        description: Date/time the object becomes inactive
        type: str
        required: false
        default: null
    defaultIV:
        description: Deprecated. This field was introduced to support specific legacy integrations and applications. New applications are strongly recommended to use a unique IV for each encryption request. Refer to Crypto encrypt endpoint for more details. Must be a 16 byte hex encoded string (32 characters long). If specified, this will be set as the default IV for this key.
        type: str
        required: false
        default: null
    destroyDate:
        description: Date/time the object was destroyed.
        type: str
        required: false
        default: null
    encoding:
        description: Specifies the encoding used for the 'material' field.
        type: str
        choices:
          - hex
          - base64
        required: false
        default: null
    keyFormat:
        description: This parameter is used while importing keys ('material' is not empty), and also when returning the key material after the key is created ('includeMaterial' is true).
        type: str
        required: false
        default: null
    generateKeyId:
        description: If specified as true, the key's keyId identifier of type long is generated. Defaults to false.
        type: bool
        required: false
        default: false
    hkdfCreateParameters:
        description: Information which is used to create a Key using HKDF.
        type: dict
        required: false
        default: null
    Id:
        description: This optional parameter specifies the identifier of the key (id). It is used only when creating keys with specific key material. If set, the key's id is set to this value.
        type: str
        required: false
        default: null
    idSize:
        description: Size of the ID for the key
        type: int
        required: false
        default: null
    keyId:
        description: Additional identifier of the key. The format of this value is of type long. This is optional and applicable for import key only. If set, the value is imported as the key's keyId.
        type: str
        required: false
        default: null
    labels:
        description: Optional key/value pairs used to group keys. APIs that list keys can use labels to filter the set of matching resources. A label's key has an optional prefix up to 253 characters followed by a forward slash and a required name up to 63 characters. For example, sales.widgets.com/region is a label key with the prefix sales.widgets.com and the name region, while region is a label key without a prefix. A label's value may be empty and may be up to 63 characters. Each part of the label (i.e. the prefix, name, and value) must begin and end with an alphanumeric character (a-zA-Z0-9). Characters inbetween the beginning and end may contain alphanumeric characters, dots (.), dashes (-) and underscores (_). A Label can be a simple tag by specifying a key with no value (e.g. { "critical": "" }). Here's a full example showing a name/value pair with prefix, a name/value pair, and a simple tag:
        "labels": {
            "sales.widgets.com/region": "noram",
            "team": "sales",
            "critical": ""
        }
        type: dict
        required: false
        default: null
    macSignBytes:
        description: This parameter specifies the MAC/Signature bytes to be used for verification while importing a key. The "wrappingMethod" should be "mac/sign" and the required parameters for the verification must be set.
        type: str
        required: false
        default: null
    macSignKeyIdentifier:
        description: This parameter specifies the identifier of the key to be used for generating MAC or signature of the key material. The "wrappingMethod" should be "mac/sign" to verify the MAC/signature("macSignBytes") of the key material("material"). For verifying the MAC, the key has to be a HMAC key. For verifying the signature, the key has to be an RSA private or public key.
        type: str
        required: false
        default: null
    macSignKeyIdentifierType:
        description: This parameter specifies the identifier of the key("macSignKeyIdentifier") used for generating MAC or signature of the key material. The "wrappingMethod" should be "mac/sign" to verify the mac/signature("macSignBytes") of the key material("material")
        type: str
        choices:
          - name
          - id
          - alias
        required: false
        default: null
    material:
        description: If set, the value will be imported as the key's material. If not set, new key material will be generated on the server (certificate objects must always specify the material). The format of this value depends on the algorithm. If the algorithm is 'aes', 'tdes', 'hmac-*', 'seed' or 'aria', the value should be the hex-encoded bytes of the key material. If the algorithm is 'rsa', and the format is 'pkcs12', it should be the base64 encoded PFX file. If the algorithm is 'rsa' or 'ec', and format is not 'pkcs12', the value should be a PEM-encoded private or public key using PKCS1 or PKCS8 format. For a X.509 DER encoded certificate, certType equals 'x509-der' and the material should equal the hex encoded certificate. The material for a X.509 PEM encoded certificate (certType = 'x509-pem') should equal the certificate itself. When placing the PEM encoded certificate inside a JSON object (as in the playground), be sure to change all new line characters in the certificate to the string newline char.
        type: str
        required: false
        default: null
    ownerId:
        description: Optional owner information for the key, required for non-admin. Value should be the user's user_id
        type: str
        required: false
        default: null
    muid:
        description: Additional identifier of the key. This is optional and applicable for import key only. If set, the value is imported as the key's muid.
        type: str
        required: false
        default: null
    name:
        description: Optional friendly name, The key name should not contain special characters such as angular brackets (<,>) and backslash ().
        type: str
        required: false
        default: null
    objectType:
        description: This specifies the type of object that is being created. Valid values are 'Symmetric Key', 'Public Key', 'Private Key', 'Secret Data', 'Opaque Object', or 'Certificate'. The object type is inferred for many objects, but must be supplied for the certificate object.
        type: str
        choices:
          - Symmetric Key
          - Public Key
          - Private Key
          - Secret Data
          - Opaque Object
          - Certificate
        required: false
        default: null
    padded:
        description: This parameter determines the padding for the wrap algorithm while unwrapping a symmetric key
        type: bool
        required: false
        default: false
    processStartDate:
        description: Date/time when a Managed Symmetric Key Object MAY begin to be used to process cryptographically protected information (e.g., decryption or unwrapping)
        type: str
        required: false
        default: null
    protectStopDate:
        description: Date/time after which a Managed Symmetric Key Object SHALL NOT be used for applying cryptographic protection (e.g., encryption or wrapping)
        type: str
        required: false
        default: null
    revocationMessage:
        description: Message explaining revocation.
        type: str
        required: false
        default: null
    revocationReason:
        description: The reason the key is being revoked.
        choices:
          - Unspecified
          - KeyCompromise
          - CACompromise
          - AffiliationChanged
          - Superseded
          - CessationOfOperation
          - PrivilegeWithdrawn
        type: str
        required: false
        default: null
    rotationFrequencyDays:
        description: Number of days from current date to rotate the key. It should be greater than or equal to 0. Default is an empty string. If set to 0, rotationFrequencyDays set to an empty string and auto rotation of key will be disabled.
        type: str
        required: false
        default: null
    secretDataEncoding:
        description: For pkcs12 format, this field specifies the encoding method used for the secretDataLink material. Ignore this field if secretData is created from REST and is in plain format. Specify the value of this field as HEX format if secretData is created from KMIP.
        type: str
        required: false
        default: null
    secretDataLink:
        description: For pkcs12 format, either secretDataLink or password should be specified. The value can be either ID or name of Secret Data.
        type: str
        required: false
        default: null
    signingAlgo:
        description: This parameter specifies the algorithm to be used for generating the signature for the verification of the "macSignBytes" during import of key material. The "wrappingMethod" should be "mac/sign" to verify the signature("macSignBytes") of the key material("material").
        choices:
          - RSA
          - RSA-PSS
        type: str
        required: false
        default: null
    size:
        description: Bit length for the key.
        type: int
        required: false
        default: null
    state:
        description: Optional initial key state (Pre-Active) upon creation. Defaults to Active. If set, activationDate and processStartDate can not be specified during key creation. In case of import, allowed values are "Pre-Active", "Active", "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". If key material is not specified, it will not be autogenerated if input parameters correspond to either of these states - "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". Key in "Destroyed" or "Destroyed Compromised" state would not have key material even if specified during key creation.
        type: str
        required: false
        default: null
    undeletable:
        description: Key is not deletable. Defaults to false.
        type: bool
        required: false
        default: false
    unexportable:
        description: Key is not exportable. Defaults to false.
        type: bool
        required: false
        default: false
    usageMaske:
        description: Cryptographic usage mask. Add the usage masks to allow certain usages. Sign (1), Verify (2), Encrypt (4), Decrypt (8), Wrap Key (16), Unwrap Key (32), Export (64), MAC Generate (128), MAC Verify (256), Derive Key (512), Content Commitment (1024), Key Agreement (2048), Certificate Sign (4096), CRL Sign (8192), Generate Cryptogram (16384), Validate Cryptogram (32768), Translate Encrypt (65536), Translate Decrypt (131072), Translate Wrap (262144), Translate Unwrap (524288), FPE Encrypt (1048576), FPE Decrypt (2097152). Add the usage mask values to allow the usages. To set all usage mask bits, use 4194303. Equivalent usageMask values for deprecated usages 'fpe' (FPE Encrypt + FPE Decrypt = 3145728), 'blob' (Encrypt + Decrypt = 12), 'hmac' (MAC Generate + MAC Verify = 384), 'encrypt' (Encrypt + Decrypt = 12), 'sign' (Sign + Verify = 3), 'any' (4194303 - all usage masks).
        type: int
        default: null
        required: false
    uuid:
        description: Additional identifier of the key. The format of this value is 32 hexadecimal lowercase digits with 4 dashes. This is optional and applicable for import key only. If set, the value is imported as the key's uuid. If not set, new key uuid is generated on the server.
        type: str
        required: false
        default: null
    xts:
        description: If set to true, then key created will be XTS/CBC-CS1 Key. Defaults to false. Key algorithm must be 'AES'.
        type: bool
        required: false
        default: false
'''

EXAMPLES = '''
- name: "Create DPG Protection Policy"
  thales.ciphertrust.dpg_protection_policy_create:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Privare IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    username: "john.doe"
    password: "cmPassw0rd!"
    email: "john.doe@example.com"
    name: "John Doe"
'''

RETURN = '''

'''

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
                aliases=dict(type='list', element='str', required=False, default=[]),
                archiveDate=dict(type='str', required=False, default=""),
                certType=dict(type='str', required=False, default=""),
                compromiseDate=dict(type='str', required=False, default=""),
                compromiseOccurrenceDate=dict(type='str', required=False, default=""),
                curveid=dict(type='str', choices=['secp224k1', 'secp224r1', 'secp256k1', 'secp384r1', 'secp521r1', 'prime256v1', 'brainpoolP224r1', 'brainpoolP224t1', 'brainpoolP256r1', 'brainpoolP256t1', 'brainpoolP384r1', 'brainpoolP384t1', 'brainpoolP512r1', 'brainpoolP512t1'], required=False),
                deactivationDate=dict(type='str', required=False, default=""),
                defaultIV=dict(type='str', required=False, default=""),
                destroyDate=dict(type='str', required=False, default=""),
                encoding=dict(type='str', choices=['hex', 'base64'], required=False),
                keyFormat=dict(type='str', required=False, default=""),
                generateKeyId=dict(type='bool', required=False, default=False),
                hkdfCreateParameters=dict(type='dict', options=hkdfCreateParams, required=False),
                Id=dict(type='str', required=False, default=""),
                idSize=dict(type='int', required=False, default=None),
                keyId=dict(type='str', required=False, default=""),
                labels=dict(type='dict', options=label, required=False),
                macSignBytes=dict(type='str', required=False, default=""),
                macSignKeyIdentifier=dict(type='str', required=False, default=""),
                macSignKeyIdentifierType=dict(type='str', choices=['name', 'id', 'alias'], required=False),
                material=dict(type='str', required=False, default=""),
                ownerId=dict(type='str', required=False, default=""),
                muid=dict(type='str', required=False, default=""),
                name=dict(type='str', required=False, default=""),
                objectType=dict(type='str', choices=['Symmetric Key', 'Public Key', 'Private Key', 'Secret Data', 'Opaque Object', 'Certificate'], required=False),
                padded=dict(type='dict', options=label, required=False),
                processStartDate=dict(type='str', required=False, default=""),
                protectStopDate=dict(type='str', required=False, default=""),
                revocationMessage=dict(type='str', required=False, default=""),
                revocationReason=dict(type='str', choices=['Unspecified', 'KeyCompromise', 'CACompromise', 'AffiliationChanged', 'Superseded', 'CessationOfOperation', 'PrivilegeWithdrawn'], required=False),
                rotationFrequencyDays=dict(type='str', required=False, default=""),
                secretDataEncoding=dict(type='str', required=False, default=""),
                secretDataLink=dict(type='str', required=False, default=""),
                signingAlgo=dict(type='str', choice=['RSA-PSS', 'RSA'], required=False),
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
    usageMask = module.params.get('usageMask');
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

