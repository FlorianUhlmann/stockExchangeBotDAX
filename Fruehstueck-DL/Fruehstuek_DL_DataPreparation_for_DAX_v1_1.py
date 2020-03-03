import pandas as pd
from datetime import datetime, time
# Set ipython's max row display
pd.set_option('display.max_row', 10)




class DataPreparation:
    def __init__(self,inputFile):
        self.inputFile = inputFile
        # self.df = pd.read_csv(self.inputFile,sep=';')
        # print(self.inputFile)
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')


    def showDataFrame(self):
        print(self.dataFrame)

    def removeDataInTimerange(self,stockData):

        #TODO überarbeiten mit "loc" methode
        #filter
        #   df_filtered2015 = df.loc[df['time']== '20:15']
        #   df_filtered2016 = df.loc[df['time']== '20:16']
        # Concat all df
        #   -> df.concat([df1, df2, df3 , .....])
        # set index in correct order
        #   df.sort_index()
        df= stockData

        #remove all times from 00:00 - 1:59 h
        for h in range(0, 2):
            for m in range(0, 60):
                t = time(h, m)
                time_convert = t.strftime("%H:%M")

                df = df.loc[df['time'] != str(time_convert)]

        #remove all times from 5:01 -13:58 ; 14:00 - 00:00
        for h in range(5, 24):
            for m in range(0, 60):
                if (h == 5 and m == 0) or (h==13 and m == 59):
                    continue

                t = time(h, m)
                time_convert = t.strftime("%H:%M")

                df = df.loc[df['time'] != str(time_convert)]
        StockDataProcessed = df
        return StockDataProcessed

    def removeColumns(self,stockData):

        # drop not needed columns
        stockData.drop(columns=['open', 'high', 'low', 'volume'], inplace=True)
        # oh.drop(oh.columns[[0]], axis=1,inplace=True)
        # reset the index to (0,1,2,3,4.....) and drop the old index ( 1,3,5,7.....)
        stockData.reset_index(inplace=True, drop=True)

        return stockData
    
    def setCloseColumnToFloat(self,stockData):

        stockData['close'] =  stockData['close'].astype(float)
        return stockData

    def saveDataFrame(self,stockData,placeToSave):

        stockData.to_csv(str(placeToSave),sep=',')

    def jobDone(self):
        print()
        print()
        print('Job Done')
        print()

def main():

    # DFtoPrepare = DataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv')
    DFtoPrepare = DataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019.csv')
    # DFtoPrepare.dataframe
    DFtoPrepare.showDataFrame()
    DFtoPrepare.dataFrame = DFtoPrepare.removeDataInTimerange(DFtoPrepare.dataFrame)
    DFtoPrepare.dataFrame = DFtoPrepare.removeColumns(DFtoPrepare.dataFrame)
    DFtoPrepare.dataFrame = DFtoPrepare.setCloseColumnToFloat(DFtoPrepare.dataFrame)
    DFtoPrepare.saveDataFrame(DFtoPrepare.dataFrame,'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_only_Close_values_UTC-5_test.csv')
    print(DFtoPrepare.dataFrame.dtypes)
    DFtoPrepare.jobDone()
main()


