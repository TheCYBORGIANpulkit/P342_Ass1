#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Q1:")
n = int(input("Enter an integer:"))
if n < 0:
    print("You've entered a negative integer.")
a = 0
for i in range(1,n+1):
    a = a + i
print("The sum of natural numbers from 1 to", n, "is", a)

print("Q2:")
n = int(input("Enter an integer:"))
if n < 0:
    print("You've entered a negative integer for which factorial is not defined.")
else: 
    a = 1
    for i in range(1,n+1):
        a = a*i
    print("The product of natural numbers from 1 to", n, "is", a)

print("Q3:")
a = 0
k = int(input("Enter an integer:"))
for i in range(1,k+1):
    c = a
    a = a + 1.0/i
    b = a - c
    if b <= 0.001:
        a = c    
print("The sum of harmonic progression of natural numbers is till ", k ," terms ", a)


# In[ ]:




