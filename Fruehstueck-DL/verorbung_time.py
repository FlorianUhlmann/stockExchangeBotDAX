import pandas as pd
import numpy as np
import time
import datetime
#generate time time range from
date_range = pd.date_range('9:00', '11:00', freq='1Min').strftime('%H:%M')


print(date_range)
#
df = pd.DataFrame(np.random.randint(1, 20, (date_range.shape[0], 0)))
print(df)
df.index = date_range  # set index
print(df)
df_missing = df.drop(df.index[[1,3]])
# print(df_missing)
# #check for missing datetimeindex values based on reference index (with all values)
missing_dates = df.index[~df.index.isin(df_missing.index)]
# #
print(missing_dates)