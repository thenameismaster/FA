#!/usr/bin/env python
# coding: utf-8

# In[16]:


def FindPeak(A):
    peak = A[0]
    for i in range(1,len(A)-2):
        prev = A[i-1]
        curr = A[i]
        next = A[i+1]
        if curr > prev and curr > next:
            index = i
            peak = curr
            print(peak)
            
    if A[len(A)-1] >  A[len(A)-2]:
        print(A[len(A)-1])

A=[35,2,40,50,33,55,82,3,2]
print(A,"\n")
FindPeak(A)


# In[ ]:




