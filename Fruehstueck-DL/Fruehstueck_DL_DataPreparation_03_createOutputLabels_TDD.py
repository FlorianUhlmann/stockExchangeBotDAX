import os
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np
from datetime import datetime, time
from Fruehstueck_DL_DataPreparation_03_createOutputLabels import OutputDataGenerator as ODG

class CreateOutputLabelTest(unittest.TestCase):

    def setUp(self):

        def createFeatures():

            self.list_features = []



            def GenerateList_featureHSI():

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

            def GenerateList_featureDAX():
                list_featuresDAX = []
                list_featuresDAX.append("DAX_close_preday_13:59")
                for h in range(2, 6):
                    for m in range(0, 60):

                        t = time(h, m)
                        time_convert = t.strftime("%H:%M")

                        list_featuresDAX.append("DAX_" + str(time_convert))
                        if (h == 5): break

                return list_featuresDAX

            self.list_features = ['tradingDate']+GenerateList_featureHSI()+GenerateList_featureDAX()

            return self.list_features



        # TestCases are often used in cooperative multiple inheritance so you should be careful to always call
        # super in these methods so that base class's setUp and tearDown methods also get called.
        super(CreateOutputLabelTest, self).setUp()
        self.mock_data = [1, 2, 3, 4, 5]
        self.SOLLDataFrame= pd.DataFrame()

        self.HSI_values = np.zeros(256)
        self.DAX_buyDayValues= np.arange((182.0))
        self.DAX_sellDayValues= self.DAX_buyDayValues[::-1]
        self.DAX_noTradeDayValuesOne= np.concatenate((np.array([0.0,1000.0]),np.arange(180.0)))
        self.DAX_noTradeDayValuesTwo=np.concatenate((np.array([1000.0,0.0]),np.arange(180.0)))
        self.tradingDate = ['02-01-2020']

        self.traidingDayOne = np.hstack((self.tradingDate, self.HSI_values, self.DAX_buyDayValues))
        self.traidingDayTwo = np.hstack((self.tradingDate, self.HSI_values,self.DAX_sellDayValues))
        self.traidingDayThree = np.hstack((self.tradingDate, self.HSI_values,self.DAX_noTradeDayValuesOne))
        self.traidingDayFour = np.hstack((self.tradingDate, self.HSI_values,self.DAX_noTradeDayValuesTwo))

        self.traidingDays = np.vstack((self.traidingDayOne,self.traidingDayTwo,self.traidingDayThree,self.traidingDayFour))

        self.features = createFeatures()
        self.inputData = pd.DataFrame(self.traidingDays,columns=self.features)
        self.outputData = pd.DataFrame([[1,0,0],[0,1,0],[0,0,1],[0,0,1]], columns= ['DAX_BUY_DAY','DAX_SELL_DAY','NO_TRADE_DAY'])

        self.SOLLDataFrame = pd.concat([self.inputData,self.outputData],axis=1)

        dirnamePath = os.path.dirname(os.path.abspath(__file__))
        DataFrameSavePath = os.path.join(dirnamePath, 'Fruehstueck_DL_DataPreparation_createOutputLabels_TDD_TestDataFrame_inputData.csv')
        self.inputData.to_csv(DataFrameSavePath, index=False)

    def test_OutputLabelsCorrectCreatedWithDataFrameWithOneDataRow(self):

        dirname = os.path.dirname(os.path.abspath(__file__))
        DataFramefilename = os.path.join(dirname,'Fruehstueck_DL_DataPreparation_createOutputLabels_TDD_TestDataFrame_inputData.csv')


        output = ODG(DataFramefilename)

        ISTDataFrame = output.createOutputDataFrame(output.DataFrame_input)

        print(ISTDataFrame)
        print(self.SOLLDataFrame)

        assert_frame_equal(ISTDataFrame, self.SOLLDataFrame, check_column_type=False, check_frame_type=False,check_index_type=True,check_dtype=False)



    def tearDown(self):
        super(CreateOutputLabelTest, self).tearDown()
        self.mock_data = []

        dirnamePath = os.path.dirname(os.path.abspath(__file__))
        DataFramePathForDeletion = os.path.join(dirnamePath,'Fruehstueck_DL_DataPreparation_createOutputLabels_TDD_TestDataFrame_inputData.csv')
        #os.remove(DataFramePathForDeletion)

if __name__ == '__main__':
    unittest.main()
