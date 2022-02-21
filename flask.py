#!/usr/bin/env python
# coding: utf-8

# # Routing using flask

# In[ ]:


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to UST'

if __name__ == '__main__':
    app.run()
    
#To see the output just open one more tab on your browser and type "localhost:5000"
#you will able to view output


# In[ ]:




