orphan

:   

::: {#ansible_collections.thales.ciphertrust.license_trial_get_module}
:::

thales.ciphertrust.license\_trial\_get module \-- This is a Thales CipherTrust Manager module for working with the CipherTrust Manager APIs.
============================================================================================================================================

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
`thales.ciphertrust.license_trial_get`.
:::

::: {.rst-class}
ansible-version-added
:::

New in thales.ciphertrust 1.0.0

::: {.contents local="" depth="1"}
:::

Synopsis
--------

-   This is a Thales CipherTrust Manager module for retrieving the ID of
    a trial license if available for a particular CM instance

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
| ::: {#ansible_collections.t      | communicate with an instance of  |
| hales.ciphertrust.license_trial_ | CipherTrust Manager (CM)         |
| get_module__parameter-localnode} |                                  |
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
| hertrust.license_trial_get_modul |                                  |
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
| ertrust.license_trial_get_module |                                  |
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
| trust.license_trial_get_module__ | :::                              |
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
| license_trial_get_module__parame | </div>                           |
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
| .ciphertrust.license_trial_get_m | ```                              |
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
| iphertrust.license_trial_get_mod |                                  |
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

Examples
--------

``` {.yaml+jinja}
- name: "Get Trial License ID"
  thales.ciphertrust.license_trial_get:
    localNode:
        server_ip: "IP/FQDN of CipherTrust Manager"
        server_private_ip: "Private IP in case that is different from above"
        server_port: 5432
        user: "CipherTrust Manager Username"
        password: "CipherTrust Manager Password"
        verify: false
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
