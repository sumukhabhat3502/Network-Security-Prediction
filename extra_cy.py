#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[2]:


df=pd.read_csv("Cybersecurity_attacks.csv")
df = pd.DataFrame(df)
df


# In[3]:


X= df[['Protocol','Source_IP','Source Port','Destination_IP','Destination Port']]
print(X)


# In[4]:


Y= df['Attack_Name']
print(Y)


# In[5]:


from sklearn.preprocessing import LabelEncoder
l_Attack_Name=LabelEncoder()
l_Source_IP=LabelEncoder()
l_Destination_IP=LabelEncoder()
l_Protocol=LabelEncoder()


# In[6]:


X['Protocol']=l_Protocol.fit_transform(df['Protocol'])
X['Source_IP']=l_Protocol.fit_transform(df['Source_IP'])
X['Destination_IP']=l_Protocol.fit_transform(df['Destination_IP'])


# In[7]:


X


# In[8]:


Y['Attack_Name']=l_Attack_Name.fit_transform(df['Attack_Name'])


# In[9]:


array=Y['Attack_Name']


# In[10]:


Attack_Name=array.reshape(-1,1)
print(Attack_Name)


# In[11]:


Attack_Name.shape


# In[12]:


X.shape


# In[13]:


from sklearn.model_selection import train_test_split


# In[14]:


X_train, X_test, Attack_Name_train,Attack_Name_test = train_test_split(X,Attack_Name, test_size=0.2)


# In[15]:


from sklearn.ensemble import RandomForestClassifier


# In[16]:


model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, Attack_Name_train)


# In[17]:


model_prediction=model.predict(X_test)
print(model_prediction)


# In[18]:


model.score(X_test,Attack_Name_test)


# In[19]:


ATTACK_NAME=l_Attack_Name.inverse_transform(model_prediction)
print(ATTACK_NAME)


# In[20]:


import pickle


# In[21]:


filename = 'finalized_model.sav'
pickle.dump(model, open(filename,'wb'))




# In[ ]:





# In[ ]:




