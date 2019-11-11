
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
import sys
import MeCab
import numpy as np
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:

start_id=0
end_id=100
#id = 10

def scraping_web_page(url):
    sleep(5)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup


# In[3]:


def write_file(string,name):
    f_name = '{}.txt'.format(name)
    with open(f_name, mode='a') as f:
        f.write(string)

# In[5]:

def get_url(id_num):
    soup = scraping_web_page('https://www.uta-net.com/artist/{}/'.format(id_num))
    pre_urls = soup.find_all(href=re.compile('/song/\d+/$'))
    base_url = 'https://www.uta-net.com'
    lyrics = [(url.string,scraping_web_page(base_url + url.get("href")).find(id='kashi_area').text) for url in pre_urls]
    return lyrics


# In[6]:


def get_lyrics():
    infos = [get_url(i) for i in range(start_id,end_id)]
    for info in infos:
        for name,kashi in info:
            kashi = kashi.replace('\u3000', '')
            write_file(name+"\n","song_name")
            write_file(kashi+"\n","kashi")


# In[7]:


if __name__ == "__main__":
    get_lyrics()

