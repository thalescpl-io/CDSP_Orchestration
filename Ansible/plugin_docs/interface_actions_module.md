orphan

:   

::: {#ansible_collections.thales.ciphertrust.interface_actions_module}
:::

thales.ciphertrust.interface\_actions module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
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

To use it in a playbook, specify:
`thales.ciphertrust.interface_actions`.
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
    CipherTrust Manager APIs, more specifically with interface actions
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
| <d                               | ```                              |
| iv class="ansibleOptionAnchor" i | The certificate and key data in  |
| d="parameter-certificate"></div> | PEM format or base64 encoded     |
| ```                              | PKCS12 format. A chain chain of  |
| ::: {#ansible_collections.tha    | certs may be included - it must  |
| les.ciphertrust.interface_action | be in ascending order (server to |
| s_module__parameter-certificate} | root ca).                        |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | required if op\_type is          |
| :::                              | put\_certificate                 |
| :::                              |                                  |
|                                  | ::: {.rst-class}                 |
| **certificate**                  | ansible-option-line              |
|                                  | :::                              |
| ```{=html}                       |                                  |
| <a class="ansibleOptionLink" hre | [Default                         |
| f="#parameter-certificate" title | :]{.ansible-option-default-bold} |
| ="Permalink to this option"></a> | `"none"`{.interpreted-text       |
| ```                              | role="ansible-option-default"}   |
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
| <div class="ansibleOption        | ```                              |
| Anchor" id="parameter-cn"></div> | Common name                      |
| ```                              |                                  |
| ::: {#ansible_collec             | required if op\_type is csr      |
| tions.thales.ciphertrust.interfa |                                  |
| ce_actions_module__parameter-cn} | ::: {.rst-class}                 |
| ::: {.rst-class}                 | ansible-option-line              |
| ansible-option-title             | :::                              |
| :::                              |                                  |
| :::                              | [Default                         |
|                                  | :]{.ansible-option-default-bold} |
| **cn**                           | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
| ```{=html}                       |                                  |
| <a class="ansibleOption          | ```{=html}                       |
| Link" href="#parameter-cn" title | </div>                           |
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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-copy_from"></div> | Source interface name            |
| ```                              |                                  |
| ::: {#ansible_collections.t      | required if op\_type is          |
| hales.ciphertrust.interface_acti | use-certificate                  |
| ons_module__parameter-copy_from} |                                  |
| ::: {.rst-class}                 | ::: {.rst-class}                 |
| ansible-option-title             | ansible-option-line              |
| :::                              | :::                              |
| :::                              |                                  |
|                                  | [Default                         |
| **copy\_from**                   | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| ```{=html}                       | role="ansible-option-default"}   |
| <a class="ansibleOptionLink" h   |                                  |
| ref="#parameter-copy_from" title | ```{=html}                       |
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
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-dns_names"></div> | Subject Alternative Names (SAN)  |
| ```                              | DNS names                        |
| ::: {#ansible_collections.t      |                                  |
| hales.ciphertrust.interface_acti | ::: {.rst-class}                 |
| ons_module__parameter-dns_names} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `["none"]`{.interpreted-text     |
| **dns\_names**                   | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLink" h   | </div>                           |
| ref="#parameter-dns_names" title | ```                              |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div c                           | ```                              |
| lass="ansibleOptionAnchor" id="p | Subject Alternative Names (SAN)  |
| arameter-email_addresses"></div> | Email addresses                  |
| ```                              |                                  |
| :                                | ::: {.rst-class}                 |
| :: {#ansible_collections.thales. | ansible-option-line              |
| ciphertrust.interface_actions_mo | :::                              |
| dule__parameter-email_addresses} |                                  |
| ::: {.rst-class}                 | [Default                         |
| ansible-option-title             | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
| :::                              | role="ansible-option-default"}   |
|                                  |                                  |
| **email\_addresses**             | ```{=html}                       |
|                                  | </div>                           |
| ```{=html}                       | ```                              |
| <a c                             |                                  |
| lass="ansibleOptionLink" href="# |                                  |
| parameter-email_addresses" title |                                  |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnch    | ```                              |
| or" id="parameter-format"></div> | The format of the certificate    |
| ```                              | data (PEM or PKCS12).            |
| ::: {#ansible_collection         |                                  |
| s.thales.ciphertrust.interface_a | required if op\_type is          |
| ctions_module__parameter-format} | put\_certificate                 |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | ::: {.rst-class}                 |
| :::                              | ansible-option-line              |
| :::                              | :::                              |
|                                  |                                  |
| **format**                       | [Default                         |
|                                  | :]{.ansible-option-default-bold} |
| ```{=html}                       | `"none"`{.interpreted-text       |
| <a class="ansibleOptionLink      | role="ansible-option-default"}   |
| " href="#parameter-format" title |                                  |
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
| <div class="ansibleOptionAnchor  | ```                              |
| " id="parameter-generate"></div> | Create a new self-signed         |
| ```                              | certificate                      |
| ::: {#ansible_collections.       |                                  |
| thales.ciphertrust.interface_act | ::: {.rst-class}                 |
| ions_module__parameter-generate} | ansible-option-line              |
| ::: {.rst-class}                 | :::                              |
| ansible-option-title             |                                  |
| :::                              | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
|                                  | `"none"`{.interpreted-text       |
| **generate**                     | role="ansible-option-default"}   |
|                                  |                                  |
| ```{=html}                       | ```{=html}                       |
| <a class="ansibleOptionLink"     | </div>                           |
| href="#parameter-generate" title | ```                              |
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
| v class="ansibleOptionAnchor" id | Identifier of the interface to   |
| ="parameter-interface_id"></div> | be updated                       |
| ```                              |                                  |
| ::: {#ansible_collections.thal   | ```{=html}                       |
| es.ciphertrust.interface_actions | </div>                           |
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
| v class="ansibleOptionAnchor" id | Subject Alternative Names (SAN)  |
| ="parameter-ip_addresses"></div> | IP addresses                     |
| ```                              |                                  |
| ::: {#ansible_collections.thal   | ::: {.rst-class}                 |
| es.ciphertrust.interface_actions | ansible-option-line              |
| _module__parameter-ip_addresses} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
| :::                              | `["none"]`{.interpreted-text     |
|                                  | role="ansible-option-default"}   |
| **ip\_addresses**                |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <                                | ```                              |
| a class="ansibleOptionLink" href |                                  |
| ="#parameter-ip_addresses" title |                                  |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAnchor" | ```                              |
|  id="parameter-localNode"></div> | this holds the connection        |
| ```                              | parameters required to           |
| ::: {#ansible_collections.t      | communicate with an instance of  |
| hales.ciphertrust.interface_acti | CipherTrust Manager (CM)         |
| ons_module__parameter-localnode} |                                  |
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
| {#ansible_collections.thales.cip | ```                              |
| hertrust.interface_actions_modul |                                  |
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
| ::: {                            | </div>                           |
| #ansible_collections.thales.ciph | ```                              |
| ertrust.interface_actions_module |                                  |
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
| ::: {#a                          | ::: {.rst-class}                 |
| nsible_collections.thales.cipher | ansible-option-line              |
| trust.interface_actions_module__ | :::                              |
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
| ::: {#ansible                    |                                  |
| _collections.thales.ciphertrust. | ```{=html}                       |
| interface_actions_module__parame | </div>                           |
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
| ::: {#ansible_collections.thales | </div>                           |
| .ciphertrust.interface_actions_m | ```                              |
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
| ::                               | ansible-option-line              |
| : {#ansible_collections.thales.c | :::                              |
| iphertrust.interface_actions_mod |                                  |
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
| <div class="ansibleOptionAnc     | ```                              |
| hor" id="parameter-names"></div> | Name fields like O, OU, L, ST, C |
| ```                              |                                  |
| ::: {#ansible_collectio          | ::: {.rst-class}                 |
| ns.thales.ciphertrust.interface_ | ansible-option-line              |
| actions_module__parameter-names} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
| :::                              | `[]`{.interpreted-text           |
|                                  | role="ansible-option-default"}   |
| **names**                        |                                  |
|                                  | ```{=html}                       |
| ```{=html}                       | </div>                           |
| <a class="ansibleOptionLin       | ```                              |
| k" href="#parameter-names" title |                                  |
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
| <                                | <                                |
| div class="ansible-option-cell"> | div class="ansible-option-cell"> |
| <div class="ansibleOptionAncho   | ```                              |
| r" id="parameter-op_type"></div> | Operation to be performed        |
| ```                              |                                  |
| ::: {#ansible_collections        | ::: {.rst-class}                 |
| .thales.ciphertrust.interface_ac | ansible-option-line              |
| tions_module__parameter-op_type} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Ch                              |
| :::                              | oices:]{.ansible-option-choices} |
| :::                              |                                  |
|                                  | -   `"put\                       |
| **op\_type**                     | _certificate"`{.interpreted-text |
|                                  |     role                         |
| ```{=html}                       | ="ansible-option-choices-entry"} |
| <a class="ansibleOptionLink"     | -   `"enable"`{.interpreted-text |
|  href="#parameter-op_type" title |     role                         |
| ="Permalink to this option"></a> | ="ansible-option-choices-entry"} |
| ```                              | -                                |
| ::: {.rst-class}                 |    `"disable"`{.interpreted-text |
| ansible-option-type-line         |     role                         |
| :::                              | ="ansible-option-choices-entry"} |
|                                  | -   `"restore-default            |
| [string]{.ansible-option-type} / | -tls-ciphers"`{.interpreted-text |
| [req                             |     role                         |
| uired]{.ansible-option-required} | ="ansible-option-choices-entry"} |
|                                  | -   `"csr"`{.interpreted-text    |
| ```{=html}                       |     role                         |
| </div>                           | ="ansible-option-choices-entry"} |
| ```                              | -   `"auto-gen                   |
|                                  | -server-cert"`{.interpreted-text |
|                                  |     role                         |
|                                  | ="ansible-option-choices-entry"} |
|                                  | -   `"use                        |
|                                  | -certificate"`{.interpreted-text |
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
| " id="parameter-password"></div> | Password to the encrypted key    |
| ```                              |                                  |
| ::: {#ansible_collections.       | ::: {.rst-class}                 |
| thales.ciphertrust.interface_act | ansible-option-line              |
| ions_module__parameter-password} | :::                              |
| ::: {.rst-class}                 |                                  |
| ansible-option-title             | [Default                         |
| :::                              | :]{.ansible-option-default-bold} |
| :::                              | `"none"`{.interpreted-text       |
|                                  | role="ansible-option-default"}   |
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

Examples
--------

``` {.yaml+jinja}
- name: "Add Cert to Interface"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: put_certificate
    interface_id: "interface_identifier"
    certificate: "cert_key_data"
    format: PEM

- name: "Enable Interface"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: enable
    interface_id: "interface_identifier"

- name: "Disable Interface"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: disable
    interface_id: "interface_identifier"

- name: "Restore default TLS Ciphers"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: restore-default-tls-ciphers
    interface_id: "interface_identifier"

- name: "Create CSR"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: csr
    interface_id: "interface_identifier"
    cn: "csr_cn"

- name: "Auto Generate Server Certificate"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: auto-gen-server-cert
    interface_id: "interface_identifier"

- name: "Use certificate"
  thales.ciphertrust.interface_actions:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
    op_type: use-certificate
    interface_id: "interface_identifier"
    copy_from: "Name_Source_Interface"
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
