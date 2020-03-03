
# coding: utf-8

# In[62]:


import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta


# In[44]:


HSI_TDDdata_raw = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/HAN_SENG_data/HSI_M1_2019/HSI_M1_2019_DemoDF_for_TDD.csv')
DAX_TDDdata_raw = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_DemoDF_for_TDD.csv')


# In[55]:


#transform date column from object to datetime
DAX_TDDdata_raw['date'] = pd.to_datetime(DAX_TDDdata_raw['date'], format='%Y.%m.%d')
HSI_TDDdata_raw['date'] = pd.to_datetime(HSI_TDDdata_raw['date'], format='%Y.%m.%d')


# In[56]:


HSI_TDDdata_raw.info()
HSI_TDDdata_raw.info


# In[259]:


#get all columns with DaxClose value
t = time(13, 59)
time_convert = t.strftime("%H:%M")
DAX_Close_only = DAX_TDDdata_raw.loc[DAX_TDDdata_raw['time'] == str(time_convert)]


# In[242]:


#get all dax values one day later
#print(DAX_Close_only['date'].iloc[0]+ timedelta(days=1))
DAX_DAY = DAX_TDDdata_raw.loc[DAX_TDDdata_raw['date'] == (DAX_Close_only['date'].iloc[0]+ timedelta(days=1))   ]
#remove 13:59h
DAX_DAY = DAX_DAY.loc[DAX_DAY['time'] != str(time_convert)]
print(DAX_DAY)
#get all dax values one day later
HSI_DAY= HSI_TDDdata_raw.loc[HSI_TDDdata_raw['date'] == (DAX_Close_only['date'].iloc[0]+ timedelta(days=1))   ]
print(HSI_DAY)


# In[260]:


# concat HSI and DAX values
HSI_DAX_concat = pd.concat([HSI_DAY,DAX_Close_only.iloc[0:1], DAX_DAY], ignore_index=True)


# In[261]:


#get close values of HSI_DAX_concat into a list
array_trainData_first_day =HSI_DAX_concat['close'].to_numpy()
#reshape numpy array (number,) -> (1,number)
array_trainData_first_day = np.reshape(array_trainData_first_day, (1, len(HSI_DAX_concat['close']) ))


# In[258]:


#prepare feature names ' HSI_00:00 , HSI_00:01 .....'
#get list of HSI operation time ' 00:00 , 00:01 .....'
list_HSI_minutes = HSI_DAY['time'].to_list()
# add string 'HSI_' to list of HSI operation time ' 00:00 , 00:01 .....' -> ' HSI_00:00 , HSI_00:01 .....'
list_featuresHSI = ['HSI_' + s for s in list_HSI_minutes]


# In[273]:


#prepare feature names ' DAX_close_preday_13:59, DAX_00:00 , DAX_00:01 .....'
list_featuresDAX = []
list_featuresDAX.append("DAX_close_preday_13:59")
#get list of HSI operation time ' 00:00 , 00:01 .....'
list_DAX_minutes = DAX_DAY['time'].to_list()
# add string 'HSI_' to list of HSI operation time ' 00:00 , 00:01 .....' -> ' DAX_00:00 , DAX_00:01 .....'
list_featuresDAX_incomplete = ['DAX_' + s for s in list_DAX_minutes]
list_featuresDAX = list_featuresDAX+ list_featuresDAX_incomplete
print(list_featuresDAX)


# In[274]:


#create TrainingData            
train_data = pd.DataFrame(array_trainData_first_day, columns=([list_HSI_minutes+list_featuresDAX]))
train_data.head(3)

