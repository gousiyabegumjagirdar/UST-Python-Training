#!/usr/bin/env python
# coding: utf-8

# # File handling:

# In[1]:


import csv


# In[3]:


with open('new.csv') as i:
    f_read = i.read()
    print(f_read)


# In[6]:


w = open('new.csv') 
read = csv.reader(w)
for i in read:
    print(i)


# In[11]:


#slicing new.csv file

w = open('new.csv')
read = csv.reader(w)
sli = list(read)
for i in sli[1:5]:
    print(i)


# In[13]:


#display the lenght of the file

w = open('new.csv')
read = csv.reader(w)
sli = list(read)
print(len(sli))


# In[20]:


#file appending

w = open('new.csv')
read = csv.reader(w)
sli = list(read)
apend = ["Shahzaib","Mustaqeem"]
for i in sli[1:]:
     apend.append(i[0])
print(apend)


# In[22]:


#fulname in append

w = open('new.csv')
read = csv.reader(w)
sli = list(read)
full_name = []
for i in sli[1:]:
    full_name.append(i[0]+' '+i[1])
print(full_name)    


# In[28]:


#first install PyPDF2 library open your cmd and type command pip install pypdf2

import PyPDF2
with open('Set Data Structure.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)


# In[29]:


with open('Set Data Structure.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    page=pdf_reader.numPages   #numPages is used to find no of pages present in the pdf
    print(page)


# In[30]:


import PyPDF2
# from PyPDF2 import PdfFileReader
with open('Set Data Structure.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    page_one=pdf_reader.getPage(2)#assigning page number
    ex_text=page_one.extractText()#extracting text for assigned page no
    print(ex_text)


# In[32]:


#     copy pages and append pages to new pdf
with open('Set Data Structure.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    page_one=pdf_reader.getPage(0)
    pdf_writer=PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output= open('copy.pdf','wb')
    pdf_writer.write(pdf_output)
    pdf_output.close


# In[33]:


# read all the text from pdf file
with open('Set Data Structure.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    f = open('Set Data Structure.pdf','rb')
    text = []
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)    
        text.append(page.extractText())
    # print(text)#prin all text
    print(text[2])#perticular page


# In[ ]:




