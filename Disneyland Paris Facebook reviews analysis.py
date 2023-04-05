#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Libraries needed
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import plotly.graph_objs as go
import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
from plotly import tools


# In[5]:


df = pd.read_csv("Desktop/facebook_reviews_disneylandParis_format.csv", engine='python')
df.head()


# In[8]:


count_of_columns = df.count().sort_values(ascending=False)
count_of_columns


# In[9]:


percent_reviewers = count_of_columns['review']/count_of_columns['user_id']*100
percent_reviewers


# In[13]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

f, g = plt.subplots(figsize=(12, 9))
df['stars'].value_counts().plot.bar(color="green")
g.set_xticklabels(g.get_xticklabels(), rotation=0)
plt.title("Categorization by rating")
plt.show(g)


# In[14]:


f, g = plt.subplots(figsize=(12, 9))
df['day_of_week'].value_counts().plot.bar(color="blue")
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.title("Categorization day of the week when the review was submitted")
plt.show(g)


# In[15]:


plt.hist(df['hour_of_day'], bins=12, histtype='bar', orientation='vertical', label='Time of day when review is submitted');


# In[16]:


df['review_nb_words'].fillna('0', inplace=True)
df['review_nb_words'].nunique()


# In[ ]:




