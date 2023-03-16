orphan

:   

::: {#ansible_collections.thales.ciphertrust.usermgmt_users_save_module}
:::

thales.ciphertrust.usermgmt\_users\_save module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
==============================================================================================================================================

::: {.note}
::: {.title}
Note
:::

This module is part of the [thales.ciphertrust
collection](https://galaxy.ansible.com/thales/ciphertrust) (version
1.0.0).

To install it, use:
`ansible-galaxy collection install thales.ciphertrust`.

To use it in a playbook, specify:
`thales.ciphertrust.usermgmt_users_save`.
:::

::: {.rst-class}
ansible-version-added
:::

New in thales.ciphertrust 1.0.0

::: {.contents local="" depth="1"}
:::

Synopsis
--------

-   This is a Thales CipherTrust Manager module for working with the
    CipherTrust Manager APIs, more specifically with user management API

Parameters
----------

::: {.rst-class}
ansible-option-table
:::

+----------------------------------+----------------------------------+
| Parameter                        | Comments                         |
+==================================+==================================+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | List of login authentication     |
| ter-allowed_auth_methods"></div> | methods allowed to the user.     |
| ```                              |                                  |
| ::: {#an                         | Default value - \[\"password\"\] |
| sible_collections.thales.ciphert | i.e. Password Authentication is  |
| rust.usermgmt_users_save_module_ | allowed by default.              |
| _parameter-allowed_auth_methods} |                                  |
| ::: {.rst-class}                 | Setting it to empty, i.e \[\],   |
| ansible-option-title             | means no authentication method   |
| :::                              | is allowed to the user.          |
| :::                              |                                  |
|                                  | If both enable\_cert\_auth and   |
| **allowed\_auth\_methods**       | allowed\_auth\_methods are       |
|                                  | provided in the request,         |
| ```{=html}                       | enable\_cert\_auth is ignored.   |
| <a class=                        |                                  |
| "ansibleOptionLink" href="#param | ```{=html}                       |
| eter-allowed_auth_methods" title | </div>                           |
| ="Permalink to this option"></a> | ```                              |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [list]{.ansible-option-type} /   |                                  |
| [elements=s                      |                                  |
| tring]{.ansible-option-elements} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | A schema-less object, which can  |
| ="parameter-app_metadata"></div> | be used by applications to store |
| ```                              | information about the resource.  |
| ::: {#ansible_collections.thales | app\_metadata is typically used  |
| .ciphertrust.usermgmt_users_save | by applications to store         |
| _module__parameter-app_metadata} | information which the end-users  |
| ::: {.rst-class}                 | are not themselves allowed to    |
| ansible-option-title             | change, like group membership or |
| :::                              | security roles.                  |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **app\_metadata**                | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-app_metadata" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [d                               |                                  |
| ictionary]{.ansible-option-type} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | The domain where user needs to   |
| d="parameter-auth_domain"></div> | be authenticated. This is the    |
| ```                              | domain where user is created.    |
| ::: {#ansible_collections.thale  | Defaults to the root domain.     |
| s.ciphertrust.usermgmt_users_sav |                                  |
| e_module__parameter-auth_domain} | required only for changew        |
| ::: {.rst-class}                 | op\_type, not mandatory though   |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **auth\_domain**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-auth_domain" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="a                    | ```                              |
| nsibleOptionAnchor" id="paramete | The Distinguished Name of the    |
| r-certificate_subject_dn"></div> | user in certificate              |
| ```                              |                                  |
| ::: {#ansi                       | ```{=html}                       |
| ble_collections.thales.ciphertru | </div>                           |
| st.usermgmt_users_save_module__p | ```                              |
| arameter-certificate_subject_dn} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **certificate\_subject\_dn**     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="a                      |                                  |
| nsibleOptionLink" href="#paramet |                                  |
| er-certificate_subject_dn" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | CM user ID of the user that      |
| id="parameter-cm_user_id"></div> | needs to be patched. Only        |
| ```                              | required if the op\_type is      |
| ::: {#ansible_collections.thal   | patch                            |
| es.ciphertrust.usermgmt_users_sa |                                  |
| ve_module__parameter-cm_user_id} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **cm\_user\_id**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hr  |                                  |
| ef="#parameter-cm_user_id" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | This attribute is required to    |
| id="parameter-connection"></div> | create a user, but is not        |
| ```                              | included in user resource        |
| ::: {#ansible_collections.thal   | responses. Can be the name of a  |
| es.ciphertrust.usermgmt_users_sa | connection or \"local\_account\" |
| ve_module__parameter-connection} | for a local user, defaults to    |
| ::: {.rst-class}                 | \"local\_account\".              |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **connection**                   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hr  |                                  |
| ef="#parameter-connection" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnc     | ```                              |
| hor" id="parameter-email"></div> | E-mail of the user               |
| ```                              |                                  |
| ::: {#ansible_collections        | ```{=html}                       |
| .thales.ciphertrust.usermgmt_use | </div>                           |
| rs_save_module__parameter-email} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **email**                        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLin       |                                  |
| k" href="#parameter-email" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cl                          | ```                              |
| ass="ansibleOptionAnchor" id="pa | Deprecated                       |
| rameter-enable_cert_auth"></div> |                                  |
| ```                              | Use allowed\_auth\_methods       |
| :::                              | instead.                         |
| {#ansible_collections.thales.cip |                                  |
| hertrust.usermgmt_users_save_mod | If both enable\_cert\_auth and   |
| ule__parameter-enable_cert_auth} | allowed\_auth\_methods are       |
| ::: {.rst-class}                 | provided in the request,         |
| ansible-option-title             | enable\_cert\_auth is ignored.   |
| :::                              |                                  |
| :::                              | Enable certificate based         |
|                                  | authentication flag. If set to   |
| **enable\_cert\_auth**           | true, the user will be able to   |
|                                  | login using certificate.         |
| ```{=html}                       |                                  |
| <a cl                            | ::: {.rst-class}                 |
| ass="ansibleOptionLink" href="#p | ansible-option-line              |
| arameter-enable_cert_auth" title | :::                              |
| ="Permalink to this option"></a> |                                  |
| ```                              | [Ch                              |
| ::: {.rst-class}                 | oices:]{.ansible-option-choices} |
| ansible-option-type-line         |                                  |
| :::                              | -   `false`{.interpreted-text    |
|                                  |     role                         |
| [boolean]{.ansible-option-type}  | ="ansible-option-choices-entry"} |
|                                  | -   `true`{.interpreted-text     |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class                       | ```                              |
| ="ansibleOptionAnchor" id="param | Set it to 0 to unlock a locked   |
| eter-failed_logins_count"></div> | user account.                    |
| ```                              |                                  |
| ::: {#a                          | ```{=html}                       |
| nsible_collections.thales.cipher | </div>                           |
| trust.usermgmt_users_save_module | ```                              |
| __parameter-failed_logins_count} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **failed\_logins\_count**        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class                         |                                  |
| ="ansibleOptionLink" href="#para |                                  |
| meter-failed_logins_count" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [integer]{.ansible-option-type}  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
| class="ansibleOptionAnchor" id=" | This flag can be used to create  |
| parameter-is_domain_user"></div> | the user in a non-root domain    |
| ```                              | where user management is         |
| ::                               | allowed.                         |
| : {#ansible_collections.thales.c |                                  |
| iphertrust.usermgmt_users_save_m | ::: {.rst-class}                 |
| odule__parameter-is_domain_user} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **is\_domain\_user**             | -   `false`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a                               | -   `true`{.interpreted-text     |
| class="ansibleOptionLink" href=" |     role                         |
| #parameter-is_domain_user" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> |                                  |
| ```                              | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-type-line         | ```                              |
| :::                              |                                  |
|                                  |                                  |
| [boolean]{.ansible-option-type}  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-localNode"></div> | this holds the connection        |
| ```                              | parameters required to           |
| ::: {#ansible_collections.tha    | communicate with an instance of  |
| les.ciphertrust.usermgmt_users_s | CipherTrust Manager (CM)         |
| ave_module__parameter-localnode} |                                  |
| ::: {.rst-class}                 | holds IP/FQDN of the server,     |
| ansible-option-title             | username, password, and port     |
| :::                              |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| **localNode**                    | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" h   |                                  |
| ref="#parameter-localNode" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [d                               |                                  |
| ictionary]{.ansible-option-type} |                                  |
| /                                |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div clas                        | ```                              |
| s="ansibleOptionAnchor" id="para | admin password of CM             |
| meter-localNode/password"></div> |                                  |
| ```                              | ```{=html}                       |
| ::: {#                           | </div>                           |
| ansible_collections.thales.ciphe | ```                              |
| rtrust.usermgmt_users_save_modul |                                  |
| e__parameter-localnode/password} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **password**                     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a clas                          |                                  |
| s="ansibleOptionLink" href="#par |                                  |
| ameter-localNode/password" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type} / |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class                       | ```                              |
| ="ansibleOptionAnchor" id="param | CM Server IP or FQDN             |
| eter-localNode/server_ip"></div> |                                  |
| ```                              | ```{=html}                       |
| ::: {#a                          | </div>                           |
| nsible_collections.thales.cipher | ```                              |
| trust.usermgmt_users_save_module |                                  |
| __parameter-localnode/server_ip} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **server\_ip**                   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class                         |                                  |
| ="ansibleOptionLink" href="#para |                                  |
| meter-localNode/server_ip" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type} / |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Port on which CM server is       |
| er-localNode/server_port"></div> | listening                        |
| ```                              |                                  |
| ::: {#ans                        | ::: {.rst-class}                 |
| ible_collections.thales.ciphertr | ansible-option-line              |
| ust.usermgmt_users_save_module__ | :::                              |
| parameter-localnode/server_port} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `5432`{.interpreted-text         |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **server\_port**                 | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="                       |                                  |
| ansibleOptionLink" href="#parame |                                  |
| ter-localNode/server_port" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [integer]{.ansible-option-type}  |                                  |
| /                                |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibl               | ```                              |
| eOptionAnchor" id="parameter-loc | internal or private IP of the CM |
| alNode/server_private_ip"></div> | Server, if different from the    |
| ```                              | server\_ip                       |
| ::: {#ansible_c                  |                                  |
| ollections.thales.ciphertrust.us | ```{=html}                       |
| ermgmt_users_save_module__parame | </div>                           |
| ter-localnode/server_private_ip} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **server\_private\_ip**          |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibl                 |                                  |
| eOptionLink" href="#parameter-lo |                                  |
| calNode/server_private_ip" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type} / |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
| class="ansibleOptionAnchor" id=" | admin username of CM             |
| parameter-localNode/user"></div> |                                  |
| ```                              | ```{=html}                       |
| ::                               | </div>                           |
| : {#ansible_collections.thales.c | ```                              |
| iphertrust.usermgmt_users_save_m |                                  |
| odule__parameter-localnode/user} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **user**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
| class="ansibleOptionLink" href=" |                                  |
| #parameter-localNode/user" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type} / |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cl                          | ```                              |
| ass="ansibleOptionAnchor" id="pa | if SSL verification is required  |
| rameter-localNode/verify"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| {#ansible_collections.thales.cip | :::                              |
| hertrust.usermgmt_users_save_mod |                                  |
| ule__parameter-localnode/verify} | [Ch                              |
| ::: {.rst-class}                 | oices:]{.ansible-option-choices} |
| ansible-option-title             |                                  |
| :::                              | -   `false`{.interpreted-text    |
| :::                              |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| **verify**                       |     [←                           |
|                                  |     (default)]{.ansi             |
| ```{=html}                       | ble-option-choices-default-mark} |
| <a cl                            | -   `true`{.interpreted-text     |
| ass="ansibleOptionLink" href="#p |     role                         |
| arameter-localNode/verify" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> |                                  |
| ```                              | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-type-line         | ```                              |
| :::                              |                                  |
|                                  |                                  |
| [boolean]{.ansible-option-type}  |                                  |
| /                                |                                  |
| [req                             |                                  |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | Flags for controlling user\'s    |
| d="parameter-login_flags"></div> | login behavior.                  |
| ```                              |                                  |
| ::: {#ansible_collections.thale  | ```{=html}                       |
| s.ciphertrust.usermgmt_users_sav | </div>                           |
| e_module__parameter-login_flags} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **login\_flags**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-login_flags" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [d                               |                                  |
| ictionary]{.ansible-option-type} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansible              | ```                              |
| OptionAnchor" id="parameter-logi | If true, user is not allowed to  |
| n_flags/prevent_ui_login"></div> | login from Web UI.               |
| ```                              |                                  |
| ::: {#ansible_co                 | Default - false                  |
| llections.thales.ciphertrust.use |                                  |
| rmgmt_users_save_module__paramet | ::: {.rst-class}                 |
| er-login_flags/prevent_ui_login} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **prevent\_ui\_login**           | -   `false`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class="ansible                | -   `true`{.interpreted-text     |
| OptionLink" href="#parameter-log |     role                         |
| in_flags/prevent_ui_login" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> |                                  |
| ```                              | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-type-line         | ```                              |
| :::                              |                                  |
|                                  |                                  |
| [boolean]{.ansible-option-type}  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-name"></div> | Full name of the user.           |
| ```                              |                                  |
| ::: {#ansible_collection         | ```{=html}                       |
| s.thales.ciphertrust.usermgmt_us | </div>                           |
| ers_save_module__parameter-name} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **name**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-name" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | the new password                 |
| ="parameter-new_password"></div> |                                  |
| ```                              | mandatory for changepw op\_type  |
| ::: {#ansible_collections.thales |                                  |
| .ciphertrust.usermgmt_users_save | ```{=html}                       |
| _module__parameter-new_password} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **new\_password**                |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-new_password" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-op_type"></div> | Operation to be performed        |
| ```                              |                                  |
| ::: {#ansible_collections.t      | ::: {.rst-class}                 |
| hales.ciphertrust.usermgmt_users | ansible-option-line              |
| _save_module__parameter-op_type} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `"create"`{.interpreted-text |
| **op\_type**                     |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -   `"patch"`{.interpreted-text  |
| <a class="ansibleOptionLink"     |     role                         |
|  href="#parameter-op_type" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -                                |
| ```                              |   `"changepw"`{.interpreted-text |
| ::: {.rst-class}                 |     role                         |
| ansible-option-type-line         | ="ansible-option-choices-entry"} |
| :::                              | -   `                            |
|                                  | "patch\_self"`{.interpreted-text |
| [string]{.ansible-option-type} / |     role                         |
| [req                             | ="ansible-option-choices-entry"} |
| uired]{.ansible-option-required} |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| </div>                           | ```                              |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-password"></div> | The password used to secure the  |
| ```                              | users account. Allowed passwords |
| ::: {#ansible_collections.th     | are defined by the password      |
| ales.ciphertrust.usermgmt_users_ | policy.                          |
| save_module__parameter-password} |                                  |
| ::: {.rst-class}                 | Password is optional when        |
| ansible-option-title             | \"certificate\_subject\_dn\" is  |
| :::                              | set and \"user\_certificate\" is |
| :::                              | in allowed\_auth\_methods.In all |
|                                  | other cases, password is         |
| **password**                     | required                         |
|                                  |                                  |
| ```{=html}                       | It is not included in user       |
| <a class="ansibleOptionLink"     | resource responses.              |
| href="#parameter-password" title |                                  |
| ="Permalink to this option"></a> | ```{=html}                       |
| ```                              | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | Password change required flag.   |
| password_change_required"></div> | If set to true, user will be     |
| ```                              | required to change their         |
| ::: {#ansibl                     | password on next successful      |
| e_collections.thales.ciphertrust | login.                           |
| .usermgmt_users_save_module__par |                                  |
| ameter-password_change_required} | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-title             | :::                              |
| :::                              |                                  |
| :::                              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| **password\_change\_required**   |                                  |
|                                  | -   `false`{.interpreted-text    |
| ```{=html}                       |     role                         |
| <a class="ans                    | ="ansible-option-choices-entry"} |
| ibleOptionLink" href="#parameter | -   `true`{.interpreted-text     |
| -password_change_required" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-type-line         | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| [boolean]{.ansible-option-type}  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-user_id"></div> | The user\_id is the ID of an     |
| ```                              | existing root domain user. This  |
| ::: {#ansible_collections.t      | field is used only when adding   |
| hales.ciphertrust.usermgmt_users | an existing root domain user to  |
| _save_module__parameter-user_id} | a different domain.              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| **user\_id**                     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
|  href="#parameter-user_id" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | A schema-less object, which can  |
| "parameter-user_metadata"></div> | be used by applications to store |
| ```                              | information about the resource.  |
| :                                | user\_metadata is typically used |
| :: {#ansible_collections.thales. | by applications to store         |
| ciphertrust.usermgmt_users_save_ | information about the resource   |
| module__parameter-user_metadata} | which the end-users are allowed  |
| ::: {.rst-class}                 | to modify, such as user          |
| ansible-option-title             | preferences.                     |
| :::                              |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| **user\_metadata**               | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-user_metadata" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [d                               |                                  |
| ictionary]{.ansible-option-type} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-username"></div> | The login name of the user. This |
| ```                              | is the identifier used to login. |
| ::: {#ansible_collections.th     |                                  |
| ales.ciphertrust.usermgmt_users_ | This attribute is required to    |
| save_module__parameter-username} | create a user, but is omitted    |
| ::: {.rst-class}                 | when getting or listing user     |
| ansible-option-title             | resources. It cannot be updated. |
| :::                              |                                  |
| :::                              | This attribute may also be used  |
|                                  | (instead of the user\_id) when   |
| **username**                     | adding an existing root domain   |
|                                  | user to a different domain.      |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     | Mandatory for create operation   |
| href="#parameter-username" title |                                  |
| ="Permalink to this option"></a> | ```{=html}                       |
| ```                              | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+

Examples
--------

``` {.yaml+jinja}
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
```

### Authors

-   Anurag Jain, Developer Advocate Thales Group

### Collection links

```{=html}
<p class="ansible-links">
  <a href="http://example.com/issue/tracker" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
  <a href="http://example.com" aria-role="button" target="_blank" rel="noopener external">Homepage</a>
  <a href="http://example.com/repository" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
</p>
```
