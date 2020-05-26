# User Guide of the System

## Requirement

1. Python Version >= 3.0
2. Openstack RC File is placed in the root folder
3. Able to run bash script
4. Connected to the UoM VPN

## Deploy The System

1. Run SETUP.SH in command line:


```bash
bash SETUP.SH
```

2. Follow the steps, type in the Openstack Password.
3. (Optional) Type in the system password of your laptop
4. Have a cup of tea.
5. Have fun with the system.

## Access To The Platform

### Web Visualization and Project Homepage

172.26.130.73 (No authorization needed)

### Cloud Monitor

115.146.94.7:8888 (User: admin, Password: group40)

### CouchDB Cluster:

Node 1: 172.26.131.165:5984 (User: admin, Password: group40)

Node 2: 172.26.130.73:5984 (User: admin, Password: group40)

Node 3: 172.26.132.193:5984 (User: admin, Password: group40)



### Software Glance Of The System

Server1: 115.146.94.7

    Jupyter Notebook/ jupyter_notebook:latest
    Node Exporter/ node_exporter:latest
    Grafana/ grafana/grafana:latest



Server2: 172.26.131.165

    CouchDB/couchdb:2.3.0
    Node Exporter/ node_exporter:latest
    CouchDB Exporter/ couchdb_exporter:latest



Server3: 172.26.130.73   

    CouchDB/couchdb:2.3.0
    Node Exporter/ node_exporter:latest
    CouchDB Exporter/ couchdb_exporter:latest
    Apache/ apache2:latest



Server4: 172.26.132.193

    CouchDB/couchdb:2.3.0
    Node Exporter/ node_exporter:latest
    CouchDB Exporter/ couchdb_exporter:latest

