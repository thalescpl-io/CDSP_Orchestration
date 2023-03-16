orphan

:   

::: {#ansible_collections.thales.ciphertrust.cm_resource_get_id_from_name_module}
:::

thales.ciphertrust.cm\_resource\_get\_id\_from\_name module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
==========================================================================================================================================================

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
`thales.ciphertrust.cm_resource_get_id_from_name`.
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
    CipherTrust Manager APIs, more specifically List API with some
    filter.

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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-localNode"></div> | this holds the connection        |
| ```                              | parameters required to           |
| ::: {#                           | communicate with an instance of  |
| ansible_collections.thales.ciphe | CipherTrust Manager (CM)         |
| rtrust.cm_resource_get_id_from_n |                                  |
| ame_module__parameter-localnode} | holds IP/FQDN of the server,     |
| ::: {.rst-class}                 | username, password, and port     |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **localNode**                    |                                  |
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
| ::: {#ansible_c                  | </div>                           |
| ollections.thales.ciphertrust.cm | ```                              |
| _resource_get_id_from_name_modul |                                  |
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
| ::: {#ansible_co                 | </div>                           |
| llections.thales.ciphertrust.cm_ | ```                              |
| resource_get_id_from_name_module |                                  |
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
| ::: {#ansible_coll               | ::: {.rst-class}                 |
| ections.thales.ciphertrust.cm_re | ansible-option-line              |
| source_get_id_from_name_module__ | :::                              |
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
| ::: {#ansible_collection         |                                  |
| s.thales.ciphertrust.cm_resource | ```{=html}                       |
| _get_id_from_name_module__parame | </div>                           |
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
| ::: {#ansib                      | </div>                           |
| le_collections.thales.ciphertrus | ```                              |
| t.cm_resource_get_id_from_name_m |                                  |
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
| ::: {#ansible                    | ansible-option-line              |
| _collections.thales.ciphertrust. | :::                              |
| cm_resource_get_id_from_name_mod |                                  |
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
| iv class="ansibleOptionAnchor" i | This is a string type of option  |
| d="parameter-query_param"></div> | that holds the query parameter   |
| ```                              | type to be used to filter the    |
| ::: {#an                         | list resources API response      |
| sible_collections.thales.ciphert |                                  |
| rust.cm_resource_get_id_from_nam | ::: {.rst-class}                 |
| e_module__parameter-query_param} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **query\_param**                 | -   `"name"`{.interpreted-text   |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class="ansibleOptionLink" hre | -                                |
| f="#parameter-query_param" title |   `"username"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -   `"email"`{.interpreted-text  |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -   `"status"`{.interpreted-text |
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
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | This is a string type of option  |
| ameter-query_param_value"></div> | that will hold the value of      |
| ```                              | filter query parameter           |
| ::: {#ansible_                   |                                  |
| collections.thales.ciphertrust.c | ```{=html}                       |
| m_resource_get_id_from_name_modu | </div>                           |
| le__parameter-query_param_value} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **query\_param\_value**          |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cla                           |                                  |
| ss="ansibleOptionLink" href="#pa |                                  |
| rameter-query_param_value" title |                                  |
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
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | This is a string type of option  |
| "parameter-resource_type"></div> | that can hold the resource type. |
| ```                              |                                  |
| ::: {#ansi                       | ::: {.rst-class}                 |
| ble_collections.thales.ciphertru | ansible-option-line              |
| st.cm_resource_get_id_from_name_ | :::                              |
| module__parameter-resource_type} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `"keys"`{.interpreted-text   |
|                                  |     role                         |
| **resource\_type**               | ="ansible-option-choices-entry"} |
|                                  | -   `"protect                    |
| ```{=html}                       | ion-policies"`{.interpreted-text |
| <a                               |     role                         |
|  class="ansibleOptionLink" href= | ="ansible-option-choices-entry"} |
| "#parameter-resource_type" title | -   `"acc                        |
| ="Permalink to this option"></a> | ess-policies"`{.interpreted-text |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         | -                                |
| :::                              |  `"user-sets"`{.interpreted-text |
|                                  |     role                         |
| [string]{.ansible-option-type} / | ="ansible-option-choices-entry"} |
| [req                             | -                                |
| uired]{.ansible-option-required} | `"interfaces"`{.interpreted-text |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           | -   `"ch                         |
| ```                              | aracter-sets"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"users"`{.interpreted-text  |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"                           |
|                                  | dpg-policies"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"cli                        |
|                                  | ent-profiles"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"mas                        |
|                                  | king-formats"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+

Examples
--------

``` {.yaml+jinja}
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
```

Return Values
-------------

Common return values are documented
`here <common_return_values>`{.interpreted-text role="ref"}, the
following are the fields unique to this module:

::: {.rst-class}
ansible-option-table
:::

+----------------------------------+----------------------------------+
| Key                              | Description                      |
+==================================+==================================+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOpt           | ```                              |
| ionAnchor" id="return-id"></div> | String with the ID returned by   |
| ```                              | the CipherTrust Manager          |
| ::: {#ansible_collections.th     |                                  |
| ales.ciphertrust.cm_resource_get | ::: {.rst-class}                 |
| _id_from_name_module__return-id} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Returned:                       |
| :::                              | ]{.ansible-option-returned-bold} |
|                                  | changed or success               |
| **id**                           |                                  |
|                                  | ::: {.rst-class}                 |
| ```{=html}                       | ansible-option-line              |
| <a class="ansibleOptionLin       | :::                              |
| k" href="#return-id" title="Perm |                                  |
| alink to this return value"></a> | ::: {.rst-class}                 |
| ```                              | ansible-option-sample            |
| ::: {.rst-class}                 | :::                              |
| ansible-option-type-line         |                                  |
| :::                              | [Sampl                           |
|                                  | e:]{.ansible-option-sample-bold} |
| [string]{.ansible-option-type}   | `"123456789"`{.interpreted-text  |
|                                  | role="ansible-rv-sample-value"}  |
| ```{=html}                       |                                  |
| </div>                           | ```{=html}                       |
| ```                              | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+

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
