from datetime import time
import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)


class DataPreparationHSI:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        # self.df = pd.read_csv(self.inputFile,sep=';')
        # print(self.inputFile)
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')

    def showDataFrame(self):
        print(self.dataFrame)

    def removeDataInTimerange(self, stockDataToCut):

        df= stockDataToCut

        #remove all times from 00:00 - 1:59 h
        for h in range(5, 24):
            for m in range(0, 60):
                if (h == 5 and m == 0):
                    continue
                t = time(h, m)
                time_convert = t.strftime("%H:%M")

                df = df.loc[df['time'] != str(time_convert)]

        stockDataProcessed = df
        return stockDataProcessed

    def removeColumns(self,stockDataToCut):

        # drop not needed columns
        stockDataToCut.drop(columns=['open', 'high', 'low', 'volume'], inplace=True)
        # oh.drop(oh.columns[[0]], axis=1,inplace=True)
        # reset the index to (0,1,2,3,4.....) and drop the old index ( 1,3,5,7.....)
        stockDataToCut.reset_index(inplace=True, drop=True)

        return stockDataToCut

    def saveDataFrame(self, stockData, placeToSave):
        def jobDoneMsg():
            print()
            print()
            print('Job Done')
            print('DataFrame Saved in ' + placeToSave)
            print()

        stockData.to_csv(str(placeToSave), sep=',')
        jobDoneMsg()


def main():

    pathRawDataFrameDAX = 'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/HSI_data/HSI_M1_2018/HSI_M1_2018.csv'
    savingpathFormatedDataFrameHSI = 'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/HSI-_data/HSI_M1_2018/HSI_M1_2018_CLOSE_UTC-5_NewTry.csv'

    DFtoPrepare = DataPreparationHSI(pathRawDataFrameDAX)
    DFtoPrepare.showDataFrame()
    DFtoPrepare.dataFrame = DFtoPrepare.removeDataInTimerange(DFtoPrepare.dataFrame)
    DFtoPrepare.dataFrame = DFtoPrepare.removeColumns(DFtoPrepare.dataFrame)
    DFtoPrepare.saveDataFrame(DFtoPrepare.dataFrame, savingpathFormatedDataFrameHSI)
    DFtoPrepare.dataFrame.info()


main()

'''
start = df_HSI.date.searchsorted(datetime.datetime(2018, 2, 1))
end = df_HSI.date.searchsorted(datetime.datetime(2018, 3, 1))
df_HSI_february = df_HSI.iloc[start:end]
df_HSI_february.to_csv('D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/HSI_data/HSI_M1_2018/HSI_M1_2018_02_february_cleanedData.csv', sep=',', index=False)

start = df_DAX.date.searchsorted(datetime.datetime(2018, 2, 1))
end = df_DAX.date.searchsorted(datetime.datetime(2018, 3, 1))
df_DAX_february = df_DAX.iloc[start:end]
df_DAX_february.to_csv('D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2018/DAX_M1_2018_02_february_cleanedData.csv', sep=',', index=False)
'''