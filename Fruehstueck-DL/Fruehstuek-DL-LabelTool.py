
import pandas as pd
import numpy as np
# Set ipython's max row display
pd.set_option('display.max_row', 10)


#oh = pd.read_csv('./Programmierung/Python/zz_boersendaten/Börsendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv')
#oh = pd.read_csv('Programmierung/python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv',sep=';');
#D:\Profiles\fuhlmann\Programmierung\Python\zz_boersendaten\Boersendaten\DAX30_TimeFrameMin_M1_CandleData_Raw.csv





oh = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Cleaned_Just_Market_Time_from_CLOSE_to11am_GTM+1.csv',
                    sep=';' )

# print(oh);

# print(oh.columns);
oh.drop(['Unnamed: 0','open','high','low','volume'],inplace = True, axis=1)
# print(oh.columns)
print(oh)



# oh.to_csv(
#     'D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Cleaned_Just_date_time_close.csv',
#     sep=';')
"""
         date   time    close
0  2019.01.02  22:59  10575.2
"""

"""
ToDO 1:
    get Array
    
ToDO 2:
    Take X9 as xo
    
ToDO 3:
    compare X9 to X11
        -> alwayshigher
        -> betweener
        -> lower
        
ToDO 4:
    Output Array
    _  _
    |  alaysyhigher |  bool
    |   betweener   |  bool
    |   lower       |  bool
    |   x1          |
    |    ..         |
    |    xn         |
    -              -
"""