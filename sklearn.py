#!/usr/bin/env python
# coding: utf-8

# In[39]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits


# In[40]:


dataset = load_digits()
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.20, random_state=0)
model = KNeighborsClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
score = model.score(x_test, y_test)
print(score)
final = score*100
print(final)


# In[41]:


f= open("sklearn_result.txt","w+")


# In[42]:


f.write(str(final))


# In[43]:


f.close()


# In[ ]:


