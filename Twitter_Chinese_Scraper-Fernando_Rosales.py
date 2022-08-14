#!/usr/bin/env python
# coding: utf-8

# To Anonymize Your Python Requests With Tor, checked this: https://www.youtube.com/watch?v=wJfa0qEzpJc&t=59s

# To get a basic understanding on how to scrape Twitter data with snscrape, this resource was very helpful: https://www.youtube.com/watch?v=QLIYJoRvd-M

# In[1]:


import json, os, sys
import snscrape.modules.twitter as sntwitter
import datetime, time, requests
from datetime import datetime 
from datetime import date
from datetime import timedelta


# In[2]:


import requests
import time, random
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
import random, time


# In[3]:


language = 'lang:zh'  #set language to Chinese
location = '36.186107, 105.163097, 2010km'


# In[4]:


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

url = 'https://ident.me'


# In[5]:


headers = { 'User-Agent': UserAgent().random }
requests.get(url, proxies=proxies, headers=headers).text


# In[6]:


def renew_ip():
    with Controller.from_port(port=9051) as c:
        c.authenticate(password='kalilinux')
        c.signal(Signal.NEWNYM)


# In[7]:


current_datetime = datetime.now()
print(current_datetime)


# In[8]:


date = date.today()
print(date)


# In[9]:


previous_hour = current_datetime - timedelta(hours=1)
print(previous_hour)


# In[12]:


Tweets = current_datetime.strftime("%Y%m%d-%H%M%S") + '.json'


# In[14]:


for r in range (10):
   for i,tweet in enumerate(sntwitter.TwitterSearchScraper(language, 'since:previous_hour until:current_datetime').get_items()):
       #if i>=500:
       if i>=100:
           break
       with open(Tweets, "a", encoding="utf-8") as f:
           print([tweet, tweet.date, tweet.id, tweet.content, tweet.user.username], file=f)
renew_ip()
time.sleep(10)


# On python open():
# 
# *https://www.programiz.com/python-programming/methods/built-in/open
# 
# *https://stackoverflow.com/questions/19774357/how-to-open-read-write-file-and-recreate-the-file

# For 'UnicodeEncodeError: 'charmap' codec can't encode characters' problem, checked this resource: https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
