#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a Python program to print the following string in a specific format (see the
# output).
print ('''twinkle, nkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are''')


# In[2]:


# Write a Python program to get the Python version you are using
from platform import python_version

print(python_version())


# In[3]:


# Write a Python program to display the current date and time
from datetime import datetime
print(datetime.fromtimestamp(1576280665))


# In[4]:


# Write a Python program which accepts the radius of a circle from the user and compute
# the area.
a = int(input('enter radius of a circle'))
pi = 3.14159265359
Area = pi * (a*a)
print(Area)


# In[5]:


# Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
a = input('enter your first name')
b = input('enter your second name')
print(a , b)


# In[7]:


# Write a python program which takes two inputs from user and print them addition
a = int(input('Enter a number'))
b = int(input('Enter second number'))
print(a + b)


# In[14]:


# Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ?
a = int(input('Eng Marks'))
b = int(input("Maths marks"))
c = int(input("computer marks"))
d = int(input("urdu marks"))
e = int(input("Islamiat marks"))
total = (a + b + c + d + e)
print (total)
percentage = total/500*100
print(percentage)
if percentage < 100 and percentage > 80:
    print('Grade A+')
elif percentage < 80 and percentage < 70:
    print('Grade A')
elif percentage > 70 and percentage < 60:
    print('Grade B')
elif percentage > 60 and percentage < 50:
    print('Grade C')
elif percentage > 50 and percentage < 40:
    print('Grade D')
elif percentage > 40 and percentage < 80:
    print('Grade E')
else:
    print("you are fail")


# In[33]:


# Write a program which take input from user and identify that the given number is even
# or odd?
a = int(input('Enter a number'))
if (a / 2) == 0:
 print('num is odd')
else :
    print ('num is even')


# In[8]:


# Write a program which print the length of the list?
listA = ["Saim", "Humayun", "maaz", "subhan", "zaheer", "faizan"]
print("The length of the list is:", len(listA))


# In[12]:


# Write a Python program to sum all the numeric items in a list?
listB = [24,56,65,76,94]
Sum = int(sum(listB))
print(Sum)


# In[14]:


# Write a Python program to get the largest number from a numeric list.
listc = [24,56,65,76,94]
print("Largest element is:", listc[-1])


# In[31]:


# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)





# In[ ]:





# In[ ]:




