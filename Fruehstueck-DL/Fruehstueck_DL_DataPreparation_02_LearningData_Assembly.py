import numpy as np
import pandas as pd
from datetime import time, timedelta, date, datetime


class LearningDataAssembly:
    """
    This class creates a DataFrame.

    The DataFrame is for the Training of a NeuralNet.
    The shape of the Dataframe ist (a x 437) - a = one traiding day | 437 amount of features
    """

    def __init__(self, HSI_DataFrame, DAX_DataFrame):
        self.HSI_DataFrame = HSI_DataFrame
        self.DAX_DataFrame = DAX_DataFrame
        self.hsi_DataFrame_rawData = pd.read_csv(self.HSI_DataFrame, sep=',')
        self.dax_DataFrame_rawData = pd.read_csv(self.DAX_DataFrame, sep=',')

    def showDataFrameRaw(self):
        print(self.hsi_DataFrame_rawData)
        print(self.dax_DataFrame_rawData)

    def createTrainingdataDataFrame(self, hsi_DataFrame_rawData, dax_DataFrame_rawData):

        def setDateColumnToDtypeDate():
            hsi_DataFrame_rawData['date'] = pd.to_datetime(hsi_DataFrame_rawData['date'], format='%Y.%m.%d')
            dax_DataFrame_rawData['date'] = pd.to_datetime(dax_DataFrame_rawData['date'], format='%Y.%m.%d')

            return (hsi_DataFrame_rawData, dax_DataFrame_rawData)

        def createDataFrameWithOnlyDaxCloseTimes(dax_DataFrame):
            # get all columns with DaxClose value
            closeTimeDAX = time(13, 59)
            closeTimeDAX = closeTimeDAX.strftime("%H:%M")
            DAX_Close_only = dax_DataFrame.loc[dax_DataFrame['time'] == str(closeTimeDAX)]
            return DAX_Close_only

        def createArrayTrainingData(DAX_Close_only, hsi_DataFrame, dax_DataFrame):

            def calculateTradingDaysFromDAX_Close_only():
                #DAX_CLose_only has the close price of the previous trading day. Important is the date of the trading day
                #it is needed to calculate the acutal trading day
                 df =  DAX_Close_only.apply(lambda x: x['date'] + pd.tseries.offsets.BusinessDay(n=1), axis=1)
                 return df
            def createArrTrainData(df_tradingDays):
                for DAXCloseDate in range(0, len(df_tradingDays)):

                    def getDAXTradingDayValues():
                        # print(DAX_Close_only['date'].iloc[0]+ timedelta(days=1))
                        DAX_DAY = dax_DataFrame.loc[dax_DataFrame['date'] == df_tradingDays.iloc[DAXCloseDate]]
                        # remove 13:59h
                        return DAX_DAY.loc[DAX_DAY['time'] != str(time(13, 59).strftime("%H:%M"))]

                    def getHSITradingDayValues():
                        # get all HSI values one day later
                        HSI_DAY = hsi_DataFrame.loc[hsi_DataFrame['date'] == df_tradingDays.iloc[DAXCloseDate]]
                        return HSI_DAY

                    def join_HSI_DAX_TradingDayValues():
                        HSI_DAX_concat = pd.concat([HSI_DAY, DAX_Close_only.iloc[0:1], DAX_DAY], ignore_index=True)
                        return HSI_DAX_concat

                    def getIndexValue():
                        # get the trading day in stringFormat from the HSI_data
                        TRAIDING_DAY = HSI_DAY['date'].iloc[0].strftime("%Y-%m-%d")
                        return TRAIDING_DAY

                    def joinIndexValueAnd_HSI_DAX__TradingDayValues():
                        def changeShapeArrayHSIDAXData():
                            # get close values of HSI_DAX_concat into a list
                            array_trainData_first_day = HSI_DAX_concat['close'].to_numpy()
                            array_trainData_first_day.astype(float)
                            # reshape numpy array (number,) -> (1,number)
                            array_trainData_first_day = np.reshape(array_trainData_first_day,
                                                                   (1, len(HSI_DAX_concat['close'])))
                            # concat tradingDate to array_trainngData_first_day
                            return array_trainData_first_day

                        HSI_DAX_data = changeShapeArrayHSIDAXData()
                        array_trainData_first_day = np.concatenate((TRAIDING_DAY, HSI_DAX_data), axis=None)
                        return array_trainData_first_day

                    DAX_DAY = getDAXTradingDayValues()
                    HSI_DAY = getHSITradingDayValues()
                    HSI_DAX_concat = join_HSI_DAX_TradingDayValues()
                    TRAIDING_DAY = getIndexValue()
                    array_trainData_buffer = joinIndexValueAnd_HSI_DAX__TradingDayValues()

                    if DAXCloseDate == 0:
                        array_trainData = array_trainData_buffer
                        print('if blocl')

                        print(array_trainData)
                    else:
                        array_trainData = np.vstack((array_trainData, array_trainData_buffer))
                        print('else blocl')

                return array_trainData

            array_trainData = []

            df_tradingDays = calculateTradingDaysFromDAX_Close_only()
            array_trainData =  createArrTrainData(df_tradingDays)
            return array_trainData

        def featureListGeneration(hsi_DataFrame, dax_DataFrame):

            def createDataFrameWithOnlyDaxCloseTimes():
                # get all columns with DaxClose value
                t = time(13, 59)
                time_convert = t.strftime("%H:%M")
                DAX_Close_only = dax_DataFrame.loc[dax_DataFrame['time'] == str(time_convert)]
                return DAX_Close_only

            DAX_Close_only = createDataFrameWithOnlyDaxCloseTimes()

            def generateListFeaturesDAX(DAX_DAY):
                # prepare feature names ' DAX_close_preday_13:59, DAX_00:00 , DAX_00:01 .....'
                list_featuresDAX = []
                list_featuresDAX.append("DAX_close_preday_13:59")
                # get list of HSI operation time ' 00:00 , 00:01 .....'
                list_DAX_minutes = DAX_DAY['time'].to_list()
                # add string 'HSI_' to list of HSI operation time ' 00:00 , 00:01 .....' -> ' DAX_00:00 , DAX_00:01 .....'
                list_featuresDAX_incomplete = ['DAX_' + s for s in list_DAX_minutes]
                list_featuresDAX = list_featuresDAX + list_featuresDAX_incomplete
                return list_featuresDAX

            def generateListFeaturesHSI(HSI_DAY):
                # get list of HSI operation time ' 00:00 , 00:01 .....'
                list_HSI_minutes = HSI_DAY['time'].to_list()
                # add string 'HSI_' to list of HSI operation time ' 00:00 , 00:01 .....' -> ' HSI_00:00 , HSI_00:01 .....'
                list_featuresHSI = ['HSI_' + s for s in list_HSI_minutes]
                # return feature names ' HSI_00:00 , HSI_00:01 .....'
                return list_featuresHSI

            # print(DAX_Close_only['date'].iloc[0]+ timedelta(days=1))
            DAX_DAY = dax_DataFrame.loc[dax_DataFrame['date'] == (DAX_Close_only['date'].iloc[0] + timedelta(days=1))]
            # remove 13:59h
            DAX_DAY = DAX_DAY.loc[DAX_DAY['time'] != str(time(13, 59).strftime("%H:%M"))]
            # get all dax values one day later
            HSI_DAY = hsi_DataFrame.loc[hsi_DataFrame['date'] == (DAX_Close_only['date'].iloc[0] + timedelta(days=1))]

            list_featuresHSI = generateListFeaturesHSI(HSI_DAY)
            list_featuresDAX = generateListFeaturesDAX(DAX_DAY)

            return  ['tradingDate'] + list_featuresHSI + list_featuresDAX

        (hsi_DataFrame, dax_DataFrame) = setDateColumnToDtypeDate()
        DAX_Close_only = createDataFrameWithOnlyDaxCloseTimes(dax_DataFrame)
        print('DAX_CLOSE_ONLY')
        print(DAX_Close_only)
        arrayTrainingData = createArrayTrainingData(DAX_Close_only, hsi_DataFrame, dax_DataFrame)
        features = featureListGeneration(hsi_DataFrame, dax_DataFrame)

        trainingDataFrame = pd.DataFrame(arrayTrainingData, columns=features)
        trainingDataFrame = trainingDataFrame.set_index('tradingDate')
        trainingDataFrame = trainingDataFrame.astype(float)

        print(trainingDataFrame)
        return trainingDataFrame

    def saveDataFrame(self, stockData, placeToSave):

        stockData.to_csv(str(placeToSave), sep=',',index=True)


def main():
    pathInputDataDAX = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2018/DAX_M1_2018_02_february_cleanedANDunifiedData.csv'
    pathInputDataHSI = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/HSI_data/HSI_M1_2018/HSI_M1_2018_02_february_cleanedANDunifiedData.csv'

    #pathInputDataDAX = 'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Fruehstueck-DL/DAX_DataFrameRaw.csv'
    #pathInputDataHSI = 'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Fruehstueck-DL/HSI_DataFrameRaw.csv'
    pathSaveOuput = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_HSI_2018_02_february.csv'

    GenerateTrainData = LearningDataAssembly(pathInputDataHSI, pathInputDataDAX)
    train_data = GenerateTrainData.createTrainingdataDataFrame(GenerateTrainData.hsi_DataFrame_rawData,
                                                              GenerateTrainData.dax_DataFrame_rawData)
    GenerateTrainData.saveDataFrame(train_data, pathSaveOuput)


main()



