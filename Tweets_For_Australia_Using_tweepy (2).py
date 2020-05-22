#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import json
import couchdb
import time
import sys
from multiprocessing import Pool


# In[2]:


listofallapi1 = [
    #{ # Harshal's API Keys
     #   "ACCESS_TOKEN":"1251501107160866816-URJKeWxOivyHA8ZJPMhauPB5mksOPI",
      #  "ACCESS_TOKEN_SECRET":"4drvt5fHN4htgFgKNu6OXXVo0jictf2CwLeBeBhwCiXsK",
       # "API_KEY":"iFP5A1DArMTGeC5JnAF3K98nM",
        #"API_SECRET":"QelmzVXvHLeBC8Ki5y4C5YB70XxTns78Mo0sd5gyq4HfRAM9x"
    #},
    { # Kamakshi's API Keys
        "ACCESS_TOKEN": "1251725408589905920-8m8RRaX999I2My5aW1b0ServY1WC0I",
        "ACCESS_TOKEN_SECRET":"9VzbT4b7168LpYQ4tCZf3CR6yFB9HJeYInH7L0m8Q06Si",
        "API_KEY": "e8A184Bnp1yEaXSa6GscSUS73",
        "API_SECRET": "EsbBC9RRCSUecXKVnlLpigUFoBzVgsorRzOUOkJ5aKK7E3aAhT",
   },
    { # Yuyang's API Keys
        "ACCESS_TOKEN": "1031003673579610113-W3Rpr3jV3fyJx6urjHU8p6vBR0xtJ0",
        "ACCESS_TOKEN_SECRET": "8Q6xFOx5KXgrp5a5vVptaSw8mqQ7eS9J4hLGiogyJxuLq",
        "API_KEY": "KvLtpBzoB0mcNZwvCjo1ulVoy",
        "API_SECRET": "nvov2ctLN8hdf9aaAgW70Fgr3myuCJXhTDXynafiZt0mL80pra",
    },
     {  #Harshal's extra API Keys
        "ACCESS_TOKEN": "1251501107160866816-j2SDRZczB8JU22Yuz7Gx5JqQcskWYF",
        "ACCESS_TOKEN_SECRET": "B95RPjcfG96Ryx9mgqRpdq7tsBXuT72B6z2a2zG07CLTj",
        "API_KEY": "iGlKniGAdTg1Mn85Cp4L11NgS",
        "API_SECRET": "ThvPCdTFyn3zf8PrrsCXkRgB0G8RjCME8gIGtXAfMmoOjrbZuJ",
   },
       { # Chongzheng's API keys
        "ACCESS_TOKEN": "1251743327042416640-8F9jwkd1Anl2BvIlSvQ5xRFGbEGXmp",
        "ACCESS_TOKEN_SECRET": "7BVf9CCG2sEsV9ZtrUZvpmUzqskStwPnofvEmMfl9xPtZ",
        "API_KEY": "lYTs2E47jpzxq6FpVFjzaTS60",
        "API_SECRET": "j1LmIHVTnQUOIGuu0RETrdEKW2ImfaTEJ6vfKKiU11HJYQwLMf", 
      },
    {   #New App's Key Harshal
        "ACCESS_TOKEN":"1108957058-NySDpIZkdANBqMbiExU5RlXNR4CoZPwgOXjcnHn",
        "ACCESS_TOKEN_SECRET":"zbFAtJUfTsBqfb64ewjgSBnBdQnapYXk9A2V4ZmrqDhK4",
        "API_SECRET":"TbkB1CfsvL1ea42dDiwST2UKmR99UTAKPXql2iz9kHYCLxqQN5",
        "API_KEY":"LIxJDmSUnhXrmeZxXoIVFZpss"
    },
   { #New App's Key Kamakshi
        "ACCESS_TOKEN":"1251725408589905920-Jghj0SKum5pZkbhF6en96EaVOmRRZ3",
        "ACCESS_TOKEN_SECRET":"vD7EaC1F7HSaBBz1YtmpPosxnWufHJDOpEjAAGnODRSIy",
        "API_SECRET":"RocuAwJU8IsvDSIq4trWdngtCsZDK7YDzHRXff4VbqZNpRhf99",
        "API_KEY":"U5lV0j7tL9aPxPL72vqmk4OWa"
    }
]


# In[3]:


def tweetcollector(index):
  l = StdOutListener()
  print(index)
  auth = tweepy.OAuthHandler(listofallapi1[index]["API_KEY"], listofallapi1[index]["API_SECRET"])
  auth.set_access_token(listofallapi1[index]["ACCESS_TOKEN"], listofallapi1[index]["ACCESS_TOKEN_SECRET"])
  #api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  while True:
    try:
      stream = tweepy.Stream(auth, l)
      print("Hello Streaming")
      stream.filter(locations=[110.95,-54.83,159.29,-11.35])
    except:
      continue


# In[4]:


dbname = 'harvest_tweets'
couchserver = 'http://admin:group40@172.26.131.165:5984/'
try:
  server = couchdb.Server(url=couchserver)
  db = server.create(dbname)
except couchdb.http.PreconditionFailed:
  db = server[dbname]


# In[5]:


class StdOutListener(tweepy.StreamListener):
    print("Hello, Listen to me!")
    def on_data(self, data):
        decoded = json.loads(data)
        x = decoded['id_str']
        if(x not in db):
            db[x] = decoded
            print("Original Added")
        else:
            print("Hello Duplicate")
        return True
    def on_error(self, status):
        if str(status)=="420":
            print("Exceeded")
            time.sleep(60*15)
        else:
            print(status)


# In[6]:


def main():
  process_list=[]
  for i in range(len(listofallapi1)):
    process_list.append(i)
  pool = Pool(processes = len(listofallapi1))
  pool.map(tweetcollector,process_list)


# In[ ]:


if __name__ == '__main__':
  main()


# In[ ]:





# In[ ]:




