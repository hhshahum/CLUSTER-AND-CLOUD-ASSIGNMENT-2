#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import json

ip_file = open("./instance_ip_address", "r") 
hosts = open("./hosts", "w")

line = ip_file.readline()
ip_list = json.loads(line)

webserver = ip_list[0]
db1 = ip_list[1]
db2 = ip_list[2]
db3 = ip_list[3]

#single node
hosts.write("[webserver]\n")
hosts.write(webserver+"\n\n")

hosts.write("[db_all]\n")
hosts.write(db1+"\n")
hosts.write(db2+"\n")
hosts.write(db3+"\n\n")

hosts.write("[db_master]\n")
hosts.write(db1+"\n\n")

hosts.write("[db_slave]\n")
hosts.write(db2+"\n")
hosts.write(db3+"\n")




hosts.write("[all:vars]\nansible_ssh_user=ubuntu\nansible_ssh_private_key_file=/Users/Ryan/Desktop/grp40-ansible/yycz.pem")

ip_file.close()
hosts.close()

print("Hosts file is created successfully!\n")
