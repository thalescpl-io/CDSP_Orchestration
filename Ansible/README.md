# Ansible Collection
For IT admins and DevOps teams who use Red Hat® Ansible® to manage their infrastructure, we have provided Ansible Modules and Playbooks that interfaces with each of the products within the CipherTrust Data Security Platform.

## Installation
Install Ansible on your host machine using instructions specific to the OS of the host machine.

Download thales-ciphertrust-1.0.0.tar.gz from this repository
* [Ansible](Ansible/thales/ciphertrust/)

Install the collection using command -
```
ansible-galaxy collection install thales-ciphertrust-1.0.0.tar.gz
```

## Run Playbooks
Sample playbooks provided as part of the repo
* [Ansible](Ansible/playbooks/)
```
ansible-playbook cluster.yml -vv
```
