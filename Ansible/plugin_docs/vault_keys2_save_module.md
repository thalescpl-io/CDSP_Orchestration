orphan

:   

::: {#ansible_collections.thales.ciphertrust.vault_keys2_save_module}
:::

thales.ciphertrust.vault\_keys2\_save module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
===========================================================================================================================================

::: {.note}
::: {.title}
Note
:::

This module is part of the [thales.ciphertrust
collection](https://galaxy.ansible.com/thales/ciphertrust) (version
1.0.0).

To install it, use:
`ansible-galaxy collection install thales.ciphertrust`.

To use it in a playbook, specify: `thales.ciphertrust.vault_keys2_save`.
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
    CipherTrust Manager APIs, more specifically with keys management API

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
| <div                             | ```                              |
| class="ansibleOptionAnchor" id=" | Date/time the object becomes     |
| parameter-activationDate"></div> | active                           |
| ```                              |                                  |
| ::: {#ansible_collections.thale  | ```{=html}                       |
| s.ciphertrust.vault_keys2_save_m | </div>                           |
| odule__parameter-activationdate} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **activationDate**               |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
| class="ansibleOptionLink" href=" |                                  |
| #parameter-activationDate" title |                                  |
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
|  id="parameter-algorithm"></div> | Cryptographic algorithm this key |
| ```                              | is used with.                    |
| ::: {#ansible_collections.       |                                  |
| thales.ciphertrust.vault_keys2_s | Defaults to \'aes\'              |
| ave_module__parameter-algorithm} |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-title             | ansible-option-line              |
| :::                              | :::                              |
| :::                              |                                  |
|                                  | [Ch                              |
| **algorithm**                    | oices:]{.ansible-option-choices} |
|                                  |                                  |
| ```{=html}                       | -   `"aes"`{.interpreted-text    |
| <a class="ansibleOptionLink" h   |     role="ansibl                 |
| ref="#parameter-algorithm" title | e-option-choices-entry-default"} |
| ="Permalink to this option"></a> |     [←                           |
| ```                              |     (default)]{.ansi             |
| ::: {.rst-class}                 | ble-option-choices-default-mark} |
| ansible-option-type-line         | -   `"tdes"`{.interpreted-text   |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `"rsa"`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           | -   `"ec"`{.interpreted-text     |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |  `"hmac-sha1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "hmac-sha256"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "hmac-sha384"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "hmac-sha512"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"seed"`{.interpreted-text   |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"aria"`{.interpreted-text   |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"opaque"`{.interpreted-text |
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
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-aliases"></div> | Aliases associated with the key. |
| ```                              |                                  |
| ::: {#ansible_collection         | The alias and alias-type must be |
| s.thales.ciphertrust.vault_keys2 | specified.                       |
| _save_module__parameter-aliases} |                                  |
| ::: {.rst-class}                 | The alias index is assigned by   |
| ansible-option-title             | this operation, and need not be  |
| :::                              | specified.                       |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **aliases**                      | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
|  href="#parameter-aliases" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [list]{.ansible-option-type} /   |                                  |
| [elements=dicti                  |                                  |
| onary]{.ansible-option-elements} |                                  |
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
|  class="ansibleOptionAnchor" id= | An alias for a key name          |
| "parameter-aliases/alias"></div> |                                  |
| ```                              | ```{=html}                       |
| ::: {#ansible_collections.thal   | </div>                           |
| es.ciphertrust.vault_keys2_save_ | ```                              |
| module__parameter-aliases/alias} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **alias**                        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-aliases/alias" title |                                  |
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
|  class="ansibleOptionAnchor" id= | Index associated with alias.     |
| "parameter-aliases/index"></div> | Each alias within an object has  |
| ```                              | a unique index                   |
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.vault_keys2_save_ | ```{=html}                       |
| module__parameter-aliases/index} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **index**                        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
|  class="ansibleOptionLink" href= |                                  |
| "#parameter-aliases/index" title |                                  |
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
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | Type of alias (allowed values    |
| ="parameter-aliases/type"></div> | are string and uri)              |
| ```                              |                                  |
| ::: {#ansible_collections.tha    | ```{=html}                       |
| les.ciphertrust.vault_keys2_save | </div>                           |
| _module__parameter-aliases/type} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **type**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-aliases/type" title |                                  |
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
| iv class="ansibleOptionAnchor" i | To update the group              |
| d="parameter-allVersions"></div> | permissions/custom attribute or  |
| ```                              | both in metadata of all versions |
| ::: {#ansible_collections.th     | of the key. By default it is set |
| ales.ciphertrust.vault_keys2_sav | to false. Set to true, only when |
| e_module__parameter-allversions} | to update the group/custom       |
| ::: {.rst-class}                 | attribute or both permissions of |
| ansible-option-title             | all versions of the key.         |
| :::                              |                                  |
| :::                              | Only applicable for op\_type     |
|                                  | \"patch\"                        |
| **allVersions**                  |                                  |
|                                  | ::: {.rst-class}                 |
| ```{=html}                       | ansible-option-line              |
| <a class="ansibleOptionLink" hre | :::                              |
| f="#parameter-allVersions" title |                                  |
| ="Permalink to this option"></a> | [Ch                              |
| ```                              | oices:]{.ansible-option-choices} |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         | -   `false`{.interpreted-text    |
| :::                              |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| [boolean]{.ansible-option-type}  |     [←                           |
|                                  |     (default)]{.ansi             |
| ```{=html}                       | ble-option-choices-default-mark} |
| </div>                           | -   `true`{.interpreted-text     |
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
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | Date/time the object becomes     |
| d="parameter-archiveDate"></div> | archived                         |
| ```                              |                                  |
| ::: {#ansible_collections.th     | ```{=html}                       |
| ales.ciphertrust.vault_keys2_sav | </div>                           |
| e_module__parameter-archivedate} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **archiveDate**                  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-archiveDate" title |                                  |
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
| " id="parameter-certType"></div> | This specifies the type of       |
| ```                              | certificate object that is being |
| ::: {#ansible_collections        | created. Valid values are        |
| .thales.ciphertrust.vault_keys2_ | \'x509-pem\' and \'x509-der\'.   |
| save_module__parameter-certtype} | At present, we only support      |
| ::: {.rst-class}                 | x.509 certificates. The          |
| ansible-option-title             | cerfificate data is passed in    |
| :::                              | via the \'material\' field. The  |
| :::                              | certificate type is infered from |
|                                  | the material if it is left       |
| **certType**                     | blank.                           |
|                                  |                                  |
| ```{=html}                       | ::: {.rst-class}                 |
| <a class="ansibleOptionLink"     | ansible-option-line              |
| href="#parameter-certType" title | :::                              |
| ="Permalink to this option"></a> |                                  |
| ```                              | [Ch                              |
| ::: {.rst-class}                 | oices:]{.ansible-option-choices} |
| ansible-option-type-line         |                                  |
| :::                              | -                                |
|                                  |   `"x509-pem"`{.interpreted-text |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -                                |
| </div>                           |   `"x509-der"`{.interpreted-text |
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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-cm_key_id"></div> | CM ID of the key that needs to   |
| ```                              | be patched.                      |
| ::: {#ansible_collections.       |                                  |
| thales.ciphertrust.vault_keys2_s | Only required if the op\_type is |
| ave_module__parameter-cm_key_id} | patch or create\_version         |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
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
| class="ansibleOptionAnchor" id=" | Date/time the object entered     |
| parameter-compromiseDate"></div> | into the compromised state.      |
| ```                              |                                  |
| ::: {#ansible_collections.thale  | ```{=html}                       |
| s.ciphertrust.vault_keys2_save_m | </div>                           |
| odule__parameter-compromisedate} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **compromiseDate**               |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a                               |                                  |
| class="ansibleOptionLink" href=" |                                  |
| #parameter-compromiseDate" title |                                  |
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
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | Date/time when the object was    |
| compromiseOccurrenceDate"></div> | first believed to be             |
| ```                              | compromised, if known. Only      |
| ::: {#ans                        | valid if the revocation reason   |
| ible_collections.thales.ciphertr | is CACompromise or               |
| ust.vault_keys2_save_module__par | KeyCompromise, otherwise         |
| ameter-compromiseoccurrencedate} | ignored.                         |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| **compromiseOccurrenceDate**     |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
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
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-curveid"></div> | Cryptographic curve id for       |
| ```                              | elliptic key.                    |
| ::: {#ansible_collection         |                                  |
| s.thales.ciphertrust.vault_keys2 | Key algorithm must be \'EC\'     |
| _save_module__parameter-curveid} |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-title             | ansible-option-line              |
| :::                              | :::                              |
| :::                              |                                  |
|                                  | [Ch                              |
| **curveid**                      | oices:]{.ansible-option-choices} |
|                                  |                                  |
| ```{=html}                       | -                                |
| <a class="ansibleOptionLink"     |  `"secp224k1"`{.interpreted-text |
|  href="#parameter-curveid" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              | -                                |
| ::: {.rst-class}                 |  `"secp224r1"`{.interpreted-text |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -                                |
| [string]{.ansible-option-type}   |  `"secp256k1"`{.interpreted-text |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           | -                                |
| ```                              |  `"secp384r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  |  `"secp521r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  | `"prime256v1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP224r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP224t1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP256r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP256t1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP384r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP384t1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP512r1"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"bra                        |
|                                  | inpoolP512t1"`{.interpreted-text |
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
| ass="ansibleOptionAnchor" id="pa | Date/time the object becomes     |
| rameter-deactivationDate"></div> | inactive                         |
| ```                              |                                  |
| :                                | ```{=html}                       |
| :: {#ansible_collections.thales. | </div>                           |
| ciphertrust.vault_keys2_save_mod | ```                              |
| ule__parameter-deactivationdate} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **deactivationDate**             |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cl                            |                                  |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-deactivationDate" title |                                  |
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
|  id="parameter-defaultIV"></div> | Deprecated. This field was       |
| ```                              | introduced to support specific   |
| ::: {#ansible_collections.       | legacy integrations and          |
| thales.ciphertrust.vault_keys2_s | applications. New applications   |
| ave_module__parameter-defaultiv} | are strongly recommended to use  |
| ::: {.rst-class}                 | a unique IV for each encryption  |
| ansible-option-title             | request. Refer to Crypto encrypt |
| :::                              | endpoint for more details. Must  |
| :::                              | be a 16 byte hex encoded string  |
|                                  | (32 characters long). If         |
| **defaultIV**                    | specified, this will be set as   |
|                                  | the default IV for this key.     |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" h   | ```{=html}                       |
| ref="#parameter-defaultIV" title | </div>                           |
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
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | Date/time the object was         |
| d="parameter-destroyDate"></div> | destroyed.                       |
| ```                              |                                  |
| ::: {#ansible_collections.th     | ```{=html}                       |
| ales.ciphertrust.vault_keys2_sav | </div>                           |
| e_module__parameter-destroydate} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **destroyDate**                  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-destroyDate" title |                                  |
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
| ```                              | the \'material\' field.          |
| ::: {#ansible_collections        |                                  |
| .thales.ciphertrust.vault_keys2_ | This parameter is used during    |
| save_module__parameter-encoding} | importing keys when key material |
| ::: {.rst-class}                 | is not empty or while returning  |
| ansible-option-title             | the key material after the key   |
| :::                              | is created (\'includeMaterial\'  |
| :::                              | is true)                         |
|                                  |                                  |
| **encoding**                     | For wrapping scenarios and       |
|                                  | PKCS12 format, the only valid    |
| ```{=html}                       | option is base64. In case of     |
| <a class="ansibleOptionLink"     | \"Symmetric Keys\" when          |
| href="#parameter-encoding" title | \'format\' parameter has         |
| ="Permalink to this option"></a> | \'base64\' value and             |
| ```                              | \'encoding\' parameter also      |
| ::: {.rst-class}                 | contains some value. The         |
| ansible-option-type-line         | encoding parameter takes the     |
| :::                              | priority. Following are the      |
|                                  | options for Symmetric Keys are   |
| [string]{.ansible-option-type}   | hex or base64                    |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| </div>                           | </div>                           |
| ```                              | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-format"></div> | This parameter is used while     |
| ```                              | importing keys (\'material\' is  |
| ::: {#ansible_collectio          | not empty), and also when        |
| ns.thales.ciphertrust.vault_keys | returning the key material after |
| 2_save_module__parameter-format} | the key is created               |
| ::: {.rst-class}                 | (\'includeMaterial\' is true).   |
| ansible-option-title             |                                  |
| :::                              | For Asymmetric keys, When this   |
| :::                              | parameter is not specified,      |
|                                  | while importing keys, the format |
| **format**                       | of the material is inferred from |
|                                  | the material itself. When this   |
| ```{=html}                       | parameter is specified, while    |
| <a class="ansibleOptionLink      | importing keys, the only allowed |
| " href="#parameter-format" title | format is \'pkcs12\', and this   |
| ="Permalink to this option"></a> | only applies to the \'rsa\'      |
| ```                              | algorithm (the \'material\'      |
| ::: {.rst-class}                 | should contain the base64        |
| ansible-option-type-line         | encoded value of the PFX file in |
| :::                              | this case). Options are pkcs1,   |
|                                  | pkcs8 (default) or pkcs12        |
| [string]{.ansible-option-type}   |                                  |
|                                  | For Symmetric keys, When         |
| ```{=html}                       | importing keys if specified, the |
| </div>                           | value must be given according to |
| ```                              | the format of the material.      |
|                                  | Options are raw or opaque        |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | If specified as true, the key\'s |
| "parameter-generateKeyId"></div> | keyId identifier of type long is |
| ```                              | generated. Defaults to false.    |
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.vault_keys2_save_ | ::: {.rst-class}                 |
| module__parameter-generatekeyid} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **generateKeyId**                | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
| ```{=html}                       | e-option-choices-entry-default"} |
| <a                               |     [←                           |
|  class="ansibleOptionLink" href= |     (default)]{.ansi             |
| "#parameter-generateKeyId" title | ble-option-choices-default-mark} |
| ="Permalink to this option"></a> | -   `true`{.interpreted-text     |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| [boolean]{.ansible-option-type}  | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | Information which is used to     |
| ter-hkdfCreateParameters"></div> | create a Key using HKDF.         |
| ```                              |                                  |
| ::: {                            | ```{=html}                       |
| #ansible_collections.thales.ciph | </div>                           |
| ertrust.vault_keys2_save_module_ | ```                              |
| _parameter-hkdfcreateparameters} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **hkdfCreateParameters**         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class=                        |                                  |
| "ansibleOptionLink" href="#param |                                  |
| eter-hkdfCreateParameters" title |                                  |
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
| Anchor" id="parameter-hkdfCreate | Hash Algorithm is used for HKDF. |
| Parameters/hashAlgorithm"></div> |                                  |
| ```                              | This is required if ikmKeyName   |
| ::: {#ansible_colle              | is specified, default is         |
| ctions.thales.ciphertrust.vault_ | hmac-sha256.                     |
| keys2_save_module__parameter-hkd |                                  |
| fcreateparameters/hashalgorithm} | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-title             | :::                              |
| :::                              |                                  |
| :::                              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| **hashAlgorithm**                |                                  |
|                                  | -                                |
| ```{=html}                       |  `"hmac-sha1"`{.interpreted-text |
| <a class="ansibleOption          |     role                         |
| Link" href="#parameter-hkdfCreat | ="ansible-option-choices-entry"} |
| eParameters/hashAlgorithm" title | -   `                            |
| ="Permalink to this option"></a> | "hmac-sha224"`{.interpreted-text |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         | -   `                            |
| :::                              | "hmac-sha256"`{.interpreted-text |
|                                  |     role="ansibl                 |
| [string]{.ansible-option-type}   | e-option-choices-entry-default"} |
|                                  |     [←                           |
| ```{=html}                       |     (default)]{.ansi             |
| </div>                           | ble-option-choices-default-mark} |
| ```                              | -   `                            |
|                                  | "hmac-sha384"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "hmac-sha512"`{.interpreted-text |
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
| <div class="ansibleOpt           | ```                              |
| ionAnchor" id="parameter-hkdfCre | Any existing symmetric key.      |
| ateParameters/ikmKeyName"></div> | Mandatory while using HKDF key   |
| ```                              | generation.                      |
| ::: {#ansible_co                 |                                  |
| llections.thales.ciphertrust.vau | ```{=html}                       |
| lt_keys2_save_module__parameter- | </div>                           |
| hkdfcreateparameters/ikmkeyname} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **ikmKeyName**                   |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOpt             |                                  |
| ionLink" href="#parameter-hkdfCr |                                  |
| eateParameters/ikmKeyName" title |                                  |
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
| <div class="ansi                 | ```                              |
| bleOptionAnchor" id="parameter-h | Info is an optional hex value    |
| kdfCreateParameters/info"></div> | for HKDF based derivation.       |
| ```                              |                                  |
| ::: {#ansi                       | ```{=html}                       |
| ble_collections.thales.ciphertru | </div>                           |
| st.vault_keys2_save_module__para | ```                              |
| meter-hkdfcreateparameters/info} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **info**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansi                   |                                  |
| bleOptionLink" href="#parameter- |                                  |
| hkdfCreateParameters/info" title |                                  |
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
| <div class="ansi                 | ```                              |
| bleOptionAnchor" id="parameter-h | Salt is an optional hex value    |
| kdfCreateParameters/salt"></div> | for HKDF based derivation.       |
| ```                              |                                  |
| ::: {#ansi                       | ```{=html}                       |
| ble_collections.thales.ciphertru | </div>                           |
| st.vault_keys2_save_module__para | ```                              |
| meter-hkdfcreateparameters/salt} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **salt**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansi                   |                                  |
| bleOptionLink" href="#parameter- |                                  |
| hkdfCreateParameters/salt" title |                                  |
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
| <div class="ansibleOption        | ```                              |
| Anchor" id="parameter-id"></div> | This optional parameter          |
| ```                              | specifies the identifier of the  |
| ::: {#ansible_colle              | key (id). It is used only when   |
| ctions.thales.ciphertrust.vault_ | creating keys with specific key  |
| keys2_save_module__parameter-id} | material. If set, the key\'s id  |
| ::: {.rst-class}                 | is set to this value.            |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **id**                           |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOption          |                                  |
| Link" href="#parameter-id" title |                                  |
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
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-idSize"></div> | Size of the ID for the key       |
| ```                              |                                  |
| ::: {#ansible_collectio          | ```{=html}                       |
| ns.thales.ciphertrust.vault_keys | </div>                           |
| 2_save_module__parameter-idsize} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
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
| <div class="ansibleOptionAnc     | ```                              |
| hor" id="parameter-keyId"></div> | Additional identifier of the     |
| ```                              | key. The format of this value is |
| ::: {#ansible_collecti           | of type long. This is optional   |
| ons.thales.ciphertrust.vault_key | and applicable for import key    |
| s2_save_module__parameter-keyid} | only. If set, the value is       |
| ::: {.rst-class}                 | imported as the key\'s keyId.    |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **keyId**                        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLin       |                                  |
| k" href="#parameter-keyId" title |                                  |
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
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-labels"></div> | Optional key/value pairs used to |
| ```                              | group keys. APIs that list keys  |
| ::: {#ansible_collectio          | can use labels to filter the set |
| ns.thales.ciphertrust.vault_keys | of matching resources. A         |
| 2_save_module__parameter-labels} | label\'s key has an optional     |
| ::: {.rst-class}                 | prefix up to 253 characters      |
| ansible-option-title             | followed by a forward slash and  |
| :::                              | a required name up to 63         |
| :::                              | characters. For example,         |
|                                  | sales.widgets.com/region is a    |
| **labels**                       | label key with the prefix        |
|                                  | sales.widgets.com and the name   |
| ```{=html}                       | region, while region is a label  |
| <a class="ansibleOptionLink      | key without a prefix. A label\'s |
| " href="#parameter-labels" title | value may be empty and may be up |
| ="Permalink to this option"></a> | to 63 characters. Each part of   |
| ```                              | the label (i.e. the prefix,      |
| ::: {.rst-class}                 | name, and value) must begin and  |
| ansible-option-type-line         | end with an alphanumeric         |
| :::                              | character (a-zA-Z0-9).           |
|                                  | Characters in between the        |
| [d                               | beginning and end may contain    |
| ictionary]{.ansible-option-type} | alphanumeric characters, dots    |
|                                  | (.), dashes (-) and underscores  |
| ```{=html}                       | (\_). A Label can be a simple    |
| </div>                           | tag by specifying a key with no  |
| ```                              | value                            |
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
| ::: {#ansible_collections.       | communicate with an instance of  |
| thales.ciphertrust.vault_keys2_s | CipherTrust Manager (CM)         |
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
| :::                              | </div>                           |
|  {#ansible_collections.thales.ci | ```                              |
| phertrust.vault_keys2_save_modul |                                  |
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
| :::                              | </div>                           |
| {#ansible_collections.thales.cip | ```                              |
| hertrust.vault_keys2_save_module |                                  |
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
| ::: {#                           | ::: {.rst-class}                 |
| ansible_collections.thales.ciphe | ansible-option-line              |
| rtrust.vault_keys2_save_module__ | :::                              |
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
| ::: {#ansibl                     |                                  |
| e_collections.thales.ciphertrust | ```{=html}                       |
| .vault_keys2_save_module__parame | </div>                           |
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
| ::: {#ansible_collections.thale  | </div>                           |
| s.ciphertrust.vault_keys2_save_m | ```                              |
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
| :                                | ansible-option-line              |
| :: {#ansible_collections.thales. | :::                              |
| ciphertrust.vault_keys2_save_mod |                                  |
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
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | This parameter specifies the     |
| ="parameter-macSignBytes"></div> | MAC/Signature bytes to be used   |
| ```                              | for verification while importing |
| ::: {#ansible_collections.tha    | a key. The \"wrappingMethod\"    |
| les.ciphertrust.vault_keys2_save | should be \"mac/sign\" and the   |
| _module__parameter-macsignbytes} | required parameters for the      |
| ::: {.rst-class}                 | verification must be set.        |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **macSignBytes**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-macSignBytes" title |                                  |
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
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | This parameter specifies the     |
| ter-macSignKeyIdentifier"></div> | identifier of the key to be used |
| ```                              | for generating MAC or signature  |
| ::: {                            | of the key material. The         |
| #ansible_collections.thales.ciph | \"wrappingMethod\" should be     |
| ertrust.vault_keys2_save_module_ | \"mac/sign\" to verify the       |
| _parameter-macsignkeyidentifier} | MAC/signature(\"macSignBytes\")  |
| ::: {.rst-class}                 | of the key                       |
| ansible-option-title             | material(\"material\"). For      |
| :::                              | verifying the MAC, the key has   |
| :::                              | to be a HMAC key. For verifying  |
|                                  | the signature, the key has to be |
| **macSignKeyIdentifier**         | an RSA private or public key.    |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class=                        | </div>                           |
| "ansibleOptionLink" href="#param | ```                              |
| eter-macSignKeyIdentifier" title |                                  |
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
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | This parameter specifies the     |
| macSignKeyIdentifierType"></div> | identifier of the                |
| ```                              | key(\"macSignKeyIdentifier\")    |
| ::: {#ans                        | used for generating MAC or       |
| ible_collections.thales.ciphertr | signature of the key material.   |
| ust.vault_keys2_save_module__par | The \"wrappingMethod\" should be |
| ameter-macsignkeyidentifiertype} | \"mac/sign\" to verify the       |
| ::: {.rst-class}                 | mac/signature(\"macSignBytes\")  |
| ansible-option-title             | of the key                       |
| :::                              | material(\"material\")           |
| :::                              |                                  |
|                                  | ::: {.rst-class}                 |
| **macSignKeyIdentifierType**     | ansible-option-line              |
|                                  | :::                              |
| ```{=html}                       |                                  |
| <a class="ans                    | [Ch                              |
| ibleOptionLink" href="#parameter | oices:]{.ansible-option-choices} |
| -macSignKeyIdentifierType" title |                                  |
| ="Permalink to this option"></a> | -   `"name"`{.interpreted-text   |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         | -   `"id"`{.interpreted-text     |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `"alias"`{.interpreted-text  |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           |                                  |
| ```                              | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-material"></div> | If set, the value will be        |
| ```                              | imported as the key\'s material. |
| ::: {#ansible_collections        | If not set, new key material     |
| .thales.ciphertrust.vault_keys2_ | will be generated on the server  |
| save_module__parameter-material} | (certificate objects must always |
| ::: {.rst-class}                 | specify the material). The       |
| ansible-option-title             | format of this value depends on  |
| :::                              | the algorithm. If the algorithm  |
| :::                              | is \'aes\', \'tdes\',            |
|                                  | \'hmac-\*\', \'seed\' or         |
| **material**                     | \'aria\', the value should be    |
|                                  | the hex-encoded bytes of the key |
| ```{=html}                       | material. If the algorithm is    |
| <a class="ansibleOptionLink"     | \'rsa\', and the format is       |
| href="#parameter-material" title | \'pkcs12\', it should be the     |
| ="Permalink to this option"></a> | base64 encoded PFX file. If the  |
| ```                              | algorithm is \'rsa\' or \'ec\',  |
| ::: {.rst-class}                 | and format is not \'pkcs12\',    |
| ansible-option-type-line         | the value should be a            |
| :::                              | PEM-encoded private or public    |
|                                  | key using PKCS1 or PKCS8 format. |
| [string]{.ansible-option-type}   | For a X.509 DER encoded          |
|                                  | certificate, certType equals     |
| ```{=html}                       | \'x509-der\' and the material    |
| </div>                           | should equal the hex encoded     |
| ```                              | certificate. The material for a  |
|                                  | X.509 PEM encoded certificate    |
|                                  | (certType = \'x509-pem\') should |
|                                  | equal the certificate itself.    |
|                                  | When placing the PEM encoded     |
|                                  | certificate inside a JSON object |
|                                  | (as in the playground), be sure  |
|                                  | to change all new line           |
|                                  | characters in the certificate to |
|                                  | the string newline char.         |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-meta"></div> | Optional end-user or service     |
| ```                              | data stored with the key         |
| ::: {#ansible_collect            |                                  |
| ions.thales.ciphertrust.vault_ke | ```{=html}                       |
| ys2_save_module__parameter-meta} | </div>                           |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | Optional owner information for   |
| ="parameter-meta/ownerId"></div> | the key, required for non-admin. |
| ```                              | Value should be the user\'s      |
| ::: {#ansible_collections.tha    | user\_id                         |
| les.ciphertrust.vault_keys2_save |                                  |
| _module__parameter-meta/ownerid} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **ownerId**                      |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <                                |                                  |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-meta/ownerId" title |                                  |
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
| chor" id="parameter-muid"></div> | Additional identifier of the     |
| ```                              | key. This is optional and        |
| ::: {#ansible_collect            | applicable for import key only.  |
| ions.thales.ciphertrust.vault_ke | If set, the value is imported as |
| ys2_save_module__parameter-muid} | the key\'s muid.                 |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
|                                  |                                  |
| **muid**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-muid" title |                                  |
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
| chor" id="parameter-name"></div> | Optional friendly name, The key  |
| ```                              | name should not contain special  |
| ::: {#ansible_collect            | characters such as angular       |
| ions.thales.ciphertrust.vault_ke | brackets (\<,\>) and backslash   |
| ys2_save_module__parameter-name} | ().                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ```{=html}                       |
| :::                              | </div>                           |
| :::                              | ```                              |
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
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | This specifies the type of       |
| id="parameter-objectType"></div> | object that is being created.    |
| ```                              | Valid values are \'Symmetric     |
| ::: {#ansible_collections.t      | Key\', \'Public Key\', \'Private |
| hales.ciphertrust.vault_keys2_sa | Key\', \'Secret Data\', \'Opaque |
| ve_module__parameter-objecttype} | Object\', or \'Certificate\'.    |
| ::: {.rst-class}                 | The object type is inferred for  |
| ansible-option-title             | many objects, but must be        |
| :::                              | supplied for the certificate     |
| :::                              | object.                          |
|                                  |                                  |
| **objectType**                   | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| ```{=html}                       | :::                              |
| <a class="ansibleOptionLink" hr  |                                  |
| ef="#parameter-objectType" title | [Ch                              |
| ="Permalink to this option"></a> | oices:]{.ansible-option-choices} |
| ```                              |                                  |
| ::: {.rst-class}                 | -   `"S                          |
| ansible-option-type-line         | ymmetric Key"`{.interpreted-text |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -                                |
|                                  | `"Public Key"`{.interpreted-text |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              | -   `                            |
|                                  | "Private Key"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "Secret Data"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"O                          |
|                                  | paque Object"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `                            |
|                                  | "Certificate"`{.interpreted-text |
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
| or" id="parameter-offset"></div> | An Offset MAY be used to         |
| ```                              | indicate the difference between  |
| ::: {#ansible_collectio          | the Creation Date and the        |
| ns.thales.ciphertrust.vault_keys | Activation Date of the           |
| 2_save_module__parameter-offset} | replacement key. If no Offset is |
| ::: {.rst-class}                 | specified, the Activation Date,  |
| ansible-option-title             | Process Start Date, Protect Stop |
| :::                              | Date and Deactivation Date       |
| :::                              | values are copied from the       |
|                                  | existing key. If Offset is set   |
| **offset**                       | and dates exist for the existing |
|                                  | key, then the dates of the       |
| ```{=html}                       | replacement key are set based on |
| <a class="ansibleOptionLink      | the dates of the existing key by |
| " href="#parameter-offset" title | adding the offset.               |
| ="Permalink to this option"></a> |                                  |
| ```                              | Only applicable for op\_type     |
| ::: {.rst-class}                 | \"create\_version\"              |
| ansible-option-type-line         |                                  |
| :::                              | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| [integer]{.ansible-option-type}  | :::                              |
|                                  |                                  |
| ```{=html}                       | [Default                         |
| </div>                           | :]{.ansible-option-default-bold} |
| ```                              | `false`{.interpreted-text        |
|                                  | role="ansible-option-default"}   |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-op_type"></div> | Operation to be performed        |
| ```                              |                                  |
| ::: {#ansible_collection         | ::: {.rst-class}                 |
| s.thales.ciphertrust.vault_keys2 | ansible-option-line              |
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
| ="Permalink to this option"></a> | -   `"cre                        |
| ```                              | ate\_version"`{.interpreted-text |
| ::: {.rst-class}                 |     role                         |
| ansible-option-type-line         | ="ansible-option-choices-entry"} |
| :::                              |                                  |
|                                  | ```{=html}                       |
| [string]{.ansible-option-type} / | </div>                           |
| [req                             | ```                              |
| uired]{.ansible-option-required} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-padded"></div> | This parameter determines the    |
| ```                              | padding for the wrap algorithm   |
| ::: {#ansible_collectio          | while unwrapping a symmetric key |
| ns.thales.ciphertrust.vault_keys |                                  |
| 2_save_module__parameter-padded} | If true, the RFC 5649(AES Key    |
| ::: {.rst-class}                 | Wrap with Padding) is followed   |
| ansible-option-title             | and if false, RFC 3394(AES Key   |
| :::                              | Wrap) is followed for unwrapping |
| :::                              | the material for the symmetric   |
|                                  | key.                             |
| **padded**                       |                                  |
|                                  | If a certificate is being        |
| ```{=html}                       | unwrapped with the               |
| <a class="ansibleOptionLink      | \"wrappingMethod\" set to        |
| " href="#parameter-padded" title | \"encrypt\", the \"padded\"      |
| ="Permalink to this option"></a> | parameter has to be set to true. |
| ```                              |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-type-line         | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| [boolean]{.ansible-option-type}  | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| </div>                           | -   `false`{.interpreted-text    |
| ```                              |     role="ansibl                 |
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
| <div cl                          | ```                              |
| ass="ansibleOptionAnchor" id="pa | Date/time when a Managed         |
| rameter-processStartDate"></div> | Symmetric Key Object MAY begin   |
| ```                              | to be used to process            |
| :                                | cryptographically protected      |
| :: {#ansible_collections.thales. | information (e.g., decryption or |
| ciphertrust.vault_keys2_save_mod | unwrapping)                      |
| ule__parameter-processstartdate} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **processStartDate**             |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cl                            |                                  |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-processStartDate" title |                                  |
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
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | Date/time after which a Managed  |
| arameter-protectStopDate"></div> | Symmetric Key Object SHALL NOT   |
| ```                              | be used for applying             |
| ::: {#ansible_collections.thales | cryptographic protection (e.g.,  |
| .ciphertrust.vault_keys2_save_mo | encryption or wrapping)          |
| dule__parameter-protectstopdate} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **protectStopDate**              |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a c                             |                                  |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-protectStopDate" title |                                  |
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
| <div class                       | ```                              |
| ="ansibleOptionAnchor" id="param | Information needed to create a   |
| eter-publicKeyParameters"></div> | public key                       |
| ```                              |                                  |
| :::                              | ```{=html}                       |
| {#ansible_collections.thales.cip | </div>                           |
| hertrust.vault_keys2_save_module | ```                              |
| __parameter-publickeyparameters} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **publicKeyParameters**          |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class                         |                                  |
| ="ansibleOptionLink" href="#para |                                  |
| meter-publicKeyParameters" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [list]{.ansible-option-type} /   |                                  |
| [elements=dicti                  |                                  |
| onary]{.ansible-option-elements} |                                  |
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
| Anchor" id="parameter-publicKeyP | Date/time the object becomes     |
| arameters/activationDate"></div> | active                           |
| ```                              |                                  |
| ::: {#ansible_colle              | ```{=html}                       |
| ctions.thales.ciphertrust.vault_ | </div>                           |
| keys2_save_module__parameter-pub | ```                              |
| lickeyparameters/activationdate} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **activationDate**               |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOption          |                                  |
| Link" href="#parameter-publicKey |                                  |
| Parameters/activationDate" title |                                  |
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
| <div class="ansibl               | ```                              |
| eOptionAnchor" id="parameter-pub | Aliases associated with the key. |
| licKeyParameters/aliases"></div> |                                  |
| ```                              | The alias and alias-type must be |
| ::: {#ansibl                     | specified.                       |
| e_collections.thales.ciphertrust |                                  |
| .vault_keys2_save_module__parame | The alias index is assigned by   |
| ter-publickeyparameters/aliases} | this operation, and need not be  |
| ::: {.rst-class}                 | specified.                       |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **aliases**                      |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibl                 |                                  |
| eOptionLink" href="#parameter-pu |                                  |
| blicKeyParameters/aliases" title |                                  |
| ="Permalink to this option"></a> |                                  |
| ```                              |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
| :::                              |                                  |
|                                  |                                  |
| [list]{.ansible-option-type} /   |                                  |
| [elements=dicti                  |                                  |
| onary]{.ansible-option-elements} |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOpt           | ```                              |
| ionAnchor" id="parameter-publicK | Date/time the object becomes     |
| eyParameters/archiveDate"></div> | archived                         |
| ```                              |                                  |
| ::: {#ansible_co                 | ```{=html}                       |
| llections.thales.ciphertrust.vau | </div>                           |
| lt_keys2_save_module__parameter- | ```                              |
| publickeyparameters/archivedate} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **archiveDate**                  |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOpt             |                                  |
| ionLink" href="#parameter-public |                                  |
| KeyParameters/archiveDate" title |                                  |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-publicKeyPar | Date/time the object becomes     |
| ameters/deactivationDate"></div> | inactive                         |
| ```                              |                                  |
| ::: {#ansible_collect            | ```{=html}                       |
| ions.thales.ciphertrust.vault_ke | </div>                           |
| ys2_save_module__parameter-publi | ```                              |
| ckeyparameters/deactivationdate} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **deactivationDate**             |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-publicKeyPa |                                  |
| rameters/deactivationDate" title |                                  |
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
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | Optional end-user or service     |
| publicKeyParameters/meta"></div> | data stored with the key         |
| ```                              |                                  |
| ::: {#ans                        | ```{=html}                       |
| ible_collections.thales.ciphertr | </div>                           |
| ust.vault_keys2_save_module__par | ```                              |
| ameter-publickeyparameters/meta} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **meta**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ans                    |                                  |
| ibleOptionLink" href="#parameter |                                  |
| -publicKeyParameters/meta" title |                                  |
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
| <div class="ans                  | ```                              |
| ibleOptionAnchor" id="parameter- | Optional friendly name, The key  |
| publicKeyParameters/name"></div> | name should not contain special  |
| ```                              | characters such as angular       |
| ::: {#ans                        | brackets (\<,\>) and backslash   |
| ible_collections.thales.ciphertr | ().                              |
| ust.vault_keys2_save_module__par |                                  |
| ameter-publickeyparameters/name} | ```{=html}                       |
| ::: {.rst-class}                 | </div>                           |
| ansible-option-title             | ```                              |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **name**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ans                    |                                  |
| ibleOptionLink" href="#parameter |                                  |
| -publicKeyParameters/name" title |                                  |
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
| <div class="ansi                 | ```                              |
| bleOptionAnchor" id="parameter-p | Optional initial key state       |
| ublicKeyParameters/state"></div> | (Pre-Active) upon creation.      |
| ```                              | Defaults to Active. If set,      |
| ::: {#ansi                       | activationDate and               |
| ble_collections.thales.ciphertru | processStartDate can not be      |
| st.vault_keys2_save_module__para | specified during key creation.   |
| meter-publickeyparameters/state} | In case of import, allowed       |
| ::: {.rst-class}                 | values are \"Pre-Active\",       |
| ansible-option-title             | \"Active\", \"Deactivated\",     |
| :::                              | \"Destroyed\", \"Compromised\"   |
| :::                              | and \"Destroyed Compromised\".   |
|                                  | If key material is not           |
| **state**                        | specified, it will not be        |
|                                  | autogenerated if input           |
| ```{=html}                       | parameters correspond to either  |
| <a class="ansi                   | of these states -                |
| bleOptionLink" href="#parameter- | \"Deactivated\", \"Destroyed\",  |
| publicKeyParameters/state" title | \"Compromised\" and \"Destroyed  |
| ="Permalink to this option"></a> | Compromised\". Key in            |
| ```                              | \"Destroyed\" or \"Destroyed     |
| ::: {.rst-class}                 | Compromised\" state would not    |
| ansible-option-type-line         | have key material even if        |
| :::                              | specified during key creation.   |
|                                  |                                  |
| [string]{.ansible-option-type}   | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOpt           | ```                              |
| ionAnchor" id="parameter-publicK | Key is not deletable. Defaults   |
| eyParameters/undeletable"></div> | to false.                        |
| ```                              |                                  |
| ::: {#ansible_co                 | ::: {.rst-class}                 |
| llections.thales.ciphertrust.vau | ansible-option-line              |
| lt_keys2_save_module__parameter- | :::                              |
| publickeyparameters/undeletable} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
| **undeletable**                  | e-option-choices-entry-default"} |
|                                  |     [←                           |
| ```{=html}                       |     (default)]{.ansi             |
| <a class="ansibleOpt             | ble-option-choices-default-mark} |
| ionLink" href="#parameter-public | -   `true`{.interpreted-text     |
| KeyParameters/undeletable" title |     role                         |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOpti          | ```                              |
| onAnchor" id="parameter-publicKe | Key is not exportable. Defaults  |
| yParameters/unexportable"></div> | to false.                        |
| ```                              |                                  |
| ::: {#ansible_col                | ::: {.rst-class}                 |
| lections.thales.ciphertrust.vaul | ansible-option-line              |
| t_keys2_save_module__parameter-p | :::                              |
| ublickeyparameters/unexportable} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `false`{.interpreted-text    |
|                                  |     role="ansibl                 |
| **unexportable**                 | e-option-choices-entry-default"} |
|                                  |     [←                           |
| ```{=html}                       |     (default)]{.ansi             |
| <a class="ansibleOpti            | ble-option-choices-default-mark} |
| onLink" href="#parameter-publicK | -   `true`{.interpreted-text     |
| eyParameters/unexportable" title |     role                         |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOp            | ```                              |
| tionAnchor" id="parameter-public | Cryptographic usage mask. Add    |
| KeyParameters/usageMaske"></div> | the usage masks to allow certain |
| ```                              | usages. Sign (1), Verify (2),    |
| ::: {#ansible_c                  | Encrypt (4), Decrypt (8), Wrap   |
| ollections.thales.ciphertrust.va | Key (16), Unwrap Key (32),       |
| ult_keys2_save_module__parameter | Export (64), MAC Generate (128), |
| -publickeyparameters/usagemaske} | MAC Verify (256), Derive Key     |
| ::: {.rst-class}                 | (512), Content Commitment        |
| ansible-option-title             | (1024), Key Agreement (2048),    |
| :::                              | Certificate Sign (4096), CRL     |
| :::                              | Sign (8192), Generate Cryptogram |
|                                  | (16384), Validate Cryptogram     |
| **usageMaske**                   | (32768), Translate Encrypt       |
|                                  | (65536), Translate Decrypt       |
| ```{=html}                       | (131072), Translate Wrap         |
| <a class="ansibleOp              | (262144), Translate Unwrap       |
| tionLink" href="#parameter-publi | (524288), FPE Encrypt (1048576), |
| cKeyParameters/usageMaske" title | FPE Decrypt (2097152). Add the   |
| ="Permalink to this option"></a> | usage mask values to allow the   |
| ```                              | usages. To set all usage mask    |
| ::: {.rst-class}                 | bits, use 4194303. Equivalent    |
| ansible-option-type-line         | usageMask values for deprecated  |
| :::                              | usages \'fpe\' (FPE Encrypt +    |
|                                  | FPE Decrypt = 3145728), \'blob\' |
| [integer]{.ansible-option-type}  | (Encrypt + Decrypt = 12),        |
|                                  | \'hmac\' (MAC Generate + MAC     |
| ```{=html}                       | Verify = 384), \'encrypt\'       |
| </div>                           | (Encrypt + Decrypt = 12),        |
| ```                              | \'sign\' (Sign + Verify = 3),    |
|                                  | \'any\' (4194303 - all usage     |
|                                  | masks).                          |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | Message explaining revocation.   |
| ameter-revocationMessage"></div> |                                  |
| ```                              | ```{=html}                       |
| ::                               | </div>                           |
| : {#ansible_collections.thales.c | ```                              |
| iphertrust.vault_keys2_save_modu |                                  |
| le__parameter-revocationmessage} |                                  |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **revocationMessage**            |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a cla                           |                                  |
| ss="ansibleOptionLink" href="#pa |                                  |
| rameter-revocationMessage" title |                                  |
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
| ass="ansibleOptionAnchor" id="pa | The reason the key is being      |
| rameter-revocationReason"></div> | revoked.                         |
| ```                              |                                  |
| :                                | ::: {.rst-class}                 |
| :: {#ansible_collections.thales. | ansible-option-line              |
| ciphertrust.vault_keys2_save_mod | :::                              |
| ule__parameter-revocationreason} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `                            |
|                                  | "Unspecified"`{.interpreted-text |
| **revocationReason**             |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -   `"K                          |
| <a cl                            | eyCompromise"`{.interpreted-text |
| ass="ansibleOptionLink" href="#p |     role                         |
| arameter-revocationReason" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -   `"                           |
| ```                              | CACompromise"`{.interpreted-text |
| ::: {.rst-class}                 |     role                         |
| ansible-option-type-line         | ="ansible-option-choices-entry"} |
| :::                              | -   `"Affili                     |
|                                  | ationChanged"`{.interpreted-text |
| [string]{.ansible-option-type}   |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| ```{=html}                       | -                                |
| </div>                           | `"Superseded"`{.interpreted-text |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"Cessatio                   |
|                                  | nOfOperation"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"Privil                     |
|                                  | egeWithdrawn"`{.interpreted-text |
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
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Number of days from current date |
| er-rotationFrequencyDays"></div> | to rotate the key. It should be  |
| ```                              | greater than or equal to 0.      |
| ::: {#                           | Default is an empty string. If   |
| ansible_collections.thales.ciphe | set to 0, rotationFrequencyDays  |
| rtrust.vault_keys2_save_module__ | set to an empty string and auto  |
| parameter-rotationfrequencydays} | rotation of key will be          |
| ::: {.rst-class}                 | disabled.                        |
| ansible-option-title             |                                  |
| :::                              | ```{=html}                       |
| :::                              | </div>                           |
|                                  | ```                              |
| **rotationFrequencyDays**        |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="                       |                                  |
| ansibleOptionLink" href="#parame |                                  |
| ter-rotationFrequencyDays" title |                                  |
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
| <div clas                        | ```                              |
| s="ansibleOptionAnchor" id="para | For pkcs12 format, this field    |
| meter-secretDataEncoding"></div> | specifies the encoding method    |
| ```                              | used for the secretDataLink      |
| :::                              | material. Ignore this field if   |
|  {#ansible_collections.thales.ci | secretData is created from REST  |
| phertrust.vault_keys2_save_modul | and is in plain format. Specify  |
| e__parameter-secretdataencoding} | the value of this field as HEX   |
| ::: {.rst-class}                 | format if secretData is created  |
| ansible-option-title             | from KMIP.                       |
| :::                              |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| **secretDataEncoding**           | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a clas                          |                                  |
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
| ::: {#ansible_collections.thale  | can be either ID or name of      |
| s.ciphertrust.vault_keys2_save_m | Secret Data.                     |
| odule__parameter-secretdatalink} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **secretDataLink**               |                                  |
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
| ::: {#ansible_collections.th     | verification of the              |
| ales.ciphertrust.vault_keys2_sav | \"macSignBytes\" during import   |
| e_module__parameter-signingalgo} | of key material. The             |
| ::: {.rst-class}                 | \"wrappingMethod\" should be     |
| ansible-option-title             | \"mac/sign\" to verify the       |
| :::                              | signature(\"macSignBytes\") of   |
| :::                              | the key material(\"material\").  |
|                                  |                                  |
| **signingAlgo**                  | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| ```{=html}                       | :::                              |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-signingAlgo" title | [Ch                              |
| ="Permalink to this option"></a> | oices:]{.ansible-option-choices} |
| ```                              |                                  |
| ::: {.rst-class}                 | -   `"RSA"`{.interpreted-text    |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -                                |
| [string]{.ansible-option-type}   |    `"RSA-PSS"`{.interpreted-text |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           |                                  |
| ```                              | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-size"></div> | Bit length for the key.          |
| ```                              |                                  |
| ::: {#ansible_collect            | ```{=html}                       |
| ions.thales.ciphertrust.vault_ke | </div>                           |
| ys2_save_module__parameter-size} | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **size**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-size" title |                                  |
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
| <div class="ansibleOptionAnc     | ```                              |
| hor" id="parameter-state"></div> | Optional initial key state       |
| ```                              | (Pre-Active) upon creation.      |
| ::: {#ansible_collecti           | Defaults to Active. If set,      |
| ons.thales.ciphertrust.vault_key | activationDate and               |
| s2_save_module__parameter-state} | processStartDate can not be      |
| ::: {.rst-class}                 | specified during key creation.   |
| ansible-option-title             | In case of import, allowed       |
| :::                              | values are \"Pre-Active\",       |
| :::                              | \"Active\", \"Deactivated\",     |
|                                  | \"Destroyed\", \"Compromised\"   |
| **state**                        | and \"Destroyed Compromised\".   |
|                                  | If key material is not           |
| ```{=html}                       | specified, it will not be        |
| <a class="ansibleOptionLin       | autogenerated if input           |
| k" href="#parameter-state" title | parameters correspond to either  |
| ="Permalink to this option"></a> | of these states -                |
| ```                              | \"Deactivated\", \"Destroyed\",  |
| ::: {.rst-class}                 | \"Compromised\" and \"Destroyed  |
| ansible-option-type-line         | Compromised\". Key in            |
| :::                              | \"Destroyed\" or \"Destroyed     |
|                                  | Compromised\" state would not    |
| [string]{.ansible-option-type}   | have key material even if        |
|                                  | specified during key creation.   |
| ```{=html}                       |                                  |
| </div>                           | ```{=html}                       |
| ```                              | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | Key is not deletable. Defaults   |
| d="parameter-undeletable"></div> | to false.                        |
| ```                              |                                  |
| ::: {#ansible_collections.th     | ::: {.rst-class}                 |
| ales.ciphertrust.vault_keys2_sav | ansible-option-line              |
| e_module__parameter-undeletable} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `false`{.interpreted-text    |
| **undeletable**                  |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| ```{=html}                       |     [←                           |
| <a class="ansibleOptionLink" hre |     (default)]{.ansi             |
| f="#parameter-undeletable" title | ble-option-choices-default-mark} |
| ="Permalink to this option"></a> | -   `true`{.interpreted-text     |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| [boolean]{.ansible-option-type}  | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | Key is not exportable. Defaults  |
| ="parameter-unexportable"></div> | to false.                        |
| ```                              |                                  |
| ::: {#ansible_collections.tha    | ::: {.rst-class}                 |
| les.ciphertrust.vault_keys2_save | ansible-option-line              |
| _module__parameter-unexportable} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `false`{.interpreted-text    |
| **unexportable**                 |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| ```{=html}                       |     [←                           |
| <                                |     (default)]{.ansi             |
| a class="ansibleOptionLink" href | ble-option-choices-default-mark} |
| ="#parameter-unexportable" title | -   `true`{.interpreted-text     |
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
| <                                | ```                              |
| div class="ansibleOptionAnchor"  | Cryptographic usage mask. Add    |
| id="parameter-usageMaske"></div> | the usage masks to allow certain |
| ```                              | usages. Sign (1), Verify (2),    |
| ::: {#ansible_collections.t      | Encrypt (4), Decrypt (8), Wrap   |
| hales.ciphertrust.vault_keys2_sa | Key (16), Unwrap Key (32),       |
| ve_module__parameter-usagemaske} | Export (64), MAC Generate (128), |
| ::: {.rst-class}                 | MAC Verify (256), Derive Key     |
| ansible-option-title             | (512), Content Commitment        |
| :::                              | (1024), Key Agreement (2048),    |
| :::                              | Certificate Sign (4096), CRL     |
|                                  | Sign (8192), Generate Cryptogram |
| **usageMaske**                   | (16384), Validate Cryptogram     |
|                                  | (32768), Translate Encrypt       |
| ```{=html}                       | (65536), Translate Decrypt       |
| <a class="ansibleOptionLink" hr  | (131072), Translate Wrap         |
| ef="#parameter-usageMaske" title | (262144), Translate Unwrap       |
| ="Permalink to this option"></a> | (524288), FPE Encrypt (1048576), |
| ```                              | FPE Decrypt (2097152). Add the   |
| ::: {.rst-class}                 | usage mask values to allow the   |
| ansible-option-type-line         | usages. To set all usage mask    |
| :::                              | bits, use 4194303. Equivalent    |
|                                  | usageMask values for deprecated  |
| [integer]{.ansible-option-type}  | usages \'fpe\' (FPE Encrypt +    |
|                                  | FPE Decrypt = 3145728), \'blob\' |
| ```{=html}                       | (Encrypt + Decrypt = 12),        |
| </div>                           | \'hmac\' (MAC Generate + MAC     |
| ```                              | Verify = 384), \'encrypt\'       |
|                                  | (Encrypt + Decrypt = 12),        |
|                                  | \'sign\' (Sign + Verify = 3),    |
|                                  | \'any\' (4194303 - all usage     |
|                                  | masks).                          |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-uuid"></div> | Additional identifier of the     |
| ```                              | key. The format of this value is |
| ::: {#ansible_collect            | 32 hexadecimal lowercase digits  |
| ions.thales.ciphertrust.vault_ke | with 4 dashes. This is optional  |
| ys2_save_module__parameter-uuid} | and applicable for import key    |
| ::: {.rst-class}                 | only. If set, the value is       |
| ansible-option-title             | imported as the key\'s uuid. If  |
| :::                              | not set, new key uuid is         |
| :::                              | generated on the server.         |
|                                  |                                  |
| **uuid**                         | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-uuid" title |                                  |
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
| " id="parameter-wrapHKDF"></div> | Information which is used to     |
| ```                              | wrap a Key using HKDF.           |
| ::: {#ansible_collections        |                                  |
| .thales.ciphertrust.vault_keys2_ | ```{=html}                       |
| save_module__parameter-wraphkdf} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
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
| ::: {#a                          | ::: {.rst-class}                 |
| nsible_collections.thales.cipher | ansible-option-line              |
| trust.vault_keys2_save_module__p | :::                              |
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
| ::: {#ansible_collections.thal   | ```{=html}                       |
| es.ciphertrust.vault_keys2_save_ | </div>                           |
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
| ::: {#ansible_collections.thales | ```{=html}                       |
| .ciphertrust.vault_keys2_save_mo | </div>                           |
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
| ::: {#ansible_collections.thal   | ```{=html}                       |
| es.ciphertrust.vault_keys2_save_ | </div>                           |
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
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | IDType specifies how the         |
| "parameter-wrapKeyIDType"></div> | wrapKeyName should be            |
| ```                              | interpreted.                     |
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.vault_keys2_save_ | ::: {.rst-class}                 |
| module__parameter-wrapkeyidtype} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **wrapKeyIDType**                | -   `"name"`{.interpreted-text   |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a                               | -   `"id"`{.interpreted-text     |
|  class="ansibleOptionLink" href= |     role                         |
| "#parameter-wrapKeyIDType" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -   `"alias"`{.interpreted-text  |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| [string]{.ansible-option-type}   | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | While creating a new key, If     |
| d="parameter-wrapKeyName"></div> | \'includeMaterial\' is true,     |
| ```                              | then only the key material will  |
| ::: {#ansible_collections.th     | be wrapped with material of the  |
| ales.ciphertrust.vault_keys2_sav | specified key name. The response |
| e_module__parameter-wrapkeyname} | \"material\" property will be    |
| ::: {.rst-class}                 | the base64 encoded ciphertext.   |
| ansible-option-title             | For more details, view           |
| :::                              | \"wrapKeyName\" in export        |
| :::                              | parameters.                      |
|                                  |                                  |
| **wrapKeyName**                  | While importing a key, the key   |
|                                  | material will be unwrapped with  |
| ```{=html}                       | material of the specified key    |
| <a class="ansibleOptionLink" hre | name. The only applicable        |
| f="#parameter-wrapKeyName" title | \"wrappingMethod\" for the       |
| ="Permalink to this option"></a> | unwrapping is \"encrypt\" and    |
| ```                              | the wrapping key has to be an    |
| ::: {.rst-class}                 | AES key or an RSA private key.   |
| ansible-option-type-line         |                                  |
| :::                              | ```{=html}                       |
|                                  | </div>                           |
| [string]{.ansible-option-type}   | ```                              |
|                                  |                                  |
| ```{=html}                       |                                  |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-wrapPBE"></div> | WrapPBE produces a derived key   |
| ```                              | from a password and other        |
| ::: {#ansible_collection         | parameters like salt, iteration  |
| s.thales.ciphertrust.vault_keys2 | count, hashing algorithm and     |
| _save_module__parameter-wrappbe} | derived key length. PBE is       |
| ::: {.rst-class}                 | currently only supported to wrap |
| ansible-option-title             | symmetric keys (AES), private    |
| :::                              | Keys and certificates.           |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **wrapPBE**                      | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
|  href="#parameter-wrapPBE" title |                                  |
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
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.vault_keys2_save_ | ```{=html}                       |
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
| ::: {#                           | keys.                            |
| ansible_collections.thales.ciphe |                                  |
| rtrust.vault_keys2_save_module__ | ::: {.rst-class}                 |
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
| ::                               | range of 1 to 1,00,00,000.       |
| : {#ansible_collections.thales.c |                                  |
| iphertrust.vault_keys2_save_modu | ```{=html}                       |
| le__parameter-wrappbe/iteration} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
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
| :                                | passwordidentifier. password     |
| :: {#ansible_collections.thales. | must be in range of 8 bytes to   |
| ciphertrust.vault_keys2_save_mod | 128 bytes.                       |
| ule__parameter-wrappbe/password} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
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
| ::: {#ansib                      |                                  |
| le_collections.thales.ciphertrus | ```{=html}                       |
| t.vault_keys2_save_module__param | </div>                           |
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
| ::: {#ansible_c                  |                                  |
| ollections.thales.ciphertrust.va | ::: {.rst-class}                 |
| ult_keys2_save_module__parameter | ansible-option-line              |
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
| ::: {#ansible_collections.thales | greater than 128 bytes.          |
| .ciphertrust.vault_keys2_save_mo |                                  |
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
| ::: {#ansible_collections.tha    |                                  |
| les.ciphertrust.vault_keys2_save | ```{=html}                       |
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
| ::: {#a                          | Algorithm/Mode/Padding. For      |
| nsible_collections.thales.cipher | example AES/AESKEYWRAP. Here AES |
| trust.vault_keys2_save_module__p | is Algorithm, AESKEYWRAP is Mode |
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
| ="Permalink to this option"></a> | ::: {.rst-class}                 |
| ```                              | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-type-line         |                                  |
| :::                              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| [string]{.ansible-option-type}   |                                  |
|                                  | -   `"AE                         |
| ```{=html}                       | S/AESKEYWRAP"`{.interpreted-text |
| </div>                           |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
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
| :                                | to \"mac/sign\". In case of MAC  |
| :: {#ansible_collections.thales. | operation, the hashing algorithm |
| ciphertrust.vault_keys2_save_mod | used will be inferred from the   |
| ule__parameter-wrappinghashalgo} | type of HMAC                     |
| ::: {.rst-class}                 | key(\"macSignKeyIdentifier\").   |
| ansible-option-title             |                                  |
| :::                              | In case of SIGN operation, the   |
| :::                              | possible values are sha1,        |
|                                  | sha224, sha256, sha384 or sha512 |
| **wrappingHashAlgo**             |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a cl                            | ```                              |
| ass="ansibleOptionLink" href="#p |                                  |
| arameter-wrappingHashAlgo" title |                                  |
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
| class="ansibleOptionAnchor" id=" | This parameter specifies the     |
| parameter-wrappingMethod"></div> | wrapping method used to          |
| ```                              | wrap/mac/sign the key material.  |
| ::: {#ansible_collections.thale  |                                  |
| s.ciphertrust.vault_keys2_save_m | ::: {.rst-class}                 |
| odule__parameter-wrappingmethod} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **wrappingMethod**               | -                                |
|                                  |    `"encrypt"`{.interpreted-text |
| ```{=html}                       |     role                         |
| <a                               | ="ansible-option-choices-entry"} |
| class="ansibleOptionLink" href=" | -                                |
| #parameter-wrappingMethod" title |   `"mac/sign"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -   `"pbe"`{.interpreted-text    |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  |                                  |
| [string]{.ansible-option-type}   | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| </div>                           |                                  |
| ```                              |                                  |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div                             | ```                              |
|  class="ansibleOptionAnchor" id= | If the algorithm is              |
| "parameter-wrapPublicKey"></div> | \'aes\',\'tdes\',\'hmac-\*\',    |
| ```                              | \'seed\' or \'aria\', this value |
| ::: {#ansible_collections.thal   | will be used to encrypt the      |
| es.ciphertrust.vault_keys2_save_ | returned key material. This      |
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
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | WrapPublicKeyPadding specifies   |
| ter-wrapPublicKeyPadding"></div> | the type of padding scheme that  |
| ```                              | needs to be set when importing   |
| ::: {                            | the Key using the specified      |
| #ansible_collections.thales.ciph | wrapkey. Accepted values are     |
| ertrust.vault_keys2_save_module_ | \"pkcs1\", \"oaep\",             |
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
| [string]{.ansible-option-type}   | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| ```{=html}                       | :::                              |
| </div>                           |                                  |
| ```                              | [Ch                              |
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
| ::: {#ansible_collections.t      | method internally requires AES   |
| hales.ciphertrust.vault_keys2_sa | key size to generate a temporary |
| ve_module__parameter-wraprsaaes} | AES key and RSA padding. To use  |
| ::: {.rst-class}                 | WrapRSAAES, algorithm            |
| ansible-option-title             | \"RSA/RSAAESKEYWRAPPADDING\"     |
| :::                              | must be specified in             |
| :::                              | WrappingEncryptionAlgo.          |
|                                  |                                  |
| **wrapRSAAES**                   | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ansibleOptionLink" hr  |                                  |
| ef="#parameter-wrapRSAAES" title |                                  |
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
| <div class="                     | ```                              |
| ansibleOptionAnchor" id="paramet | Size of AES key for RSA AES KWP. |
| er-wrapRSAAES/aesKeySize"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#                           | ansible-option-line              |
| ansible_collections.thales.ciphe | :::                              |
| rtrust.vault_keys2_save_module__ |                                  |
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
| :::                              | RSA AES wrap                     |
|  {#ansible_collections.thales.ci |                                  |
| phertrust.vault_keys2_save_modul | ::: {.rst-class}                 |
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
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionA       | ```                              |
| nchor" id="parameter-xts"></div> | If set to true, then key created |
| ```                              | will be XTS/CBC-CS1 Key.         |
| ::: {#ansible_collec             | Defaults to false. Key algorithm |
| tions.thales.ciphertrust.vault_k | must be \'AES\'.                 |
| eys2_save_module__parameter-xts} |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-title             | ansible-option-line              |
| :::                              | :::                              |
| :::                              |                                  |
|                                  | [Ch                              |
| **xts**                          | oices:]{.ansible-option-choices} |
|                                  |                                  |
| ```{=html}                       | -   `false`{.interpreted-text    |
| <a class="ansibleOptionL         |     role="ansibl                 |
| ink" href="#parameter-xts" title | e-option-choices-entry-default"} |
| ="Permalink to this option"></a> |     [←                           |
| ```                              |     (default)]{.ansi             |
| ::: {.rst-class}                 | ble-option-choices-default-mark} |
| ansible-option-type-line         | -   `true`{.interpreted-text     |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [boolean]{.ansible-option-type}  |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| </div>                           | ```                              |
| ```                              |                                  |
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
