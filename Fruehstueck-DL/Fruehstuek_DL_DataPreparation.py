import pandas as pd
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

    def removeDataInTimerange(self,stockDataToCut):

        #TODO überarbeiten mit "loc" methode
        #filter
        #   df_filtered2015 = df.loc[df['time']== '20:15']
        #   df_filtered2016 = df.loc[df['time']== '20:16']
        # Concat all df
        #   -> df.concat([df1, df2, df3 , .....])
        # set index in correct order
        #   df.sort_index()
        oh= stockDataToCut

        for hh in range(0, 2):
            for mm in range(0, 60):
                mm_digits = len(str(mm))
                if mm_digits < 2:
                    oh = oh[oh.time != "0%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "0%d:%d" % (hh, mm)]

        for hh in range(5, 10):
            for mm in range(0, 60):
                mm_digits = len(str(mm))
                if mm==00 and hh==5:
                    continue
                if mm_digits < 2:
                    oh = oh[oh.time != "0%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "0%d:%d" % (hh, mm)]
        print(oh.head(10))
        '''
        for hh in range(2, 3):
            for mm in range(1, 60):
                mm_digits = len(str(mm))
                if mm_digits < 2:
                    oh = oh[oh.time != "0%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "0%d:%d" % (hh, mm)]
        print(oh.head(10))
        '''
        for hh in range(3, 5):
            for mm in range(1, 60):
                mm_digits = len(str(mm))
                if mm_digits < 2:
                    oh = oh[oh.time != "%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "%d:%d" % (hh, mm)]
        print(oh.head(10))


        for hh in range(5, 9):
            for mm in range(1, 60):
                mm_digits = len(str(mm))
                if mm_digits < 2:
                    oh = oh[oh.time != "%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "0%d:%d" % (hh, mm)]

        for hh in range(10, 25):
            for mm in range(0, 60):
                mm_digits = len(str(mm))
                if mm == 00 and hh == 5:
                    continue
                if mm == 59 and hh == 13:
                    continue
                if mm_digits < 2:
                    oh = oh[oh.time != "%d:0%d" % (hh, mm)]
                else:
                    oh = oh[oh.time != "%d:%d" % (hh, mm)]

        # """
        # drop rows with 11:00 o clock in it
        #oh = oh[oh.time != '11:00']

        StockDataProcessed = oh
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

    # DFtoPrepare = DataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/zz_boersendaten/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_Raw.csv')
    DFtoPrepare = DataPreparation('D:/Profiles/fuhlmann/Programmierung/Python/zz_boersendaten/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019.csv')
    # DFtoPrepare.dataframe
    DFtoPrepare.showDataFrame()
    DFtoPrepare.dataFrame = DFtoPrepare.removeDataInTimerange(DFtoPrepare.dataFrame)
    DFtoPrepare.showDataFrame()
    DFtoPrepare.dataFrame = DFtoPrepare.removeColumns(DFtoPrepare.dataFrame)
    DFtoPrepare.saveDataFrame(DFtoPrepare.dataFrame,'D:/Profiles/fuhlmann/Programmierung/python/zz_boersendaten/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_only_Close_values_UTC-5.csv')
    DFtoPrepare.jobDone()

main()


