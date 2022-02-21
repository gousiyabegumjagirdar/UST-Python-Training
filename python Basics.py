#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keyword
keyword.kwlist


# In[2]:


keyword.iskeyword('try')


# In[3]:


keyword.iskeyword('gousiya')


# In[5]:


name - 'gousiya'
my_identifire - name


# In[6]:


# this is a comment


# In[7]:


s = 10
print(s)


# In[8]:


a = 10
def function():
    global a
    a += 10
    print(a)
print(a)
function()

    


# In[10]:


#list
my_list = ["RCB","CSK","MI","RCB","CSK","MI"]
print(my_list)


# In[11]:


len(my_list)


# In[12]:


print(len(my_list))


# In[13]:


list1 = ["India","Austrelia","England"]
list2 = [1,2,3,4,5]
list3 = [True,False]
print(list1,list2,list3)


# In[14]:


list1 = ["India","Austrelia","England",1,2,3,4,5,"male","Female"]
print(list1)


# In[16]:


#Tuple
tuple1 = ("India","Austrelia","America")
print(tuple1)


# In[23]:


my_tuple = ("RCB","CSK","MI","RCB","CSK","MI","DD")
print(my_tuple)


# In[24]:


print(len(my_tuple))


# In[25]:


# sets
set = {"RCB","CSK","MI","RCB","CSK","MI"}
print(set)


# In[26]:


set = {"India","Austrelia","England",1,2,3,4,5,"male","Female"}
print(set)


# In[27]:


set = {"India","Austrelia","England",1,2,3,4,5,"male","Female","true","false"}
print(set)


# In[32]:


list = ["Aus","Ind","Pak","Eng",1,2,3,4,5]
set = {"Aus","Ind","Pak","Eng",1,2,3,4,5}
tuple = ("Aus","Ind","Pak","Eng",1,2,3,4,5)
print(list,set,tuple)
print(len(list))
print(len(set))
print(len(tuple))


# In[38]:


#Converting list to Tuple
list = ["hi","hello","WRU",1,2,3,4]
tuple = (list)
print(tuple)


# In[46]:


x = ("CSK","RCB","MI")
y = x
y = "Gousiya"
x = y

print(y)


# In[6]:


x = 10 

assert x > 10 

print(x)


# In[3]:


x = 5

assert x < 10 

print(x)


# In[ ]:


def functionB(first_val=2, last_val=2):
    # we would print() here to check the code inside our funtion is getting  executed or not by printing any thing
    print("i am working perfectly")
    response = functionB(first_val, last_val)
    result = response * first_val / 2
    return result


functionB(3, 8)


# In[2]:


x = 10
assert x<=10
print(x)


# In[5]:


x = 10
assert x<=10
print(x)


# In[6]:


x = [1,2,3]
y = 3
z = 6
r = y+z
print(r)

r1 = x+z
print(r1)


# In[7]:


import pdb

x = [1,2,3]
y = 3
z = 6
r = y+z
print(r)
pdb.set_trace()
r1 = x+z
print(r1)


# In[ ]:




