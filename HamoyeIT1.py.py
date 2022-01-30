#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
foods = pd.read_csv(r'C:\Users\USER\Desktop\FoodBalanceSheets_E_Africa_NOFLAG.csv')
print(foods)


# In[3]:


foods.describe()


# In[4]:


foods.isnull().sum()


# In[5]:


foods.groupby('Area')['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018'].count()


# In[6]:


foods[['Y2014']] = foods[['Y2014']].fillna(value='134.196282')
foods[['Y2015']] = foods[['Y2015']].fillna(value='135.235966')
foods[['Y2016']] = foods[['Y2016']].fillna(value='136.555222')
foods[['Y2017']] = foods[['Y2017']].fillna(value='140.917765')
foods[['Y2018']] = foods[['Y2018']].fillna(value='143.758381')


# In[7]:


foods.isnull().sum()


# In[8]:


foods.groupby('Area')['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018'].count()


# In[10]:


foods1 = foods.iloc[0:30471].reset_index(drop=True)
foods2 = foods.iloc[30471:].reset_index(drop=True)
print(foods1)
print(foods2)


# In[12]:


assert len(foods) == (len(foods1) + len(foods2))


# In[13]:


pd.merge(foods1, foods2, how="inner")


# In[14]:


pd.merge(foods1, foods2, how="outer")


# In[15]:


pd.merge(foods1, foods2, how="left")


# In[17]:


foods.duplicated().any()


# In[18]:


foods_fds = foods[foods['Element'].isin(['Food supply (kcal/capita/day)'])]
print(foods_fds)


# In[19]:


foods_fds.head()


# In[21]:


foods_fds.iloc[0:30, :]


# In[ ]:




