
# coding: utf-8

# ### make_bricks

# In[7]:

def make_bricks(small, big, goal):
    if goal > small+big*5:
        return False 
    if goal == small+big*5:
        return True
    if goal < small+big*5 and goal%5 <= small:
        return True
    else:
        return False
        


# In[ ]:



