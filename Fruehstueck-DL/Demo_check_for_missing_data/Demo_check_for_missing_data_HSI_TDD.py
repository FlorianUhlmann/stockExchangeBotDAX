import os
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

from Demo_check_for_missing_data_HSI import *

pd.set_option('display.max_row', 50)


class MissingValuesInDataFrames(unittest.TestCase):

    def setUp(self):

        def createDFSOLL_testCase_onePlaceFalse():
            dateData = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03']
            timeData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1004, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1016,
                         1016, 1017, 1018, 1019, 1020]
            return pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})

        def createDFSOLL_testCase_TwoPlacesFalse():
            dateData = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-02', '2020-01-03', '2020-01-03',
                        '2020-01-03',
                        '2020-01-03']
            timeData = [1, 2,  4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014,
                         1016, 1017, 1018, 1019, 1020]
            df_data_correct_SOLL = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_correct_SOLL

            return pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})

        def createDFSOLL_testCase_twoConsecutivePlacesFalse_plusOnePlaceFalse():
            dateData = ['2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03']
            timeData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1006, 1006, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015,
                         1018, 1018, 1018, 1019, 1020]
            df_data_correct_SOLL = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_correct_SOLL

        def createDFSOLL_testCase_MissingPlacesAtEndOfListCorrectTime():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04']
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1019, 1019, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2029]
            df_data_correct_SOLL_last_place_missing = pd.DataFrame(
                {'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_correct_SOLL_last_place_missing

        def createDFSOLL_testCase_MissingPlacesAtEndOfListCorrectTimeAndLast3Values():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04']
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1019, 1019, 2021, 2022, 2023, 2024, 2025, 2026, 2026, 2026, 2026, 2026]
            df_data_correct_SOLL_last_place_missing = pd.DataFrame(
                {'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_correct_SOLL_last_place_missing

        def createDFSOLL_testCase_Missing9PlacesAtIndex4and8a16a17a18a21a22a23a24():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04']
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1004, 1006, 1006, 1007, 1008, 1009, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1018, 1018, 2022, 2022, 2023, 2024, 2025, 2026, 2026, 2026, 2026, 2026]
            df_data_correct_SOLL__missing_9_values = pd.DataFrame(
                {'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_correct_SOLL__missing_9_values

        def createDFSOLL_testCase_Missing12Places():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04']
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1004, 1006, 1006, 1007, 1008, 1009, 1009, 1011, 1012, 1013, 1016, 1016, 1016,
                         1017, 1018, 1018, 1018, 2023, 2023, 2023, 2024, 2025, 2026, 2026, 2026, 2026, 2026]
            df_data_correct_SOLL_missing_12_values = pd.DataFrame({'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_correct_SOLL_missing_12_values

        def createListCorrectTime():
            list_time = [1,2,3,4,5,6,7,8,9,10]
            return list_time

        def createDFIncorrectOnePlaceFalse():
            dateData = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                        '2020-01-03',
                        '2020-01-03']
            timeData = [1, 2, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 6, 7, 8, 9, 10]
            valueData = [1001, 1002, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014,
                         1016, 1017, 1018, 1019, 1020]
            df_data_incorrect_second_place_missing_time_1 = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_incorrect_second_place_missing_time_1

        def createDFIncorrectTwoPlacesFalse():
            dateData = ['2020-01-01', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                        '2020-01-03', '2020-01-03']
            timeData = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1, 2, 3, 4, 5, 6, 7, 9, 10]
            valueData = [1000, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1020, 1021]
            df_data_incorrect_secondAnd18th_place_false_time = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_incorrect_secondAnd18th_place_false_time

        def createDFIncorrectMissingTwoConsecutiveValuesAndOneValue():
            dateData = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                        '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                        '2020-01-03', '2020-01-03', '2020-01-03']
            timeData = [1, 2, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 8, 9, 10]
            valueData = [1001, 1002, 1003, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015,
                         1018, 1019, 1020]
            df_data_incorrect = pd.DataFrame({'date': dateData, 'time': timeData, 'close': valueData})
            return df_data_incorrect

        def createDFIncorrectMissingPlacesAtEndOfListCorrectTime():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04', '2020-01-04']
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            valueData = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1019, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
            df_data_INcorrect_missing_last_place_from_list = pd.DataFrame(
                {'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_INcorrect_missing_last_place_from_list

        def createDFIncorrectMissingPlacesFalseAtEndOfListCorrectTimeANDlast3values():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-04', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', ]
            dateData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, ]
            valueData = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 1019, 2021, 2022, 2023, 2024, 2025, 2026]
            df_data_INcorrect_missing_last_place_from_list_and_last_3_values = pd.DataFrame(
                {'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_INcorrect_missing_last_place_from_list_and_last_3_values


        def createDFINcorrectMissing9PlacesAtIndex4and8a16a17a18a21a22a23a24():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', ]
            dateData = [1, 2, 3, 4, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, ]
            valueData = [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1014, 1015, 1016,
                         1017, 1018, 2022, 2023, 2024, 2025, 2026]
            df_data_INcorrect_missing_9_values = pd.DataFrame({'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_INcorrect_missing_9_values

        def createDFINcorrectMissing12places():
            dateOne = ['2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02', '2020-01-02',
                       '2020-01-02', '2020-01-02', '2020-01-03',
                       '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-03', '2020-01-04',
                       '2020-01-04', '2020-01-04', '2020-01-04', ]
            dateData = [1, 2, 3, 4, 6, 7, 8, 9, 1, 2, 3, 6, 7, 8, 3, 4, 5, 6, ]
            valueData = [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1016,
                         1017, 1018, 2023, 2024, 2025, 2026]
            df_data_INcorrect_missing_12_values = pd.DataFrame({'date': dateOne, 'time': dateData, 'close': valueData})
            return df_data_INcorrect_missing_12_values

        #create DataFrames
        self.DFSOLL_testCase_onePlaceFalse = createDFSOLL_testCase_onePlaceFalse()
        self.DFIncorrectOnePlaceFalse = createDFIncorrectOnePlaceFalse()
        
        self.DFSOLL_testCase_TwoPlacesFalse = createDFSOLL_testCase_TwoPlacesFalse()
        self.DFIncorrectTwoPlacesFalse = createDFIncorrectTwoPlacesFalse()

        self.DFSOLL_testCase_twoConsecutivePlacesFalse = createDFSOLL_testCase_twoConsecutivePlacesFalse_plusOnePlaceFalse()
        self.DFIncorrectMissingTwoConsecutiveValuesAndOneValue = createDFIncorrectMissingTwoConsecutiveValuesAndOneValue()

        self.DFSOLL_testCase_MissingPlacesAtEndOfListCorrectTime = createDFSOLL_testCase_MissingPlacesAtEndOfListCorrectTime()
        self.DFIncorrectOnePlaceFalseAtEndOfListCorrectTime = createDFIncorrectMissingPlacesAtEndOfListCorrectTime()

        self.DFSOLL_testCase_MissingPlacesAtEndOfListCorrectTimeAndLast3Values = createDFSOLL_testCase_MissingPlacesAtEndOfListCorrectTimeAndLast3Values()
        self.DFIncorrectMissingPlacesFalseAtEndOfListCorrectTimeANDlast3values = createDFIncorrectMissingPlacesFalseAtEndOfListCorrectTimeANDlast3values()

        self.DFSOLL_testCase_Missing9PlacesAtIndex4and8a16a17a18a21a22a23a24 = createDFSOLL_testCase_Missing9PlacesAtIndex4and8a16a17a18a21a22a23a24()
        self.DFINcorrectMissing9PlacesAtIndex4and8a16a17a18a21a22a23a24 = createDFINcorrectMissing9PlacesAtIndex4and8a16a17a18a21a22a23a24()

        self.DFSOLL_testCase_Missing12Places = createDFSOLL_testCase_Missing12Places()
        self.DFINcorrectMissing12places = createDFINcorrectMissing12places()

        self.listCorrectTime = createListCorrectTime()


    def test_find_one_missing_value_in_DataFrame_and_replace_it(self):
        SOLL_DataFrame = self.DFSOLL_testCase_onePlaceFalse
        DFIncorrectOnePlaceFalse = self.DFIncorrectOnePlaceFalse

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrectOnePlaceFalse,self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame,IST_DataFrame, check_dtype=False)


    '''
    def test_find_two_missing_value_in_DataFrame_and_replace_it(self):
        SOLL_DataFrame = self.DFSOLL_testCase_TwoPlacesFalse
        DFIncorrectTwoPlacesFalse = self.DFIncorrectTwoPlacesFalse

        CheckForMissingData = DemoCheckForMissingData()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingData(DFIncorrectTwoPlacesFalse,self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)
    '''

    def test_find_two_consecutive_places_missing__and_one_simple_missing_value_and_replace_them(self):
        DFIncorrect = self.DFIncorrectMissingTwoConsecutiveValuesAndOneValue
        SOLL_DataFrame = self.DFSOLL_testCase_twoConsecutivePlacesFalse

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrect, self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)

    def test_find_missing_data_on_last_place_of_list(self):
        DFIncorrect = self.DFIncorrectOnePlaceFalseAtEndOfListCorrectTime
        SOLL_DataFrame = self.DFSOLL_testCase_MissingPlacesAtEndOfListCorrectTime

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrect, self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)

    def test_find_missing_data_on_last_place_of_list_and_3_missing_values_at_the_end(self):
        DFIncorrect = self.DFIncorrectMissingPlacesFalseAtEndOfListCorrectTimeANDlast3values
        SOLL_DataFrame = self.DFSOLL_testCase_MissingPlacesAtEndOfListCorrectTimeAndLast3Values

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrect, self.listCorrectTime)
        print("IST_DataFrame")

        print(IST_DataFrame)
        print("SOLL_DataFrame")
        print(SOLL_DataFrame)
        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)

    def test_find_missing_data_missing_9_values(self):
        DFIncorrect = self.DFINcorrectMissing9PlacesAtIndex4and8a16a17a18a21a22a23a24
        SOLL_DataFrame = self.DFSOLL_testCase_Missing9PlacesAtIndex4and8a16a17a18a21a22a23a24

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrect, self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)

    def test_find_missing_data_missing_12_values(self):
        DFIncorrect = self.DFINcorrectMissing12places
        SOLL_DataFrame = self.DFSOLL_testCase_Missing12Places

        CheckForMissingData = DemoCheckForMissingDataHSI()
        IST_DataFrame = CheckForMissingData.seachAndReplaceMissingDataHSI(DFIncorrect, self.listCorrectTime)

        assert_frame_equal(SOLL_DataFrame, IST_DataFrame, check_dtype=False)
    def tearDown(self):
        self.DFSOLL_testCase_onePlaceFalse = None
        self.DFIncorrectOnePlaceFalse = None
        self.DFIncorrectTwoPlacesFalse = None
        self.listCorrectTime = None


if __name__ == '__main__':
    unittest.main()



"""
        print("IST_DataFrame")

        print(IST_DataFrame)
        print("SOLL_DataFrame")
        print(SOLL_DataFrame)
"""