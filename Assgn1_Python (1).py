#!/usr/bin/env python
# coding: utf-8

# In[33]:


print("Q1:")
n = int(input("Enter an integer:"))
if n < 0:
    print("You've entered a negative integer.")
a = 0
for i in range(n):
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

r = 1
a = 0
k = int(input("Enter an integer:"))
if k > 1001:
    while 1/r > 0.001:
        a = a + 1/r
        r = r+1
    print("The sum of harmonic progression of natural numbers is",a,"(till 1001 terms).")
else:
    for r in range(1,n+1):
        a = a + 1/r
    print("The sum of harmonic progression of natural numbers is",a,"till" , k , "terms." )
    


# In[ ]:




