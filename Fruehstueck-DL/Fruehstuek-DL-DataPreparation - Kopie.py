
# coding: utf-8

# In[174]:


import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)


#oh = pd.read_csv('./Programmierung/Python/zz_boersendaten/Börsendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv')
#oh = pd.read_csv('Programmierung/python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv',sep=';');
#D:\Profiles\fuhlmann\Programmierung\Python\zz_boersendaten\Boersendaten\DAX30_TimeFrameMin_M1_CandleData_Raw.csv





oh = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/Python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv',
                 sep=';' )  # doctest: +SKIP
#print(oh.index);
print(oh.head(2))

#oh.columns['date', 'time', 'open', 'high', 'low', 'close', 'volume'];
print(oh.loc[0:2, ['date', 'time', 'close']])

oh = oh[oh.time != '02:15']
oh_timeCleaned = oh[oh.time != '02:16']

print(oh_timeCleaned.loc[0:4, ['date', 'time', 'close']])

"""
def removeTimeIntervall(timesSeriesObject, startHour,startMin, stopHour, stopMin ):
    for hh in range(startHour, stopHour):
        for mm in range(startMin, stopMin):
            mm_digits = len(str(mm))
            if mm_digits < 2:
                timesSeriesObject = timesSeriesObject[timesSeriesObject.time != "0%d:0%d" % (hh, mm)]
            else:
                timesSeriesObject = timesSeriesObject[timesSeriesObject.time != "0%d:%d" % (hh, mm)]
"""

for hh in range(0, 9):
    for mm in range(00, 60):
        mm_digits = len(str(mm))
        if mm_digits < 2:
            oh = oh[oh.time != "0%d:0%d" % (hh, mm)]
        else:
            oh = oh[oh.time != "0%d:%d" % (hh, mm)]

# """


for hh in range(9, 10):
    for mm in range(1, 60):
        mm_digits = len(str(mm))
        if mm_digits < 2:
            oh = oh[oh.time != "0%d:0%d" % (hh, mm)]
        else:
            oh = oh[oh.time != "0%d:%d" % (hh, mm)]


for hh in range(10, 12):
    for mm in range(1, 60):
        mm_digits = len(str(mm))
        if mm_digits < 2:
            oh = oh[oh.time != "%d:0%d" % (hh, mm)]
        else:
            oh = oh[oh.time != "%d:%d" % (hh, mm)]



for hh in range(12, 24):
    for mm in range(0, 60):
        mm_digits = len(str(mm))
        if mm==59 and hh==22:
            continue
        elif mm==00 and hh==12:
            continue
        elif mm_digits < 2:
            oh = oh[oh.time != "%d:0%d" % (hh, mm)]
        else:
            oh = oh[oh.time != "%d:%d" % (hh, mm)]
# """
#drop rows with 11:00 o clock in it
oh = oh[oh.time != '11:00']

#drop not needed columns
oh.drop(columns=['open','high','low','volume'],inplace=True)
#oh.drop(oh.columns[[0]], axis=1,inplace=True)
#reset the index to (0,1,2,3,4.....) and drop the old index ( 1,3,5,7.....)
oh.reset_index(inplace=True,drop=True)
#save the new dataframe
oh.to_csv(
    'D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Cleaned_Just_Market_Time_from_CLOSE_to9am_plus_11am_GTM+1.csv',
    sep=';')

