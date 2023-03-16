
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.thales.ciphertrust.vault_keys2_save_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

thales.ciphertrust.vault_keys2_save module -- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `thales.ciphertrust collection <https://galaxy.ansible.com/thales/ciphertrust>`_ (version 1.0.0).

    To install it, use: :code:`ansible-galaxy collection install thales.ciphertrust`.

    To use it in a playbook, specify: :code:`thales.ciphertrust.vault_keys2_save`.

.. version_added

.. rst-class:: ansible-version-added

New in thales.ciphertrust 1.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with keys management API


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-activationDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-activationdate:

      .. rst-class:: ansible-option-title

      **activationDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-activationDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time the object becomes active


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-algorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-algorithm:

      .. rst-class:: ansible-option-title

      **algorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-algorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cryptographic algorithm this key is used with.

      Defaults to 'aes'


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"aes"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"tdes"`
      - :ansible-option-choices-entry:`"rsa"`
      - :ansible-option-choices-entry:`"ec"`
      - :ansible-option-choices-entry:`"hmac-sha1"`
      - :ansible-option-choices-entry:`"hmac-sha256"`
      - :ansible-option-choices-entry:`"hmac-sha384"`
      - :ansible-option-choices-entry:`"hmac-sha512"`
      - :ansible-option-choices-entry:`"seed"`
      - :ansible-option-choices-entry:`"aria"`
      - :ansible-option-choices-entry:`"opaque"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-aliases"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-aliases:

      .. rst-class:: ansible-option-title

      **aliases**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-aliases" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Aliases associated with the key.

      The alias and alias-type must be specified.

      The alias index is assigned by this operation, and need not be specified.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-aliases/alias"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-aliases/alias:

      .. rst-class:: ansible-option-title

      **alias**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-aliases/alias" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      An alias for a key name


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-aliases/index"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-aliases/index:

      .. rst-class:: ansible-option-title

      **index**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-aliases/index" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Index associated with alias. Each alias within an object has a unique index


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-aliases/type"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-aliases/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-aliases/type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Type of alias (allowed values are string and uri)


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allVersions"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-allversions:

      .. rst-class:: ansible-option-title

      **allVersions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allVersions" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      To update the group permissions/custom attribute or both in metadata of all versions of the key. By default it is set to false. Set to true, only when to update the group/custom attribute or both permissions of all versions of the key.

      Only applicable for op\_type "patch"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-archiveDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-archivedate:

      .. rst-class:: ansible-option-title

      **archiveDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-archiveDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time the object becomes archived


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-certType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-certtype:

      .. rst-class:: ansible-option-title

      **certType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-certType" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This specifies the type of certificate object that is being created. Valid values are 'x509-pem' and 'x509-der'. At present, we only support x.509 certificates. The cerfificate data is passed in via the 'material' field. The certificate type is infered from the material if it is left blank.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"x509-pem"`
      - :ansible-option-choices-entry:`"x509-der"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cm_key_id"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-cm_key_id:

      .. rst-class:: ansible-option-title

      **cm_key_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cm_key_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CM ID of the key that needs to be patched.

      Only required if the op\_type is patch or create\_version


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compromiseDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-compromisedate:

      .. rst-class:: ansible-option-title

      **compromiseDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compromiseDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time the object entered into the compromised state.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compromiseOccurrenceDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-compromiseoccurrencedate:

      .. rst-class:: ansible-option-title

      **compromiseOccurrenceDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compromiseOccurrenceDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time when the object was first believed to be compromised, if known. Only valid if the revocation reason is CACompromise or KeyCompromise, otherwise ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-curveid"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-curveid:

      .. rst-class:: ansible-option-title

      **curveid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-curveid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cryptographic curve id for elliptic key.

      Key algorithm must be 'EC'


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"secp224k1"`
      - :ansible-option-choices-entry:`"secp224r1"`
      - :ansible-option-choices-entry:`"secp256k1"`
      - :ansible-option-choices-entry:`"secp384r1"`
      - :ansible-option-choices-entry:`"secp521r1"`
      - :ansible-option-choices-entry:`"prime256v1"`
      - :ansible-option-choices-entry:`"brainpoolP224r1"`
      - :ansible-option-choices-entry:`"brainpoolP224t1"`
      - :ansible-option-choices-entry:`"brainpoolP256r1"`
      - :ansible-option-choices-entry:`"brainpoolP256t1"`
      - :ansible-option-choices-entry:`"brainpoolP384r1"`
      - :ansible-option-choices-entry:`"brainpoolP384t1"`
      - :ansible-option-choices-entry:`"brainpoolP512r1"`
      - :ansible-option-choices-entry:`"brainpoolP512t1"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-deactivationDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-deactivationdate:

      .. rst-class:: ansible-option-title

      **deactivationDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-deactivationDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time the object becomes inactive


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultIV"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-defaultiv:

      .. rst-class:: ansible-option-title

      **defaultIV**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultIV" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Deprecated. This field was introduced to support specific legacy integrations and applications. New applications are strongly recommended to use a unique IV for each encryption request. Refer to Crypto encrypt endpoint for more details. Must be a 16 byte hex encoded string (32 characters long). If specified, this will be set as the default IV for this key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-destroyDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-destroydate:

      .. rst-class:: ansible-option-title

      **destroyDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-destroyDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time the object was destroyed.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-encoding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-encoding:

      .. rst-class:: ansible-option-title

      **encoding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-encoding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies the encoding used for the 'material' field.

      This parameter is used during importing keys when key material is not empty or while returning the key material after the key is created ('includeMaterial' is true)

      For wrapping scenarios and PKCS12 format, the only valid option is base64. In case of "Symmetric Keys" when 'format' parameter has 'base64' value and 'encoding' parameter also contains some value. The encoding parameter takes the priority. Following are the options for Symmetric Keys are hex or base64


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-format"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-format:

      .. rst-class:: ansible-option-title

      **format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter is used while importing keys ('material' is not empty), and also when returning the key material after the key is created ('includeMaterial' is true).

      For Asymmetric keys, When this parameter is not specified, while importing keys, the format of the material is inferred from the material itself. When this parameter is specified, while importing keys, the only allowed format is 'pkcs12', and this only applies to the 'rsa' algorithm (the 'material' should contain the base64 encoded value of the PFX file in this case). Options are pkcs1, pkcs8 (default) or pkcs12

      For Symmetric keys, When importing keys if specified, the value must be given according to the format of the material. Options are raw or opaque


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-generateKeyId"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-generatekeyid:

      .. rst-class:: ansible-option-title

      **generateKeyId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-generateKeyId" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If specified as true, the key's keyId identifier of type long is generated. Defaults to false.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hkdfCreateParameters"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-hkdfcreateparameters:

      .. rst-class:: ansible-option-title

      **hkdfCreateParameters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hkdfCreateParameters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information which is used to create a Key using HKDF.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hkdfCreateParameters/hashAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-hkdfcreateparameters/hashalgorithm:

      .. rst-class:: ansible-option-title

      **hashAlgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hkdfCreateParameters/hashAlgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Hash Algorithm is used for HKDF.

      This is required if ikmKeyName is specified, default is hmac-sha256.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"hmac-sha1"`
      - :ansible-option-choices-entry:`"hmac-sha224"`
      - :ansible-option-choices-entry-default:`"hmac-sha256"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"hmac-sha384"`
      - :ansible-option-choices-entry:`"hmac-sha512"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hkdfCreateParameters/ikmKeyName"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-hkdfcreateparameters/ikmkeyname:

      .. rst-class:: ansible-option-title

      **ikmKeyName**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hkdfCreateParameters/ikmKeyName" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Any existing symmetric key. Mandatory while using HKDF key generation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hkdfCreateParameters/info"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-hkdfcreateparameters/info:

      .. rst-class:: ansible-option-title

      **info**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hkdfCreateParameters/info" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Info is an optional hex value for HKDF based derivation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hkdfCreateParameters/salt"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-hkdfcreateparameters/salt:

      .. rst-class:: ansible-option-title

      **salt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hkdfCreateParameters/salt" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Salt is an optional hex value for HKDF based derivation.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This optional parameter specifies the identifier of the key (id). It is used only when creating keys with specific key material. If set, the key's id is set to this value.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-idSize"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-idsize:

      .. rst-class:: ansible-option-title

      **idSize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-idSize" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Size of the ID for the key


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyId"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-keyid:

      .. rst-class:: ansible-option-title

      **keyId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyId" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Additional identifier of the key. The format of this value is of type long. This is optional and applicable for import key only. If set, the value is imported as the key's keyId.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-labels"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-labels:

      .. rst-class:: ansible-option-title

      **labels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional key/value pairs used to group keys. APIs that list keys can use labels to filter the set of matching resources. A label's key has an optional prefix up to 253 characters followed by a forward slash and a required name up to 63 characters. For example, sales.widgets.com/region is a label key with the prefix sales.widgets.com and the name region, while region is a label key without a prefix. A label's value may be empty and may be up to 63 characters. Each part of the label (i.e. the prefix, name, and value) must begin and end with an alphanumeric character (a-zA-Z0-9). Characters in between the beginning and end may contain alphanumeric characters, dots (.), dashes (-) and underscores (\_). A Label can be a simple tag by specifying a key with no value


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode:

      .. rst-class:: ansible-option-title

      **localNode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      this holds the connection parameters required to communicate with an instance of CipherTrust Manager (CM)

      holds IP/FQDN of the server, username, password, and port


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/password"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      admin password of CM


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/server_ip"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/server_ip:

      .. rst-class:: ansible-option-title

      **server_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/server_ip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      CM Server IP or FQDN


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/server_port"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/server_port:

      .. rst-class:: ansible-option-title

      **server_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/server_port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Port on which CM server is listening


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`5432`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/server_private_ip"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/server_private_ip:

      .. rst-class:: ansible-option-title

      **server_private_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/server_private_ip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      internal or private IP of the CM Server, if different from the server\_ip


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/user"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/user:

      .. rst-class:: ansible-option-title

      **user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/user" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      admin username of CM


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode/verify"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-localnode/verify:

      .. rst-class:: ansible-option-title

      **verify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-localNode/verify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      if SSL verification is required


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macSignBytes"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-macsignbytes:

      .. rst-class:: ansible-option-title

      **macSignBytes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-macSignBytes" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the MAC/Signature bytes to be used for verification while importing a key. The "wrappingMethod" should be "mac/sign" and the required parameters for the verification must be set.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macSignKeyIdentifier"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-macsignkeyidentifier:

      .. rst-class:: ansible-option-title

      **macSignKeyIdentifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-macSignKeyIdentifier" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the identifier of the key to be used for generating MAC or signature of the key material. The "wrappingMethod" should be "mac/sign" to verify the MAC/signature("macSignBytes") of the key material("material"). For verifying the MAC, the key has to be a HMAC key. For verifying the signature, the key has to be an RSA private or public key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macSignKeyIdentifierType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-macsignkeyidentifiertype:

      .. rst-class:: ansible-option-title

      **macSignKeyIdentifierType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-macSignKeyIdentifierType" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the identifier of the key("macSignKeyIdentifier") used for generating MAC or signature of the key material. The "wrappingMethod" should be "mac/sign" to verify the mac/signature("macSignBytes") of the key material("material")


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"id"`
      - :ansible-option-choices-entry:`"alias"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-material"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-material:

      .. rst-class:: ansible-option-title

      **material**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-material" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set, the value will be imported as the key's material. If not set, new key material will be generated on the server (certificate objects must always specify the material). The format of this value depends on the algorithm. If the algorithm is 'aes', 'tdes', 'hmac-\*', 'seed' or 'aria', the value should be the hex-encoded bytes of the key material. If the algorithm is 'rsa', and the format is 'pkcs12', it should be the base64 encoded PFX file. If the algorithm is 'rsa' or 'ec', and format is not 'pkcs12', the value should be a PEM-encoded private or public key using PKCS1 or PKCS8 format. For a X.509 DER encoded certificate, certType equals 'x509-der' and the material should equal the hex encoded certificate. The material for a X.509 PEM encoded certificate (certType = 'x509-pem') should equal the certificate itself. When placing the PEM encoded certificate inside a JSON object (as in the playground), be sure to change all new line characters in the certificate to the string newline char.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-meta:

      .. rst-class:: ansible-option-title

      **meta**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-meta" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional end-user or service data stored with the key


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta/ownerId"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-meta/ownerid:

      .. rst-class:: ansible-option-title

      **ownerId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-meta/ownerId" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Optional owner information for the key, required for non-admin. Value should be the user's user\_id


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-muid"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-muid:

      .. rst-class:: ansible-option-title

      **muid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-muid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Additional identifier of the key. This is optional and applicable for import key only. If set, the value is imported as the key's muid.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional friendly name, The key name should not contain special characters such as angular brackets (\<,\>) and backslash ().


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-objectType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-objecttype:

      .. rst-class:: ansible-option-title

      **objectType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-objectType" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This specifies the type of object that is being created. Valid values are 'Symmetric Key', 'Public Key', 'Private Key', 'Secret Data', 'Opaque Object', or 'Certificate'. The object type is inferred for many objects, but must be supplied for the certificate object.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Symmetric Key"`
      - :ansible-option-choices-entry:`"Public Key"`
      - :ansible-option-choices-entry:`"Private Key"`
      - :ansible-option-choices-entry:`"Secret Data"`
      - :ansible-option-choices-entry:`"Opaque Object"`
      - :ansible-option-choices-entry:`"Certificate"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-offset"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-offset:

      .. rst-class:: ansible-option-title

      **offset**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-offset" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      An Offset MAY be used to indicate the difference between the Creation Date and the Activation Date of the replacement key. If no Offset is specified, the Activation Date, Process Start Date, Protect Stop Date and Deactivation Date values are copied from the existing key. If Offset is set and dates exist for the existing key, then the dates of the replacement key are set based on the dates of the existing key by adding the offset.

      Only applicable for op\_type "create\_version"


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`false`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-op_type"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-op_type:

      .. rst-class:: ansible-option-title

      **op_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-op_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Operation to be performed


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"create"`
      - :ansible-option-choices-entry:`"patch"`
      - :ansible-option-choices-entry:`"create\_version"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-padded"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-padded:

      .. rst-class:: ansible-option-title

      **padded**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-padded" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter determines the padding for the wrap algorithm while unwrapping a symmetric key

      If true, the RFC 5649(AES Key Wrap with Padding) is followed and if false, RFC 3394(AES Key Wrap) is followed for unwrapping the material for the symmetric key.

      If a certificate is being unwrapped with the "wrappingMethod" set to "encrypt", the "padded" parameter has to be set to true.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-processStartDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-processstartdate:

      .. rst-class:: ansible-option-title

      **processStartDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-processStartDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time when a Managed Symmetric Key Object MAY begin to be used to process cryptographically protected information (e.g., decryption or unwrapping)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-protectStopDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-protectstopdate:

      .. rst-class:: ansible-option-title

      **protectStopDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-protectStopDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date/time after which a Managed Symmetric Key Object SHALL NOT be used for applying cryptographic protection (e.g., encryption or wrapping)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters:

      .. rst-class:: ansible-option-title

      **publicKeyParameters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information needed to create a public key


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/activationDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/activationdate:

      .. rst-class:: ansible-option-title

      **activationDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/activationDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Date/time the object becomes active


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/aliases"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/aliases:

      .. rst-class:: ansible-option-title

      **aliases**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/aliases" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Aliases associated with the key.

      The alias and alias-type must be specified.

      The alias index is assigned by this operation, and need not be specified.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/archiveDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/archivedate:

      .. rst-class:: ansible-option-title

      **archiveDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/archiveDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Date/time the object becomes archived


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/deactivationDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/deactivationdate:

      .. rst-class:: ansible-option-title

      **deactivationDate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/deactivationDate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Date/time the object becomes inactive


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/meta"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/meta:

      .. rst-class:: ansible-option-title

      **meta**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/meta" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Optional end-user or service data stored with the key


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/name"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Optional friendly name, The key name should not contain special characters such as angular brackets (\<,\>) and backslash ().


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/state"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Optional initial key state (Pre-Active) upon creation. Defaults to Active. If set, activationDate and processStartDate can not be specified during key creation. In case of import, allowed values are "Pre-Active", "Active", "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". If key material is not specified, it will not be autogenerated if input parameters correspond to either of these states - "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". Key in "Destroyed" or "Destroyed Compromised" state would not have key material even if specified during key creation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/undeletable"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/undeletable:

      .. rst-class:: ansible-option-title

      **undeletable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/undeletable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Key is not deletable. Defaults to false.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/unexportable"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/unexportable:

      .. rst-class:: ansible-option-title

      **unexportable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/unexportable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Key is not exportable. Defaults to false.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-publicKeyParameters/usageMaske"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-publickeyparameters/usagemaske:

      .. rst-class:: ansible-option-title

      **usageMaske**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-publicKeyParameters/usageMaske" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Cryptographic usage mask. Add the usage masks to allow certain usages. Sign (1), Verify (2), Encrypt (4), Decrypt (8), Wrap Key (16), Unwrap Key (32), Export (64), MAC Generate (128), MAC Verify (256), Derive Key (512), Content Commitment (1024), Key Agreement (2048), Certificate Sign (4096), CRL Sign (8192), Generate Cryptogram (16384), Validate Cryptogram (32768), Translate Encrypt (65536), Translate Decrypt (131072), Translate Wrap (262144), Translate Unwrap (524288), FPE Encrypt (1048576), FPE Decrypt (2097152). Add the usage mask values to allow the usages. To set all usage mask bits, use 4194303. Equivalent usageMask values for deprecated usages 'fpe' (FPE Encrypt + FPE Decrypt = 3145728), 'blob' (Encrypt + Decrypt = 12), 'hmac' (MAC Generate + MAC Verify = 384), 'encrypt' (Encrypt + Decrypt = 12), 'sign' (Sign + Verify = 3), 'any' (4194303 - all usage masks).


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-revocationMessage"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-revocationmessage:

      .. rst-class:: ansible-option-title

      **revocationMessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-revocationMessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Message explaining revocation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-revocationReason"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-revocationreason:

      .. rst-class:: ansible-option-title

      **revocationReason**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-revocationReason" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The reason the key is being revoked.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Unspecified"`
      - :ansible-option-choices-entry:`"KeyCompromise"`
      - :ansible-option-choices-entry:`"CACompromise"`
      - :ansible-option-choices-entry:`"AffiliationChanged"`
      - :ansible-option-choices-entry:`"Superseded"`
      - :ansible-option-choices-entry:`"CessationOfOperation"`
      - :ansible-option-choices-entry:`"PrivilegeWithdrawn"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rotationFrequencyDays"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-rotationfrequencydays:

      .. rst-class:: ansible-option-title

      **rotationFrequencyDays**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rotationFrequencyDays" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of days from current date to rotate the key. It should be greater than or equal to 0. Default is an empty string. If set to 0, rotationFrequencyDays set to an empty string and auto rotation of key will be disabled.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secretDataEncoding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-secretdataencoding:

      .. rst-class:: ansible-option-title

      **secretDataEncoding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secretDataEncoding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For pkcs12 format, this field specifies the encoding method used for the secretDataLink material. Ignore this field if secretData is created from REST and is in plain format. Specify the value of this field as HEX format if secretData is created from KMIP.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secretDataLink"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-secretdatalink:

      .. rst-class:: ansible-option-title

      **secretDataLink**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secretDataLink" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For pkcs12 format, either secretDataLink or password should be specified. The value can be either ID or name of Secret Data.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-signingAlgo"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-signingalgo:

      .. rst-class:: ansible-option-title

      **signingAlgo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-signingAlgo" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the algorithm to be used for generating the signature for the verification of the "macSignBytes" during import of key material. The "wrappingMethod" should be "mac/sign" to verify the signature("macSignBytes") of the key material("material").


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"RSA"`
      - :ansible-option-choices-entry:`"RSA-PSS"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-size"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-size:

      .. rst-class:: ansible-option-title

      **size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bit length for the key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional initial key state (Pre-Active) upon creation. Defaults to Active. If set, activationDate and processStartDate can not be specified during key creation. In case of import, allowed values are "Pre-Active", "Active", "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". If key material is not specified, it will not be autogenerated if input parameters correspond to either of these states - "Deactivated", "Destroyed", "Compromised" and "Destroyed Compromised". Key in "Destroyed" or "Destroyed Compromised" state would not have key material even if specified during key creation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-undeletable"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-undeletable:

      .. rst-class:: ansible-option-title

      **undeletable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-undeletable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Key is not deletable. Defaults to false.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-unexportable"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-unexportable:

      .. rst-class:: ansible-option-title

      **unexportable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-unexportable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Key is not exportable. Defaults to false.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usageMaske"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-usagemaske:

      .. rst-class:: ansible-option-title

      **usageMaske**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usageMaske" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cryptographic usage mask. Add the usage masks to allow certain usages. Sign (1), Verify (2), Encrypt (4), Decrypt (8), Wrap Key (16), Unwrap Key (32), Export (64), MAC Generate (128), MAC Verify (256), Derive Key (512), Content Commitment (1024), Key Agreement (2048), Certificate Sign (4096), CRL Sign (8192), Generate Cryptogram (16384), Validate Cryptogram (32768), Translate Encrypt (65536), Translate Decrypt (131072), Translate Wrap (262144), Translate Unwrap (524288), FPE Encrypt (1048576), FPE Decrypt (2097152). Add the usage mask values to allow the usages. To set all usage mask bits, use 4194303. Equivalent usageMask values for deprecated usages 'fpe' (FPE Encrypt + FPE Decrypt = 3145728), 'blob' (Encrypt + Decrypt = 12), 'hmac' (MAC Generate + MAC Verify = 384), 'encrypt' (Encrypt + Decrypt = 12), 'sign' (Sign + Verify = 3), 'any' (4194303 - all usage masks).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-uuid"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-uuid:

      .. rst-class:: ansible-option-title

      **uuid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Additional identifier of the key. The format of this value is 32 hexadecimal lowercase digits with 4 dashes. This is optional and applicable for import key only. If set, the value is imported as the key's uuid. If not set, new key uuid is generated on the server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraphkdf:

      .. rst-class:: ansible-option-title

      **wrapHKDF**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapHKDF" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information which is used to wrap a Key using HKDF.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF/hashAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraphkdf/hashalgorithm:

      .. rst-class:: ansible-option-title

      **hashAlgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapHKDF/hashAlgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Hash Algorithm is used for HKDF Wrapping.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"hmac-sha1"`
      - :ansible-option-choices-entry:`"hmac-sha224"`
      - :ansible-option-choices-entry:`"hmac-sha256"`
      - :ansible-option-choices-entry:`"hmac-sha384"`
      - :ansible-option-choices-entry:`"hmac-sha512"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF/info"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraphkdf/info:

      .. rst-class:: ansible-option-title

      **info**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapHKDF/info" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Info is an optional hex value for HKDF based derivation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF/okmLen"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraphkdf/okmlen:

      .. rst-class:: ansible-option-title

      **okmLen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapHKDF/okmLen" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The desired output key material length in integer.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF/salt"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraphkdf/salt:

      .. rst-class:: ansible-option-title

      **salt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapHKDF/salt" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Salt is an optional hex value for HKDF based derivation.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapKeyIDType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrapkeyidtype:

      .. rst-class:: ansible-option-title

      **wrapKeyIDType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapKeyIDType" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IDType specifies how the wrapKeyName should be interpreted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"id"`
      - :ansible-option-choices-entry:`"alias"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapKeyName"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrapkeyname:

      .. rst-class:: ansible-option-title

      **wrapKeyName**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapKeyName" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      While creating a new key, If 'includeMaterial' is true, then only the key material will be wrapped with material of the specified key name. The response "material" property will be the base64 encoded ciphertext. For more details, view "wrapKeyName" in export parameters.

      While importing a key, the key material will be unwrapped with material of the specified key name. The only applicable "wrappingMethod" for the unwrapping is "encrypt" and the wrapping key has to be an AES key or an RSA private key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe:

      .. rst-class:: ansible-option-title

      **wrapPBE**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      WrapPBE produces a derived key from a password and other parameters like salt, iteration count, hashing algorithm and derived key length. PBE is currently only supported to wrap symmetric keys (AES), private Keys and certificates.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/dklen"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/dklen:

      .. rst-class:: ansible-option-title

      **dklen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/dklen" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Intended length in octets of the derived key. dklen must be in range of 14 bytes to 512 bytes.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/hashAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/hashalgorithm:

      .. rst-class:: ansible-option-title

      **hashAlgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/hashAlgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Underlying hashing algorithm that acts as a pseudorandom function to generate derive keys.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"hmac-sha1"`
      - :ansible-option-choices-entry:`"hmac-sha224"`
      - :ansible-option-choices-entry:`"hmac-sha256"`
      - :ansible-option-choices-entry:`"hmac-sha384"`
      - :ansible-option-choices-entry:`"hmac-sha512"`
      - :ansible-option-choices-entry:`"hmac-sha512/224"`
      - :ansible-option-choices-entry:`"hmac-sha512/256"`
      - :ansible-option-choices-entry:`"hmac-sha3-224"`
      - :ansible-option-choices-entry:`"hmac-sha3-256"`
      - :ansible-option-choices-entry:`"hmac-sha3-384"`
      - :ansible-option-choices-entry:`"hmac-sha3-512"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/iteration"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/iteration:

      .. rst-class:: ansible-option-title

      **iteration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/iteration" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Iteration count increase the cost of producing keys from a password. Iteration must be in range of 1 to 1,00,00,000.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/password"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Base password to generate derive keys. It cannot be used in conjunction with passwordidentifier. password must be in range of 8 bytes to 128 bytes.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/passwordIdentifier"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/passwordidentifier:

      .. rst-class:: ansible-option-title

      **passwordIdentifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/passwordIdentifier" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Secret password identifier for password. It cannot be used in conjunction with password.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/passwordIdentifierType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/passwordidentifiertype:

      .. rst-class:: ansible-option-title

      **passwordIdentifierType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/passwordIdentifierType" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Type of the Passwordidentifier. If not set then default value is name.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"id"`
      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"slug"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/purpose"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/purpose:

      .. rst-class:: ansible-option-title

      **purpose**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/purpose" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      User defined purpose. If specified will be prefixed to pbeSalt. pbePurpose must not be greater than 128 bytes.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/salt"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappbe/salt:

      .. rst-class:: ansible-option-title

      **salt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPBE/salt" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A Hex encoded string. pbeSalt must be in range of 16 bytes to 512 bytes.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrappingEncryptionAlgo"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappingencryptionalgo:

      .. rst-class:: ansible-option-title

      **wrappingEncryptionAlgo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrappingEncryptionAlgo" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      It indicates the Encryption Algorithm information for wrapping the key. Format is Algorithm/Mode/Padding. For example AES/AESKEYWRAP. Here AES is Algorithm, AESKEYWRAP is Mode & Padding is not specified. AES/AESKEYWRAP is RFC-3394 & AES/AESKEYWRAPPADDING is RFC-5649. For wrapping private key, only AES/AESKEYWRAPPADDING is allowed. RSA/RSAAESKEYWRAPPADDING is used to wrap/unwrap asymmetric keys using RSA AES KWP method. Refer "WrapRSAAES" to provide optional parameters.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AES/AESKEYWRAP"`
      - :ansible-option-choices-entry:`"AES/AESKEYWRAPPADDING"`
      - :ansible-option-choices-entry:`"RSA/RSAAESKEYWRAPPADDING"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrappingHashAlgo"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappinghashalgo:

      .. rst-class:: ansible-option-title

      **wrappingHashAlgo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrappingHashAlgo" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the hashing algorithm used if "wrappingMethod" corresponds to "mac/sign". In case of MAC operation, the hashing algorithm used will be inferred from the type of HMAC key("macSignKeyIdentifier").

      In case of SIGN operation, the possible values are sha1, sha224, sha256, sha384 or sha512


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrappingMethod"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappingmethod:

      .. rst-class:: ansible-option-title

      **wrappingMethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrappingMethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter specifies the wrapping method used to wrap/mac/sign the key material.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"encrypt"`
      - :ansible-option-choices-entry:`"mac/sign"`
      - :ansible-option-choices-entry:`"pbe"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPublicKey"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappublickey:

      .. rst-class:: ansible-option-title

      **wrapPublicKey**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPublicKey" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If the algorithm is 'aes','tdes','hmac-\*', 'seed' or 'aria', this value will be used to encrypt the returned key material. This value is ignored for other algorithms. Value must be an RSA public key, PEM-encoded public key in either PKCS1 or PKCS8 format, or a PEM-encoded X.509 certificate. If set, the returned 'material' value will be a Base64 encoded PKCS#1 v1.5 encrypted key. View "wrapPublicKey" in export parameters for more information. Only applicable if 'includeMaterial' is true.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPublicKeyPadding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wrappublickeypadding:

      .. rst-class:: ansible-option-title

      **wrapPublicKeyPadding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapPublicKeyPadding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      WrapPublicKeyPadding specifies the type of padding scheme that needs to be set when importing the Key using the specified wrapkey. Accepted values are "pkcs1", "oaep", "oaep256", "oaep384", "oaep512", and will default to "pkcs1" when 'wrapPublicKeyPadding' is not set and 'WrapPublicKey' is set.

      While creating a new key, wrapPublicKeyPadding parameter should be specified only if 'includeMaterial' is true. In this case, key will get created and in response wrapped material using specified wrapPublicKeyPadding and other wrap parameters will be returned.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"pkcs1"`
      - :ansible-option-choices-entry:`"oaep"`
      - :ansible-option-choices-entry:`"oaep256"`
      - :ansible-option-choices-entry:`"oaep384"`
      - :ansible-option-choices-entry:`"oaep512"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapRSAAES"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraprsaaes:

      .. rst-class:: ansible-option-title

      **wrapRSAAES**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapRSAAES" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information which is used to wrap/unwrap asymmetric keys using RSA AES KWP method. This method internally requires AES key size to generate a temporary AES key and RSA padding. To use WrapRSAAES, algorithm "RSA/RSAAESKEYWRAPPADDING" must be specified in WrappingEncryptionAlgo.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapRSAAES/aesKeySize"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraprsaaes/aeskeysize:

      .. rst-class:: ansible-option-title

      **aesKeySize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapRSAAES/aesKeySize" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Size of AES key for RSA AES KWP.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`128`
      - :ansible-option-choices-entry:`192`
      - :ansible-option-choices-entry-default:`256` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapRSAAES/padding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-wraprsaaes/padding:

      .. rst-class:: ansible-option-title

      **padding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapRSAAES/padding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Padding specifies the type of padding scheme that needs to be set when exporting the Key using RSA AES wrap


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"oaep"`
      - :ansible-option-choices-entry-default:`"oaep256"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"oaep384"`
      - :ansible-option-choices-entry:`"oaep512"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xts"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_save_module__parameter-xts:

      .. rst-class:: ansible-option-title

      **xts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xts" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, then key created will be XTS/CBC-CS1 Key. Defaults to false. Key algorithm must be 'AES'.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create Key"
      thales.ciphertrust.vault_keys2_create:
        localNode:
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
        op_type: create
        name: "key_name"
        algorithm: aes
        size: 256
        usageMask: 3145740

    - name: "Patch Key"
      thales.ciphertrust.vault_keys2_create:
        localNode:
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
        op_type: patch
        cm_key_id: "4ae2649a705e479589ef65759d3287f6ff452a788531445fbc7f0240516d028d"
        unexportable: false




.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Anurag Jain, Developer Advocate Thales Group



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="http://example.com/issue/tracker" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="http://example.com" aria-role="button" target="_blank" rel="noopener external">Homepage</a>
    <a href="http://example.com/repository" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

