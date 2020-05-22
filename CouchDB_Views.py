#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb


# In[2]:


server = couchdb.Server("http://admin:group40@172.26.131.165:5984/")
db = server["harvest_tweets"] 


# In[3]:


#total-number-of-tweets-by-crime-date
map_fun = """
           function(doc)
{
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit(new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),1);
  }
}
              """
reduce_fun ="_count"


# In[4]:


design = { 'views': {
              'total-number-of-tweets-by-crime-date': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view1"] = design


# In[5]:


crimedate_list = db.iterview('view1/total-number-of-tweets-by-crime-date',500,group=True, group_level=1,stale="ok")


# In[6]:


#crimedate_dict={}
try:
    for r in crimedate_list :
        print(r.key)
        print(r.value)
except:
    pass
#    if r.key in crimedate_dict:
 #       crimedate_dict[r.key]+=r.value
  #  else:
   #     crimedate_dict[r.key] = r.value
#crimedate_dict


# In[7]:


#total-number-of-tweets-by-crime-date-lang
map_fun = """
           function(doc)
{
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.lang],1);
  }
}
              """
reduce_fun ="_count"


# In[8]:


design = { 'views': {
              'total-number-of-tweets-by-crime-date-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view2"] = design


# In[9]:


crimedatelang_list = db.iterview('view2/total-number-of-tweets-by-crime-date-lang',500,group=True, group_level=2,stale="ok")


# In[10]:


try:
    for r in crimedatelang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[11]:


#total-number-of-tweets-by-crime-date-loc
map_fun = """
           function(doc)
{
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0]],1);
  }
}
              """
reduce_fun ="_count"


# In[12]:


design = { 'views': {
              'total-number-of-tweets-by-crime-date-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view3"] = design


# In[13]:


crimedateloc_list = db.iterview('view3/total-number-of-tweets-by-crime-date-loc',500,group=True, group_level=2,stale="ok")


# In[14]:


try:
    for r in crimedateloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[15]:


#total-number-of-tweets-by-crime-date-loc-lang
map_fun = """
function(doc)
{
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([new Date(Date.parse(doc.doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0],doc.lang],1);
  }
}
              """
reduce_fun ="_count"


# In[16]:


design = { 'views': {
              'total-number-of-tweets-by-crime-date-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view4"] = design


# In[17]:


crimedateloclang_list = db.iterview('view4/total-number-of-tweets-by-crime-date-loc-lang',500,group=True, group_level=3,stale="ok")


# In[18]:


try:
    for r in crimedateloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[19]:


#total-number-of-tweets-by-crime-lang
map_fun = """
function(doc){
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit(doc.lang,1);
  }
}
"""
reduce_fun ="_count"


# In[20]:


design = { 'views': {
              'total-number-of-tweets-by-crime-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view5"] = design


# In[21]:


crimelang_list = db.iterview('view5/total-number-of-tweets-by-crime-lang',500,group=True, group_level=1,stale="ok")


# In[22]:


try:
    for r in crimelang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[23]:


#total-number-of-tweets-by-crime-loc
map_fun = """
function(doc)
{
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result)&&doc.place.bounding_box.coordinates)
  {
      emit(doc.place.bounding_box.coordinates[0][0],1);
  }
}
"""
reduce_fun ="_count"


# In[24]:


design = { 'views': {
              'total-number-of-tweets-by-crime-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view6"] = design


# In[25]:


crimeloc_list = db.iterview('view6/total-number-of-tweets-by-crime-loc',500,group=True, group_level=2,stale="ok")


# In[26]:


try:
    for r in crimeloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[27]:


#total-number-of-tweets-by-crime-loc-lang
map_fun = """
function(doc){
  var acceptedwords = /crime|criminal|harassment|robbery|assault|rape|blackmail|extortion|robbery|graffiti|deception|theft|offence|drugs|homicide|abduction|arson|burglary|bribe|trafficking|breach/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([doc.place.bounding_box.coordinates[0][0],doc.lang],1);
  }
}
"""
reduce_fun ="_count"


# In[28]:


design = { 'views': {
              'total-number-of-tweets-by-crime-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view7"] = design


# In[29]:


crimeloclang_list = db.iterview('view7/total-number-of-tweets-by-crime-loc-lang',500,group=True, group_level=3,stale="ok")




# In[30]:


try:
    for r in crimeloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[31]:


#total-number-of-tweets-by-date-lang
map_fun="""
function (doc) {
  emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.lang], 1);
}
"""
reduce_fun ="_count"


# In[32]:


design = { 'views': {
              'total-number-of-tweets-by-date-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view8"] = design


# In[33]:


totaldatelang_list = db.iterview('view8/total-number-of-tweets-by-date-lang',500,group=True, group_level=2,stale="ok")


# In[34]:


try:
    for r in totaldatelang_list :
        print(r.key)
        print(r.value)
except:
        pass


# In[35]:


#total-number-of-tweets-by-date-loc
map_fun="""
function (doc) {
  if(doc.place.bounding_box.coordinates)
  {
  emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0]], 1);
}
}
"""
reduce_fun ="_count"


# In[36]:


design = { 'views': {
              'total-number-of-tweets-by-date-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view9"] = design


# In[37]:


totaldateloc_list = db.iterview('view9/total-number-of-tweets-by-date-loc',500,group=True, group_level=3,stale="ok")


# In[38]:


try:
    for r in totaldateloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[39]:


#total-number-of-tweets-by-date-loc-lang
map_fun="""
function (doc) {
  if (doc.place.bounding_box.coordinates){
  emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0],doc.lang], 1);
}
}
"""
reduce_fun ="_count"


# In[40]:


design = { 'views': {
              'total-number-of-tweets-by-date-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view10"] = design


# In[41]:


totaldateloclang_list = db.iterview('view10/total-number-of-tweets-by-date-loc-lang',500,group=True, group_level=3,stale="ok")


# In[42]:


try:
    for r in totaldateloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[43]:


#total-number-of-tweets-by-date
map_fun="""
function (doc) {
  emit(new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),1);
}
"""
reduce_fun ="_count"


# In[44]:


design = { 'views': {
              'total-number-of-tweets-by-date': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view11"] = design


# In[45]:


totaldate_list = db.iterview('view11/total-number-of-tweets-by-date',500,group=True, group_level=1,stale="ok")


# In[46]:


try:
    for r in totaldate_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[47]:


#total-number-of-tweets-by-discrim-date-lang
map_fun="""
function(doc)
{
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.lang],1);
  }
}
"""
reduce_fun ="_count"


# In[48]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-date-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view12"] = design


# In[49]:



discrimdatelang_list = db.iterview('view12/total-number-of-tweets-by-discrim-date-lang',500,group=True, group_level=2,stale="ok")


# In[50]:


try:
    for r in discrimdatelang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[51]:


#total-number-of-tweets-by-discrim-date-loc
map_fun="""
function(doc)
{
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0]],1);
  }
}
"""
reduce_fun ="_count"


# In[52]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-date-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view13"] = design


# In[53]:


discrimdateloc_list = db.iterview('view13/total-number-of-tweets-by-discrim-date-loc',500,group=True, group_level=3,stale="ok")


# In[54]:


try:
    for r in discrimdateloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[55]:


#total-number-of-tweets-by-discrim-date-loc-lang
map_fun="""
function(doc)
{
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),doc.place.bounding_box.coordinates[0][0],doc.lang],1);
  }
}
"""
reduce_fun ="_count"


# In[56]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-date-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view14"] = design


# In[57]:



discrimdateloclang_list = db.iterview('view14/total-number-of-tweets-by-discrim-date-loc-lang',500,group=True, group_level=4,stale="ok")


# In[58]:


try:
    for r in discrimdateloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[59]:


#total-number-of-tweets-by-discrim-lang
map_fun="""
function(doc){
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit(doc.lang,1);
  }
}
"""
reduce_fun ="_count"


# In[60]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view15"] = design


# In[61]:


discrimlang_list = db.iterview('view15/total-number-of-tweets-by-discrim-lang',500,group=True, group_level=1,stale="ok")


# In[62]:


try:
    for r in discrimlang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[63]:


#total-number-of-tweets-by-discrim-loc
map_fun="""
function(doc)
{
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit(doc.place.bounding_box.coordinates[0][0],1);
  }
}
"""
reduce_fun ="_count"


# In[64]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view16"] = design


# In[65]:


discrimloc_list = db.iterview('view16/total-number-of-tweets-by-discrim-loc',500,group=True, group_level=2,stale="ok")


# In[66]:


try:
    for r in discrimloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[67]:


#total-number-of-tweets-by-discrim-loc-lang
map_fun="""
function(doc){
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result) && doc.place.bounding_box.coordinates)
  {
      emit([doc.place.bounding_box.coordinates[0][0],doc.lang],1);
  }
}
"""
reduce_fun ="_count"


# In[68]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view17"] = design


# In[69]:


discrimloclang_list = db.iterview('view17/total-number-of-tweets-by-discrim-loc-lang',500,group=True, group_level=3,stale="ok")


# In[70]:


try:
    for r in discrimloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[71]:


#total-number-of-tweets-by-discrimin-date
map_fun="""
function(doc)
{
  var acceptedwords = /discrimination|niggas|sexual discrimination|age discrimination|sexualism|gay liberation|job discrimination|fair employment|okboomer|racial|racism|nigro|currypeople|lookism|fattism|sizeism|sexist|misogynist|heterosexism|ageist|menaretrash|paygap|classism|ableism/i;
  var result = (doc.text).match(acceptedwords);
  if (Boolean(result))
  {
      emit(new Date(Date.parse(doc.created_at.replace(/(\+\S+) (.*)/, '$2 $1'))).toLocaleDateString(),1);
  }
}
"""
reduce_fun ="_count"


# In[72]:


design = { 'views': {
              'total-number-of-tweets-by-discrim-date': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view18"] = design


# In[73]:


discrimdate_list = db.iterview('view18/total-number-of-tweets-by-discrim-date',500,group=True, group_level=1,stale="ok")


# In[74]:


try:
    for r in discrimdate_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[75]:


#total-number-of-tweets-by-lang
map_fun="""
function (doc) {
  emit(doc.lang, 1);
}
"""
reduce_fun ="_count"


# In[76]:


design = { 'views': {
              'total-number-of-tweets-by-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view19"] = design


# In[77]:


totallang_list = db.iterview('view19/total-number-of-tweets-by-lang',500,group=True, group_level=1,stale="ok")


# In[78]:


try:
    for r in totallang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[79]:


#total-number-of-tweets-by-loc
map_fun="""
function (doc) {
  if (doc.place.bounding_box.coordinates)
  {
  emit(doc.place.bounding_box.coordinates[0][0], 1);
  }
}
"""
reduce_fun ="_count"


# In[80]:


design = { 'views': {
              'total-number-of-tweets-by-loc': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view20"] = design


# In[81]:


totalloc_list = db.iterview('view20/total-number-of-tweets-by-loc',500,group=True, group_level=2,stale="ok")


# In[82]:


try:
    for r in totalloc_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[83]:


#total-number-of-tweets-by-loc-lang
map_fun="""
function (doc) {
  if (doc.place.bounding_box.coordinates){
  emit([doc.place.bounding_box.coordinates[0][0],doc.lang], 1);
}
}
"""
reduce_fun ="_count"


# In[84]:


design = { 'views': {
              'total-number-of-tweets-by-loc-lang': {
                  'map': map_fun,
                  'reduce': reduce_fun
                }
            } }
db["_design/view21"] = design


# In[85]:


totalloclang_list = db.iterview('view21/total-number-of-tweets-by-loc-lang',500,group=True, group_level=3,stale="ok")


# In[86]:


try:
    for r in totalloclang_list :
        print(r.key)
        print(r.value)
except:
    pass


# In[ ]:




