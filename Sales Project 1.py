#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 


# In[6]:


a = pd.read_csv(r"C:\Users\Dell\Downloads\transaction.csv")


# In[97]:


a


# In[8]:


a.info()


# In[9]:


a.drop(a.iloc[:, 13:30], axis = 1, inplace = True)


# In[10]:


a.head(5)


# Now we'll add one more column i.e., "CostPerTransaction" which will be the multiple of "CostPerItem" and "NumberOfItemsPurchased".

# In[11]:


a["CostPerTransaction"] = a["CostPerItem"]*a["NumberOfItemsPurchased"]


# In[12]:


a.info()


# In[13]:


a.head(5)


# Now we can see a new column in our Data Frame i.e., "CostPerTransaction"

# In the same way we'll add one more column in our Data Frmae i.e., "SalesPertransaction" which will be the multiple of "SellingPricePerItem" and "NumberOfItemPurchased".

# In[14]:


a['SalesPerTransaction'] = a['SellingPricePerItem']*a['NumberOfItemsPurchased']


# In[15]:


a.head(4)


# Now we will calculate Profit and markup for transaction.
# 
# Formula:-
# 
# Profit:- Sales-Cost
# 
# Markup:- (Sale-cost)/cost

# In[16]:


a["ProfitPertransaction"] = a["SalesPerTransaction"] - a["CostPerTransaction"]


# In[17]:


a.head(3)


# In[18]:


a["Markup"] = (a["SalesPerTransaction"] - a["CostPerTransaction"])/a["CostPerTransaction"]


# In[19]:


a.head(3)


# Rounding Markups

# In[20]:


roundmarkup = round(a["Markup"], 2)


# In[21]:


a["Markup"] = round(a["Markup"], 2) 


# In[22]:


a.head(10)


# Combining Data Field

# First let's change data type

# In[23]:


day = a["Day"].astype(str)


# In[24]:


day.dtype


# In[25]:


year = a["Year"].astype(str)


# In[26]:


year.dtype


# In[27]:


Date = day + "-" + a["Month"] + "-" + year


# In[28]:


a["Date"] = Date


# In[29]:


a.head(3)


# In[30]:


a.iloc[0:5]


# In[31]:


a.iloc[0:10:2]


# In[32]:


a.iloc[2,3]


# In[66]:


a.drop(['ClientAge','ClientType'], axis=1, inplace = True)


# In[67]:


a.head(2)


# In[82]:


a.drop(["ClientKeywords"], axis =1 , inplace = True)


# In[83]:


a.head(1)


# In[84]:


a["ItemDescription"] = a["ItemDescription"].str.lower()


# In[85]:


a.head(1)


# In[87]:


b = pd.read_csv(r"C:\Users\Dell\Downloads\[FreeCourseSite.com] Udemy - Python and Tableau The Complete Data Analytics Bootcamp!\3. Python - Project 1 Value Inc. Sales Analysis\4.4 value_inc_seasons.csv")


# In[88]:


b


# Merging 2 files.
# 
# df1 = pd.merge(df_old, df_new, on = "key" 

# In[90]:


df = pd.merge(a,b, on = "Month")


# In[91]:


df.head(5)


# In[93]:


df1 = df.drop(["Day", "Year", "Month"], axis =1)


# In[98]:


df1


# Export into csv

# In[96]:


df1.to_csv("Sales Data.csv", index= False)


# Now we have exported our data in csv and will upload it on tableau.

# In[ ]:




