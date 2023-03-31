#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sum_of_squares_of_numbers(list1):
    sum = 0
    for j in list1:
        sum = sum + j**2
    print("Sum of the squares of all the numbers in",list1,":",sum)

list1 = [int(i) for i in input("Enter values in list1 : ").split(",")]

sum_of_squares_of_numbers(list1)

