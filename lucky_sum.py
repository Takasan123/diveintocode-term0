
# coding: utf-8

# In[ ]:

## lucky_sum


# In[12]:

def lucky_sum(a, b, c):
    if a != 13 and b != 13 and c != 13:
        return a + b + c
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b


# In[13]:

lucky_sum(a, b, c)


# In[ ]:



