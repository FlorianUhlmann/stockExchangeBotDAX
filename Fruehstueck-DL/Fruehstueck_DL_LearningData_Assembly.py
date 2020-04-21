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
            t = time(13, 59)
            time_convert = t.strftime("%H:%M")
            DAX_Close_only = dax_DataFrame.loc[dax_DataFrame['time'] == str(time_convert)]
            return DAX_Close_only

        def createArrayTrainingData(DAX_Close_only, hsi_DataFrame, dax_DataFrame):
            #TODO CleanCode !!!
            array_trainData = []

            for DAXClose in range(0, len(DAX_Close_only['date'])):
                #TODO check for nextday is existing traiding day

                if(DAXClose < len(DAX_Close_only['date'])-1):
                    if (DAX_Close_only['date'].iloc[DAXClose] + timedelta(days=1) == DAX_Close_only['date'].iloc[
                        DAXClose + 1]):
                        print('not Friday')
                        nextDay = int(1)
                    else:
                        print('its Friday')
                        nextDay = int(3)

                # print(DAX_Close_only['date'].iloc[0]+ timedelta(days=1))
                DAX_DAY = dax_DataFrame.loc[
                    dax_DataFrame['date'] == (DAX_Close_only['date'].iloc[DAXClose] + timedelta(days=nextDay))]
                # remove 13:59h
                DAX_DAY = DAX_DAY.loc[DAX_DAY['time'] != str(time(13, 59).strftime("%H:%M"))]
                # get all HSI values one day later
                HSI_DAY = hsi_DataFrame.loc[
                    hsi_DataFrame['date'] == (DAX_Close_only['date'].iloc[DAXClose] + timedelta(days=nextDay))]
                # get the traiding day in stringFormat from the HSI
                TRAIDING_DAY = HSI_DAY['date'].iloc[0].strftime("%Y-%m-%d")
                HSI_DAX_concat = pd.concat([HSI_DAY, DAX_Close_only.iloc[0:1], DAX_DAY], ignore_index=True)
                # get close values of HSI_DAX_concat into a list
                array_trainData_first_day = HSI_DAX_concat['close'].to_numpy()
                # reshape numpy array (number,) -> (1,number)
                array_trainData_first_day = np.reshape(array_trainData_first_day, (1, len(HSI_DAX_concat['close'])))
                # concat tradingDate to array_trainngData_first_day
                array_trainData_first_day = np.concatenate((TRAIDING_DAY,array_trainData_first_day), axis=None)
                array_trainData_first_day = np.hstack((array_trainData_first_day))
                print(array_trainData_first_day)
                if DAXClose == 0:
                    array_trainData = array_trainData_first_day
                else:
                    array_trainData = np.vstack((array_trainData, array_trainData_first_day))

                # array_trainData_as_float = array_trainData.astype(float)

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

            return  ['traidingDate'] + list_featuresHSI + list_featuresDAX

        (hsi_DataFrame, dax_DataFrame) = setDateColumnToDtypeDate()
        DAX_Close_only = createDataFrameWithOnlyDaxCloseTimes(dax_DataFrame)

        arrayTrainingData = createArrayTrainingData(DAX_Close_only, hsi_DataFrame, dax_DataFrame)
        features = featureListGeneration(hsi_DataFrame, dax_DataFrame)

        return pd.DataFrame(arrayTrainingData, columns=features)

    def saveDataFrame(self, stockData, placeToSave):

        stockData.to_csv(str(placeToSave), sep=',')


def main():
    pathInputDataDAX = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_only_Close_values_january.csv'
    pathInputDataHSI = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/HAN_SENG_data/HSI_M1_2019/HSI_M1_2019_CLOSE_values.csv'
    pathSaveOuput = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/Fruehstueck_training_data_2019_january.csv'

    GenerateTrainData = LearningDataAssembly(pathInputDataHSI, pathInputDataDAX)
    train_data = GenerateTrainData.createTrainingdataDataFrame(GenerateTrainData.hsi_DataFrame_rawData,
                                                               GenerateTrainData.dax_DataFrame_rawData)

    GenerateTrainData.saveDataFrame(train_data, pathSaveOuput)


main()
