#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:


import os
os.chdir("C:/Users/Pradeep/Desktop/DataSets")


# In[3]:


df=pd.read_csv('inventory_data_total(AutoRecovered).csv')


# In[4]:


df


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.columns


# In[8]:


df.corr()


# In[9]:


df.columns


# In[10]:


df.shape


# In[11]:


sns.heatmap(df.corr(),annot=True)
plt.title("Correlation Matrix")
plt.show()


# In[14]:


df['preco(Price)'].hist(bins=10)


# In[15]:


df['venda(Sales)'].hist(bins=10)


# In[19]:


df['Month'].hist(bins=10)


# In[16]:


df.boxplot(column='Revenue')


# In[17]:


df.boxplot(column='Month')


# In[18]:


df.boxplot(column='venda(Sales)')


# In[20]:


sns.pairplot(df, x_vars=['Revenue','preco(Price)','estoque(Stock)'], y_vars='venda(Sales)', height = 4)


# In[21]:


sns.displot(df['preco(Price)'])


# In[22]:


sns.distplot(df['venda(Sales)'], fit=stats.norm)


# In[ ]:




