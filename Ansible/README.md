# Ansible (CDSP_Orchestration)
For IT admins and DevOps teams who use Ansible to manage their infrastructure, we have provided Ansible Collection that interfaces with each of the products within the CipherTrust Data Security Platform.
* [CipherTrust Manager](./CipherTrustManager/)

# Building the collection locally for testing
## Pull the code from Github repository
```
gil pull https://github.com/thalescpl-io/CDSP_Orchestration.git
```
## Install Ansible
## Build and Install the collection
```
cd thales/ciphertrust
ansible-galaxy collection build
ansible-galaxy collection install thales-ciphertrust-1.0.0.tar.gz
```
## Update the vars file
```
this_node_address: <IP Address/FQDN of the Ciphertrust Manager instance you will be interacting with>
this_node_private_ip: <Private IP of this CM instance if not same as public IP>
this_node_username: <Username with admin role for this CM instance>
this_node_password: <Password for this user>

# Below section is valid for testing the createCluster.yml playbook
# This is an array of CM instances...add as many you want
cluster_nodes:
  - public_address: <IP Address/FQDN of the Ciphertrust Manager instance you want to add to cluster>
    private_address: <Private IP of this CM instance if not same as public IP>
    username: <Username with admin role for this CM instance>
    password: <Password for this user>

# Leave this as is unless you want to change server port...default port for CM is 5432
this_node_connection_string:
  server_ip: "{{ this_node_address }}"
  server_private_ip: "{{ this_node_private_ip }}"
  server_port: 5432
  user: "{{ this_node_username }}"
  password: "{{ this_node_password }}"
  verify: false

# Below variables are needed to run the sample playbooks:
# createDPGResources.yml
# deleteDPGResources.yml
# These sample playbooks will configure the CM to run a Data Protection Gateway (DPG) demo

dpg_key_name: AnsibleKey
nae_port_number: 9006
char_set_name: AnsibleCharset
fpe_card_protection_policy_name: "AnsibleProtPolicyCard"
non_card_protection_policy_name: "AnsibleProtPolicyNonCard"
access_policy_name: AnsibleAccessPolicy
var_users:
  - username: "AnsibleUser1"
    password: "KeySecure01!"
  - username: "AnsibleUser2"
    password: "KeySecure01!"
var_usersets:
  - name: "AnsibleUserset101"
    users:
      - ccaccountowner
  - name: "AnsibleUserset102"
    users:
      - AnsibleUser1
      - AnsibleUser2
var_usersetPolicies:
  - user_set_name: "AnsibleUserset101"
    reveal_type: "Plaintext"
  - user_set_name: "AnsibleUserset102"
    reveal_type: "Masked Value"
    masking_format_name: "SHOW_LAST_FOUR"
dpg_policy_name: AnsibleDpgPolicy
client_profile_name: AnsibleClientProfile
```
## Run the sample playbook
```
ansible-playbook createCluster.yml
```
