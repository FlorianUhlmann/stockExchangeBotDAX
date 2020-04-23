import unittest
import os
from datetime import time
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
from Fruehstueck_DL_LearningData_Assembly import LearningDataAssembly as LDA




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
                    [['2019-01-10'], ['2020-01-06'], ['2020-01-07'], ['2020-01-08'], ['2020-01-09'], ['2020-01-10'],
                     ['2020-01-13'], ['2020-01-14'], ['2020-01-15']], dtype=np.datetime64)
                return tradingDays
            #generate list(column header) for DataFrame
            list_featuresDAX = GenerateList_featureDAX(self)
            list_featuresHSI = GenerateList_featureHSI(self)
            list_tradingDays = GenerateList_tradingDays(self)
            #generate values for DataFrame
            arr_valuesHSI = np.array([range(len(list_featuresHSI)),range(len(list_featuresHSI)),
                                      range(len(list_featuresHSI)),range(len(list_featuresHSI)),
                                      range(len(list_featuresHSI)),range(len(list_featuresHSI)),
                                      range(len(list_featuresHSI)),range(len(list_featuresHSI)),
                                      range(len(list_featuresHSI))]).astype(float)
            arr_valuesDAX = np.array([range(len(list_featuresDAX)),range(len(list_featuresDAX)),
                                      range(len(list_featuresDAX)),range(len(list_featuresDAX)),
                                      range(len(list_featuresDAX)),range(len(list_featuresDAX)),
                                      range(len(list_featuresDAX)),range(len(list_featuresDAX)),
                                      range(len(list_featuresDAX))]).astype(float)
            #create DataFrame
            df_HSI_UTCminus5 = pd.DataFrame(arr_valuesHSI,columns=list_featuresHSI)
            df_DAX_UTCminus5 = pd.DataFrame(arr_valuesDAX,columns=list_featuresDAX)
            df_tradingDays = pd.DataFrame(list_tradingDays, columns=['tradingDay'])
            # merge DataFrames
            df_prefinal = pd.concat([df_tradingDays, df_HSI_UTCminus5, df_DAX_UTCminus5], axis=1)
            #set traidingDay as index of DataFrame
            df_HSI_DAX_UTCminus5 = df_prefinal.set_index('tradingDay')

            return df_HSI_DAX_UTCminus5

        super(LearningDataAssembly, self).setUp()
        self.SOLLDataFrame_3Weeks = Generate_SollDataFrame_10tradingDays_2Weekends(self)

        dirnamePath = os.path.dirname(os.path.abspath(__file__))
        DataFrameSavePath = os.path.join(dirnamePath,
                'Fruehstueck_DL_LearningData_Assembly_TDD_DataFrame_10traidingDays_3Weeks_2Weekends.csv')
        self.SOLLDataFrame_3Weeks.to_csv(DataFrameSavePath, index=True)

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
            list_tradingDates = np.array([['2019-01-10']], dtype=np.datetime64)
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

                x = np.array([['2019-01-10']], dtype=np.datetime64)
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



if __name__ == '__main__':
    unittest.main()




"""
function to create a DataFrame with with trading day. The Days are from 2020-01-02 - 2020-01-15, no weekends
def GenerateDAXDataFrameRawBiggerBetter():

            def GenerateList_timeDAX():
                list_traidingTimeDAX = []

                list_traidingTimeDAX.append(time(13, 59).strftime("%H:%M"))
                for h in range(2, 6):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_traidingTimeDAX.append(str(time_convert))
                        if (h == 5): break
                            
                list_traidingTimeDax_10TradinigDays=np.concatenate((list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                list_traidingTimeDAX,
                ),axis = 0)

                return list_traidingTimeDax_10TradinigDays


            def GenerateList_traidingDateDAX():

                dayBeforeTraidingDate = np.array('2019-01-01', dtype=np.datetime64)
                traidingDate = np.array('2019-01-02', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW1_02 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-02', dtype=np.datetime64)
                traidingDate = np.array('2019-01-03', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW1_03 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-03', dtype=np.datetime64)
                traidingDate = np.array('2019-01-06', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_06 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-06', dtype=np.datetime64)
                traidingDate = np.array('2019-01-07', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_07 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-07', dtype=np.datetime64)
                traidingDate = np.array('2019-01-08', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_08 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-08', dtype=np.datetime64)
                traidingDate = np.array('2019-01-09', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_09 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-09', dtype=np.datetime64)
                traidingDate = np.array('2019-01-10', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW2_10 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-10', dtype=np.datetime64)
                traidingDate = np.array('2019-01-13', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW3_13 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-13', dtype=np.datetime64)
                traidingDate = np.array('2019-01-14', dtype=np.datetime64)
                array_traidingDay = np.repeat(traidingDate, 181)
                array_date_KW3_14 = np.concatenate((dayBeforeTraidingDate + np.arange(1), array_traidingDay), axis=0)

                dayBeforeTraidingDate = np.array('2019-01-14', dtype=np.datetime64)
                traidingDate = np.array('2019-01-15', dtype=np.datetime64)
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
                            array_date_KW3_15), axis = 0)


                return arr_10TradingDays_over3Weeks_with2Weekends

            array_traidingDate = GenerateList_traidingDateDAX()
            list_traidingTimeDAX = GenerateList_timeDAX()

            df_date = pd.DataFrame(array_traidingDate, columns=['date'])
            df_time = pd.DataFrame(list_traidingTimeDAX, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeDAX))])), columns=['close'])

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)
            
            
            
            
            def GenerateHSIDataFrameRawBiggerBetter():

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


                list_traidingTimeHSI = np.concatenate((list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI,
                                                      list_traidingTimeHSI), axis = 0)
                
             
                return list_traidingTimeHSI
            def GenerateList_traidingDateHSI():

                x = np.array([['2019-01-02']], dtype=np.datetime64)
                array_traidingDay_W1_02 = np.repeat(x, 256, axis=0)
                
                x = np.array([['2019-01-03']], dtype=np.datetime64)
                array_traidingDay_W1_03 = np.repeat(x, 256, axis=0)
                
                x = np.array([['2019-01-06']], dtype=np.datetime64)
                array_traidingDay_W2_06 = np.repeat(x, 256, axis=0)
                
                x = np.array([['2019-01-07']], dtype=np.datetime64)
                array_traidingDay_W2_07 = np.repeat(x, 256, axis=0)

                x = np.array([['2019-01-08']], dtype=np.datetime64)
                array_traidingDay_W2_08 = np.repeat(x, 256, axis=0)

                x = np.array([['2019-01-09']], dtype=np.datetime64)
                array_traidingDay_W2_09 = np.repeat(x, 256, axis=0)

                x = np.array([['2019-01-10']], dtype=np.datetime64)
                array_traidingDay_W2_010 = np.repeat(x, 256, axis=0)
                
                x = np.array([['2019-01-13']], dtype=np.datetime64)
                array_traidingDay_W3_13 = np.repeat(x, 256, axis=0)

                x = np.array([['2019-01-14']], dtype=np.datetime64)
                array_traidingDay_W3_14 = np.repeat(x, 256, axis=0)

                x = np.array([['2019-01-15']], dtype=np.datetime64)
                array_traidingDay_W3_15 = np.repeat(x, 256, axis=0)

                
                arr_10TradingDays_HSI_over3Weeks_with2Weekends = np.concatenate((array_traidingDay_W1_02,
                        array_traidingDay_W1_03,
                        array_traidingDay_W2_06,
                        array_traidingDay_W2_07,
                        array_traidingDay_W2_08,
                        array_traidingDay_W2_09,
                        array_traidingDay_W2_010,
                        array_traidingDay_W3_13,
                        array_traidingDay_W3_14,
                        array_traidingDay_W3_15), axis = 0)

                return arr_10TradingDays_HSI_over3Weeks_with2Weekends

            array_traidingDate = GenerateList_traidingDateHSI()
            list_traidingTimeHSI = GenerateList_timeHSI()

            df_time = pd.DataFrame(list_traidingTimeHSI, columns=['time'])
            df_close = pd.DataFrame(np.transpose(np.array([range(len(list_traidingTimeHSI))])), columns=['close'])
            df_date = pd.DataFrame(array_traidingDate, columns=['date'])

            return pd.concat([df_date, df_time, df_close], axis=1, sort=False)

"""