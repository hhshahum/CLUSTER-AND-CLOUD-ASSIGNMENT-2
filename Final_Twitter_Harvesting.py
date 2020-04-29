#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
import couchdb.design
from TwitterAPI.TwitterAPI import TwitterAPI
import time
from multiprocessing import Pool


# In[2]:


def tweetcollector(index):
    tweetgather(index,listofallapi[index]["ACCESS_TOKEN"],listofallapi[index]["ACCESS_TOKEN_SECRET"],listofallapi[index]["API_KEY"],listofallapi[index]["API_SECRET"])


# In[3]:


def tweetgather(index, ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_KEY,API_SECRET):

    dbname = 'tweets_for_api_with_index_0'
    try:
        server = couchdb.Server(url=couchserver)
        db = server.create(dbname)
    except couchdb.http.PreconditionFailed:
        db = server[dbname]
    
    api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    while True:
        try:
            for single in api.request(tweet_endpoint,tweet_params):
                print("~~~~~~~~~~ Collecting tweets from API INDEX "+str(index)+" ~~~~~~~~~~")
                time.sleep(5)
                mytemp = db.get(single['user']['id_str'])
                if((single['user']['location']!=None)): 
                    if mytemp!=None:
                        continue
                    else:
                        db.save(single) 
        except:
            continue


# In[4]:


listofallapi = [
    { # Yuyang's API Keys
        "ACCESS_TOKEN": "1031003673579610113-W3Rpr3jV3fyJx6urjHU8p6vBR0xtJ0",
        "ACCESS_TOKEN_SECRET": "8Q6xFOx5KXgrp5a5vVptaSw8mqQ7eS9J4hLGiogyJxuLq",
        "API_KEY": "KvLtpBzoB0mcNZwvCjo1ulVoy",
        "API_SECRET": "nvov2ctLN8hdf9aaAgW70Fgr3myuCJXhTDXynafiZt0mL80pra",
    }]

#,{ # Kamakshi's API Keys
 #       "ACCESS_TOKEN": "1251725408589905920-8m8RRaX999I2My5aW1b0ServY1WC0I",
  #      "ACCESS_TOKEN_SECRET": "9VzbT4b7168LpYQ4tCZf3CR6yFB9HJeYInH7L0m8Q06Si",
   #     "API_KEY": "e8A184Bnp1yEaXSa6GscSUS73",
    #    "API_SECRET": "EsbBC9RRCSUecXKVnlLpigUFoBzVgsorRzOUOkJ5aKK7E3aAhT",
    #}
#]


# In[5]:


couchserver = 'http://admin:group40@115.146.94.7:8888/'
tweet_endpoint = 'statuses/filter'
tweet_params = {'track':['New South Wales','Melbourne','Brisbane','Perth','Adelaide',
                         'Gold Coast-Tweed Heads','Newcastle-Maitland','Canberra-Queanbeyan',
                         'Sunshine Coast','Wollongong','Hobart','Geelong','Townsville','Cairns',
                         'Darwin','Toowoomba','Ballarat','Bendigo','Albury-Wodonga','Launceston',
                         'Mackay','Rockhampton','Bunbury','Bundaberg','Coffs Harbour','Wagga Wagga',
                         'Hervey Bay','Mildura-Wentworth','Shepparton-Mooroopna','Gladstone-Tannum Sands',
                         'Port Macquarie','Tamworth','Victoria','Queensland','Western Australia',
                         'South Australia','Queensland','Australian Capital Territory','Tasmania',
                         'Northern Territory','Australia']}


# In[6]:


def main():
    process_list=[]
    for i in range(len(listofallapi)):
        process_list.append(i)
    pool = Pool(processes = len(listofallapi))
    pool.map(tweetcollector,process_list)


# In[ ]:


if __name__ == '__main__':
    main()

