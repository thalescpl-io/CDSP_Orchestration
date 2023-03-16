orphan

:   

::: {#ansible_collections.thales.ciphertrust.vault_keys2_op_module}
:::

thales.ciphertrust.vault\_keys2\_op module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
=========================================================================================================================================

::: {.note}
::: {.title}
Note
:::

This module is part of the [thales.ciphertrust
collection](https://galaxy.ansible.com/thales/ciphertrust) (version
1.0.0).

To install it, use:
`ansible-galaxy collection install thales.ciphertrust`.

To use it in a playbook, specify: `thales.ciphertrust.vault_keys2_op`.
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
    CipherTrust Manager APIs, more specifically with key operations API

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
|  id="parameter-cm_key_id"></div> | CM ID of the key that needs to   |
| ```                              | be patched.                      |
| ::: {#ansible_collection         |                                  |
| s.thales.ciphertrust.vault_keys2 | ```{=html}                       |
| _op_module__parameter-cm_key_id} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **cm\_key\_id**                  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" h   |                                  |
| ref="#parameter-cm_key_id" title |                                  |
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
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | If set to true, then full        |
| id="parameter-combineXts"></div> | material of XTS/CBC-CS1 key will |
| ```                              | be exported.                     |
| ::: {#ansible_collections        |                                  |
| .thales.ciphertrust.vault_keys2_ | Only applicable for op\_type     |
| op_module__parameter-combinexts} | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **combineXts**                   | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hr  | -   `false`{.interpreted-text    |
| ef="#parameter-combineXts" title |     role="ansibl                 |
| ="Permalink to this option"></a> | e-option-choices-entry-default"} |
| ```                              |     [←                           |
| ::: {.rst-class}                 |     (default)]{.ansi             |
| ansible-option-type-line         | ble-option-choices-default-mark} |
| :::                              | -   `true`{.interpreted-text     |
|                                  |     role                         |
| [boolean]{.ansible-option-type}  | ="ansible-option-choices-entry"} |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| </div>                           | </div>                           |
| ```                              | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | Date/time when the object was    |
| compromiseOccurrenceDate"></div> | first believed to be             |
| ```                              | compromised, if known.           |
| ::: {#a                          |                                  |
| nsible_collections.thales.cipher | Only valid if the revocation     |
| trust.vault_keys2_op_module__par | reason is CACompromise or        |
| ameter-compromiseoccurrencedate} | KeyCompromise, otherwise         |
| ::: {.rst-class}                 | ignored.                         |
| ansible-option-title             |                                  |
| :::                              | Defaults to key\'s creation      |
| :::                              | time.                            |
|                                  |                                  |
| **compromiseOccurrenceDate**     | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ans                    |                                  |
| ibleOptionLink" href="#parameter |                                  |
| -compromiseOccurrenceDate" title |                                  |
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
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-encoding"></div> | Specifies the encoding used for  |
| ```                              | the material field.              |
| ::: {#ansible_collectio          |                                  |
| ns.thales.ciphertrust.vault_keys | For wrapping scenarios and       |
| 2_op_module__parameter-encoding} | PKCS12 format, the only valid    |
| ::: {.rst-class}                 | option is base64. In case of     |
| ansible-option-title             | \"Symmetric Keys\" when          |
| :::                              | \'format\' parameter has         |
| :::                              | \'base64\' value and             |
|                                  | \'encoding\' parameter also      |
| **encoding**                     | contains some value. The         |
|                                  | encoding parameter takes the     |
| ```{=html}                       | priority. Options for Symmetric  |
| <a class="ansibleOptionLink"     | Keys are hex or base64           |
| href="#parameter-encoding" title |                                  |
| ="Permalink to this option"></a> | Only applicable for op\_type     |
| ```                              | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
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
| r" id="parameter-id_type"></div> | Query Parameter                  |
| ```                              |                                  |
| ::: {#ansible_collecti           | Type of identifier for the key   |
| ons.thales.ciphertrust.vault_key |                                  |
| s2_op_module__parameter-id_type} | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-title             | :::                              |
| :::                              |                                  |
| :::                              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| **id\_type**                     |                                  |
|                                  | -   `"name"`{.interpreted-text   |
| ```{=html}                       |     role                         |
| <a class="ansibleOptionLink"     | ="ansible-option-choices-entry"} |
|  href="#parameter-id_type" title | -   `"id"`{.interpreted-text     |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -   `"uri"`{.interpreted-text    |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -   `"alias"`{.interpreted-text  |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       |                                  |
| </div>                           | ```{=html}                       |
| ```                              | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-idSize"></div> | Size of the ID for the key       |
| ```                              |                                  |
| ::: {#ansible_collect            | Only applicable for op\_type     |
| ions.thales.ciphertrust.vault_ke | \"clone\"                        |
| ys2_op_module__parameter-idsize} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **idSize**                       |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink      |                                  |
| " href="#parameter-idSize" title |                                  |
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
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | Query Parameter                  |
| arameter-includeMaterial"></div> |                                  |
| ```                              | weather to include the key       |
| ::: {#ansible_collections.thal   | material if the op\_type is      |
| es.ciphertrust.vault_keys2_op_mo | clone                            |
| dule__parameter-includematerial} |                                  |
| ::: {.rst-class}                 | applicable only if op\_type is   |
| ansible-option-title             | clone                            |
| :::                              |                                  |
| :::                              | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| **includeMaterial**              | :::                              |
|                                  |                                  |
| ```{=html}                       | [Ch                              |
| <a c                             | oices:]{.ansible-option-choices} |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-includeMaterial" title | -   `false`{.interpreted-text    |
| ="Permalink to this option"></a> |     role="ansibl                 |
| ```                              | e-option-choices-entry-default"} |
| ::: {.rst-class}                 |     [←                           |
| ansible-option-type-line         |     (default)]{.ansi             |
| :::                              | ble-option-choices-default-mark} |
|                                  | -   `true`{.interpreted-text     |
| [boolean]{.ansible-option-type}  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       |                                  |
| </div>                           | ```{=html}                       |
| ```                              | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | Query Parameter                  |
| d="parameter-key_version"></div> |                                  |
| ```                              | Key version                      |
| ::: {#ansible_collections.       |                                  |
| thales.ciphertrust.vault_keys2_o | Defaults to the latest version   |
| p_module__parameter-key_version} |                                  |
| ::: {.rst-class}                 | Valid only if id\_type is        |
| ansible-option-title             | \"name\"                         |
| :::                              |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| **key\_version**                 | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-key_version" title |                                  |
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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-keyFormat"></div> | The format of the returned key   |
| ```                              | material. If the algorithm is    |
| ::: {#ansible_collection         | \'rsa\' or \'ec\'. The value can |
| s.thales.ciphertrust.vault_keys2 | be one of \'pkcs1\', \'pkcs8\' , |
| _op_module__parameter-keyformat} | \'pkcs12\', or \'jwe\'. The      |
| ::: {.rst-class}                 | default value is \'pkcs8\'. If   |
| ansible-option-title             | algorithm is 'rsa' and format is |
| :::                              | \'pkcs12\', the key material     |
| :::                              | will contain the base64-encoded  |
|                                  | value of the PFX file. The value |
| **keyFormat**                    | \'base64\' is used for symmetric |
|                                  | keys, for which the format of    |
| ```{=html}                       | the returned key material is     |
| <a class="ansibleOptionLink" h   | base64-encoded if wrapping is    |
| ref="#parameter-keyFormat" title | applied (i.e., either            |
| ="Permalink to this option"></a> | \'wrapKeyName\' or               |
| ```                              | \'wrapPublicKey\' is             |
| ::: {.rst-class}                 | specified),otherwise, the format |
| ansible-option-type-line         | is hex-encoded, unless           |
| :::                              | \'base64\' is given. If the      |
|                                  | \"format\" is \'jwe\' then the   |
| [string]{.ansible-option-type}   | \"material\" for the symmetric   |
|                                  | key, asymmetric key or           |
| ```{=html}                       | certificate will be wrapped in   |
| </div>                           | JWE format.                      |
| ```                              | \"wrapKeyName\"(should be a      |
|                                  | public key) or \"wrapPublicKey\" |
|                                  | and \"wrapJWE\" parameters are   |
|                                  | required for \'jwe\' format. The |
|                                  | value \'opaque\' is supported    |
|                                  | for symmetric keys with          |
|                                  | \'opaque\' format only.          |
|                                  |                                  |
|                                  | Only applicable for op\_type     |
|                                  | \"export\"                       |
|                                  |                                  |
|                                  | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
|                                  | :::                              |
|                                  |                                  |
|                                  | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
|                                  |                                  |
|                                  | -   `"pkcs1"`{.interpreted-text  |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"pkcs8"`{.interpreted-text  |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"pkcs12"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"jwe"`{.interpreted-text    |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-localNode"></div> | this holds the connection        |
| ```                              | parameters required to           |
| ::: {#ansible_collection         | communicate with an instance of  |
| s.thales.ciphertrust.vault_keys2 | CipherTrust Manager (CM)         |
| _op_module__parameter-localnode} |                                  |
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
| :                                | </div>                           |
| :: {#ansible_collections.thales. | ```                              |
| ciphertrust.vault_keys2_op_modul |                                  |
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
| ::                               | </div>                           |
| : {#ansible_collections.thales.c | ```                              |
| iphertrust.vault_keys2_op_module |                                  |
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
| :::                              | ::: {.rst-class}                 |
| {#ansible_collections.thales.cip | ansible-option-line              |
| hertrust.vault_keys2_op_module__ | :::                              |
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
| ::: {#ansi                       |                                  |
| ble_collections.thales.ciphertru | ```{=html}                       |
| st.vault_keys2_op_module__parame | </div>                           |
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
| ::: {#ansible_collections.tha    | </div>                           |
| les.ciphertrust.vault_keys2_op_m | ```                              |
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
| ::: {#ansible_collections.thale  | ansible-option-line              |
| s.ciphertrust.vault_keys2_op_mod | :::                              |
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
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | This parameter specifies the     |
| ter-macSignKeyIdentifier"></div> | identifier of the key used for   |
| ```                              | generating the MAC or            |
| :::                              | signature(\"macSignBytes\") of   |
|  {#ansible_collections.thales.ci | the key whose key material is to |
| phertrust.vault_keys2_op_module_ | be exported                      |
| _parameter-macsignkeyidentifier} |                                  |
| ::: {.rst-class}                 | The \"wrappingMethod\" should be |
| ansible-option-title             | \"mac/sign\" to generate the     |
| :::                              | MAC/signature.                   |
| :::                              |                                  |
|                                  | To generate a MAC, the key       |
| **macSignKeyIdentifier**         | should be a HMAC key.            |
|                                  |                                  |
| ```{=html}                       | To generate a signature, the key |
| <a class=                        | should be an RSA private key.    |
| "ansibleOptionLink" href="#param |                                  |
| eter-macSignKeyIdentifier" title | Only applicable for op\_type     |
| ="Permalink to this option"></a> | \"export\"                       |
| ```                              |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-type-line         | </div>                           |
| :::                              | ```                              |
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
| ibleOptionAnchor" id="parameter- | This parameter specifies the     |
| macSignKeyIdentifierType"></div> | identifier of the                |
| ```                              | key(\"macSignKeyIdentifier\")    |
| ::: {#a                          | used for generating MAC or       |
| nsible_collections.thales.cipher | signature of the key material.   |
| trust.vault_keys2_op_module__par | The \"wrappingMethod\" should be |
| ameter-macsignkeyidentifiertype} | \"mac/sign\" to verify the       |
| ::: {.rst-class}                 | mac/signature(\"macSignBytes\")  |
| ansible-option-title             | of the key                       |
| :::                              | material(\"material\")           |
| :::                              |                                  |
|                                  | Only applicable for op\_type     |
| **macSignKeyIdentifierType**     | \"export\"                       |
|                                  |                                  |
| ```{=html}                       | ::: {.rst-class}                 |
| <a class="ans                    | ansible-option-line              |
| ibleOptionLink" href="#parameter | :::                              |
| -macSignKeyIdentifierType" title |                                  |
| ="Permalink to this option"></a> | [Ch                              |
| ```                              | oices:]{.ansible-option-choices} |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | -   `"name"`{.interpreted-text   |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `"id"`{.interpreted-text     |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           | -   `"alias"`{.interpreted-text  |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-message"></div> | Message explaining revocation.   |
| ```                              |                                  |
| ::: {#ansible_collecti           | Message explaining reactivation. |
| ons.thales.ciphertrust.vault_key |                                  |
| s2_op_module__parameter-message} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **message**                      |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
|  href="#parameter-message" title |                                  |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-meta"></div> | Optional end-user or service     |
| ```                              | data stored with the key         |
| ::: {#ansible_colle              |                                  |
| ctions.thales.ciphertrust.vault_ | Only applicable for op\_type     |
| keys2_op_module__parameter-meta} | \"clone\"                        |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
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
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | Key name for the new cloned key. |
| id="parameter-newKeyName"></div> |                                  |
| ```                              | Only applicable for op\_type     |
| ::: {#ansible_collections        | \"clone\"                        |
| .thales.ciphertrust.vault_keys2_ |                                  |
| op_module__parameter-newkeyname} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **newKeyName**                   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hr  |                                  |
| ef="#parameter-newKeyName" title |                                  |
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
| ::: {#ansible_collecti           | ::: {.rst-class}                 |
| ons.thales.ciphertrust.vault_key | ansible-option-line              |
| s2_op_module__parameter-op_type} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -                                |
| **op\_type**                     |    `"destroy"`{.interpreted-text |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class="ansibleOptionLink"     | -                                |
|  href="#parameter-op_type" title |    `"archive"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -                                |
| ansible-option-type-line         |    `"recover"`{.interpreted-text |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type} / | -   `"revoke"`{.interpreted-text |
| [req                             |     role                         |
| uired]{.ansible-option-required} | ="ansible-option-choices-entry"} |
|                                  | -                                |
| ```{=html}                       | `"reactivate"`{.interpreted-text |
| </div>                           |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
|                                  | -   `"export"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"clone"`{.interpreted-text  |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-padded"></div> | This parameter determines the    |
| ```                              | padding for the wrap algorithm   |
| ::: {#ansible_collect            | while exporting a symmetric key  |
| ions.thales.ciphertrust.vault_ke |                                  |
| ys2_op_module__parameter-padded} | If true, the RFC 5649(AES Key    |
| ::: {.rst-class}                 | Wrap with Padding) is followed   |
| ansible-option-title             | and if false, RFC 3394(AES Key   |
| :::                              | Wrap) is followed for wrapping   |
| :::                              | the material for the symmetric   |
|                                  | key.                             |
| **padded**                       |                                  |
|                                  | If a certificate is being        |
| ```{=html}                       | exported with the                |
| <a class="ansibleOptionLink      | \"wrappingMethod\" set to        |
| " href="#parameter-padded" title | \"encrypt\", the \"padded\"      |
| ="Permalink to this option"></a> | parameter must be set to true.   |
| ```                              |                                  |
| ::: {.rst-class}                 | This parameter defaults to       |
| ansible-option-type-line         | false.                           |
| :::                              |                                  |
|                                  | Only applicable for op\_type     |
| [boolean]{.ansible-option-type}  | \"export\"                       |
|                                  |                                  |
| ```{=html}                       | ::: {.rst-class}                 |
| </div>                           | ansible-option-line              |
| ```                              | :::                              |
|                                  |                                  |
|                                  | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
|                                  |                                  |
|                                  | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
|                                  |     [←                           |
|                                  |     (default)]{.ansi             |
|                                  | ble-option-choices-default-mark} |
|                                  | -   `true`{.interpreted-text     |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-password"></div> | For pkcs12 format, if the        |
| ```                              | pkcs12passwordLink is not        |
| ::: {#ansible_collectio          | present in the Key (RSA keys),   |
| ns.thales.ciphertrust.vault_keys | specify either password or       |
| 2_op_module__parameter-password} | secretDataLink. This should be   |
| ::: {.rst-class}                 | the base64 encoded value of the  |
| ansible-option-title             | password.                        |
| :::                              |                                  |
| :::                              | Only applicable for op\_type     |
|                                  | \"export\"                       |
| **password**                     |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a class="ansibleOptionLink"     | ```                              |
| href="#parameter-password" title |                                  |
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
| r" id="parameter-pemWrap"></div> | If the parameter is set to true, |
| ```                              | it wraps the PEM encoding of the |
| ::: {#ansible_collecti           | private key (asymmetric)         |
| ons.thales.ciphertrust.vault_key | otherwise, the DER encoding of   |
| s2_op_module__parameter-pemwrap} | the key is wrapped.              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | Only valid when private keys     |
| :::                              | (asymmetric) and certificates    |
| :::                              | are to be wrapped for            |
|                                  | \"mac/sign\" and \"encrypt\"     |
| **pemWrap**                      | values for \"wrappingMethod\"    |
|                                  | parameter.                       |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     | This parameter defaults to       |
|  href="#parameter-pemWrap" title | false.                           |
| ="Permalink to this option"></a> |                                  |
| ```                              | Only applicable for op\_type     |
| ::: {.rst-class}                 | \"export\"                       |
| ansible-option-type-line         |                                  |
| :::                              | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| [boolean]{.ansible-option-type}  | :::                              |
|                                  |                                  |
| ```{=html}                       | [Ch                              |
| </div>                           | oices:]{.ansible-option-choices} |
| ```                              |                                  |
|                                  | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
|                                  |     [←                           |
|                                  |     (default)]{.ansi             |
|                                  | ble-option-choices-default-mark} |
|                                  | -   `true`{.interpreted-text     |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-reason"></div> | The reason the key is being      |
| ```                              | revoked. Choices are             |
| ::: {#ansible_collect            | Unspecified, KeyCompromise,      |
| ions.thales.ciphertrust.vault_ke | CACompromise,                    |
| ys2_op_module__parameter-reason} | AffiliationChanged, Superseded,  |
| ::: {.rst-class}                 | CessationOfOperation or          |
| ansible-option-title             | PrivilegeWithdrawn               |
| :::                              |                                  |
| :::                              | The reason the key is being      |
|                                  | reactivated. Choices are         |
| **reason**                       | DeactivatedToActive,             |
|                                  | ActiveProtectStopToActive or     |
| ```{=html}                       | DeactivatedToActiveProtectStop   |
| <a class="ansibleOptionLink      |                                  |
| " href="#parameter-reason" title | Required if op\_type is either   |
| ="Permalink to this option"></a> | revoke or reactivate             |
| ```                              |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-type-line         | </div>                           |
| :::                              | ```                              |
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
| <div clas                        | ```                              |
| s="ansibleOptionAnchor" id="para | For pkcs12 format, this field    |
| meter-secretDataEncoding"></div> | specifies the encoding method    |
| ```                              | used for the secretDataLink      |
| :                                | material. Ignore this field if   |
| :: {#ansible_collections.thales. | secretData is created from REST  |
| ciphertrust.vault_keys2_op_modul | and is in plain format. Specify  |
| e__parameter-secretdataencoding} | the value of this field as HEX   |
| ::: {.rst-class}                 | format if secretData is created  |
| ansible-option-title             | from KMIP.                       |
| :::                              |                                  |
| :::                              | Only applicable for op\_type     |
|                                  | \"export\"                       |
| **secretDataEncoding**           |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a clas                          | ```                              |
| s="ansibleOptionLink" href="#par |                                  |
| ameter-secretDataEncoding" title |                                  |
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
| class="ansibleOptionAnchor" id=" | For pkcs12 format, either        |
| parameter-secretDataLink"></div> | secretDataLink or password       |
| ```                              | should be specified. The value   |
| ::: {#ansible_collections.tha    | can be either ID or name of      |
| les.ciphertrust.vault_keys2_op_m | Secret Data.                     |
| odule__parameter-secretdatalink} |                                  |
| ::: {.rst-class}                 | Only applicable for op\_type     |
| ansible-option-title             | \"export\"                       |
| :::                              |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| **secretDataLink**               | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
| class="ansibleOptionLink" href=" |                                  |
| #parameter-secretDataLink" title |                                  |
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
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | This parameter specifies the     |
| d="parameter-signingAlgo"></div> | algorithm to be used for         |
| ```                              | generating the signature for the |
| ::: {#ansible_collections.       | verification of the              |
| thales.ciphertrust.vault_keys2_o | \"macSignBytes\" during import   |
| p_module__parameter-signingalgo} | of key material. The             |
| ::: {.rst-class}                 | \"wrappingMethod\" should be     |
| ansible-option-title             | \"mac/sign\" to verify the       |
| :::                              | signature(\"macSignBytes\") of   |
| :::                              | the key material(\"material\").  |
|                                  |                                  |
| **signingAlgo**                  | Only applicable for op\_type     |
|                                  | \"export\"                       |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre | ::: {.rst-class}                 |
| f="#parameter-signingAlgo" title | ansible-option-line              |
| ="Permalink to this option"></a> | :::                              |
| ```                              |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-type-line         | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `"RSA"`{.interpreted-text    |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -                                |
| </div>                           |    `"RSA-PSS"`{.interpreted-text |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-wrapHKDF"></div> | Information which is used to     |
| ```                              | wrap a Key using HKDF.           |
| ::: {#ansible_collectio          |                                  |
| ns.thales.ciphertrust.vault_keys | Only applicable for op\_type     |
| 2_op_module__parameter-wraphkdf} | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| **wrapHKDF**                     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
| href="#parameter-wrapHKDF" title |                                  |
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
| <div class="a                    | ```                              |
| nsibleOptionAnchor" id="paramete | Hash Algorithm is used for HKDF  |
| r-wrapHKDF/hashAlgorithm"></div> | Wrapping.                        |
| ```                              |                                  |
| ::: {                            | ::: {.rst-class}                 |
| #ansible_collections.thales.ciph | ansible-option-line              |
| ertrust.vault_keys2_op_module__p | :::                              |
| arameter-wraphkdf/hashalgorithm} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -                                |
|                                  |  `"hmac-sha1"`{.interpreted-text |
| **hashAlgorithm**                |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -   `                            |
| <a class="a                      | "hmac-sha224"`{.interpreted-text |
| nsibleOptionLink" href="#paramet |     role                         |
| er-wrapHKDF/hashAlgorithm" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -   `                            |
| ```                              | "hmac-sha256"`{.interpreted-text |
| ::: {.rst-class}                 |     role                         |
| ansible-option-type-line         | ="ansible-option-choices-entry"} |
| :::                              | -   `                            |
|                                  | "hmac-sha384"`{.interpreted-text |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -   `                            |
| </div>                           | "hmac-sha512"`{.interpreted-text |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | Info is an optional hex value    |
| "parameter-wrapHKDF/info"></div> | for HKDF based derivation.       |
| ```                              |                                  |
| ::: {#ansible_collections.th     | ```{=html}                       |
| ales.ciphertrust.vault_keys2_op_ | </div>                           |
| module__parameter-wraphkdf/info} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **info**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-wrapHKDF/info" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | The desired output key material  |
| arameter-wrapHKDF/okmLen"></div> | length in integer.               |
| ```                              |                                  |
| ::: {#ansible_collections.thal   | ```{=html}                       |
| es.ciphertrust.vault_keys2_op_mo | </div>                           |
| dule__parameter-wraphkdf/okmlen} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **okmLen**                       |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a c                             |                                  |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-wrapHKDF/okmLen" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | Salt is an optional hex value    |
| "parameter-wrapHKDF/salt"></div> | for HKDF based derivation.       |
| ```                              |                                  |
| ::: {#ansible_collections.th     | ```{=html}                       |
| ales.ciphertrust.vault_keys2_op_ | </div>                           |
| module__parameter-wraphkdf/salt} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **salt**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-wrapHKDF/salt" title |                                  |
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
| r" id="parameter-wrapJWE"></div> | Information which is used to     |
| ```                              | wrap a Key using JWE. (JWT ID    |
| ::: {#ansible_collecti           | (JTI) provides a unique          |
| ons.thales.ciphertrust.vault_key | identifier for the JWT. JTI will |
| s2_op_module__parameter-wrapjwe} | be automatically included in JWE |
| ::: {.rst-class}                 | if it is available in JWT        |
| ansible-option-title             | identity token.)                 |
| :::                              |                                  |
| :::                              | Only applicable for op\_type     |
|                                  | \"export\"                       |
| **wrapJWE**                      |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a class="ansibleOptionLink"     | ```                              |
|  href="#parameter-wrapJWE" title |                                  |
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
| <div class="ansibleOption        | ```                              |
| Anchor" id="parameter-wrapJWE/co | Content Encryption Algorithm is  |
| ntentEncryptionAlgorithm"></div> | symmetric encryption algorithm   |
| ```                              | used to encrypt the data ,       |
| ::: {#ansible_col                | default is AES\_256\_GCM.        |
| lections.thales.ciphertrust.vaul |                                  |
| t_keys2_op_module__parameter-wra | ::: {.rst-class}                 |
| pjwe/contentencryptionalgorithm} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **contentEncryptionAlgorithm**   | -   `"AES\_128\_CBC\_HM          |
|                                  | AC\_SHA\_256"`{.interpreted-text |
| ```{=html}                       |     role                         |
| <a class="ansibleOption          | ="ansible-option-choices-entry"} |
| Link" href="#parameter-wrapJWE/c | -   `"AES\_192\_CBC\_HM          |
| ontentEncryptionAlgorithm" title | AC\_SHA\_384"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -   `"AES\_256\_CBC\_HM          |
| ansible-option-type-line         | AC\_SHA\_512"`{.interpreted-text |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `"A                          |
|                                  | ES\_128\_GCM"`{.interpreted-text |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              | -   `"A                          |
|                                  | ES\_192\_GCM"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"A                          |
|                                  | ES\_256\_GCM"`{.interpreted-text |
|                                  |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
|                                  |     [←                           |
|                                  |     (default)]{.ansi             |
|                                  | ble-option-choices-default-mark} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | JWT identifier (JTI) is unique   |
| er-wrapJWE/jwtIdentifier"></div> | identifier for the JWT used by   |
| ```                              | SFDC for cache key replay        |
| :::                              | detection.                       |
| {#ansible_collections.thales.cip |                                  |
| hertrust.vault_keys2_op_module__ | ```{=html}                       |
| parameter-wrapjwe/jwtidentifier} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **jwtIdentifier**                |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="                       |                                  |
| ansibleOptionLink" href="#parame |                                  |
| ter-wrapJWE/jwtIdentifier" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOp            | ```                              |
| tionAnchor" id="parameter-wrapJW | Key Encryption Algorithm is used |
| E/keyEncryptionAlgorithm"></div> | to encrypt the Content           |
| ```                              | Encryption Key (CEK), default is |
| ::: {#ansible                    | RSA\_OAEP\_SHA1. Algorithm       |
| _collections.thales.ciphertrust. | should correspond to type of     |
| vault_keys2_op_module__parameter | public key provided for          |
| -wrapjwe/keyencryptionalgorithm} | wrapping.                        |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **keyEncryptionAlgorithm**       | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| <a class="ansibleOp              | -                                |
| tionLink" href="#parameter-wrapJ |    `"RSA1\_5"`{.interpreted-text |
| WE/keyEncryptionAlgorithm" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              | -   `"RSA                        |
| ::: {.rst-class}                 | \_OAEP\_SHA1"`{.interpreted-text |
| ansible-option-type-line         |     role="ansibl                 |
| :::                              | e-option-choices-entry-default"} |
|                                  |     [←                           |
| [string]{.ansible-option-type}   |     (default)]{.ansi             |
|                                  | ble-option-choices-default-mark} |
| ```{=html}                       | -   `"RSA\_                      |
| </div>                           | OAEP\_SHA256"`{.interpreted-text |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |   `"ECDH\_ES"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"ECDH\_ES\_AES\_12          |
|                                  | 8\_KEY\_WRAP"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"ECDH\_ES\_AES\_19          |
|                                  | 2\_KEY\_WRAP"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"ECDH\_ES\_AES\_25          |
|                                  | 6\_KEY\_WRAP"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Key identifier to be used as     |
| er-wrapJWE/keyIdentifier"></div> | \"kid\" parameter in JWE         |
| ```                              | material and JWE header.         |
| :::                              | Defaults to key id.              |
| {#ansible_collections.thales.cip |                                  |
| hertrust.vault_keys2_op_module__ | ```{=html}                       |
| parameter-wrapjwe/keyidentifier} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **keyIdentifier**                |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="                       |                                  |
| ansibleOptionLink" href="#parame |                                  |
| ter-wrapJWE/keyIdentifier" title |                                  |
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
|  class="ansibleOptionAnchor" id= | IDType specifies how the         |
| "parameter-wrapKeyIDType"></div> | wrapKeyName should be            |
| ```                              | interpreted.                     |
| ::: {#ansible_collections.th     |                                  |
| ales.ciphertrust.vault_keys2_op_ | Only applicable for op\_type     |
| module__parameter-wrapkeyidtype} | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **wrapKeyIDType**                | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| <a                               | -   `"name"`{.interpreted-text   |
|  class="ansibleOptionLink" href= |     role                         |
| "#parameter-wrapKeyIDType" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -   `"id"`{.interpreted-text     |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         | -   `"alias"`{.interpreted-text  |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| </div>                           | ```                              |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | The key material will be wrapped |
| d="parameter-wrapKeyName"></div> | with material of the specified   |
| ```                              | key name. The \"material\"       |
| ::: {#ansible_collections.       | property in the response will be |
| thales.ciphertrust.vault_keys2_o | base64 encoded ciphertext. If    |
| p_module__parameter-wrapkeyname} | the \"wrappingMethod\" field is  |
| ::: {.rst-class}                 | set to \"encrypt\", then the     |
| ansible-option-title             | wrapping key must be an AES key, |
| :::                              | RSA private key or RSA public    |
| :::                              | key. For the export of symmetric |
|                                  | keys with the \"encrypt\"        |
| **wrapKeyName**                  | method, the three key types are  |
|                                  | allowed but for the export of a  |
| ```{=html}                       | private key if the               |
| <a class="ansibleOptionLink" hre | \"wrapRSAAES\" parameters are    |
| f="#parameter-wrapKeyName" title | not set, the wrapping key has to |
| ="Permalink to this option"></a> | be an AES key with a size of 256 |
| ```                              | bits. If \"wrapRSAAES\"          |
| ::: {.rst-class}                 | parameters are set, then the     |
| ansible-option-type-line         | wrapping key has to either be an |
| :::                              | RSA private or public key. You   |
|                                  | can set either \"wrapKeyName\"   |
| [string]{.ansible-option-type}   | parameter or \"wrapPublicKey\"   |
|                                  | at a time. The wrapping key      |
| ```{=html}                       | should be active with a protect  |
| </div>                           | stop date that is not expired.   |
| ```                              |                                  |
|                                  | Only applicable for op\_type     |
|                                  | \"export\"                       |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-wrapPBE"></div> | WrapPBE produces a derived key   |
| ```                              | from a password and other        |
| ::: {#ansible_collecti           | parameters like salt, iteration  |
| ons.thales.ciphertrust.vault_key | count, hashing algorithm and     |
| s2_op_module__parameter-wrappbe} | derived key length. PBE is       |
| ::: {.rst-class}                 | currently only supported to wrap |
| ansible-option-title             | symmetric keys (AES), private    |
| :::                              | Keys and certificates.           |
| :::                              |                                  |
|                                  | Only applicable for op\_type     |
| **wrapPBE**                      | \"export\"                       |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLink"     | </div>                           |
|  href="#parameter-wrapPBE" title | ```                              |
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
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | Intended length in octets of the |
| "parameter-wrapPBE/dklen"></div> | derived key. dklen must be in    |
| ```                              | range of 14 bytes to 512 bytes.  |
| ::: {#ansible_collections.th     |                                  |
| ales.ciphertrust.vault_keys2_op_ | ```{=html}                       |
| module__parameter-wrappbe/dklen} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **dklen**                        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-wrapPBE/dklen" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Underlying hashing algorithm     |
| er-wrapPBE/hashAlgorithm"></div> | that acts as a pseudorandom      |
| ```                              | function to generate derive      |
| :::                              | keys.                            |
| {#ansible_collections.thales.cip |                                  |
| hertrust.vault_keys2_op_module__ | ::: {.rst-class}                 |
| parameter-wrappbe/hashalgorithm} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **hashAlgorithm**                | -                                |
|                                  |  `"hmac-sha1"`{.interpreted-text |
| ```{=html}                       |     role                         |
| <a class="                       | ="ansible-option-choices-entry"} |
| ansibleOptionLink" href="#parame | -   `                            |
| ter-wrapPBE/hashAlgorithm" title | "hmac-sha224"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -   `                            |
| ansible-option-type-line         | "hmac-sha256"`{.interpreted-text |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `                            |
|                                  | "hmac-sha384"`{.interpreted-text |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              | -   `                            |
|                                  | "hmac-sha512"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"hma                        |
|                                  | c-sha512/224"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"hma                        |
|                                  | c-sha512/256"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"h                          |
|                                  | mac-sha3-224"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"h                          |
|                                  | mac-sha3-256"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"h                          |
|                                  | mac-sha3-384"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"h                          |
|                                  | mac-sha3-512"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | Iteration count increase the     |
| ameter-wrapPBE/iteration"></div> | cost of producing keys from a    |
| ```                              | password. Iteration must be in   |
| ::: {#ansible_collections.thales | range of 1 to 1,00,00,000.       |
| .ciphertrust.vault_keys2_op_modu |                                  |
| le__parameter-wrappbe/iteration} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **iteration**                    |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cla                           |                                  |
| ss="ansibleOptionLink" href="#pa |                                  |
| rameter-wrapPBE/iteration" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cl                          | ```                              |
| ass="ansibleOptionAnchor" id="pa | Base password to generate derive |
| rameter-wrapPBE/password"></div> | keys. It cannot be used in       |
| ```                              | conjunction with                 |
| ::: {#ansible_collections.thale  | passwordidentifier. password     |
| s.ciphertrust.vault_keys2_op_mod | must be in range of 8 bytes to   |
| ule__parameter-wrappbe/password} | 128 bytes.                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| **password**                     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cl                            |                                  |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-wrapPBE/password" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansib                | ```                              |
| leOptionAnchor" id="parameter-wr | Secret password identifier for   |
| apPBE/passwordIdentifier"></div> | password. It cannot be used in   |
| ```                              | conjunction with password.       |
| ::: {#ans                        |                                  |
| ible_collections.thales.ciphertr | ```{=html}                       |
| ust.vault_keys2_op_module__param | </div>                           |
| eter-wrappbe/passwordidentifier} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **passwordIdentifier**           |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansib                  |                                  |
| leOptionLink" href="#parameter-w |                                  |
| rapPBE/passwordIdentifier" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOp            | ```                              |
| tionAnchor" id="parameter-wrapPB | Type of the Passwordidentifier.  |
| E/passwordIdentifierType"></div> | If not set then default value is |
| ```                              | name.                            |
| ::: {#ansible                    |                                  |
| _collections.thales.ciphertrust. | ::: {.rst-class}                 |
| vault_keys2_op_module__parameter | ansible-option-line              |
| -wrappbe/passwordidentifiertype} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `"id"`{.interpreted-text     |
| **passwordIdentifierType**       |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -   `"name"`{.interpreted-text   |
| <a class="ansibleOp              |     role                         |
| tionLink" href="#parameter-wrapP | ="ansible-option-choices-entry"} |
| BE/passwordIdentifierType" title | -   `"slug"`{.interpreted-text   |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| [string]{.ansible-option-type}   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | User defined purpose. If         |
| arameter-wrapPBE/purpose"></div> | specified will be prefixed to    |
| ```                              | pbeSalt. pbePurpose must not be  |
| ::: {#ansible_collections.thal   | greater than 128 bytes.          |
| es.ciphertrust.vault_keys2_op_mo |                                  |
| dule__parameter-wrappbe/purpose} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **purpose**                      |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a c                             |                                  |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-wrapPBE/purpose" title |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | A Hex encoded string. pbeSalt    |
| ="parameter-wrapPBE/salt"></div> | must be in range of 16 bytes to  |
| ```                              | 512 bytes.                       |
| ::: {#ansible_collections.t      |                                  |
| hales.ciphertrust.vault_keys2_op | ```{=html}                       |
| _module__parameter-wrappbe/salt} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **salt**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-wrapPBE/salt" title |                                  |
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
| nsibleOptionAnchor" id="paramete | It indicates the Encryption      |
| r-wrappingEncryptionAlgo"></div> | Algorithm information for        |
| ```                              | wrapping the key. Format is      |
| ::: {                            | Algorithm/Mode/Padding. For      |
| #ansible_collections.thales.ciph | example AES/AESKEYWRAP. Here AES |
| ertrust.vault_keys2_op_module__p | is Algorithm, AESKEYWRAP is Mode |
| arameter-wrappingencryptionalgo} | & Padding is not specified.      |
| ::: {.rst-class}                 | AES/AESKEYWRAP is RFC-3394 &     |
| ansible-option-title             | AES/AESKEYWRAPPADDING is         |
| :::                              | RFC-5649. For wrapping private   |
| :::                              | key, only AES/AESKEYWRAPPADDING  |
|                                  | is allowed.                      |
| **wrappingEncryptionAlgo**       | RSA/RSAAESKEYWRAPPADDING is used |
|                                  | to wrap/unwrap asymmetric keys   |
| ```{=html}                       | using RSA AES KWP method. Refer  |
| <a class="a                      | \"WrapRSAAES\" to provide        |
| nsibleOptionLink" href="#paramet | optional parameters.             |
| er-wrappingEncryptionAlgo" title |                                  |
| ="Permalink to this option"></a> | Only applicable for op\_type     |
| ```                              | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
|                                  | :::                              |
| [string]{.ansible-option-type}   |                                  |
|                                  | [Ch                              |
| ```{=html}                       | oices:]{.ansible-option-choices} |
| </div>                           |                                  |
| ```                              | -   `"AE                         |
|                                  | S/AESKEYWRAP"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"AES/AESKE                  |
|                                  | YWRAPPADDING"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"RSA/RSAAESKE               |
|                                  | YWRAPPADDING"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cl                          | ```                              |
| ass="ansibleOptionAnchor" id="pa | This parameter specifies the     |
| rameter-wrappingHashAlgo"></div> | hashing algorithm used if        |
| ```                              | \"wrappingMethod\" corresponds   |
| ::: {#ansible_collections.thale  | to \"mac/sign\". In case of MAC  |
| s.ciphertrust.vault_keys2_op_mod | operation, the hashing algorithm |
| ule__parameter-wrappinghashalgo} | used will be inferred from the   |
| ::: {.rst-class}                 | type of HMAC                     |
| ansible-option-title             | key(\"macSignKeyIdentifier\").   |
| :::                              |                                  |
| :::                              | In case of SIGN operation, the   |
|                                  | possible values are sha1,        |
| **wrappingHashAlgo**             | sha224, sha256, sha384 or sha512 |
|                                  |                                  |
| ```{=html}                       | Only applicable for op\_type     |
| <a cl                            | \"export\"                       |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-wrappingHashAlgo" title | ```{=html}                       |
| ="Permalink to this option"></a> | </div>                           |
| ```                              | ```                              |
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
| class="ansibleOptionAnchor" id=" | This parameter specifies the     |
| parameter-wrappingMethod"></div> | wrapping method used to          |
| ```                              | wrap/mac/sign the key material.  |
| ::: {#ansible_collections.tha    |                                  |
| les.ciphertrust.vault_keys2_op_m | Only applicable for op\_type     |
| odule__parameter-wrappingmethod} | \"export\"                       |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **wrappingMethod**               | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| <a                               | -                                |
| class="ansibleOptionLink" href=" |    `"encrypt"`{.interpreted-text |
| #parameter-wrappingMethod" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              | -                                |
| ::: {.rst-class}                 |   `"mac/sign"`{.interpreted-text |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -   `"pbe"`{.interpreted-text    |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       |                                  |
| </div>                           | ```{=html}                       |
| ```                              | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | If the algorithm is              |
| "parameter-wrapPublicKey"></div> | \'aes\',\'tdes\',\'hmac-\*\',    |
| ```                              | \'seed\' or \'aria\', this value |
| ::: {#ansible_collections.th     | will be used to encrypt the      |
| ales.ciphertrust.vault_keys2_op_ | returned key material. This      |
| module__parameter-wrappublickey} | value is ignored for other       |
| ::: {.rst-class}                 | algorithms. Value must be an RSA |
| ansible-option-title             | public key, PEM-encoded public   |
| :::                              | key in either PKCS1 or PKCS8     |
| :::                              | format, or a PEM-encoded X.509   |
|                                  | certificate. If set, the         |
| **wrapPublicKey**                | returned \'material\' value will |
|                                  | be a Base64 encoded PKCS\#1 v1.5 |
| ```{=html}                       | encrypted key. View              |
| <a                               | \"wrapPublicKey\" in export      |
|  class="ansibleOptionLink" href= | parameters for more information. |
| "#parameter-wrapPublicKey" title | Only applicable if               |
| ="Permalink to this option"></a> | \'includeMaterial\' is true.     |
| ```                              |                                  |
| ::: {.rst-class}                 | Only applicable for op\_type     |
| ansible-option-type-line         | \"export\"                       |
| :::                              |                                  |
|                                  | ```{=html}                       |
| [string]{.ansible-option-type}   | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | WrapPublicKeyPadding specifies   |
| ter-wrapPublicKeyPadding"></div> | the type of padding scheme that  |
| ```                              | needs to be set when importing   |
| :::                              | the Key using the specified      |
|  {#ansible_collections.thales.ci | wrapkey. Accepted values are     |
| phertrust.vault_keys2_op_module_ | \"pkcs1\", \"oaep\",             |
| _parameter-wrappublickeypadding} | \"oaep256\", \"oaep384\",        |
| ::: {.rst-class}                 | \"oaep512\", and will default to |
| ansible-option-title             | \"pkcs1\" when                   |
| :::                              | \'wrapPublicKeyPadding\' is not  |
| :::                              | set and \'WrapPublicKey\' is     |
|                                  | set.                             |
| **wrapPublicKeyPadding**         |                                  |
|                                  | While creating a new key,        |
| ```{=html}                       | wrapPublicKeyPadding parameter   |
| <a class=                        | should be specified only if      |
| "ansibleOptionLink" href="#param | \'includeMaterial\' is true. In  |
| eter-wrapPublicKeyPadding" title | this case, key will get created  |
| ="Permalink to this option"></a> | and in response wrapped material |
| ```                              | using specified                  |
| ::: {.rst-class}                 | wrapPublicKeyPadding and other   |
| ansible-option-type-line         | wrap parameters will be          |
| :::                              | returned.                        |
|                                  |                                  |
| [string]{.ansible-option-type}   | Only applicable for op\_type     |
|                                  | \"export\"                       |
| ```{=html}                       |                                  |
| </div>                           | ::: {.rst-class}                 |
| ```                              | ansible-option-line              |
|                                  | :::                              |
|                                  |                                  |
|                                  | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
|                                  |                                  |
|                                  | -   `"pkcs1"`{.interpreted-text  |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"oaep"`{.interpreted-text   |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |    `"oaep256"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |    `"oaep384"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |    `"oaep512"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | Information which is used to     |
| id="parameter-wrapRSAAES"></div> | wrap/unwrap asymmetric keys      |
| ```                              | using RSA AES KWP method. This   |
| ::: {#ansible_collections        | method internally requires AES   |
| .thales.ciphertrust.vault_keys2_ | key size to generate a temporary |
| op_module__parameter-wraprsaaes} | AES key and RSA padding. To use  |
| ::: {.rst-class}                 | WrapRSAAES, algorithm            |
| ansible-option-title             | \"RSA/RSAAESKEYWRAPPADDING\"     |
| :::                              | must be specified in             |
| :::                              | WrappingEncryptionAlgo.          |
|                                  |                                  |
| **wrapRSAAES**                   | Only applicable for op\_type     |
|                                  | \"export\"                       |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hr  | ```{=html}                       |
| ef="#parameter-wrapRSAAES" title | </div>                           |
| ="Permalink to this option"></a> | ```                              |
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
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Size of AES key for RSA AES KWP. |
| er-wrapRSAAES/aesKeySize"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| {#ansible_collections.thales.cip | :::                              |
| hertrust.vault_keys2_op_module__ |                                  |
| parameter-wraprsaaes/aeskeysize} | [Ch                              |
| ::: {.rst-class}                 | oices:]{.ansible-option-choices} |
| ansible-option-title             |                                  |
| :::                              | -   `128`{.interpreted-text      |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| **aesKeySize**                   | -   `192`{.interpreted-text      |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class="                       | -   `256`{.interpreted-text      |
| ansibleOptionLink" href="#parame |     role="ansibl                 |
| ter-wrapRSAAES/aesKeySize" title | e-option-choices-entry-default"} |
| ="Permalink to this option"></a> |     [←                           |
| ```                              |     (default)]{.ansi             |
| ::: {.rst-class}                 | ble-option-choices-default-mark} |
| ansible-option-type-line         |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| [integer]{.ansible-option-type}  | ```                              |
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
| s="ansibleOptionAnchor" id="para | Padding specifies the type of    |
| meter-wrapRSAAES/padding"></div> | padding scheme that needs to be  |
| ```                              | set when exporting the Key using |
| :                                | RSA AES wrap                     |
| :: {#ansible_collections.thales. |                                  |
| ciphertrust.vault_keys2_op_modul | ::: {.rst-class}                 |
| e__parameter-wraprsaaes/padding} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **padding**                      | -   `"oaep"`{.interpreted-text   |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a clas                          | -                                |
| s="ansibleOptionLink" href="#par |    `"oaep256"`{.interpreted-text |
| ameter-wrapRSAAES/padding" title |     role="ansibl                 |
| ="Permalink to this option"></a> | e-option-choices-entry-default"} |
| ```                              |     [←                           |
| ::: {.rst-class}                 |     (default)]{.ansi             |
| ansible-option-type-line         | ble-option-choices-default-mark} |
| :::                              | -                                |
|                                  |    `"oaep384"`{.interpreted-text |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -                                |
| </div>                           |    `"oaep512"`{.interpreted-text |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+

Examples
--------

``` {.yaml+jinja}
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
