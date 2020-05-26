#!/bin/bash
. ./unimelb-comp90024-2020-grp-40-openrc.sh; ansible-playbook launch_instance.yaml

python3 create_hosts_file.py

sleep 150

sudo chmod 400 yycz.pem
ansible-playbook setup_instance_proxy.yaml

sleep 10
ansible-playbook instance_setup.yaml

ansible-playbook install_docker.yaml

ansible-playbook couchdb_and_cluster.yaml
sleep 5

ansible-playbook install_webserver.yaml







