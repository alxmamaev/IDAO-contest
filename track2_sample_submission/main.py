
# coding: utf-8

# In[1]:


import pandas
import numpy as np
import sklearn as sk

import time
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsRegressor
import time
import pickle

import time
#get_ipython().run_line_magic('matplotlib', 'inline')
from random import randint

from scipy.spatial import KDTree


# In[2]:


dataset_name = "train.csv.zip"
data = pandas.read_csv(dataset_name).drop(["id1", "id2"], axis=1)
data.head()


t = time.time()

# In[3]:


data = data[data["user_id"].isin(data["user_id"].unique()[:5000//5*25])][["user_id", "id3"]].get_values()


# In[4]:


users = np.unique(data[:,0])
users_vectors = dict([(user, np.zeros(931)) for user in users])


# In[5]:


def ohe(id3):
    vector = np.zeros(931)
    vector[id3] = 1
    
    return vector


# In[6]:


users = np.unique(data[:,0])
users_vectors = dict([(user, np.zeros(931)) for user in users])


# In[7]:


for row in data:
    users_vectors[row[0]] += ohe(row[1])


# In[8]:


for user in users:
    vec = users_vectors[user]
    users_vectors[user] = vec/vec.sum()


# In[9]:


usvecs = []
for key, item in users_vectors.items():
    usvecs.append(item)


# In[10]:


items = [i for i in range(931)]


# In[11]:


knn = KNeighborsRegressor(n_neighbors=70)


# In[12]:


knn.fit(usvecs, usvecs)


# In[13]:


items = [i for i in range(931)]


# In[22]:


recomendations = []
for uid in users[:5000]:
    mean_vector = []
    
    vec = knn.predict([users_vectors[uid]])[0]
    vec[users_vectors[uid] > 0] = 0
    row = [uid] + [i[1] for i in sorted(list(zip(vec.tolist(), items)), reverse=True)[:5]]
    
    recomendations.append(row)


# In[23]:


submit = pandas.DataFrame(data=recomendations, columns=["user_id", "id3_1", "id3_2", "id3_3", "id3_4", "id3_5"])
submit.to_csv("submission.csv", index=False)

print(time.time()-t)

