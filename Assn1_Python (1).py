#!/usr/bin/env python
# coding: utf-8

# In[12]:


print("Q1:")
n = int(input("Enter an integer:"))
if n < 0:
    print("You've entered a negative integer.")
a = 0
for i in range(n):
    a = a + i
print("The sum of natural numbers from 1 to", n, "is", a)


# In[28]:


print("Q2:")
n = int(input("Enter an integer:"))
if n < 0:
    print("You've entered a negative integer for which factorial is not defined.")
else: 
    a = 1
    for i in range(1,n+1):
        a = a*i
    print("The product of natural numbers from 1 to", n, "is", a)


# In[27]:


print("Q3:")
r = 1
a = 0
while 1/r >= 0.001:
    a = a + 1/r
    r = r+1
print("The sum of harmonic progression of natural numbers is",a,"(till 1001 terms).")


# In[ ]:




