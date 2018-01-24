
# coding: utf-8

# ###### Importing the important packages
# 

# In[119]:


# importing the important packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# ###### Reading the data

# In[30]:


# Reading the inputs
crimetrain=pd.read_csv("C:/Users/USER/Desktop/MS in Business Analytics/Python/SF Crime Classification/SFcrimetrain.csv",
                       parse_dates=['Dates'])
crimetest= pd.read_csv("C:/Users/USER/Desktop/MS in Business Analytics/Python/SF Crime Classification/SFcrimetest.csv",
                        parse_dates=['Dates'])


# ###### Reading the column names of both train and test dataset

# In[121]:


# Columns of Training dataset
print(list(crimetrain.columns.values))
# Columns of Test dataset
print(list(crimetest.columns.values))


# ###### Data type of train and test dataset columns.

# In[125]:


# Datatypes of training dataset
print(' Datatype of training dataset')
print(crimetrain.dtypes)
print('\n')

# Datatypes of test dataset
print(' Datatype of test dataset')
print(crimetest.dtypes)


# ###### First few rows of training and test datasets

# In[15]:


crimetrain.head()


# In[16]:


crimetest.head()


# ###### Shape of the datasets - train and test

# In[17]:


crimetrain.shape


# In[18]:


crimetest.shape


# ###### Dataset information - train & test

# In[19]:


crimetrain.info()


# In[20]:


crimetest.info()


# ###### Checking the dataset for the missing values

# ###### There seems to be no missing value in the dataset

# In[101]:


crimetrain.isnull().any()


# In[22]:


crimetest.isnull().sum()


# ###### Crime Frequency in San Francisco by Category

# In[7]:


get_ipython().magic('matplotlib inline')
crimetrain.Category.value_counts().plot(kind="bar",figsize=(15,5),alpha=0.55)
plt.title("Crime Frequency in San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# ###### Crime Frequency per district

# In[8]:



crimetrain.groupby(["PdDistrict","Category"]).size()


# In[128]:


crimetrain.PdDistrict.sort_values().unique()


# Most of the other offenses occurs in Bayview, Ingleside and Mission.
# 
# Larceny/Theft occurs mostly in Park , Taraval,Central,Richmond, Southern and Northern districts.
# 
# Drugs and narcotics seems to be prevalent in Tenderloin area.

# In[115]:


bayview= crimetrain.loc[crimetrain.PdDistrict == "BAYVIEW"]
bayview.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Bayview district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[120]:


tenderloin= crimetrain.loc[crimetrain.PdDistrict == "TENDERLOIN"]
tenderloin.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Tenderloin district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[129]:


central= crimetrain.loc[crimetrain.PdDistrict == "CENTRAL"]
central.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Central district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[130]:


ingleside= crimetrain.loc[crimetrain.PdDistrict == "INGLESIDE"]
ingleside.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Ingleside district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[131]:


mission= crimetrain.loc[crimetrain.PdDistrict == "MISSION"]
mission.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Mission district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[132]:


northern= crimetrain.loc[crimetrain.PdDistrict == "NORTHERN"]
northern.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Northern district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[133]:


park= crimetrain.loc[crimetrain.PdDistrict == "PARK"]
park.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Park district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[134]:


richmond= crimetrain.loc[crimetrain.PdDistrict == "RICHMOND"]
richmond.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Richmond district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[135]:


southern= crimetrain.loc[crimetrain.PdDistrict == "SOUTHERN"]
southern.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Southern district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# In[136]:


taraval= crimetrain.loc[crimetrain.PdDistrict == "TARAVAL"]
taraval.Category.value_counts().plot(kind="bar",figsize=(7,3),alpha=0.55)
plt.title("Crime Frequency in Taraval district of San Francisco")
plt.ylabel("Count")
plt.xlabel("Crime Category")
plt.show()


# From year 2003 till 2014, the crimes in San francisco seems to be pretty high 
# but in year 2015, there seem to be a sharp fall. 
# 

# In[44]:


crimetrain['Date'] = pd.to_datetime(crimetrain['Dates'].dt.date)
crimetrain['Year'] = crimetrain['Dates'].dt.year


# In[93]:


crimetrain.head()
yearlycrime= pd.DataFrame(data=crimetrain.groupby('Year').size())
yearlycrime.plot()
plt.ylabel('Crime Frequency')
plt.xticks(np.arange(2003,2018,2),rotation='vertical');

