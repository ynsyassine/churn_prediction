#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests 


# In[11]:


url = "http://0.0.0.0:5000/predict"


# In[12]:


customer = {
    "customerid": "8879-zkjof",
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "no",
    "tenure": 41,
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "dsl",
    "onlinesecurity": "yes",
    "onlinebackup": "no",
    "deviceprotection": "yes",
    "techsupport": "yes",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "one_year",
    "paperlessbilling": "yes",
    "paymentmethod": "bank_transfer_(automatic)",
    "monthlycharges": 79.85,
    "totalcharges": 3320.75
}


# In[4]:


print(customer) 


# In[13]:


response = requests.post(url , json = customer).json()
print(response)
# In[ ]:




