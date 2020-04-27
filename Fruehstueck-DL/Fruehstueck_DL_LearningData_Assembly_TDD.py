import unittest
import os
from datetime import time
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
from Fruehstueck_DL_LearningData_Assembly import LearningDataAssembly as LDA
import time as timE




class LearningDataAssembly(unittest.TestCase):

    def setUp(self):

        def createFeatures():
            self.SOLLDataFrame = pd.DataFrame()

        def Generate_SollDataFrame_10tradingDays_2Weekends(self):

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

            def GenerateList_tradingDays(self):
                tradingDays = np.array(
                    [['2020-01-02'], ['2020-01-03'], ['2020-01-06'], ['2020-01-07'], ['2020-01-08'], ['2020-01-09'], ['2020-01-10'],
                     ['2020-01-13'], ['2020-01-14'], ['2020-01-15']])
                return tradingDays

            def generate_HSI_DAX_DataFrames():

                # generate list(column header) for DataFrame
                list_featuresDAX = GenerateList_featureDAX(self)
                list_featuresHSI = GenerateList_featureHSI(self)
                # generate values for DataFrame
                arr_valuesHSI = np.array([range(len(list_featuresHSI)), range(len(list_featuresHSI)),
                                          range(len(list_featuresHSI)), range(len(list_featuresHSI)),
                                          range(len(list_featuresHSI)), range(len(list_featuresHSI)),
                                          range(len(list_featuresHSI)), range(len(list_featuresHSI)),
                                          range(len(list_featuresHSI)), range(len(list_featuresHSI))]).astype(float)
                arr_valuesDAX = np.array([range(len(list_featuresDAX)), range(len(list_featuresDAX)),
                                          range(len(list_featuresDAX)), range(len(list_featuresDAX)),
                                          range(len(list_featuresDAX)), range(len(list_featuresDAX)),
                                          range(len(list_featuresDAX)), range(len(list_featuresDAX)),
                                          range(len(list_featuresDAX)), range(len(list_featuresDAX))]).astype(float)

                DataFrame_HSI = pd.DataFrame(arr_valuesHSI, columns=list_featuresHSI)
                DataFrame_DAX = pd.DataFrame(arr_valuesDAX,columns=list_featuresDAX)


                return DataFrame_HSI,DataFrame_DAX

            #create DataFrames
            df_HSI_UTCminus5, df_DAX_UTCminus5 = generate_HSI_DAX_DataFrames()
            df_tradingDays = pd.DataFrame(GenerateList_tradingDays(self), columns=['tradingDate'])

            # merge DataFrames
            df_merge = pd.concat([df_tradingDays, df_HSI_UTCminus5, df_DAX_UTCminus5], axis=1)
            #set traidingDay as index of DataFrame
            df_HSI_DAX_UTCminus5 = df_merge.set_index('tradingDate')
            return df_HSI_DAX_UTCminus5

        def Generate_HSIDataFrameRaw_10tradingDays_2Weekends(self):

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

                list_traidingTimeHSI = list_traidingTimeHSI * 10

                return list_traidingTimeHSI

            def GenerateList_traidingDateHSI():

                x = np.array([['2020-01-02']], dtype=np.datetime64)
                array_traidingDay_W1_02 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-03']], dtype=np.datetime64)
                array_traidingDay_W1_03 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-06']], dtype=np.datetime64)
                array_traidingDay_W2_06 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-07']], dtype=np.datetime64)
                array_traidingDay_W2_07 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-08']], dtype=np.datetime64)
                array_traidingDay_W2_08 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-09']], dtype=np.datetime64)
                array_traidingDay_W2_09 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-10']], dtype=np.datetime64)
                array_traidingDay_W2_010 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-13']], dtype=np.datetime64)
                array_traidingDay_W3_13 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-14']], dtype=np.datetime64)
                array_traidingDay_W3_14 = np.repeat(x, 256, axis=0)

                x = np.array([['2020-01-15']], dtype=np.datetime64)
                array_traidingDay_W3_15 = np.repeat(x, 256, axis=0)

                return np.concatenate((array_traidingDay_W1_02,
                                       array_traidingDay_W1_03,
                                       array_traidingDay_W2_06,
                                       array_traidingDay_W2_07,
                                       array_traidingDay_W2_08,
                                       array_traidingDay_W2_09,
                                       array_traidingDay_W2_010,
                                       array_traidingDay_W3_13,
                                       array_traidingDay_W3_14,
                                       array_traidingDay_W3_15), axis=0)

            array_traidingDate = GenerateList_traidingDateHSI()
            list_traidingTimeHSI = GenerateList_timeHSI()

            df_time = pd.DataFrame(list_traidingTimeHSI, columns=['time'])
            df_close = pd.DataFrame(np.tile(np.transpose(np.array([range(256)])), (10, 1)), columns=['close'])
            df_date = pd.DataFrame(array_traidingDate, columns=['date'])

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)

        def Generate_DAXDataFrameRaw_10tradingDays_2Weekends(self):

            def GenerateList_timeDAX():
                list_traidingTimeDAX = []

                list_traidingTimeDAX = []
                list_traidingTimeDAX.append(time(13, 59).strftime("%H:%M"))
                for h in range(2, 6):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeDAX.append(str(time_convert))
                        if (h == 5): break

                return list_traidingTimeDAX * 10

            def GenerateList_traidingDateDAX():

                dayBeforeTraidingDate = np.array('2020-01-01', dtype=np.datetime64)
                traidingDate = np.array('2020-01-02', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW1_02 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-02', dtype=np.datetime64)
                traidingDate = np.array('2020-01-03', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW1_03 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-03', dtype=np.datetime64)
                traidingDate = np.array('2020-01-06', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_06 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-06', dtype=np.datetime64)
                traidingDate = np.array('2020-01-07', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_07 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-07', dtype=np.datetime64)
                traidingDate = np.array('2020-01-08', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_08 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-08', dtype=np.datetime64)
                traidingDate = np.array('2020-01-09', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_09 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-09', dtype=np.datetime64)
                traidingDate = np.array('2020-01-10', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_10 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-10', dtype=np.datetime64)
                traidingDate = np.array('2020-01-13', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW3_13 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-13', dtype=np.datetime64)
                traidingDate = np.array('2020-01-14', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW3_14 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2020-01-14', dtype=np.datetime64)
                traidingDate = np.array('2020-01-15', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW3_15 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                arr_10TradingDays_over3Weeks_with2Weekends = np.concatenate((array_date_KW1_02,
                                                                             array_date_KW1_03,
                                                                             array_date_KW2_06,
                                                                             array_date_KW2_07,
                                                                             array_date_KW2_08,
                                                                             array_date_KW2_09,
                                                                             array_date_KW2_10,
                                                                             array_date_KW3_13,
                                                                             array_date_KW3_14,
                                                                             array_date_KW3_15), axis=0)

                return arr_10TradingDays_over3Weeks_with2Weekends

            array_traidingDate = GenerateList_traidingDateDAX()
            list_traidingTimeDAX = GenerateList_timeDAX()

            df_date = pd.DataFrame(array_traidingDate, columns=['date'])
            df_time = pd.DataFrame(list_traidingTimeDAX, columns=['time'])
            df_close = pd.DataFrame(np.tile(np.transpose(np.array([range(182)])), (10, 1)), columns=['close'], dtype=float)

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)


        super(LearningDataAssembly, self).setUp()
        dirnamePath = os.path.dirname(os.path.abspath(__file__))

        self.SOLLDataFrame_3Weeks = Generate_SollDataFrame_10tradingDays_2Weekends(self)
        DataFrameSavePath = os.path.join(dirnamePath,
                'Fruehstueck_DL_LearningData_Assembly_TDD_DataFrame_10traidingDays_3Weeks_2Weekends.csv')
        self.SOLLDataFrame_3Weeks.to_csv(DataFrameSavePath, index=True)

        self.DAXRaw = Generate_DAXDataFrameRaw_10tradingDays_2Weekends(self)
        DataFrameSavePath_HSIRaw = os.path.join(dirnamePath,'DaxRawData_10traidingDays_3Weeks_2Weekends.csv')
        self.DAXRaw.to_csv(DataFrameSavePath_HSIRaw, index=True)

        self.HSIRaw = Generate_HSIDataFrameRaw_10tradingDays_2Weekends(self)
        DataFrameSavePath_DAXRaw = os.path.join(dirnamePath,'HSIRawData_10traidingDays_3Weeks_2Weekends.csv')
        self.HSIRaw.to_csv(DataFrameSavePath_DAXRaw, index=True)
    '''
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
            list_tradingDates = np.array([['2020-01-10']], dtype=np.datetime64)
            index_tradingDay = ['tradingDay']
            df_HSI_UTCminus5 = pd.DataFrame(np.array([range(len(list_featuresHSI))]).astype(float), columns=list_featuresHSI)
            df_DAX_UTCminus5 = pd.DataFrame(np.array([range(len(list_featuresDAX))]).astype(float), columns=list_featuresDAX)
            df_tradingDays = pd.DataFrame(list_tradingDates, columns=index_tradingDay)

            df_prefinal = pd.concat([df_tradingDays, df_HSI_UTCminus5, df_DAX_UTCminus5], axis=1)
            df_HSI_DAX_UTCminus5 = df_prefinal.set_index('tradingDay')

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

                x = np.array([['2020-01-10']], dtype=np.datetime64)
                array_date = np.repeat(x, 256, axis=0)

                return array_date

            array_traidingDate = GenerateList_traidingDateHSI()
            list_traidingTimeHSI = GenerateList_timeHSI()

            df_time = pd.DataFrame(list_traidingTimeHSI, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeHSI))])), columns=['close'])
            df_date = pd.DataFrame(array_traidingDate, columns=['date'])

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)

        def GenerateDAXDataFrameRaw(self):

            def GenerateList_timeDAX():
                list_traidingTimeDAX = []

                list_traidingTimeDAX = []
                list_traidingTimeDAX.append(time(13, 59).strftime("%H:%M"))
                for h in range(2, 6):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeDAX.append(str(time_convert))
                        if (h == 5): break

                return list_traidingTimeDAX


            def GenerateList_traidingDateDAX():

                dayBeforeTraidingDate = np.array('2020-01-09', dtype=np.datetime64)
                traidingDate = np.array('2020-01-10', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)
                array_date = array_date.reshape(182, 1)


                return array_date

            array_traidingDate = GenerateList_traidingDateDAX()
            list_traidingTimeDAX = GenerateList_timeDAX()

            df_date = pd.DataFrame(array_traidingDate, columns=['date'])
            df_time = pd.DataFrame(list_traidingTimeDAX, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeDAX))])), columns=['close'])

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)


        ISTDataFrame = pd.DataFrame()
        SollDataFrame = Generate_SollDataFrame(self)

        Dax_DataFrameRaw = GenerateDAXDataFrameRaw(self)

        dirname = os.path.dirname(os.path.abspath(__file__))
        DAXfilename = os.path.join(dirname, 'DAX_DataFrameRaw.csv')
        Dax_DataFrameRaw.to_csv(DAXfilename)


        HSI_DataFrameRaw = GenerateHSIDataFrameRaw(self)

        HSIfilename = os.path.join(dirname, 'HSI_DataFrameRaw.csv')
        HSI_DataFrameRaw.to_csv(HSIfilename)

        CreateISTDataFrame = LDA(HSIfilename, DAXfilename)
        CreateISTDataFrame.showDataFrameRaw()

        ISTDataFrame = CreateISTDataFrame.createTrainingdataDataFrame(CreateISTDataFrame.hsi_DataFrame_rawData, CreateISTDataFrame.dax_DataFrame_rawData)

        Dax_DataFrameRaw = GenerateDAXDataFrameRaw(self)

        HSI_DataFrameRaw = GenerateHSIDataFrameRaw(self)

        ISTDataFrame.to_csv("d:\ISTDATAFRAME.csv")
        SollDataFrame.to_csv("d:\SOLLDATAFRAME.csv")

        assert_frame_equal(ISTDataFrame, SollDataFrame, check_column_type=False, check_frame_type=False,
                          check_index_type=False)
    
    '''
    def testTakeRawDataFromDAXandHSIandAssembleLearningData_10tradingDays_2Weekends(self):

        SOLLDataFrame = self.SOLLDataFrame_3Weeks

        ISTDataFrame = pd.DataFrame()

        dirname = os.path.dirname(os.path.abspath(__file__))
        pathFileDAXDataRaw = os.path.join(dirname, 'DaxRawData_10traidingDays_3Weeks_2Weekends.csv')
        pathFileHSIDataRaw = os.path.join(dirname, 'HSIRawData_10traidingDays_3Weeks_2Weekends.csv')

        CreateISTDataFrame = LDA(pathFileHSIDataRaw, pathFileDAXDataRaw)
        CreateISTDataFrame.showDataFrameRaw()
        ISTDataFrame = CreateISTDataFrame.createTrainingdataDataFrame(CreateISTDataFrame.hsi_DataFrame_rawData,CreateISTDataFrame.dax_DataFrame_rawData)
        print('ISTDataFrame view')
        print(ISTDataFrame.info())
        print('SOLLDataFrame view')
        print(SOLLDataFrame.info())
        assert_frame_equal(SOLLDataFrame, ISTDataFrame, check_dtype=False, check_index_type=False, check_column_type=False, check_frame_type=True, check_less_precise=False, check_names=False, by_blocks=False, check_exact=False, check_datetimelike_compat=False, check_categorical=True, check_like=False )


    def tearDown(self):
        timE.sleep(3)
        super(LearningDataAssembly,self).tearDown()

        dirnamePath = os.path.dirname(os.path.abspath(__file__))

        pathDataFrameForDeletion0 = os.path.join(dirnamePath,'Fruehstueck_DL_DataPreparation_createOutputLabels_TDD_TestDataFrame_inputData.csv')
        pathDataFrameForDeletion1 = os.path.join(dirnamePath, 'Fruehstueck_DL_LearningData_Assembly_TDD_DataFrame_10traidingDays_3Weeks_2Weekends.csv')
        pathDataFrameForDeletion2 = os.path.join(dirnamePath, 'DaxRawData_10traidingDays_3Weeks_2Weekends.csv')
        pathDataFrameForDeletion3 = os.path.join(dirnamePath, 'HSIRawData_10traidingDays_3Weeks_2Weekends.csv')

        try:
            #os.remove(pathDataFrameForDeletion0)
            os.remove(pathDataFrameForDeletion1)
            os.remove(pathDataFrameForDeletion2)
            os.remove(pathDataFrameForDeletion3)
        except():
            print('error occured while deleting file')
if __name__ == '__main__':
    unittest.main()

