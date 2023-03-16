orphan

:   

::: {#ansible_collections.thales.ciphertrust.interface_save_module}
:::

thales.ciphertrust.interface\_save module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
========================================================================================================================================

::: {.note}
::: {.title}
Note
:::

This module is part of the [thales.ciphertrust
collection](https://galaxy.ansible.com/thales/ciphertrust) (version
1.0.0).

To install it, use:
`ansible-galaxy collection install thales.ciphertrust`.

To use it in a playbook, specify: `thales.ciphertrust.interface_save`.
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
    CipherTrust Manager APIs, more specifically with interface
    management API

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
| class="ansibleOptionAnchor" id=" | Auto-generate a new server       |
| parameter-auto_gen_ca_id"></div> | certificate on server startup    |
| ```                              | using the identifier (URI) of a  |
| ::: {#ansible_collections.tha    | Local CA resource if the current |
| les.ciphertrust.interface_save_m | server certificate is issued by  |
| odule__parameter-auto_gen_ca_id} | a different Local CA.            |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | This is especially useful when a |
| :::                              | new node joins the cluster. In   |
| :::                              | this case, the existing data of  |
|                                  | the joining node is overwritten  |
| **auto\_gen\_ca\_id**            | by the data in the cluster. A    |
|                                  | new server certificate is        |
| ```{=html}                       | generated on the joining node    |
| <a                               | using the existing Local CA of   |
| class="ansibleOptionLink" href=" | the cluster.                     |
| #parameter-auto_gen_ca_id" title |                                  |
| ="Permalink to this option"></a> | Auto-generation of the server    |
| ```                              | certificate can be disabled by   |
| ::: {.rst-class}                 | setting auto\_gen\_ca\_id to an  |
| ansible-option-type-line         | empty string (\"\") to allow     |
| :::                              | full control over the server     |
|                                  | certificate.                     |
| [string]{.ansible-option-type}   |                                  |
|                                  | ::: {.rst-class}                 |
| ```{=html}                       | ansible-option-line              |
| </div>                           | :::                              |
| ```                              |                                  |
|                                  | [Default                         |
|                                  | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | Set auto registration to allow   |
| ameter-auto_registration"></div> | auto registration of KMIP        |
| ```                              | clients.                         |
| ::: {#ansible_collections.thales |                                  |
| .ciphertrust.interface_save_modu | ::: {.rst-class}                 |
| le__parameter-auto_registration} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **auto\_registration**           | -   `false`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a cla                           | -   `true`{.interpreted-text     |
| ss="ansibleOptionLink" href="#pa |     role                         |
| rameter-auto_registration" title | ="ansible-option-choices-entry"} |
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
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | Specifies how the user name is   |
| arameter-cert_user_field"></div> | extracted from the client        |
| ```                              | certificate.                     |
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.interface_save_mo | ::: {.rst-class}                 |
| dule__parameter-cert_user_field} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **cert\_user\_field**            | -   `"CN"`{.interpreted-text     |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a c                             | -   `"SN"`{.interpreted-text     |
| lass="ansibleOptionLink" href="# |     role                         |
| parameter-cert_user_field" title | ="ansible-option-choices-entry"} |
| ="Permalink to this option"></a> | -   `"E"`{.interpreted-text      |
| ```                              |     role                         |
| ::: {.rst-class}                 | ="ansible-option-choices-entry"} |
| ansible-option-type-line         | -   `"E\_ND"`{.interpreted-text  |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -   `"UID"`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| </div>                           | -   `"OU"`{.interpreted-text     |
| ```                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  |                                  |
|                                  | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
|                                  | :::                              |
|                                  |                                  |
|                                  | [Default                         |
|                                  | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | This flag is used to define the  |
| arameter-custom_uid_size"></div> | custom uid size of managed       |
| ```                              | object over the KMIP interface.  |
| ::: {#ansible_collections.thal   |                                  |
| es.ciphertrust.interface_save_mo | ```{=html}                       |
| dule__parameter-custom_uid_size} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **custom\_uid\_size**            |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a c                             |                                  |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-custom_uid_size" title |                                  |
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
|  class="ansibleOptionAnchor" id= | This flag specifies which        |
| "parameter-custom_uid_v2"></div> | version of custom uid feature is |
| ```                              | to be used for KMIP interface.   |
| ::: {#ansible_collections.th     | If it is set to true, new        |
| ales.ciphertrust.interface_save_ | implementation i.e. Custom uid   |
| module__parameter-custom_uid_v2} | version 2 will be used.          |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **custom\_uid\_v2**              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| ```{=html}                       |                                  |
| <a                               | -   `false`{.interpreted-text    |
|  class="ansibleOptionLink" href= |     role                         |
| "#parameter-custom_uid_v2" title | ="ansible-option-choices-entry"} |
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
| <div clas                        | ```                              |
| s="ansibleOptionAnchor" id="para | The default connection may be    |
| meter-default_connection"></div> | \"local\_account\" for local     |
| ```                              | authentication or the LDAP       |
| :                                | domain for LDAP authentication.  |
| :: {#ansible_collections.thales. | This value is applied when the   |
| ciphertrust.interface_save_modul | username does not embed the      |
| e__parameter-default_connection} | connection name (e.g. \"jdoe\"   |
| ::: {.rst-class}                 | effectively becomes              |
| ansible-option-title             | \"local\_account\|jdoe\"). This  |
| :::                              | value only applies to NAE only   |
| :::                              | and is ignored if set for web    |
|                                  | and KMIP interfaces.             |
| **default\_connection**          |                                  |
|                                  | ::: {.rst-class}                 |
| ```{=html}                       | ansible-option-line              |
| <a clas                          | :::                              |
| s="ansibleOptionLink" href="#par |                                  |
| ameter-default_connection" title | [Default                         |
| ="Permalink to this option"></a> | :]{.ansible-option-default-bold} |
| ```                              | `"none"`{.interpreted-text       |
| ::: {.rst-class}                 | role="ansible-option-default"}   |
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
| <di                              | ```                              |
| v class="ansibleOptionAnchor" id | Identifier of the interface to   |
| ="parameter-interface_id"></div> | be patched                       |
| ```                              |                                  |
| ::: {#ansible_collections.t      | ```{=html}                       |
| hales.ciphertrust.interface_save | </div>                           |
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
| <div                             | ```                              |
| class="ansibleOptionAnchor" id=" | This parameter is used to        |
| parameter-interface_type"></div> | identify the type of interface,  |
| ```                              | what service to run on the       |
| ::: {#ansible_collections.tha    | interface.                       |
| les.ciphertrust.interface_save_m |                                  |
| odule__parameter-interface_type} | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-title             | :::                              |
| :::                              |                                  |
| :::                              | [Ch                              |
|                                  | oices:]{.ansible-option-choices} |
| **interface\_type**              |                                  |
|                                  | -   `"web"`{.interpreted-text    |
| ```{=html}                       |     role                         |
| <a                               | ="ansible-option-choices-entry"} |
| class="ansibleOptionLink" href=" | -   `"kmip"`{.interpreted-text   |
| #parameter-interface_type" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              | -   `"nae"`{.interpreted-text    |
| ::: {.rst-class}                 |     role="ansibl                 |
| ansible-option-type-line         | e-option-choices-entry-default"} |
| :::                              |     [←                           |
|                                  |     (default)]{.ansi             |
| [string]{.ansible-option-type}   | ble-option-choices-default-mark} |
|                                  | -   `"snmp"`{.interpreted-text   |
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
| <div class="an                   | ```                              |
| sibleOptionAnchor" id="parameter | Enables hard delete of keys on   |
| -kmip_enable_hard_delete"></div> | KMIP Destroy operation, that is  |
| ```                              | both meta-data and material will |
| ::: {#                           | be removed from CipherTrust      |
| ansible_collections.thales.ciphe | Manager for the key being        |
| rtrust.interface_save_module__pa | deleted.                         |
| rameter-kmip_enable_hard_delete} |                                  |
| ::: {.rst-class}                 | By default, only key material is |
| ansible-option-title             | removed and meta-data is         |
| :::                              | preserved with the updated key   |
| :::                              | state.                           |
|                                  |                                  |
| **kmip\_enable\_hard\_delete**   | This setting applies only to     |
|                                  | KMIP interface.                  |
| ```{=html}                       |                                  |
| <a class="an                     | Should be set to 1 for enabling  |
| sibleOptionLink" href="#paramete | the feature or 0 for returning   |
| r-kmip_enable_hard_delete" title | to default behavior.             |
| ="Permalink to this option"></a> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-type-line         | :::                              |
| :::                              |                                  |
|                                  | [Ch                              |
| [integer]{.ansible-option-type}  | oices:]{.ansible-option-choices} |
|                                  |                                  |
| ```{=html}                       | -   `0`{.interpreted-text        |
| </div>                           |     role="ansibl                 |
| ```                              | e-option-choices-entry-default"} |
|                                  |     [←                           |
|                                  |     (default)]{.ansi             |
|                                  | ble-option-choices-default-mark} |
|                                  | -   `1`{.interpreted-text        |
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
| <div class="ansi                 | ```                              |
| bleOptionAnchor" id="parameter-l | Local CSR parameters for         |
| ocal_auto_gen_attributes"></div> | interface\'s certificate. These  |
| ```                              | are for the local node itself,   |
| ::: {#an                         | and they do not affect other     |
| sible_collections.thales.ciphert | nodes in the cluster. This gives |
| rust.interface_save_module__para | user a convenient way to supply  |
| meter-local_auto_gen_attributes} | custom fields for automatic      |
| ::: {.rst-class}                 | interface certification          |
| ansible-option-title             | generation. Without them, the    |
| :::                              | system defaults are used.        |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **local\_auto\_gen\_attributes** | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansi                   |                                  |
| bleOptionLink" href="#parameter- |                                  |
| local_auto_gen_attributes" title |                                  |
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
| OptionAnchor" id="parameter-loca | Common name                      |
| l_auto_gen_attributes/cn"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#ansib                      | ansible-option-line              |
| le_collections.thales.ciphertrus | :::                              |
| t.interface_save_module__paramet |                                  |
| er-local_auto_gen_attributes/cn} | [Default                         |
| ::: {.rst-class}                 | :]{.ansible-option-default-bold} |
| ansible-option-title             | `"none"`{.interpreted-text       |
| :::                              | role="ansible-option-default"}   |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **cn**                           | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansible                |                                  |
| OptionLink" href="#parameter-loc |                                  |
| al_auto_gen_attributes/cn" title |                                  |
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
| <div class="ansibleOptionA       | ```                              |
| nchor" id="parameter-local_auto_ | Subject Alternative Names (SAN)  |
| gen_attributes/dns_names"></div> | DNS names                        |
| ```                              |                                  |
| ::: {#ansible_coll               | ::: {.rst-class}                 |
| ections.thales.ciphertrust.inter | ansible-option-line              |
| face_save_module__parameter-loca | :::                              |
| l_auto_gen_attributes/dns_names} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **dns\_names**                   | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ansibleOptionL         |                                  |
| ink" href="#parameter-local_auto |                                  |
| _gen_attributes/dns_names" title |                                  |
| ="Permalink to this option"></a> |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-local_auto_gen_at | Subject Alternative Names (SAN)  |
| tributes/email_addresses"></div> | Email addresses                  |
| ```                              |                                  |
| ::: {#ansible_collection         | ::: {.rst-class}                 |
| s.thales.ciphertrust.interface_s | ansible-option-line              |
| ave_module__parameter-local_auto | :::                              |
| _gen_attributes/email_addresses} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **email\_addresses**             | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ansibleOptionLink" h   |                                  |
| ref="#parameter-local_auto_gen_a |                                  |
| ttributes/email_addresses" title |                                  |
| ="Permalink to this option"></a> |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-local_auto_gen | Subject Alternative Names (SAN)  |
| _attributes/ip_addresses"></div> | IP addresses                     |
| ```                              |                                  |
| ::: {#ansible_collect            | ::: {.rst-class}                 |
| ions.thales.ciphertrust.interfac | ansible-option-line              |
| e_save_module__parameter-local_a | :::                              |
| uto_gen_attributes/ip_addresses} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **ip\_addresses**                | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a class="ansibleOptionLink      |                                  |
| " href="#parameter-local_auto_ge |                                  |
| n_attributes/ip_addresses" title |                                  |
| ="Permalink to this option"></a> |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOpt           | ```                              |
| ionAnchor" id="parameter-local_a | Name fields like O, OU, L, ST, C |
| uto_gen_attributes/names"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#ansible_                   | ansible-option-line              |
| collections.thales.ciphertrust.i | :::                              |
| nterface_save_module__parameter- |                                  |
| local_auto_gen_attributes/names} | [Default                         |
| ::: {.rst-class}                 | :]{.ansible-option-default-bold} |
| ansible-option-title             | `[]`{.interpreted-text           |
| :::                              | role="ansible-option-default"}   |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **names**                        | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansibleOpt             |                                  |
| ionLink" href="#parameter-local_ |                                  |
| auto_gen_attributes/names" title |                                  |
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
| <div class="ansibleO             | ```                              |
| ptionAnchor" id="parameter-local | User ID                          |
| _auto_gen_attributes/uid"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#ansibl                     | ansible-option-line              |
| e_collections.thales.ciphertrust | :::                              |
| .interface_save_module__paramete |                                  |
| r-local_auto_gen_attributes/uid} | [Default                         |
| ::: {.rst-class}                 | :]{.ansible-option-default-bold} |
| ansible-option-title             | `"none"`{.interpreted-text       |
| :::                              | role="ansible-option-default"}   |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **uid**                          | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ansibleO               |                                  |
| ptionLink" href="#parameter-loca |                                  |
| l_auto_gen_attributes/uid" title |                                  |
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
| ::: {#ansible_collection         | communicate with an instance of  |
| s.thales.ciphertrust.interface_s | CipherTrust Manager (CM)         |
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
| :                                | </div>                           |
| :: {#ansible_collections.thales. | ```                              |
| ciphertrust.interface_save_modul |                                  |
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
| iphertrust.interface_save_module |                                  |
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
| hertrust.interface_save_module__ | :::                              |
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
| st.interface_save_module__parame | </div>                           |
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
| les.ciphertrust.interface_save_m | ```                              |
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
| s.ciphertrust.interface_save_mod | :::                              |
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
| <div class                       | ```                              |
| ="ansibleOptionAnchor" id="param | Maximum TLS version to be        |
| eter-maximum_tls_version"></div> | configured for NAE or KMIP       |
| ```                              | interface, default is latest     |
| ::                               | maximum supported protocol.      |
| : {#ansible_collections.thales.c |                                  |
| iphertrust.interface_save_module | ::: {.rst-class}                 |
| __parameter-maximum_tls_version} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **maximum\_tls\_version**        | -                                |
|                                  |  `"tls\_1\_0"`{.interpreted-text |
| ```{=html}                       |     role                         |
| <a class                         | ="ansible-option-choices-entry"} |
| ="ansibleOptionLink" href="#para | -                                |
| meter-maximum_tls_version" title |  `"tls\_1\_1"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -                                |
| ansible-option-type-line         |  `"tls\_1\_2"`{.interpreted-text |
| :::                              |     role                         |
|                                  | ="ansible-option-choices-entry"} |
| [string]{.ansible-option-type}   | -                                |
|                                  |  `"tls\_1\_3"`{.interpreted-text |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              |                                  |
|                                  | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
|                                  | :::                              |
|                                  |                                  |
|                                  | [Default                         |
|                                  | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
|                                  |                                  |
|                                  | ```{=html}                       |
|                                  | </div>                           |
|                                  | ```                              |
+----------------------------------+----------------------------------+
| ```{=html}                       | ```{=html}                       |
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-meta"></div> | Meta information related to      |
| ```                              | interface                        |
| ::: {#ansible_colle              |                                  |
| ctions.thales.ciphertrust.interf | ::: {.rst-class}                 |
| ace_save_module__parameter-meta} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| **meta**                         | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLi        | </div>                           |
| nk" href="#parameter-meta" title | ```                              |
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
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-meta/nae"></div> | Meta information related to NAE  |
| ```                              | interface                        |
| ::: {#ansible_collectio          |                                  |
| ns.thales.ciphertrust.interface_ | ```{=html}                       |
| save_module__parameter-meta/nae} | </div>                           |
| ::: {.rst-class}                 | ```                              |
| ansible-option-title             |                                  |
| :::                              |                                  |
| :::                              |                                  |
|                                  |                                  |
| **nae**                          |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink"     |                                  |
| href="#parameter-meta/nae" title |                                  |
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
| <div class="ansible              | <div class="ansible-option-in    |
| -option-indent"></div><div class | dent-desc"></div><div class="ans |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibl               | ```                              |
| eOptionAnchor" id="parameter-met | Flag for masking system groups   |
| a/nae/mask_system_groups"></div> | in NAE requests                  |
| ```                              |                                  |
| ::: {#ansi                       | ::: {.rst-class}                 |
| ble_collections.thales.ciphertru | ansible-option-line              |
| st.interface_save_module__parame | :::                              |
| ter-meta/nae/mask_system_groups} |                                  |
| ::: {.rst-class}                 | [Ch                              |
| ansible-option-title             | oices:]{.ansible-option-choices} |
| :::                              |                                  |
| :::                              | -   `false`{.interpreted-text    |
|                                  |     role                         |
| **mask\_system\_groups**         | ="ansible-option-choices-entry"} |
|                                  | -   `true`{.interpreted-text     |
| ```{=html}                       |     role                         |
| <a class="ansibl                 | ="ansible-option-choices-entry"} |
| eOptionLink" href="#parameter-me |                                  |
| ta/nae/mask_system_groups" title | ```{=html}                       |
| ="Permalink to this option"></a> | </div>                           |
| ```                              | ```                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-type-line         |                                  |
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
| <div class                       | ```                              |
| ="ansibleOptionAnchor" id="param | Minimum TLS version to be        |
| eter-minimum_tls_version"></div> | configured for NAE or KMIP       |
| ```                              | interface, default is v1.2       |
| ::                               | (tls\_1\_2).                     |
| : {#ansible_collections.thales.c |                                  |
| iphertrust.interface_save_module | ::: {.rst-class}                 |
| __parameter-minimum_tls_version} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **minimum\_tls\_version**        | -                                |
|                                  |  `"tls\_1\_0"`{.interpreted-text |
| ```{=html}                       |     role                         |
| <a class                         | ="ansible-option-choices-entry"} |
| ="ansibleOptionLink" href="#para | -                                |
| meter-minimum_tls_version" title |  `"tls\_1\_1"`{.interpreted-text |
| ="Permalink to this option"></a> |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
| ::: {.rst-class}                 | -                                |
| ansible-option-type-line         |  `"tls\_1\_2"`{.interpreted-text |
| :::                              |     role="ansibl                 |
|                                  | e-option-choices-entry-default"} |
| [string]{.ansible-option-type}   |     [←                           |
|                                  |     (default)]{.ansi             |
| ```{=html}                       | ble-option-choices-default-mark} |
| </div>                           | -                                |
| ```                              |  `"tls\_1\_3"`{.interpreted-text |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-mode"></div> | The interface mode can be one of |
| ```                              | no-tls-pw-opt, no-tls-pw-req,    |
| ::: {#ansible_colle              | unauth-tls-pw-opt,               |
| ctions.thales.ciphertrust.interf | tls-cert-opt-pw-opt, tls-pw-opt, |
| ace_save_module__parameter-mode} | tls-pw-req, tls-cert-pw-opt, or  |
| ::: {.rst-class}                 | tls-cert-and-pw. Default mode is |
| ansible-option-title             | no-tls-pw-opt.                   |
| :::                              |                                  |
| :::                              | ::: {.rst-class}                 |
|                                  | ansible-option-line              |
| **mode**                         | :::                              |
|                                  |                                  |
| ```{=html}                       | [Ch                              |
| <a class="ansibleOptionLi        | oices:]{.ansible-option-choices} |
| nk" href="#parameter-mode" title |                                  |
| ="Permalink to this option"></a> | -   `"n                          |
| ```                              | o-tls-pw-opt"`{.interpreted-text |
| ::: {.rst-class}                 |     role="ansibl                 |
| ansible-option-type-line         | e-option-choices-entry-default"} |
| :::                              |     [←                           |
|                                  |     (default)]{.ansi             |
| [string]{.ansible-option-type}   | ble-option-choices-default-mark} |
|                                  | -   `"n                          |
| ```{=html}                       | o-tls-pw-req"`{.interpreted-text |
| </div>                           |     role                         |
| ```                              | ="ansible-option-choices-entry"} |
|                                  | -   `"unaut                      |
|                                  | h-tls-pw-opt"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"tls-cer                    |
|                                  | t-opt-pw-opt"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  | `"tls-pw-opt"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -                                |
|                                  | `"tls-pw-req"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"tls                        |
|                                  | -cert-pw-opt"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"tls                        |
|                                  | -cert-and-pw"`{.interpreted-text |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-name"></div> | The name of the interface. Not   |
| ```                              | valid for interface\_type nae.   |
| ::: {#ansible_colle              |                                  |
| ctions.thales.ciphertrust.interf | ::: {.rst-class}                 |
| ace_save_module__parameter-name} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| **name**                         | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLi        | </div>                           |
| nk" href="#parameter-name" title | ```                              |
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
| ss="ansibleOptionAnchor" id="par | Defines what ethernet adapter    |
| ameter-network_interface"></div> | the interface should listen to,  |
| ```                              | use \"all\" for all.             |
| ::: {#ansible_collections.thales |                                  |
| .ciphertrust.interface_save_modu | ::: {.rst-class}                 |
| le__parameter-network_interface} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| **network\_interface**           | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a cla                           | </div>                           |
| ss="ansibleOptionLink" href="#pa | ```                              |
| rameter-network_interface" title |                                  |
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
| ons.thales.ciphertrust.interface | ansible-option-line              |
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
| <div class="ansibleOptionAn      | ```                              |
| chor" id="parameter-port"></div> | The new interface will listen on |
| ```                              | the specified port. The port     |
| ::: {#ansible_colle              | number should not be negative, 0 |
| ctions.thales.ciphertrust.interf | or the one already in-use.       |
| ace_save_module__parameter-port} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **port**                         |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLi        |                                  |
| nk" href="#parameter-port" title |                                  |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div clas                        | ```                              |
| s="ansibleOptionAnchor" id="para | Registration token in case auto  |
| meter-registration_token"></div> | registration is true.            |
| ```                              |                                  |
| :                                | ::: {.rst-class}                 |
| :: {#ansible_collections.thales. | ansible-option-line              |
| ciphertrust.interface_save_modul | :::                              |
| e__parameter-registration_token} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `"none"`{.interpreted-text       |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **registration\_token**          | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a clas                          |                                  |
| s="ansibleOptionLink" href="#par |                                  |
| ameter-registration_token" title |                                  |
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
| iv class="ansibleOptionAnchor" i | TLS Ciphers contain the list of  |
| d="parameter-tls_ciphers"></div> | cipher suites available in the   |
| ```                              | system for the respective        |
| ::: {#ansible_collections.       | interfaces (KMIP, NAE & WEB) for |
| thales.ciphertrust.interface_sav | TLS handshake.                   |
| e_module__parameter-tls_ciphers} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **tls\_ciphers**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-tls_ciphers" title |                                  |
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
| ibleOptionAnchor" id="parameter- | TLS cipher suite name.           |
| tls_ciphers/cipher_suite"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#a                          | ansible-option-line              |
| nsible_collections.thales.cipher | :::                              |
| trust.interface_save_module__par |                                  |
| ameter-tls_ciphers/cipher_suite} | [Default                         |
| ::: {.rst-class}                 | :]{.ansible-option-default-bold} |
| ansible-option-title             | `"none"`{.interpreted-text       |
| :::                              | role="ansible-option-default"}   |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **cipher\_suite**                | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class="ans                    |                                  |
| ibleOptionLink" href="#parameter |                                  |
| -tls_ciphers/cipher_suite" title |                                  |
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
| ="ansibleOptionAnchor" id="param | TLS cipher suite enabled flag.   |
| eter-tls_ciphers/enabled"></div> | If set to true, cipher suite     |
| ```                              | will be available for TLS        |
| ::                               | handshake.                       |
| : {#ansible_collections.thales.c |                                  |
| iphertrust.interface_save_module | ::: {.rst-class}                 |
| __parameter-tls_ciphers/enabled} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
|                                  |                                  |
| **enabled**                      | -   `false`{.interpreted-text    |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class                         | -   `true`{.interpreted-text     |
| ="ansibleOptionLink" href="#para |     role                         |
| meter-tls_ciphers/enabled" title | ="ansible-option-choices-entry"} |
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
| iv class="ansibleOptionAnchor" i | Collection of local and external |
| d="parameter-trusted_cas"></div> | CA IDs to trust for client       |
| ```                              | authentication. See section      |
| ::: {#ansible_collections.       | \"Certificate Authority\" for    |
| thales.ciphertrust.interface_sav | more details.                    |
| e_module__parameter-trusted_cas} |                                  |
| ::: {.rst-class}                 | ```{=html}                       |
| ansible-option-title             | </div>                           |
| :::                              | ```                              |
| :::                              |                                  |
|                                  |                                  |
| **trusted\_cas**                 |                                  |
|                                  |                                  |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre |                                  |
| f="#parameter-trusted_cas" title |                                  |
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
| <div class=                      | ```                              |
| "ansibleOptionAnchor" id="parame | A list of External CA IDs        |
| ter-trusted_cas/external"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
|  {#ansible_collections.thales.ci | :::                              |
| phertrust.interface_save_module_ |                                  |
| _parameter-trusted_cas/external} | [Default                         |
| ::: {.rst-class}                 | :]{.ansible-option-default-bold} |
| ansible-option-title             | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
| :::                              |                                  |
|                                  | ```{=html}                       |
| **external**                     | </div>                           |
|                                  | ```                              |
| ```{=html}                       |                                  |
| <a class=                        |                                  |
| "ansibleOptionLink" href="#param |                                  |
| eter-trusted_cas/external" title |                                  |
| ="Permalink to this option"></a> |                                  |
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
| <div class                       | <div class="ans                  |
| ="ansible-option-indent"></div>< | ible-option-indent-desc"></div>< |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div cla                         | ```                              |
| ss="ansibleOptionAnchor" id="par | A list of Local CA IDs           |
| ameter-trusted_cas/local"></div> |                                  |
| ```                              | ::: {.rst-class}                 |
| ::: {#ansible_collections.thales | ansible-option-line              |
| .ciphertrust.interface_save_modu | :::                              |
| le__parameter-trusted_cas/local} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **local**                        | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a cla                           |                                  |
| ss="ansibleOptionLink" href="#pa |                                  |
| rameter-trusted_cas/local" title |                                  |
| ="Permalink to this option"></a> |                                  |
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

Examples
--------

``` {.yaml+jinja}
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
