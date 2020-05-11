import os
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np
from datetime import datetime, time
from Demo_check_for_missing_data import *
pd.set_option('display.max_row', 50)


class MissingValuesInDataFrames(unittest.TestCase):

    def setUp(self):

        def createDFSOLL_testCase_onePlaceFalse():
            dateData = ['2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03']
            timeData = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1000, 1002, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015,
                         1016, 1017, 1018, 1019, 1020, 1021]
            df_data_correct_SOLL = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_correct_SOLL

            return pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})

        def createDFSOLL_testCase_TwoPlacesFalse():
            dateData = ['2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03']
            timeData = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1000, 1002, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015,
                         1016, 1017, 1018, 1020, 1020, 1021]
            df_data_correct_SOLL = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_correct_SOLL

            return pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})

        def createListCorrectTime():
            list_time = [100,1,2,3,4,5,6,7,8,9,10,100,1,2,3,4,5,6,7,8,9,10]
            return list_time

        def createDFIncorrectOnePlaceFalse():
            dateData = ['2020-01-01','2020-01-02','2020-01-02','2020-01-02','2020-01-02','2020-01-02','2020-01-02',
                        '2020-01-02','2020-01-02','2020-01-02','2020-01-02','2020-01-03','2020-01-03','2020-01-03',
                        '2020-01-03','2020-01-03','2020-01-02','2020-01-03','2020-01-03','2020-01-03','2020-01-03']
            timeData = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1000, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1019, 1020, 1021]
            df_data_incorrect_second_place_missing_time_1 = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_incorrect_second_place_missing_time_1

        def createDFIncorrectTwoPlacesFalse():
            dateData = ['2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-02', '2020-01-03',
                        '2020-01-03', '2020-01-03']
            timeData = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1, 2, 3, 4, 5, 6, 7, 9, 10]
            valueData = [1000, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1020, 1021]
            df_data_incorrect_secondAnd18th_place_false_time = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_incorrect_secondAnd18th_place_false_time
        #create DataFrames
        self.DFCorrectSOLL_testCase_onePlaceFalse = createDFSOLL_testCase_onePlaceFalse()
        self.DFSOLL_testCase_TwoPlacesFalse = createDFSOLL_testCase_TwoPlacesFalse()
        self.DFIncorrectOnePlaceFalse = createDFIncorrectOnePlaceFalse()
        self.DFIncorrectTwoPlacesFalse = createDFIncorrectTwoPlacesFalse()
        self.listCorrectTime = createListCorrectTime()

    def test_find_one_missing_value_in_DataFrame_and_replace_it(self):
        SOLL_DataFrame = self.DFCorrectSOLL_testCase_onePlaceFalse
        DFIncorrectOnePlaceFalse = self.DFIncorrectOnePlaceFalse
        listCorrectTime = self.listCorrectTime

        CheckForMissingData = DemoCheckForMissingData()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingData(DFIncorrectOnePlaceFalse,listCorrectTime)

        assert_frame_equal(SOLL_DataFrame,IST_DataFrame, check_dtype=False)




    def test_find_two_missing_value_in_DataFrame_and_replace_it(self):
        SOLL_DataFrame = self.DFSOLL_testCase_TwoPlacesFalse
        DFIncorrectTwoPlacesFalse = self.DFIncorrectTwoPlacesFalse
        print('DFIncorrectTwoPlacesFalse')
        print(DFIncorrectTwoPlacesFalse)
        CheckForMissingData = DemoCheckForMissingData()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingData(DFIncorrectTwoPlacesFalse,self.listCorrectTime)


        print("IST_DataFrame")

        print(IST_DataFrame)
        print("SOLL_DataFrame")
        print(SOLL_DataFrame)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)

    def tearDown(self):
        self.DFCorrectSOLL_testCase_onePlaceFalse = None
        self.DFIncorrectOnePlaceFalse = None
        self.DFIncorrectTwoPlacesFalse = None
        self.listCorrectTime = None


if __name__ == '__main__':
    unittest.main()
