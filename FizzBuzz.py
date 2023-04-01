#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter a number : "))

if(n%3==0 and n%5==0):
    print(n,"is divisible by both 3 and 5 so FizzBuzz")
elif(n%5==0):
    print(n,"is divisible by 5 so Buzz")
elif(n%3==0):
    print(n,"is divisible by 3 so Fizz")
else:
    print(n,"is not divisible by either 3 or 5 so",n,"itself")

