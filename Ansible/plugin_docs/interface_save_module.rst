
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

.. _ansible_collections.thales.ciphertrust.interface_save_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

thales.ciphertrust.interface_save module -- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `thales.ciphertrust collection <https://galaxy.ansible.com/thales/ciphertrust>`_ (version 1.0.0).

    To install it, use: :code:`ansible-galaxy collection install thales.ciphertrust`.

    To use it in a playbook, specify: :code:`thales.ciphertrust.interface_save`.

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

- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with interface management API


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
        <div class="ansibleOptionAnchor" id="parameter-auto_gen_ca_id"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-auto_gen_ca_id:

      .. rst-class:: ansible-option-title

      **auto_gen_ca_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto_gen_ca_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Auto-generate a new server certificate on server startup using the identifier (URI) of a Local CA resource if the current server certificate is issued by a different Local CA.

      This is especially useful when a new node joins the cluster. In this case, the existing data of the joining node is overwritten by the data in the cluster. A new server certificate is generated on the joining node using the existing Local CA of the cluster.

      Auto-generation of the server certificate can be disabled by setting auto\_gen\_ca\_id to an empty string ("") to allow full control over the server certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto_registration"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-auto_registration:

      .. rst-class:: ansible-option-title

      **auto_registration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto_registration" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set auto registration to allow auto registration of KMIP clients.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cert_user_field"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-cert_user_field:

      .. rst-class:: ansible-option-title

      **cert_user_field**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cert_user_field" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies how the user name is extracted from the client certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CN"`
      - :ansible-option-choices-entry:`"SN"`
      - :ansible-option-choices-entry:`"E"`
      - :ansible-option-choices-entry:`"E\_ND"`
      - :ansible-option-choices-entry:`"UID"`
      - :ansible-option-choices-entry:`"OU"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom_uid_size"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-custom_uid_size:

      .. rst-class:: ansible-option-title

      **custom_uid_size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom_uid_size" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This flag is used to define the custom uid size of managed object over the KMIP interface.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom_uid_v2"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-custom_uid_v2:

      .. rst-class:: ansible-option-title

      **custom_uid_v2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom_uid_v2" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This flag specifies which version of custom uid feature is to be used for KMIP interface. If it is set to true, new implementation i.e. Custom uid version 2 will be used.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-default_connection"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-default_connection:

      .. rst-class:: ansible-option-title

      **default_connection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-default_connection" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The default connection may be "local\_account" for local authentication or the LDAP domain for LDAP authentication. This value is applied when the username does not embed the connection name (e.g. "jdoe" effectively becomes "local\_account|jdoe"). This value only applies to NAE only and is ignored if set for web and KMIP interfaces.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interface_id"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-interface_id:

      .. rst-class:: ansible-option-title

      **interface_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interface_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Identifier of the interface to be patched


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interface_type"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-interface_type:

      .. rst-class:: ansible-option-title

      **interface_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interface_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter is used to identify the type of interface, what service to run on the interface.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"web"`
      - :ansible-option-choices-entry:`"kmip"`
      - :ansible-option-choices-entry-default:`"nae"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"snmp"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-kmip_enable_hard_delete"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-kmip_enable_hard_delete:

      .. rst-class:: ansible-option-title

      **kmip_enable_hard_delete**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-kmip_enable_hard_delete" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enables hard delete of keys on KMIP Destroy operation, that is both meta-data and material will be removed from CipherTrust Manager for the key being deleted.

      By default, only key material is removed and meta-data is preserved with the updated key state.

      This setting applies only to KMIP interface.

      Should be set to 1 for enabling the feature or 0 for returning to default behavior.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`0` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`1`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes:

      .. rst-class:: ansible-option-title

      **local_auto_gen_attributes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Local CSR parameters for interface's certificate. These are for the local node itself, and they do not affect other nodes in the cluster. This gives user a convenient way to supply custom fields for automatic interface certification generation. Without them, the system defaults are used.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/cn"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/cn:

      .. rst-class:: ansible-option-title

      **cn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/cn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Common name


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/dns_names"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/dns_names:

      .. rst-class:: ansible-option-title

      **dns_names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/dns_names" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Subject Alternative Names (SAN) DNS names


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/email_addresses"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/email_addresses:

      .. rst-class:: ansible-option-title

      **email_addresses**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/email_addresses" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Subject Alternative Names (SAN) Email addresses


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/ip_addresses"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/ip_addresses:

      .. rst-class:: ansible-option-title

      **ip_addresses**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/ip_addresses" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Subject Alternative Names (SAN) IP addresses


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/names"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/names:

      .. rst-class:: ansible-option-title

      **names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/names" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name fields like O, OU, L, ST, C


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_auto_gen_attributes/uid"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-local_auto_gen_attributes/uid:

      .. rst-class:: ansible-option-title

      **uid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_auto_gen_attributes/uid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      User ID


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/password:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/server_ip:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/server_port:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/server_private_ip:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/user:

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

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-localnode/verify:

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
        <div class="ansibleOptionAnchor" id="parameter-maximum_tls_version"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-maximum_tls_version:

      .. rst-class:: ansible-option-title

      **maximum_tls_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximum_tls_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum TLS version to be configured for NAE or KMIP interface, default is latest maximum supported protocol.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"tls\_1\_0"`
      - :ansible-option-choices-entry:`"tls\_1\_1"`
      - :ansible-option-choices-entry:`"tls\_1\_2"`
      - :ansible-option-choices-entry:`"tls\_1\_3"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-meta:

      .. rst-class:: ansible-option-title

      **meta**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-meta" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Meta information related to interface


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta/nae"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-meta/nae:

      .. rst-class:: ansible-option-title

      **nae**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-meta/nae" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Meta information related to NAE interface


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-meta/nae/mask_system_groups"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-meta/nae/mask_system_groups:

      .. rst-class:: ansible-option-title

      **mask_system_groups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-meta/nae/mask_system_groups" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Flag for masking system groups in NAE requests


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-minimum_tls_version"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-minimum_tls_version:

      .. rst-class:: ansible-option-title

      **minimum_tls_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-minimum_tls_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Minimum TLS version to be configured for NAE or KMIP interface, default is v1.2 (tls\_1\_2).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"tls\_1\_0"`
      - :ansible-option-choices-entry:`"tls\_1\_1"`
      - :ansible-option-choices-entry-default:`"tls\_1\_2"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"tls\_1\_3"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mode"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The interface mode can be one of no-tls-pw-opt, no-tls-pw-req, unauth-tls-pw-opt, tls-cert-opt-pw-opt, tls-pw-opt, tls-pw-req, tls-cert-pw-opt, or tls-cert-and-pw. Default mode is no-tls-pw-opt.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"no-tls-pw-opt"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"no-tls-pw-req"`
      - :ansible-option-choices-entry:`"unauth-tls-pw-opt"`
      - :ansible-option-choices-entry:`"tls-cert-opt-pw-opt"`
      - :ansible-option-choices-entry:`"tls-pw-opt"`
      - :ansible-option-choices-entry:`"tls-pw-req"`
      - :ansible-option-choices-entry:`"tls-cert-pw-opt"`
      - :ansible-option-choices-entry:`"tls-cert-and-pw"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-name:

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

      The name of the interface. Not valid for interface\_type nae.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-network_interface"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-network_interface:

      .. rst-class:: ansible-option-title

      **network_interface**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-network_interface" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines what ethernet adapter the interface should listen to, use "all" for all.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-op_type"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-op_type:

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


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-port"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-port:

      .. rst-class:: ansible-option-title

      **port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The new interface will listen on the specified port. The port number should not be negative, 0 or the one already in-use.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-registration_token"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-registration_token:

      .. rst-class:: ansible-option-title

      **registration_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-registration_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Registration token in case auto registration is true.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls_ciphers"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-tls_ciphers:

      .. rst-class:: ansible-option-title

      **tls_ciphers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls_ciphers" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TLS Ciphers contain the list of cipher suites available in the system for the respective interfaces (KMIP, NAE & WEB) for TLS handshake.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls_ciphers/cipher_suite"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-tls_ciphers/cipher_suite:

      .. rst-class:: ansible-option-title

      **cipher_suite**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls_ciphers/cipher_suite" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      TLS cipher suite name.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls_ciphers/enabled"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-tls_ciphers/enabled:

      .. rst-class:: ansible-option-title

      **enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls_ciphers/enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      TLS cipher suite enabled flag. If set to true, cipher suite will be available for TLS handshake.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trusted_cas"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-trusted_cas:

      .. rst-class:: ansible-option-title

      **trusted_cas**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trusted_cas" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Collection of local and external CA IDs to trust for client authentication. See section "Certificate Authority" for more details.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trusted_cas/external"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-trusted_cas/external:

      .. rst-class:: ansible-option-title

      **external**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trusted_cas/external" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A list of External CA IDs


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trusted_cas/local"></div>

      .. _ansible_collections.thales.ciphertrust.interface_save_module__parameter-trusted_cas/local:

      .. rst-class:: ansible-option-title

      **local**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trusted_cas/local" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A list of Local CA IDs


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>



.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create Interface"
      thales.ciphertrust.interface_save:
        localNode:
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
        op_type: create
        port: 9005
        auto_registration: false
        interface_type: nae
        mode: no-tls-pw-opt
        network_interface: all




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

