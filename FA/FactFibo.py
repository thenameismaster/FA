#!/usr/bin/env python
# coding: utf-8

# In[19]:


factTable ={}
def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n==0:
            factTable[0] = 1
            return 1
        else:
            factTable[n]=n*factorial(n-1)
            return factTable[n]

print(factorial(10))

def fibo(n):
    fibTable =[0,1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1]+fibTable[i-2])
    return fibTable[n]

print(fibo(10))


# In[ ]:




