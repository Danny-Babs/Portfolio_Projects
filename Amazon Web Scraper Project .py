#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[4]:


# Connection to the Website

URL ='https://www.amazon.com/Show-Perfect-Mathematical-Statics-Shirt/dp/B07FLKB2CH/ref=pd_day0_d_sccl_1_5/137-2385444-1008720?pd_rd_w=sSlXB&content-id=amzn1.sym.93b79d61-3ac2-4c6e-a810-43d3e837e910&pf_rd_p=93b79d61-3ac2-4c6e-a810-43d3e837e910&pf_rd_r=NPZT6KDADAFFDBC0M5F0&pd_rd_wg=lJ0gG&pd_rd_r=35c2764a-debb-419c-b5f7-9eadde51051b&pd_rd_i=B07FLKB2CH&customId=B07537HNQY&customizationToken=MC_Assembly_1%23B07537HNQY&th=1&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


title = soup2.find(id='productTitle').get_text()
ratings = soup2.find(id='acrPopover').get_text()


print(title)
print(ratings)














# In[5]:


title = title.strip()
ratings = ratings.strip()

print(title)
print(ratings)


# In[6]:


import datetime

today = datetime.date.today()

print(today)


# In[7]:


import csv

header = ['Title', 'Ratings','Date']
data = [title, ratings, today]

type(data)

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[85]:


pip install pandas


# In[12]:


import pandas as pd

df = pd.read_csv(r'C:\Users\dbabs\AmazonWebScraperDataset.csv')

print(df)


# In[11]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[13]:


def check_ratings():
    URL ='https://www.amazon.com/Show-Perfect-Mathematical-Statics-Shirt/dp/B07FLKB2CH/ref=pd_day0_d_sccl_1_5/137-2385444-1008720?pd_rd_w=sSlXB&content-id=amzn1.sym.93b79d61-3ac2-4c6e-a810-43d3e837e910&pf_rd_p=93b79d61-3ac2-4c6e-a810-43d3e837e910&pf_rd_r=NPZT6KDADAFFDBC0M5F0&pd_rd_wg=lJ0gG&pd_rd_r=35c2764a-debb-419c-b5f7-9eadde51051b&pd_rd_i=B07FLKB2CH&customId=B07537HNQY&customizationToken=MC_Assembly_1%23B07537HNQY&th=1&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


    title = soup2.find(id='productTitle').get_text()
    ratings = soup2.find(id='acrPopover').get_text()
    
    title = title.strip()
    ratings = ratings.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Ratings','Date']
    data = [title, ratings, today]
    
    with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


    


# In[ ]:


while(True):
    check_ratings()
    time.sleep(5)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\dbabs\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:





# In[ ]:




