#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Load json database into your local couchdb database
or change the db string to point you any other db on network
* use at your own risk and feel free to use and distribute this code * 
Author Tanmay Dutta

"""
import os
import sys
import couchdb
import json


# In[11]:




def main(json_file,
         db_name,
         couchdb_address):
    # 1. Create the database.. No error checking here because we want to get exception if db exists
    couch = couchdb.Server(couchdb_address)
    # db = couch.create(db_name)
    db = couch[db_name]
    # 2 Read the json line by line and put into the db
    with open(json_file,encoding='utf-8') as jsonfile:
        for i,line in enumerate(jsonfile):
            line = line.replace(",\n", "")
            try:
                if True:
                    data = json.loads(line)
                    db.save(data)
                    print(i)
            except Exception as e:
                print(e)
                print("读取本行出错,自动跳过")
    



# In[7]:



DB_STRING="http://admin:group40@172.26.131.165:5984"


# In[12]:


if __name__=='__main__':
    path = "/Users/Ryan/Desktop/untitled folder/"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    db_name = 'aurin_vic_crime_with_location'
    # p = "twitter-melb.json"
    db_str = DB_STRING
    
    for file in files:
        if file != ".DS_Store":
            p = "/Users/Ryan/Desktop/untitled folder/"
            print(file + " begins!")
            main(p+file,db_name,db_str)
            print(file + "ends!")
    # main(p,db_name,db_str)
    # print("读取{}文件完毕".format(p))




