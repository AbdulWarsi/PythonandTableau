#!/usr/bin/env python
# coding: utf-8

# Importing JSON file

# In[1]:


import pandas as pd


# In[2]:


import json


# Method 1 to read json data

# In[4]:


json_file = open(r"C:\Users\Dell\Downloads\loan_data_json.json")
df = json.load(json_file)


# In[5]:


df


# Method 2 to extract json file

# with open(r"C:\Users\Dell\Downloads\loan_data_json.json") as json_file:
#     data = json.load(json_file)
#     print(data)

# Transform to DataFrame

# In[26]:


df = pd.DataFrame(df)


# In[27]:


df


# # Finding unique values for the purpose column

# In[28]:


df["purpose"].unique()


# In[30]:


df.describe()


# In[31]:


df["int.rate"].describe()


# In[32]:


df["fico"].describe() #fico is Credit score


# fico seems fine(fico > 650 is considered good).

# In[33]:


df["dti"].describe() #debt to income ratio


# To get Annual Income we need to get "Exponent"  of log annual inc and for this we will use Numpy

# In[34]:


import numpy as np


# Using exp() to get annual income

# In[35]:


income = np.exp(df["log.annual.inc"])


# In[36]:


df["Annual Income"] = income


# In[37]:


df.head(3)


# fico = 700
# if fico >= 300 and fico<400:
#     ficocat = "Very poor"
# elif fico>=400 and fico < 600:
#     ficocat = "Poor"
# elif fico >= 600 and fico<660:
#     ficocat = "Fair"
# elif fico >= 660 and fico < 700:
#     ficocat = "Good"
# elif fico >= 700:
#     ficocat = "Excellent"
# else:
#     ficocat = "Unknown"
# print(ficocat)

# In[47]:


ficocat = []
for x in range(0,9578):
    category = df["fico"][x]
    if category >= 300 and category<400:
        cat = "Very poor"
    elif category>=400 and category < 600:
        cat = "Poor"
    elif category >= 600 and category<660:
        cat = "Fair"
    elif category >= 660 and category < 700:
        cat = "Good"
    elif category >= 700:
        cat = "Excellent"
    else:
        cat = "Unknown"
    ficocat.append(cat)


# In[48]:


ficocat


# In[53]:


ficocat = pd.Series(ficocat)


# In[54]:


df["ficocat"] = ficocat


# In[55]:


df.head()


# In[59]:


df["ficocat"].unique()


# In[62]:


df.loc[df["int.rate"] > .12, "int.rate.type"] = "High"
df.loc[df["int.rate"] < .12, "int.rate.type"] = "Low"


# In[63]:


df.head()


# In[68]:


import matplotlib.pyplot as plt
    


# In[73]:


catplot = df.groupby(["ficocat"]).size()


# In[74]:


catplot


# In[75]:


purposecount = df.groupby(["purpose"]).size()


# In[76]:


purposecount


# In[77]:


catplot.plot.bar()
plt.show()


# In[79]:


purposecount.plot.bar(color = "red")
plt.show()


# In[83]:


ypoint = df["Annual Income"]
xpoint = df["dti"]
plt.scatter(xpoint, ypoint, color = "#4caf50")
plt.show()


# Above Scatter plot represents that high level of Annual Income results in lesser DTI(debt to income ratio).

# Exporting file

# In[84]:


df.to_csv("loan_data.csv", index = True)


# In[ ]:




