orphan

:   

::: {#ansible_collections.thales.ciphertrust.domain_save_module}
:::

thales.ciphertrust.domain\_save module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
=====================================================================================================================================

::: {.note}
::: {.title}
Note
:::

This module is part of the [thales.ciphertrust
collection](https://galaxy.ansible.com/thales/ciphertrust) (version
1.0.0).

To install it, use:
`ansible-galaxy collection install thales.ciphertrust`.

To use it in a playbook, specify: `thales.ciphertrust.domain_save`.
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
    CipherTrust Manager APIs, more specifically with domains management
    API

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
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-admins"></div> | List of administrators for the   |
| ```                              | domain                           |
| ::: {#ansible_coll               |                                  |
| ections.thales.ciphertrust.domai | ::: {.rst-class}                 |
| n_save_module__parameter-admins} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `["none"]`{.interpreted-text     |
| **admins**                       | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLink      | </div>                           |
| " href="#parameter-admins" title | ```                              |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [list]{.ansible-option-type} /   |                                  |
| [elements=s                      |                                  |
| tring]{.ansible-option-elements} |                                  |
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
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | To allow user creation and       |
| er-allow_user_management"></div> | management in the domain, set it |
| ```                              | to true                          |
| :                                |                                  |
| :: {#ansible_collections.thales. | ::: {.rst-class}                 |
| ciphertrust.domain_save_module__ | ansible-option-line              |
| parameter-allow_user_management} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `false`{.interpreted-text    |
| **allow\_user\_management**      |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| ```{=html}                       |     [←                           |
| <a class="                       |     (default)]{.ansi             |
| ansibleOptionLink" href="#parame | ble-option-choices-default-mark} |
| ter-allow_user_management" title | -   `true`{.interpreted-text     |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| [boolean]{.ansible-option-type}  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | HSM connection ID pertaining to  |
| "parameter-connection_id"></div> | the domain KEK                   |
| ```                              |                                  |
| ::: {#ansible_collections        | ::: {.rst-class}                 |
| .thales.ciphertrust.domain_save_ | ansible-option-line              |
| module__parameter-connection_id} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
| :::                              | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
| **connection\_id**               |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a                               | ```                              |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-connection_id" title |                                  |
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
| ass="ansibleOptionAnchor" id="pa | Label of the target domain KEK   |
| rameter-domain_kek_label"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#ansible_collections.th     | ansible-option-line              |
| ales.ciphertrust.domain_save_mod | :::                              |
| ule__parameter-domain_kek_label} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `"none"`{.interpreted-text       |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **domain\_kek\_label**           | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a cl                            |                                  |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-domain_kek_label" title |                                  |
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
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | The ID of the HSM connection.    |
| ameter-hsm_connection_id"></div> | Required for HSM-anchored        |
| ```                              | domains.                         |
| ::: {#ansible_collections.tha    |                                  |
| les.ciphertrust.domain_save_modu | ::: {.rst-class}                 |
| le__parameter-hsm_connection_id} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| **hsm\_connection\_id**          | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a cla                           | </div>                           |
| ss="ansibleOptionLink" href="#pa | ```                              |
| rameter-hsm_connection_id" title |                                  |
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
|  class="ansibleOptionAnchor" id= | Optional name field for the      |
| "parameter-hsm_kek_label"></div> | domain KEK for an HSM-anchored   |
| ```                              | domain. If not provided, a       |
| ::: {#ansible_collections        | random UUID is assigned for KEK  |
| .thales.ciphertrust.domain_save_ | label.                           |
| module__parameter-hsm_kek_label} |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-title             | ansible-option-line              |
| :::                              | :::                              |
| :::                              |                                  |
|                                  | [Default                         |
| **hsm\_kek\_label**              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| ```{=html}                       | role="ansible-option-default"}   |
| <a                               |                                  |
|  class="ansibleOptionLink" href= | ```{=html}                       |
| "#parameter-hsm_kek_label" title | </div>                           |
| ="Permalink to this option"></a> | ```                              |
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
| v class="ansibleOptionAnchor" id | Identifier of the domain to be   |
| ="parameter-interface_id"></div> | patched                          |
| ```                              |                                  |
| ::: {#ansible_collection         | ```{=html}                       |
| s.thales.ciphertrust.domain_save | </div>                           |
| _module__parameter-interface_id} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **interface\_id**                |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-interface_id" title |                                  |
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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-localNode"></div> | this holds the connection        |
| ```                              | parameters required to           |
| ::: {#ansible_collect            | communicate with an instance of  |
| ions.thales.ciphertrust.domain_s | CipherTrust Manager (CM)         |
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
| ::: {#ansible_collections.thal   | </div>                           |
| es.ciphertrust.domain_save_modul | ```                              |
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
| ::: {#ansible_collections.thale  | </div>                           |
| s.ciphertrust.domain_save_module | ```                              |
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
| :                                | ::: {.rst-class}                 |
| :: {#ansible_collections.thales. | ansible-option-line              |
| ciphertrust.domain_save_module__ | :::                              |
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
| ::: {#a                          |                                  |
| nsible_collections.thales.cipher | ```{=html}                       |
| trust.domain_save_module__parame | </div>                           |
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
| ::: {#ansible_collections.       | </div>                           |
| thales.ciphertrust.domain_save_m | ```                              |
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
| ::: {#ansible_collections.th     | ansible-option-line              |
| ales.ciphertrust.domain_save_mod | :::                              |
| ule__parameter-localnode/verify} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
| **verify**                       | e-option-choices-entry-default"} |
|                                  |     [←                           |
| ```{=html}                       |     (default)]{.ansi             |
| <a cl                            | ble-option-choices-default-mark} |
| ass="ansibleOptionLink" href="#p | -   `true`{.interpreted-text     |
| arameter-localNode/verify" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-type-line         | </div>                           |
| :::                              | ```                              |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-meta"></div> | Optional end-user or service     |
| ```                              | data stored with the domain.     |
| ::: {#ansible_co                 |                                  |
| llections.thales.ciphertrust.dom | ```{=html}                       |
| ain_save_module__parameter-meta} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **meta**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-meta" title |                                  |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-name"></div> | The name of the domain           |
| ```                              |                                  |
| ::: {#ansible_co                 | ::: {.rst-class}                 |
| llections.thales.ciphertrust.dom | ansible-option-line              |
| ain_save_module__parameter-name} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
| :::                              | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
| **name**                         |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a class="ansibleOptionLi        | ```                              |
| nk" href="#parameter-name" title |                                  |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-op_type"></div> | Operation to be performed        |
| ```                              |                                  |
| ::: {#ansible_colle              | ::: {.rst-class}                 |
| ctions.thales.ciphertrust.domain | ansible-option-line              |
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
| ="Permalink to this option"></a> |                                  |
| ```                              | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-type-line         | ```                              |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | This optional parameter is the   |
| ="parameter-parent_ca_id"></div> | ID or URI of the parent          |
| ```                              | domain\'s CA. This CA is used    |
| ::: {#ansible_collection         | for signing the default CA of a  |
| s.thales.ciphertrust.domain_save | newly created sub-domain. The    |
| _module__parameter-parent_ca_id} | oldest CA in the parent domain   |
| ::: {.rst-class}                 | is used if this value is not     |
| ansible-option-title             | supplied.                        |
| :::                              |                                  |
| :::                              | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| **parent\_ca\_id**               | :::                              |
|                                  |                                  |
| ```{=html}                       | [Default                         |
| <                                | :]{.ansible-option-default-bold} |
| a class="ansibleOptionLink" href | `"none"`{.interpreted-text       |
| ="#parameter-parent_ca_id" title | role="ansible-option-default"}   |
| ="Permalink to this option"></a> |                                  |
| ```                              | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-type-line         | ```                              |
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
- name: "Create Domain"
  thales.ciphertrust.domain_save:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: create
    admins:
      - local|4d1c26ab-8730-4d44-af5c-9a8641d0266d
      - local|c7cf4efc-df81-4446-a30e-2dd5badf44b4
    name: AnsibleDomain
    parent_ca_id: a5e0fa8a-a7f7-434c-ade8-f84de040269a

- name: "Patch Domain"
  thales.ciphertrust.domain_save:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: patch
    domain_id: "ID_STRING"
    connection_id: "ID_STRING"
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
