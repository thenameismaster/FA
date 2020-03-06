#!/usr/bin/env python
# coding: utf-8

# In[11]:


def FindSmallestAndLargestInArray(A):
    max = 0
    min = 0
    for number in A:
        if number > max:
            max = number 
        elif number < min:
            min = number
    print("Smallest",min)
    print('Largest',max)
    
FindSmallestAndLargestInArray([44,355,636,231])


# In[ ]:




