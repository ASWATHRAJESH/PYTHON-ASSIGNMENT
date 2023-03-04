#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input("Enter a number : "))

def factorial(n):
    fact = 1
    if(n < 0):
        print("Factorial does not exist for negative numbers")
    elif(n == 0):
        print("\nFactorial of 0 : 1")
    else:
        for i in range(1,n + 1):
            fact = fact * i
        print("\nFactorial of",n,":",fact)
        
factorial(n)


# In[ ]:




