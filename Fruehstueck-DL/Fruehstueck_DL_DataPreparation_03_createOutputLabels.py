import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta
# überlegen alle hardcoded werte in paramterliste zu schreiben

class OutputDataGenerator():
    def __init__(self, DataFrameLocation):
        self.DataFrameLocation = DataFrameLocation
        self.DataFrame_input = pd.read_csv(self.DataFrameLocation, sep=',')

    def showDataFrameRaw(self):
        print(self.DataFrame_input)

    def infoDataFrameRaw(self):
        print(self.DataFrame_input.info())

    def createOutputDataFrame(self, dataFrameRaw):
        #gucken ob unterfunktionen anders aufbaubar sind - python knwoledge
        def sliceRawDataToRelevantDAXData(dataFrame):
            #hardocded numbers in variablen namen ändern
            DAXbegin = dataFrame.iloc[:, 182:184]
            DAXend = dataFrame.iloc[:, 242:]
            relevantDaxData = pd.concat([DAXbegin, DAXend], axis=1)
            return relevantDaxData
        def createDataFrameWithTradingDayInfo(DataFrameRelevantDAXData):
            DF_DAX = DataFrameRelevantDAXData
            DataFrame_TraidingAdvice = pd.DataFrame([],columns=('DAX_BUY_DAY','DAX_SELL_DAY','NO_TRADE_DAY'))
            Tradesuccess = 0
            TradeMade = 0
            TradeFail = 0
            DAX_BUY_DAY = 0
            DAX_SELL_DAY = 0
            NO_TRADE_DAY =0
            stockExchangeDay = 0
            threshold = 10

            for row,index in DF_DAX.iterrows():

                DAXclose = index['DAX_close_preday_13:59']
                DAXopen     = index['DAX_02:00']
                DAXstart = index['DAX_02:59']
                DAXflat = index['DAX_05:00']
                #TradeDay Case BUY signal
                if (DAXclose < (DAXopen - threshold) < (DAXstart - 3 * threshold)):
                    TradeMade += 1
                    if (DAXstart < DAXflat):
                        Tradesuccess += 1
                        DAX_BUY_DAY = 1
                    else:
                        TradeFail += 1
                        NO_TRADE_DAY = 0
                #TradeDay Case SELL signal
                elif (DAXclose > (DAXopen + threshold) > (DAXstart + 3 * threshold)):
                    TradeMade += 1
                    if (DAXstart > DAXflat):
                        Tradesuccess += 1
                        DAX_SELL_DAY = 1
                    else:
                        TradeFail += 1
                        NO_TRADE_DAY = 0
                else:
                    NO_TRADE_DAY = 1



                f = pd.Series(np.array([DAX_BUY_DAY, DAX_SELL_DAY, NO_TRADE_DAY]), index=('DAX_BUY_DAY', 'DAX_SELL_DAY', 'NO_TRADE_DAY'))
                DataFrame_TraidingAdvice = DataFrame_TraidingAdvice.append(f, ignore_index=True, sort=True)

                DAX_BUY_DAY = 0
                DAX_SELL_DAY = 0
                NO_TRADE_DAY = 0

            print('stockExchangeDays ' + str(stockExchangeDay))
            print('TradeMade ' + str(TradeMade))
            print('TradeSuccess ' + str(Tradesuccess))
            print('TradeFail ' + str(TradeFail))
            print()

            return DataFrame_TraidingAdvice
        def mergeInputAndOutputDataFrame(dataframeRaw, outputDataFrame):
            return dataFrameRaw.join(outputDataFrame)

        # cut dataframe - get only dax data DAX_closePreday,DAX_open,DAX_start,DAX_03:00 - DAX_05:00
        slicedDataFrame = sliceRawDataToRelevantDAXData(dataFrameRaw)
        outputDataFrame = createDataFrameWithTradingDayInfo(slicedDataFrame)
        trainingDataFrame = mergeInputAndOutputDataFrame(dataFrameRaw,outputDataFrame)

        return trainingDataFrame

    def saveDataFrame(self, trainingsDataFrame, pathSaveDataFrame):

        trainingsDataFrame.to_csv(str(pathSaveDataFrame), sep=',',index = False)


def main():

    pathDataFrame = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/Fruehstueck_training_data_2019_january.csv'
    pathSaveDataFrame = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Fruehstueck-DL/DataFrameTrainingDataForAI_2019_january.csv'

    createOutput = OutputDataGenerator(pathDataFrame)
    trainingDataFrame = createOutput.createOutputDataFrame(createOutput.DataFrame_input)
    #trainingDataFrame  als Property in classe speichern.
    createOutput.saveDataFrame(trainingDataFrame,pathSaveDataFrame)

main()