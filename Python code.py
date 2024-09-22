#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv('Desktop/games.csv')


# In[107]:


print(df.head())


# In[108]:


df.head()


# In[21]:


df.sort_values('Initial release')


# In[24]:


df.sort_values('Revenue', ascending=False)


# In[51]:


new_df = df.loc[(df['Revenue']>3000000000)&(df['Initial release'] > '2015')]


# In[55]:


new_df.reset_index()


# In[56]:


import matplotlib as pt


# In[104]:


new_df.plot(kind='bar', color='green', title='Top 10 Mobile Games with revenue > 3 Billion ', xlabel='Games', ylabel='Revenue in billions')


# In[105]:


print(new_df)


# In[106]:


df.head()


# In[131]:


import seaborn as sns
sns.barplot(data=new_df,x='Game', y='Revenue')


# In[137]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
plt.xticks(rotation=65)
sns.barplot(x=new_df['Game'], y=new_df['Revenue'])


# In[ ]:




