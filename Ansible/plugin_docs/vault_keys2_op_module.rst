
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

.. _ansible_collections.thales.ciphertrust.vault_keys2_op_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

thales.ciphertrust.vault_keys2_op module -- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `thales.ciphertrust collection <https://galaxy.ansible.com/thales/ciphertrust>`_ (version 1.0.0).

    To install it, use: :code:`ansible-galaxy collection install thales.ciphertrust`.

    To use it in a playbook, specify: :code:`thales.ciphertrust.vault_keys2_op`.

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

- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with key operations API


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
        <div class="ansibleOptionAnchor" id="parameter-cm_key_id"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-cm_key_id:

      .. rst-class:: ansible-option-title

      **cm_key_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cm_key_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CM ID of the key that needs to be patched.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-combineXts"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-combinexts:

      .. rst-class:: ansible-option-title

      **combineXts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-combineXts" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, then full material of XTS/CBC-CS1 key will be exported.

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compromiseOccurrenceDate"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-compromiseoccurrencedate:

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

      Date/time when the object was first believed to be compromised, if known.

      Only valid if the revocation reason is CACompromise or KeyCompromise, otherwise ignored.

      Defaults to key's creation time.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-encoding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-encoding:

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

      Specifies the encoding used for the material field.

      For wrapping scenarios and PKCS12 format, the only valid option is base64. In case of "Symmetric Keys" when 'format' parameter has 'base64' value and 'encoding' parameter also contains some value. The encoding parameter takes the priority. Options for Symmetric Keys are hex or base64

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id_type"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-id_type:

      .. rst-class:: ansible-option-title

      **id_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Query Parameter

      Type of identifier for the key


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"id"`
      - :ansible-option-choices-entry:`"uri"`
      - :ansible-option-choices-entry:`"alias"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-idSize"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-idsize:

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

      Only applicable for op\_type "clone"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-includeMaterial"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-includematerial:

      .. rst-class:: ansible-option-title

      **includeMaterial**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-includeMaterial" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Query Parameter

      weather to include the key material if the op\_type is clone

      applicable only if op\_type is clone


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-key_version"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-key_version:

      .. rst-class:: ansible-option-title

      **key_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-key_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Query Parameter

      Key version

      Defaults to the latest version

      Valid only if id\_type is "name"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyFormat"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-keyformat:

      .. rst-class:: ansible-option-title

      **keyFormat**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyFormat" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The format of the returned key material. If the algorithm is 'rsa' or 'ec'. The value can be one of 'pkcs1', 'pkcs8' , 'pkcs12', or 'jwe'. The default value is 'pkcs8'. If algorithm is ‘rsa’ and format is 'pkcs12', the key material will contain the base64-encoded value of the PFX file. The value 'base64' is used for symmetric keys, for which the format of the returned key material is base64-encoded if wrapping is applied (i.e., either 'wrapKeyName' or 'wrapPublicKey' is specified),otherwise, the format is hex-encoded, unless 'base64' is given. If the "format" is 'jwe' then the "material" for the symmetric key, asymmetric key or certificate will be wrapped in JWE format. "wrapKeyName"(should be a public key) or "wrapPublicKey" and "wrapJWE" parameters are required for 'jwe' format. The value 'opaque' is supported for symmetric keys with 'opaque' format only.

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"pkcs1"`
      - :ansible-option-choices-entry:`"pkcs8"`
      - :ansible-option-choices-entry:`"pkcs12"`
      - :ansible-option-choices-entry:`"jwe"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/password:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/server_ip:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/server_port:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/server_private_ip:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/user:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-localnode/verify:

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
        <div class="ansibleOptionAnchor" id="parameter-macSignKeyIdentifier"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-macsignkeyidentifier:

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

      This parameter specifies the identifier of the key used for generating the MAC or signature("macSignBytes") of the key whose key material is to be exported

      The "wrappingMethod" should be "mac/sign" to generate the MAC/signature.

      To generate a MAC, the key should be a HMAC key.

      To generate a signature, the key should be an RSA private key.

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macSignKeyIdentifierType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-macsignkeyidentifiertype:

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

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"id"`
      - :ansible-option-choices-entry:`"alias"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-message"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-message:

      .. rst-class:: ansible-option-title

      **message**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-message" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Message explaining revocation.

      Message explaining reactivation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-meta:

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

      Only applicable for op\_type "clone"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newKeyName"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-newkeyname:

      .. rst-class:: ansible-option-title

      **newKeyName**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-newKeyName" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Key name for the new cloned key.

      Only applicable for op\_type "clone"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-op_type"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-op_type:

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

      - :ansible-option-choices-entry:`"destroy"`
      - :ansible-option-choices-entry:`"archive"`
      - :ansible-option-choices-entry:`"recover"`
      - :ansible-option-choices-entry:`"revoke"`
      - :ansible-option-choices-entry:`"reactivate"`
      - :ansible-option-choices-entry:`"export"`
      - :ansible-option-choices-entry:`"clone"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-padded"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-padded:

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

      This parameter determines the padding for the wrap algorithm while exporting a symmetric key

      If true, the RFC 5649(AES Key Wrap with Padding) is followed and if false, RFC 3394(AES Key Wrap) is followed for wrapping the material for the symmetric key.

      If a certificate is being exported with the "wrappingMethod" set to "encrypt", the "padded" parameter must be set to true.

      This parameter defaults to false.

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For pkcs12 format, if the pkcs12passwordLink is not present in the Key (RSA keys), specify either password or secretDataLink. This should be the base64 encoded value of the password.

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pemWrap"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-pemwrap:

      .. rst-class:: ansible-option-title

      **pemWrap**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pemWrap" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If the parameter is set to true, it wraps the PEM encoding of the private key (asymmetric) otherwise, the DER encoding of the key is wrapped.

      Only valid when private keys (asymmetric) and certificates are to be wrapped for "mac/sign" and "encrypt" values for "wrappingMethod" parameter.

      This parameter defaults to false.

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reason"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-reason:

      .. rst-class:: ansible-option-title

      **reason**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reason" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The reason the key is being revoked. Choices are Unspecified, KeyCompromise, CACompromise, AffiliationChanged, Superseded, CessationOfOperation or PrivilegeWithdrawn

      The reason the key is being reactivated. Choices are DeactivatedToActive, ActiveProtectStopToActive or DeactivatedToActiveProtectStop

      Required if op\_type is either revoke or reactivate


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secretDataEncoding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-secretdataencoding:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secretDataLink"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-secretdatalink:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-signingAlgo"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-signingalgo:

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

      Only applicable for op\_type "export"


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"RSA"`
      - :ansible-option-choices-entry:`"RSA-PSS"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraphkdf:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapHKDF/hashAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraphkdf/hashalgorithm:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraphkdf/info:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraphkdf/okmlen:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraphkdf/salt:

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
        <div class="ansibleOptionAnchor" id="parameter-wrapJWE"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapjwe:

      .. rst-class:: ansible-option-title

      **wrapJWE**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapJWE" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information which is used to wrap a Key using JWE. (JWT ID (JTI) provides a unique identifier for the JWT. JTI will be automatically included in JWE if it is available in JWT identity token.)

      Only applicable for op\_type "export"


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapJWE/contentEncryptionAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapjwe/contentencryptionalgorithm:

      .. rst-class:: ansible-option-title

      **contentEncryptionAlgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapJWE/contentEncryptionAlgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Content Encryption Algorithm is symmetric encryption algorithm used to encrypt the data , default is AES\_256\_GCM.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AES\_128\_CBC\_HMAC\_SHA\_256"`
      - :ansible-option-choices-entry:`"AES\_192\_CBC\_HMAC\_SHA\_384"`
      - :ansible-option-choices-entry:`"AES\_256\_CBC\_HMAC\_SHA\_512"`
      - :ansible-option-choices-entry:`"AES\_128\_GCM"`
      - :ansible-option-choices-entry:`"AES\_192\_GCM"`
      - :ansible-option-choices-entry-default:`"AES\_256\_GCM"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapJWE/jwtIdentifier"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapjwe/jwtidentifier:

      .. rst-class:: ansible-option-title

      **jwtIdentifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapJWE/jwtIdentifier" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      JWT identifier (JTI) is unique identifier for the JWT used by SFDC for cache key replay detection.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapJWE/keyEncryptionAlgorithm"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapjwe/keyencryptionalgorithm:

      .. rst-class:: ansible-option-title

      **keyEncryptionAlgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapJWE/keyEncryptionAlgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Key Encryption Algorithm is used to encrypt the Content Encryption Key (CEK), default is RSA\_OAEP\_SHA1. Algorithm should correspond to type of public key provided for wrapping.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"RSA1\_5"`
      - :ansible-option-choices-entry-default:`"RSA\_OAEP\_SHA1"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"RSA\_OAEP\_SHA256"`
      - :ansible-option-choices-entry:`"ECDH\_ES"`
      - :ansible-option-choices-entry:`"ECDH\_ES\_AES\_128\_KEY\_WRAP"`
      - :ansible-option-choices-entry:`"ECDH\_ES\_AES\_192\_KEY\_WRAP"`
      - :ansible-option-choices-entry:`"ECDH\_ES\_AES\_256\_KEY\_WRAP"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapJWE/keyIdentifier"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapjwe/keyidentifier:

      .. rst-class:: ansible-option-title

      **keyIdentifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrapJWE/keyIdentifier" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Key identifier to be used as "kid" parameter in JWE material and JWE header. Defaults to key id.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapKeyIDType"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapkeyidtype:

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

      Only applicable for op\_type "export"


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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrapkeyname:

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

      The key material will be wrapped with material of the specified key name. The "material" property in the response will be base64 encoded ciphertext. If the "wrappingMethod" field is set to "encrypt", then the wrapping key must be an AES key, RSA private key or RSA public key. For the export of symmetric keys with the "encrypt" method, the three key types are allowed but for the export of a private key if the "wrapRSAAES" parameters are not set, the wrapping key has to be an AES key with a size of 256 bits. If "wrapRSAAES" parameters are set, then the wrapping key has to either be an RSA private or public key. You can set either "wrapKeyName" parameter or "wrapPublicKey" at a time. The wrapping key should be active with a protect stop date that is not expired.

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPBE/dklen"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/dklen:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/hashalgorithm:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/iteration:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/password:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/passwordidentifier:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/passwordidentifiertype:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/purpose:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappbe/salt:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappingencryptionalgo:

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

      Only applicable for op\_type "export"


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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappinghashalgo:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrappingMethod"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappingmethod:

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

      Only applicable for op\_type "export"


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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappublickey:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapPublicKeyPadding"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wrappublickeypadding:

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

      Only applicable for op\_type "export"


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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraprsaaes:

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

      Only applicable for op\_type "export"


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrapRSAAES/aesKeySize"></div>

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraprsaaes/aeskeysize:

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

      .. _ansible_collections.thales.ciphertrust.vault_keys2_op_module__parameter-wraprsaaes/padding:

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

