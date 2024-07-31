#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv('C:\\Users\\jeeya\\Downloads\\archive\\Expanded_data_with_more_features.csv')


# In[5]:


df=pd.read_csv('C:\\Users\\jeeya\\Downloads\\archive\\Expanded_data_with_more_features.csv')


# In[6]:


df.head(10)


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


round(df.describe(),2)


# In[10]:


df.isnull().sum()


# In[11]:


df.isnull().sum().sum()


# In[12]:


df.tail(25)


# # change weekly study hours

# In[15]:


df['WklyStudyHours ']=df['WklyStudyHours'].str.replace("5-Oct",'5-10')
df.head()


# # gender distribution

# In[56]:


plt.figure(figsize=(2,4))
ax=sns.countplot(data=df,x='Gender')
ax.bar_label(ax.containers[0])
plt.title("gender distribution")
plt.show()


# In[33]:


#in the above chart we have analyse that the count of female is more than men


# In[36]:


gb=df.groupby('ParentEduc').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
gb


# In[57]:


plt.figure(figsize=(4,3))
sns.heatmap(gb,annot=True)
plt.title("Relationship between parent edu.and student")
plt.show()


# In[49]:


#from the above map we have conclude that the students parents education have good impact on thier childerns 


# In[51]:


gb1=round(df.groupby('ParentMaritalStatus').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'}))
gb1


# In[58]:


plt.figure(figsize=(3,2))
sns.heatmap(gb1,annot=True)
plt.title("Relationship between parent marital status and student")
plt.show()


# In[54]:


#from the above map we have conclude that the students parents marital status does  not impact on thier childerns education 


# In[63]:


sns.boxplot(data=df,x="MathScore")
plt.show()


# In[64]:


sns.boxplot(data=df,x="WritingScore")
plt.show()


# In[72]:


print(df['EthnicGroup'].unique())


# # Distribution of ethnic groups

# In[88]:


groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupB = df.loc[(df['EthnicGroup'] == 'group B')].count()
groupC = df.loc[(df['EthnicGroup'] == 'group C')].count()
groupD = df.loc[(df['EthnicGroup'] == 'group D')].count()
groupE = df.loc[(df['EthnicGroup'] == 'group E')].count()
l=["group A","group B","group C","group D","group E"]
mlist=[groupA['EthnicGroup'],groupB["EthnicGroup"],groupC['EthnicGroup'],groupD['EthnicGroup'],groupE['EthnicGroup']]
plt.pie(mlist , labels=l)

plt.title("DISTRIBUTION OF ETHNIC GROUP")
plt.show()


# In[92]:


ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])


# In[ ]:




