
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

.. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

thales.ciphertrust.usermgmt_users_save module -- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `thales.ciphertrust collection <https://galaxy.ansible.com/thales/ciphertrust>`_ (version 1.0.0).

    To install it, use: :code:`ansible-galaxy collection install thales.ciphertrust`.

    To use it in a playbook, specify: :code:`thales.ciphertrust.usermgmt_users_save`.

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

- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs, more specifically with user management API


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
        <div class="ansibleOptionAnchor" id="parameter-allowed_auth_methods"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-allowed_auth_methods:

      .. rst-class:: ansible-option-title

      **allowed_auth_methods**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allowed_auth_methods" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of login authentication methods allowed to the user.

      Default value - ["password"] i.e. Password Authentication is allowed by default.

      Setting it to empty, i.e [], means no authentication method is allowed to the user.

      If both enable\_cert\_auth and allowed\_auth\_methods are provided in the request, enable\_cert\_auth is ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-app_metadata"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-app_metadata:

      .. rst-class:: ansible-option-title

      **app_metadata**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-app_metadata" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A schema-less object, which can be used by applications to store information about the resource. app\_metadata is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_domain"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-auth_domain:

      .. rst-class:: ansible-option-title

      **auth_domain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auth_domain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The domain where user needs to be authenticated. This is the domain where user is created. Defaults to the root domain.

      required only for changew op\_type, not mandatory though


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-certificate_subject_dn"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-certificate_subject_dn:

      .. rst-class:: ansible-option-title

      **certificate_subject_dn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-certificate_subject_dn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Distinguished Name of the user in certificate


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cm_user_id"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-cm_user_id:

      .. rst-class:: ansible-option-title

      **cm_user_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cm_user_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CM user ID of the user that needs to be patched. Only required if the op\_type is patch


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-connection"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-connection:

      .. rst-class:: ansible-option-title

      **connection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-connection" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This attribute is required to create a user, but is not included in user resource responses. Can be the name of a connection or "local\_account" for a local user, defaults to "local\_account".


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-email"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-email:

      .. rst-class:: ansible-option-title

      **email**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-email" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      E-mail of the user


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable_cert_auth"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-enable_cert_auth:

      .. rst-class:: ansible-option-title

      **enable_cert_auth**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable_cert_auth" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Deprecated

      Use allowed\_auth\_methods instead.

      If both enable\_cert\_auth and allowed\_auth\_methods are provided in the request, enable\_cert\_auth is ignored.

      Enable certificate based authentication flag. If set to true, the user will be able to login using certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-failed_logins_count"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-failed_logins_count:

      .. rst-class:: ansible-option-title

      **failed_logins_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-failed_logins_count" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set it to 0 to unlock a locked user account.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_domain_user"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-is_domain_user:

      .. rst-class:: ansible-option-title

      **is_domain_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_domain_user" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This flag can be used to create the user in a non-root domain where user management is allowed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-localNode"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/password:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/server_ip:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/server_port:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/server_private_ip:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/user:

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

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-localnode/verify:

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
        <div class="ansibleOptionAnchor" id="parameter-login_flags"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-login_flags:

      .. rst-class:: ansible-option-title

      **login_flags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-login_flags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flags for controlling user's login behavior.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-login_flags/prevent_ui_login"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-login_flags/prevent_ui_login:

      .. rst-class:: ansible-option-title

      **prevent_ui_login**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-login_flags/prevent_ui_login" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      If true, user is not allowed to login from Web UI.

      Default - false


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-name:

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

      Full name of the user.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-new_password"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-new_password:

      .. rst-class:: ansible-option-title

      **new_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-new_password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      the new password

      mandatory for changepw op\_type


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-op_type"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-op_type:

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
      - :ansible-option-choices-entry:`"changepw"`
      - :ansible-option-choices-entry:`"patch\_self"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-password:

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

      The password used to secure the users account. Allowed passwords are defined by the password policy.

      Password is optional when "certificate\_subject\_dn" is set and "user\_certificate" is in allowed\_auth\_methods.In all other cases, password is required

      It is not included in user resource responses.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password_change_required"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-password_change_required:

      .. rst-class:: ansible-option-title

      **password_change_required**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password_change_required" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password change required flag. If set to true, user will be required to change their password on next successful login.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user_id"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-user_id:

      .. rst-class:: ansible-option-title

      **user_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The user\_id is the ID of an existing root domain user. This field is used only when adding an existing root domain user to a different domain.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user_metadata"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-user_metadata:

      .. rst-class:: ansible-option-title

      **user_metadata**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user_metadata" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A schema-less object, which can be used by applications to store information about the resource. user\_metadata is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.thales.ciphertrust.usermgmt_users_save_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The login name of the user. This is the identifier used to login.

      This attribute is required to create a user, but is omitted when getting or listing user resources. It cannot be updated.

      This attribute may also be used (instead of the user\_id) when adding an existing root domain user to a different domain.

      Mandatory for create operation


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create new user"
        thales.ciphertrust.usermgmt_users_save:
          localNode: 
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
          op_type: "create"
          username: "john.doe"
          password: "oldPassword12!"
          email: "john.doe@example.com"
          name: "John Doe"

    - name: "Update user info"
        thales.ciphertrust.usermgmt_users_save:
          localNode: 
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
          op_type: "patch"
          cm_user_id: "local|UUID"
          username: "john.doe"
          email: "aj@example.com"
          name: "New Name"

    - name: "Change user password"
        thales.ciphertrust.usermgmt_users_save:
          localNode: 
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
          op_type: "changepw"
          username: "john.doe"
          password: "oldPassword12!"
          new_password: "newPassword12!"

    - name: "Update self"
        thales.ciphertrust.usermgmt_users_save:
          localNode: 
            server_ip: "IP/FQDN of CipherTrust Manager"
            server_private_ip: "Private IP in case that is different from above"
            server_port: 5432
            user: "CipherTrust Manager Username"
            password: "CipherTrust Manager Password"
            verify: false
          op_type: "patch_self"
          name: "CM Admin"




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

