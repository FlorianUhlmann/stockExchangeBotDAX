import unittest
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
from datetime import datetime, time
import os
from Fruehstueck_DL_LearningData_Assembly import LearningDataAssembly as LDA


class LearningDataAssembly(unittest.TestCase):

    def testForConcatinationOfHsiAndDaxData(self):

        def GenerateList_featureHSI(self):

            list_featuresHSI = []
            for h in range(0, 4):
                for m in range(0, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresHSI.append("HSI_" + str(time_convert))
                    if (h == 3 and m >= 29): break
            for h in range(4, 5):
                for m in range(15, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresHSI.append("HSI_" + str(time_convert))
                    if (h == 5): break

            hsiClose = time(5, 0).strftime("%H:%M")
            list_featuresHSI.append("HSI_" + str(hsiClose))

            return list_featuresHSI

        def GenerateList_featureDAX(self):
            list_featuresDAX = []
            list_featuresDAX.append("DAX_close_preday_13:59")
            for h in range(2, 6):
                for m in range(0, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresDAX.append("DAX_" + str(time_convert))
                    if (h == 5): break

            return list_featuresDAX

        def Generate_SollDataFrame(self):
            def GenerateDataFrameHSI_UTCminus5(self, list_featuresHSI):
                return pd.DataFrame(np.array([range(len(list_featuresHSI))]), columns=list_featuresHSI)

            list_featuresDAX = GenerateList_featureDAX(self)
            list_featuresHSI = GenerateList_featureHSI(self)
            df_HSI_UTCminus5 = pd.DataFrame(np.array([range(len(list_featuresHSI))]).astype(float), columns=list_featuresHSI)
            df_DAX_UTCminus5 = pd.DataFrame(np.array([range(len(list_featuresDAX))]).astype(float), columns=list_featuresDAX)

            df_HSI_DAX_UTCminus5 = pd.concat([df_HSI_UTCminus5, df_DAX_UTCminus5], axis=1)


            return df_HSI_DAX_UTCminus5

        def GenerateHSIDataFrameRaw(self):

            def GenerateList_timeHSI():
                list_traidingTimeHSI = []
                for h in range(0, 4):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeHSI.append(str(time_convert))
                        if h == 3 and m >= 29:
                            break
                for h in range(4, 5):
                    for m in range(15, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeHSI.append(str(time_convert))
                        if h == 5:
                            break

                hsiClose = time(5, 0).strftime("%H:%M")
                list_traidingTimeHSI.append(str(hsiClose))

                return list_traidingTimeHSI
            def GenerateList_traidingDateHSI():

                x = np.array([['2019-01-10']], dtype=np.datetime64)
                array_date = np.repeat(x, 256, axis=0)

                return array_date

            array_traidingDate = GenerateList_traidingDateHSI()
            list_traidingTimeHSI = GenerateList_timeHSI()

            df_time = pd.DataFrame(list_traidingTimeHSI, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeHSI))])), columns=['close'])
            df_date = pd.DataFrame(array_traidingDate, columns=['date'])

            return pd.concat([df_date,df_time, df_close], axis=1, sort=False)

        def GenerateDAXDataFrameRaw(self):

            def GenerateList_timeDAX():
                list_traidingTimeDAX = []

                list_traidingTimeDAX = []
                list_traidingTimeDAX.append(time(13,59).strftime("%H:%M"))
                for h in range(2, 6):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeDAX.append(str(time_convert))
                        if (h == 5): break

                return list_traidingTimeDAX


            def GenerateList_traidingDateDAX():

                dayBeforeTraidingDate = np.array('2019-01-09', dtype=np.datetime64)
                traidingDate = np.array('2019-01-10', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)
                array_date = array_date.reshape(182, 1)


                return array_date

            array_traidingDate = GenerateList_traidingDateDAX()
            list_traidingTimeDAX = GenerateList_timeDAX()

            df_date = pd.DataFrame(array_traidingDate, columns=['date'])
            df_time = pd.DataFrame(list_traidingTimeDAX, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeDAX))])), columns=['close'])

            return pd.concat([df_date,df_time, df_close], axis=1, sort=False)


        ISTDataFrame = pd.DataFrame()
        SollDataFrame = Generate_SollDataFrame(self)
        print(SollDataFrame)
        Dax_DataFrameRaw = GenerateDAXDataFrameRaw(self)
        #print(Dax_DataFrameRaw)
        dirname = os.path.dirname(os.path.abspath(__file__))
        DAXfilename = os.path.join(dirname, 'DAX_DataFrameRaw.csv')
        Dax_DataFrameRaw.to_csv(DAXfilename)


        HSI_DataFrameRaw = GenerateHSIDataFrameRaw(self)
        #print(HSI_DataFrameRaw)
        HSIfilename = os.path.join(dirname, 'HSI_DataFrameRaw.csv')
        HSI_DataFrameRaw.to_csv(HSIfilename)

        CreateSOLLDataFrame = LDA(HSIfilename,DAXfilename)
        CreateSOLLDataFrame.showDataFrameRaw()
        (hsi_DataFrame, dax_DataFrame) = CreateSOLLDataFrame.setDateColumnToDtypeDate(
        CreateSOLLDataFrame.hsi_DataFrame_rawData, CreateSOLLDataFrame.dax_DataFrame_rawData)
        DaxClose_DataFrame = CreateSOLLDataFrame.createDataFrameWithOnlyDaxCloseTimes(dax_DataFrame)
        arrayTrainingData = CreateSOLLDataFrame.createArrayTrainingData(DaxClose_DataFrame, hsi_DataFrame, dax_DataFrame)
        features = CreateSOLLDataFrame.featureListGeneration(DaxClose_DataFrame, hsi_DataFrame, dax_DataFrame)
        # create TrainingData
        ISTDataFrame = pd.DataFrame(arrayTrainingData, columns=(features))

        Dax_DataFrameRaw = GenerateDAXDataFrameRaw(self)

        HSI_DataFrameRaw = GenerateHSIDataFrameRaw(self)

        ISTDataFrame.to_csv("d:\ISTDATAFRAME.csv")
        SollDataFrame.to_csv("d:\SOLLDATAFRAME.csv")

        assert_frame_equal(ISTDataFrame, SollDataFrame, check_column_type=False, check_frame_type=False,
                           check_index_type=False)



if __name__ == '__main__':
    unittest.main()
