
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

.. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

thales.ciphertrust.cm_resource_get_id_from_name module -- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `thales.ciphertrust collection <https://galaxy.ansible.com/thales/ciphertrust>`_ (version 1.0.0).

    To install it, use: :code:`ansible-galaxy collection install thales.ciphertrust`.

    To use it in a playbook, specify: :code:`thales.ciphertrust.cm_resource_get_id_from_name`.

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

- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically List API with some filter.


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
        <div class="ansibleOptionAnchor" id="parameter-localNode"></div>

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/password:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/server_ip:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/server_port:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/server_private_ip:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/user:

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

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-localnode/verify:

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
        <div class="ansibleOptionAnchor" id="parameter-query_param"></div>

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-query_param:

      .. rst-class:: ansible-option-title

      **query_param**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_param" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This is a string type of option that holds the query parameter type to be used to filter the list resources API response


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"name"`
      - :ansible-option-choices-entry:`"username"`
      - :ansible-option-choices-entry:`"email"`
      - :ansible-option-choices-entry:`"status"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query_param_value"></div>

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-query_param_value:

      .. rst-class:: ansible-option-title

      **query_param_value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_param_value" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This is a string type of option that will hold the value of filter query parameter


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resource_type"></div>

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__parameter-resource_type:

      .. rst-class:: ansible-option-title

      **resource_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resource_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This is a string type of option that can hold the resource type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"keys"`
      - :ansible-option-choices-entry:`"protection-policies"`
      - :ansible-option-choices-entry:`"access-policies"`
      - :ansible-option-choices-entry:`"user-sets"`
      - :ansible-option-choices-entry:`"interfaces"`
      - :ansible-option-choices-entry:`"character-sets"`
      - :ansible-option-choices-entry:`"users"`
      - :ansible-option-choices-entry:`"dpg-policies"`
      - :ansible-option-choices-entry:`"client-profiles"`
      - :ansible-option-choices-entry:`"masking-formats"`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Get Key ID"
      thales.ciphertrust.cm_resource_get_id_from_name:
        localNode:
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
        query_param: "name"
        query_param_value: "AnsibleKey"
        resource_type: "keys"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module__return-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      String with the ID returned by the CipherTrust Manager


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` changed or success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"123456789"`


      .. raw:: html

        </div>



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

