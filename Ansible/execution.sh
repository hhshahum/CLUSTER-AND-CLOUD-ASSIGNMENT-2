#!/bin/bash
# echo launch instances on NECTAR
# . ./unimelb-comp90024-2020-grp-40-openrc.sh; ansible-playbook launch_instance.yaml

# echo import ip address to inventory
# python3 import_ip_to_hosts.py

echo wait until all nodes can be accessed
. ./unimelb-comp90024-2020-grp-40-openrc.sh; ansible-playbook test_connection.yaml

# echo set proxy for all instances
# sudo chmod 400 yycz.pem
# ansible-playbook setup_instance_proxy.yaml

# echo reconnect to make proxy work then setup common dependencies for instances
# sleep 10
# ansible-playbook instance_common_setup.yaml

# echo install docker for harvesters
# ansible-playbook install_docker.yaml

# echo install couchdb and setup cluster by docker
# ansible-playbook couchdb_and_cluster.yaml
# sleep 5

echo setup webserver
# ansible-playbook webserver_setup.yaml
ansible-playbook apache.yaml







