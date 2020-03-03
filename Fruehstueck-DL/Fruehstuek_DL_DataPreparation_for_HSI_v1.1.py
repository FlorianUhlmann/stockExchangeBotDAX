import pandas as pd
from datetime import datetime, time
# Set ipython's max row display
pd.set_option('display.max_row', 10)




class HsiDataPreparation:
    def __init__(self,inputFile):
        self.inputFile = inputFile
        # self.df = pd.read_csv(self.inputFile,sep=';')
        # print(self.inputFile)
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')


    def showDataFrame(self):
        print(self.dataFrame)

    def removeDataInTimerange(self,stockDataToCut):

        #TODO überarbeiten mit "loc" methode
        #filter
        #   df_filtered2015 = df.loc[df['time']== '20:15']
        #   df_filtered2016 = df.loc[df['time']== '20:16']
        # Concat all df
        #   -> df.concat([df1, df2, df3 , .....])
        # set index in correct order
        #   df.sort_index()
        df= stockDataToCut

        #remove all times from 00:00 - 1:59 h
        for h in range(5, 24):
            for m in range(0, 60):
                if (h == 5 and m == 0):
                    continue
                t = time(h, m)
                time_convert = t.strftime("%H:%M")

                df = df.loc[df['time'] != str(time_convert)]

        StockDataProcessed = df
        return StockDataProcessed

    def removeColumns(self,stockDataToCut):

        # drop not needed columns
        stockDataToCut.drop(columns=['open', 'high', 'low', 'volume'], inplace=True)
        # oh.drop(oh.columns[[0]], axis=1,inplace=True)
        # reset the index to (0,1,2,3,4.....) and drop the old index ( 1,3,5,7.....)
        stockDataToCut.reset_index(inplace=True, drop=True)

        return stockDataToCut

    def saveDataFrame(self,stockData,placeToSave):

        stockData.to_csv(str(placeToSave),sep=',')

    def jobDone(self):
        print()
        print()
        print('Job Done')
        print()

def main():

    # DFtoPrepare = HsiDataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv')
    DFtoPrepare = HsiDataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/zz_boersendaten/Boersendaten/HAN_SENG_data/HSI_M1_2019/HSI_M1_2019.csv')
    # DFtoPrepare.dataframe
    DFtoPrepare.showDataFrame()
    DFtoPrepare.dataFrame = DFtoPrepare.removeDataInTimerange(DFtoPrepare.dataFrame)
    DFtoPrepare.dataFrame = DFtoPrepare.removeColumns(DFtoPrepare.dataFrame)
    DFtoPrepare.jobDone()
    DFtoPrepare.dataFrame.info()
main()


