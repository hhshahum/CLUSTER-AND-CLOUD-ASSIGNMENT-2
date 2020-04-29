#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tweepy
import json
import couchdb
import time
import sys
from multiprocessing import Pool


# In[4]:


listofallapi1 = [
    { # Harshal's API Keys
        "ACCESS_TOKEN": "1108957058-NySDpIZkdANBqMbiExU5RlXNR4CoZPwgOXjcnHn",
        "ACCESS_TOKEN_SECRET": "zbFAtJUfTsBqfb64ewjgSBnBdQnapYXk9A2V4ZmrqDhK4",
        "API_KEY": "LIxJDmSUnhXrmeZxXoIVFZpss",
        "API_SECRET": "TbkB1CfsvL1ea42dDiwST2UKmR99UTAKPXql2iz9kHYCLxqQN5",
    },{ # Kamakshi's API Keys
        "ACCESS_TOKEN": "1251725408589905920-8m8RRaX999I2My5aW1b0ServY1WC0I",
        "ACCESS_TOKEN_SECRET": "9VzbT4b7168LpYQ4tCZf3CR6yFB9HJeYInH7L0m8Q06Si",
        "API_KEY": "e8A184Bnp1yEaXSa6GscSUS73",
        "API_SECRET": "EsbBC9RRCSUecXKVnlLpigUFoBzVgsorRzOUOkJ5aKK7E3aAhT",
    }
]


# In[5]:


def tweetcollector(index):
  l = StdOutListener()
  print(index)
  auth = tweepy.OAuthHandler(listofallapi1[index]["API_KEY"], listofallapi1[index]["API_SECRET"])
  auth.set_access_token(listofallapi1[index]["ACCESS_TOKEN"], listofallapi1[index]["ACCESS_TOKEN_SECRET"])
  while True:
    try:
      stream = tweepy.Stream(auth, l)
      stream.filter(locations=[110.95,-54.83,159.29,-11.35])
    except:
      continue


# In[7]:


dbname = 'tweets_using_tweepy_for_australia'
couchserver = 'http://admin:group40@115.146.94.7:8888/'
try:
  server = couchdb.Server(url=couchserver)
  db = server.create(dbname)
except couchdb.http.PreconditionFailed:
  db = server[dbname]


# In[8]:


def add_to_db(tweet):
  mytemp = db.get(tweet['user']['id_str'])
  if mytemp==None:
    db.save(tweet)


# In[9]:


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        add_to_db(decoded)
        return True

    def on_error(self, status):
        print(status)


# In[10]:


def main():
  process_list=[]
  for i in range(len(listofallapi1)):
    process_list.append(i)
  pool = Pool(processes = len(listofallapi1))
  pool.map(tweetcollector,process_list)


# In[ ]:


if __name__ == '__main__':
  main()

