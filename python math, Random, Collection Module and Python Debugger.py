#!/usr/bin/env python
# coding: utf-8

# # Math module
# 
# Python comes with a built in math module and random module.
# 
# here i am going to discuss with some mathematical function that we can perfom in python like,
# 1) Math function
# 2) Ronding numbers
# 3) Mathematical constant
# 4) Logarithemic values
# 5) Trignometric functions
# 

# In[4]:


import math
help(math)


# # Rounding numbers

# In[5]:


value = 4.35


# In[6]:


math.floor(value) #it will display flor value


# In[7]:


math.ceil(value) #it will display ciel value


# In[8]:


round(value) #display round value


# # Mathematical Constent

# In[9]:


math.pi


# In[10]:


from math import pi


# In[12]:


math.e


# In[11]:


pi


# # Logarithemics

# In[13]:


math.log(math.e)


# In[14]:


math.log(math.10)


# In[15]:


#getting error if typing wrong
math.loh(10)


# In[16]:


math.log(10)


# # Trignometric

# In[17]:


math.sin(10)


# In[19]:


math.degrees(pi/2)


# In[20]:


math.radians(180)


# # Random module
# 
# Random Module allows us to create random numbers. We can even set a seed to produce the same random set every time.
# 
# 

# In[21]:


import random


# In[22]:


random.randint(0,100)


# In[23]:


mylist = list(range(0,20))


# In[24]:


mylist


# In[26]:


#select random chioce

random.choices(population=mylist, k=10)


# In[27]:


random.sample(population=mylist, k=10)


# In[28]:


#shuffle list
random.shuffle(mylist) 


# In[29]:


mylist


# # Collection module
# 
# The collections module is a built-in module that implements specialized container data types providing alternatives to Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.
# 
# Now we'll learn about the alternatives that the collections module provides.
# 1) OrderedDict
# 2) DefaultDict
# 3) Counter
# 4) Named Tuple
# 
# "Counter" is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

# In[32]:


from collections import Counter


# In[33]:


#count the how many time items are appers in the list.

lst = [1,2,2,2,2,2,4,4,5,6,7,8,9,8]


# In[34]:


Counter(lst)


# In[35]:


#count how many time string charecters appers in the list.
Counter('asdfdbkbfgklasfmdfgw')


# In[36]:


#display how many times words are apear.

s = "How many times does each word show up in this sentence word time each word each"
word = s.split()
Counter(word)


# In[38]:


c = Counter(word)
c.most_common(3)


# # defaultdict
# defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) as a default data type for the dictionary. 
# Using defaultdict is faster than doing the same using dict.set_default method.

# In[2]:


from collections import defaultdict


# In[3]:


d = {} #default


# In[4]:


d['one']


# In[5]:


d = defaultdict(object)
d['one']


# In[6]:


for item in d:
    print(item)


# # OrderedDict
# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

# In[7]:


print('Normal Dictionary')
d={}
d['a']='A'
d['b']='B'
d['c']='C'
d['d']='D'
d['e']='E'
d['f']='F'
for k,v in d.items():
    print(k,v)


# # Equality with an Ordered Dictionary
# A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

# In[8]:


print('Equality of Dictionary')
d1={}
d['a']='A'
d['b']='B'
d['c']='C'

d2={}
d['d']='D'
d['e']='E'
d['f']='F'
print(d1==d2)


# # namedtuple¶
# The standard tuple uses numerical indexes to access its members,

# In[10]:


t = (12,13,14)


# In[11]:


t[0]


# In[16]:


from collections import namedtuple


# In[17]:


dog = namedtuple('dog',['age','food','breed'])
sam = dog(age=12,food="yumm",breed="sammy")
shah = dog(age=3,food="mouthwatering",breed="shahu")


# In[18]:


sam


# In[19]:


shah


# In[20]:


shah.age


# In[21]:


shah.food


# In[22]:


shah[2]


# # Methods of debugging:
# 
# 1) assert(),
# 2) print(), 
# 3) pen and paper,
# 4) brakpoint(),
# 5) IDE (Integrated development environment),
# 6) pdb(),
# etc

# # Python Debugger
# You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). The pdb module implements an interactive debugging environment for Python programs. It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.

# In[23]:


# create an error on purpose, trying to add a list to an integer
x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)
result2 = y+x
print(result2)


# Hmmm, looks like we get an error! Let's implement a set_trace() using the pdb module. This will allow us to basically pause the code at the point of the trace and check if anything is wrong.

# In[24]:


import pdb

x = [1,2,3]
y = 2
z=4
result=y+z
print(result)

# Set a trace using Python Debugger

pdb.set_trace()
result1=x+y
print(result1)


# # To debug the code it will incorporate three most important things:
# 
# 1)  pause the program
# 2) look at the exicution of each line of code
# 3) check the values of varaible
# 
# 
# we can perform commands like,
# 
# c - continue exicution
# q - quit the exicution
# n - step to next line within same function
# s - step to next line in this fucntion or a called function
