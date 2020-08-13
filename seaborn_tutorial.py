#!/usr/bin/env python
# coding: utf-8

# In[16]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


example_four= sns.load_dataset('flights')
example_four=example_four.pivot('month','year','passengers')
display_four=sns.heatmap(example_four)


# In[8]:


import pandas as pd


# In[10]:


poke_df=pd.read_csv('Pokemon.csv')


# In[11]:


poke_df.head(10)


# In[21]:


sns.swarmplot(x="Type 1",y="Attack", data =poke_df,hue="Generation")


# In[13]:





# In[ ]:




