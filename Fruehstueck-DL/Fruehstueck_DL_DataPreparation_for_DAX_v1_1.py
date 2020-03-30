from datetime import time
import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)


class DataPreparationDAX:
    dataFrame = None

    def __init__(self, pathInputFile):
        self.inputFile = pathInputFile
        # self.df = pd.read_csv(self.inputFile,sep=';')
        # print(self.inputFile)
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')


    def showDataFrame(self):
        print(self.dataFrame)

    def formatDataFrame(self):

        def dropUnwantedTradingTimes():
            # JAN würde die "remove all times" nochmal zerkleinern

            df = self.dataFrame

            # remove all times from 00:00 - 1:59 h ## variablen ausschreiben!!!!!!!
            # JAN guter code ist auf einem Notebook screen lesbar
            for h in range(0, 2):
                for m in range(0, 60):
                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    df = df.loc[df['time'] != str(time_convert)]

            # remove all times from 5:01 -13:58 ; 14:00 - 00:00
            for h in range(5, 24):
                for m in range(0, 60):
                    if (h == 5 and m == 0) or (h == 13 and m == 59):
                        continue

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    df = df.loc[df['time'] != str(time_convert)]

            self.dataFrame = df
        def keepOnlyColumnsDateTimeClose():  # function name umbennen

            # drop not needed columns
            self.dataFrame.drop(columns=['open', 'high', 'low', 'volume'], inplace=True)
            # reset the index to (0,1,2,3,4.....) and drop the old index ( 1,3,5,7.....)
            self.dataFrame.reset_index(inplace=True, drop=True)

        def setColumnCloseToFloat():
            # TODO '{:06.2f}'.format(3.141592653589793) format to float with one digit after point 002.X
            self.dataFrame['close'] = self.dataFrame['close'].astype(float)
        dropUnwantedTradingTimes()
        keepOnlyColumnsDateTimeClose()
        setColumnCloseToFloat()

        return self.dataFrame
    @classmethod
    def saveDataFrame(cls, stockData, pathToSave):
        def jobDoneMsg(pathToSave):
            print()
            print()
            print('Job Done')
            print('DataFrame saved under' + pathToSave)
            print()

        stockData.to_csv(str(pathToSave), sep=',')

        jobDoneMsg(pathToSave)



def main():

    pathRawDataFrameDAX = 'D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019.csv'
    savingpathFormatedDataFrame = 'D:/Profiles/fuhlmann/Programmierung/python/boerse_DataScience_project/Boersendaten/DAX_data/DAX_M1_2019/DAX_M1_2019_only_Close_values_UTC-5_test.csv'
    # performance gedanke, Erst columns dann rows deleten oder umgekehert -> timewatch messung
    # JAN performance gedanken, überlegen aus der tehorie heraus warum so einen best. code aufrauf und nciht anders.
    DFtoPrepare = DataPreparationDAX(pathRawDataFrameDAX)
    DFtoPrepare.showDataFrame()
    formatedDataFrame = DFtoPrepare.formatDataFrame()
    DFtoPrepare.saveDataFrame(formatedDataFrame, savingpathFormatedDataFrame)
    print(formatedDataFrame)

main()
