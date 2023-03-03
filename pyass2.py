#!/usr/bin/env python
# coding: utf-8

# In[5]:


list1 = [int(l) for l in input("List : ").split(",")]
print("\nEntered List :",list1)

def small_no(list1):
    mini = list1[0]
    for i in range(len(list1)):
        if list1[i] < mini:
            mini = list1[i]
    return mini

small = small_no(list1)
print("\nSmallest number in the entered list :",small)


# In[ ]:




