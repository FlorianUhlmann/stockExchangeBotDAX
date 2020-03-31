import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import datetime as h
from Fruehstueck_DL_DataPreparation_for_DAX_v1_1 import DataPreparationDAX


class TestDataPreparation(unittest.TestCase):

    def testForSimpleDataframe(self):
        ISTDataFrame = pd.DataFrame()
        SollDataFrame = pd.DataFrame()

        #create dataframe reference
        SollDataFrame = pd.DataFrame({'Hello': []}, columns=['Hello'])
        SollDataFrame = SollDataFrame.astype(object)
        #get dataframe to check
        dataPreparation = DataPreparationDAX('d:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/testCSV.csv')
        ISTDataFrame = dataPreparation.dataFrame
        #compare both dataframes
        assert_frame_equal(ISTDataFrame, SollDataFrame, check_column_type = True, check_frame_type = False, check_index_type = False)

    def testForColumnCut(self):

        ISTDataFrame = pd.DataFrame()
        SollDataFrame = pd.DataFrame({'date':[h.date(2019,1,2),h.date(2019,1,2),h.date(2019,1,2),h.date(2019,1,2),h.date(2019,1,3),h.date(2019,1,3),h.date(2019,1,3),h.date(2019,1,4),h.date(2019,1,4)],
                                        'time': [h.time(22,59),h.time(9,00),h.time(10),h.time(12),h.time(22,59),h.time(9,00),h.time(10),h.time(12),h.time(22,59)],
                                        'close':[1000.0,1200.0,1400.0,1600.0,1000.0,1200.0,1400.0,1600.0,1000.0]})
        DFtoPrepare = DataPreparationDAX(
            'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DAX30_TimeFrameMin_M1_CandleData_TDD_DataFrameMuster.csv')
        DFtoPrepare.dataFrame = DFtoPrepare.removeDataInTimerange(DFtoPrepare.dataFrame)
        DFtoPrepare.showDataFrame()
        DFtoPrepare.dataFrame = DFtoPrepare.keepOnlyColumnsDateTimeClose(DFtoPrepare.dataFrame)
        ISTDataFrame = DFtoPrepare.dataFrame
        #DFtoPrepare.dataFrame = DFtoPrepare.dataFrame.iloc[9:]
        #DFtoPrepare.showDataFrame()
        assert_frame_equal(ISTDataFrame, SollDataFrame, check_column_type = False, check_frame_type = False, check_index_type = False)


if __name__ == '__main__':
    unittest.main()