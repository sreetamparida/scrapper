#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from SqlUpload import Engine
import warnings
warnings.filterwarnings("ignore")


# In[18]:


def getDataFrame(summary):
    data = []
    rows = summary.findAll('tr')
    temp=[]
    for tr in rows:
        cols = tr.findAll('td')
        data = []
        for td in cols:
            text = td.findAll(text=True)
            text = ' '.join(text)
            data.append(text)
        temp.append(data)
    return temp


# In[19]:


url = 'https://clinicaltrials.gov/ct2/results?cond=&term=&cntry=US&state=&city=&dist='


# In[20]:


result = requests.get(url)
c = result.content
soup = BeautifulSoup(c)


# In[21]:


summary = soup.find("table",{'id':'theDataTable'})


# In[22]:


colum = ['Row','Saved','Status','Study Title','COnditions','Interventions','Study Type','Phase','Sponsor','Funders Type'
          'Study Design','Outcome Measures','Outcome_measures2','Number Enrolled','Sex','Age','NCT number','Other Id', 'Title Acro','Study Start'
          ,'Primary Completion','Study COmpletion', 'First Posted', 'Last Posted', 'Results', 'Location', 'Study Documents']


# In[23]:


data = pd.DataFrame(getDataFrame(summary),columns=colum)


# In[24]:

try:
    up_eng = Engine('mysql','pymysql','sudipta.das','Mu@14021998','localhost','med_db')
except:
    up_eng = Engine('mysql:/sudipta.das:Mu@14021998@localhost/med_db')


# In[25]:


up_eng.uploadData(data,'Med_table')

print('DATA UPLOADED SUCCESSFULLY')

