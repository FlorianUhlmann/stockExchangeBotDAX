#imports
import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)
import numpy as np

#read data from csv
df_DaxData = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_only_Close_values_UTC-5_test.csv',sep=',')

#iterate over all csv-file entries, one iteration takes 4 rows into account. 4 values(Close) are assigned to variables -> 40 rows in total = 10 iterations
    #compare 3 out of 4 variables
        # if  x1 < x2 < x3
            #compare x3 with x4
            # x3 < x3*30pt = x4 then ++tradewin
            # x3 < x4  then ++tradesuccessfull
            # x3 > x3*30pt = x4 then --tradelose
        # if x1 > x2 > x3
            #compare x3 with x4
            # x3 > x3*30pt = x4 then ++tradewin
            # x3 > x4  then ++tradesuccessfull
            # x3 < x3*30pt = x4 then --tradelose
        # ifelse
            #counter ++unexpectedresult


# df.to_numpy()
print(df_DaxData.head(15))




# df_9h_DAXopen_values= pd.DataFrame(data_9h_DAXopen,columns=['time','close'])
df_20hDAXclose = df_DaxData.loc[df_DaxData['time'] == '13:59']
df_8hDAXopen = df_DaxData.loc[df_DaxData['time'] == '02:00']
df_859hDAXstart = df_DaxData.loc[df_DaxData['time'] == '02:59']
df_11hDAXflat = df_DaxData.loc[df_DaxData['time'] == '05:00']

print(df_8hDAXopen)
print()
print(df_859hDAXstart)
print()
print(df_11hDAXflat)
print()
print(df_20hDAXclose)


df_concat_uncleaned = pd.concat([df_8hDAXopen, df_859hDAXstart,df_11hDAXflat, df_20hDAXclose])
df_DAXcleaned = df_concat_uncleaned.sort_index()

print(df_DAXcleaned)

'''
#check if list have same length
try:
   (len(df_8hDAXopen) == len(df_859hDAXstart)== df_11hDAXflat == df_20hDAXclose)
except:
    (
    print('the Input_data is inconsice')
    )
'''
Tradesuccess = 0
TradeMade = 0
TradeFail = 0
stockExchangeDay = 0
threshold = 10.0

for threshold in range(0,30 , 5):
    for i in range(len(df_20hDAXclose)):
        DAXclose = df_20hDAXclose.iloc[i,3]
        DAXopen  = df_8hDAXopen.iloc[i,3]
        DAXstart = df_859hDAXstart.iloc[i,3]
        DAXflat  =  df_11hDAXflat.iloc[i,3]
        stockExchangeDay += 1

        if(DAXclose  < (DAXopen - threshold) < (DAXstart - 3*threshold) ):
            TradeMade += 1
            if( DAXstart < DAXflat):
                Tradesuccess += 1
            else:
                TradeFail += 1

        if(DAXclose  > (DAXopen + threshold)  > (DAXstart + 3*threshold) ):
            TradeMade += 1
            if( DAXstart > DAXflat):
                Tradesuccess+= 1
            else:
                TradeFail += 1

    print('stockExchangeDays ' + str(stockExchangeDay))
    print('TradeMade ' + str(TradeMade))
    print('TradeSuccess ' + str(Tradesuccess))
    print('TradeFail ' + str(TradeFail))
    print()
    Tradesuccess = 0
    TradeMade = 0
    TradeFail = 0
    stockExchangeDay = 0




