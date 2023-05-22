#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# *In this notebook, Data Science Tools and Ecosystem are summarized.*

# **Objectives:**
# 
# - List popular languages for Data Science.
# - Some of the commonly used libraries used by Data Scientists.
# - Examples of evaluating arithmetic expressions in Python.
# - Provide an overview of the Data Science workflow.
# - Introduce common data manipulation and analysis techniques.

# ### Some of the popular languages that Data Scientists use are:

# In[4]:


languages = ['Python', 'R', 'Julia']
ordered_list = [f"{index}. {language}" for index, language in enumerate(languages, start=1)]
print("\n".join(ordered_list))


# ### Some of the commonly used libraries used by Data Scientists include:

# In[3]:


libraries = ['NumPy', 'Pandas', 'scikit-learn']
ordered_list = [f"{index}. {library}" for index, library in enumerate(libraries, start=1)]
print("\n".join(ordered_list))


# | Data Science Tools |
# |-------------------|
# | Jupyter Notebook  |
# | Anaconda          |
# | PyCharm           |

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[8]:


#Addition
3 + 4


# In[9]:


#Subtraction
8 - 5


# In[10]:


#Multiplication
2 * 6


# In[11]:


#Division
10 / 2


# In[12]:


#Exponentiation
2 ** 3


# In[13]:


(3*4)+5
#This a simple arithmetic expression to mutiply then add integers.


# In[15]:


minutes = 200
hours = minutes / 60
hours
#This will convert 200 minutes to hours by diving by 60.


# ## Author
#  Yuvaraj
