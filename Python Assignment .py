#!/usr/bin/env python
# coding: utf-8

# ## Description of approach that I used

# As given in the assignment I have to find the names that are similar and are around 200 metre in distance from each other. For this I sorted my csv file using .sort_values() function based on the name ,latitides and longitudes.
# After sorting the file I ran some test cases to find the distance between coordinates and I got to know that they are almost less than 200 metre in distance.
# After that I imported the difflib module of python that helped me in comparison of values of name column. I gave in the input of the name column. It gave me the output as 1 for the names that are similar and have minimum levensthien distance and it returned 0 as output for dissimilar names.

# In[1]:


import pandas as pd


# In[2]:


#importing the csv file
file=pd.read_csv("assignment_data.csv")


# In[3]:


file.head()


# In[13]:


#sorting the values based on the name , latitude and longitude
a=file.sort_values(by=['name',"latitude", "longitude",])[['name',"latitude", "longitude"]]


# In[15]:


a.head()


# In[18]:


#method to calculate the distance between two coordinates
import h3


# In[21]:


coords_1 = (12.915150, 77.641385)
coords_2 = (12.914391, 77.642164)
distance = h3.point_dist(coords_1, coords_2, unit='m') # To get distance in meters


# In[38]:


print(distance)


# as we can see that the distance is coming out to be around 120 metres which is less than 200 metres.

# In[32]:


import difflib


# In[35]:


#adding a new column in our file and passing the output as 1 for similar string and 0 for rest.
a['is_similar'] = [(len(difflib.get_close_matches(x, a['name'], cutoff=0.7))>1)*1 
              for x in a['name']]


# In[39]:


print(a)


# In[37]:


#Saving the output in a new csv file and naming the file as output.
a.to_csv('output.csv', index=False)


# In[ ]:




