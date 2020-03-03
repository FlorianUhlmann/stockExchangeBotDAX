import pandas as pd
import numpy as np
import time
import datetime


#generate a dataframe in two steps
#1. time from 9-11 am
#2. time 23:59
#concat 1. && 2.

#start
# generate a dataframe from 9 till 11 o clock
#generate time time range from 9 to 11
date_range = pd.date_range('9:00', '11:00', freq='1Min').strftime('%H:%M')
#genrate a dataframe. amount of entries == data_range.length
df = pd.DataFrame(np.random.randint(1, 20, (date_range.shape[0], 0)))
#set the time from data_range into dataframe df
df.index = date_range  # set index
df_missing = df.drop(df.index[[1,3]])
# print(df_missing)
# #check for missing datetimeindex values based on reference index (with all values)
missing_dates = df.index[~df.index.isin(df_missing.index)]
# #
# generate dataframe with time 23:59
time_dax_close=pd.date_range('23:59', '23:59', freq='1Min').strftime('%H:%M')
df_end = pd.DataFrame(np.random.randint(1, 20, (time_dax_close.shape[0], 0)))
df_end.index = time_dax_close
# concat both times
dax_observation_time = pd.concat([df_end,df])

print(dax_observation_time)
