import os
import pandas as pd
from datetime import datetime, time
pd.set_option('display.max_rows', None)

class DataPreparationDAX_checkForMissingData:
    dataFrame = None

    def __init__(self, pathInputFile):
        self.inputFile = pathInputFile
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')

    def showDataFrame(self):
        print(self.dataFrame)

    def seachAndReplaceMissingData(self,inputDataFrame):

        def GenerateList_tradingTimesDAX():
            list_featuresDAX = []
            list_featuresDAX.append("13:59")
            for h in range(2, 6):
                for m in range(0, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresDAX.append(str(time_convert))
                    if (h == 5): break

            return list_featuresDAX

        def resetListIndex(inx, inc):
            # reset list index at end of list = 182
            if inx % 182 == 0 and inx != 0:
                return 0
            else:
                return inc

        def checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df_incrt, inx, inc, DAX_list_Time):

            if (df_incrt.time[inx] == 10):
                print("is correct end")
                df_incrt
            elif (df_incrt.time[inx] == 9):
                rowToAppend = pd.DataFrame(
                    {"date": df_incrt.date.loc[inx], "time": DAX_list_Time[inc], "close": df_incrt.close.loc[inx]},
                    index=[inx])
                print(rowToAppend)
                return df_incrt.append(rowToAppend, ignore_index=True)
            else:
                print("check the last rows of input data. The time column is missing values")
                df_incrt
            return df_incrt

        DAX_list_tradingTimes = GenerateList_tradingTimesDAX()

        df = inputDataFrame


        inc = 0
        inc_index = 0
        lengthDataFrame = len(df)
        while inc_index < lengthDataFrame:

            for inx, curTime in enumerate(df.time):
                inc = resetListIndex(inx, inc)

                # print( inx ,curTime,DAX_list_Time[inc] )
                if curTime == DAX_list_tradingTimes[inc]:
                    # print( inx ,curTime ,DAX_list_Time[inc] )
                    inc_index = inx + 1

                    # print('inc_index = ',inc_index)

                else:
                    if DAX_list_tradingTimes[inc] == '13:59' and curTime != DAX_list_tradingTimes[inc]:
                        print()
                        print('time 13:59 missing at index {}'.format(inx))
                        print('CODE EXECUTION STOPS HERE')
                        print('please add missing data and run the program again')
                        print()
                        # stop loop
                        exit(1)

                    elif (inx % 181 == 0 and inx != 0):
                        rowToInsert = pd.DataFrame({"date": df.date.loc[inx - 1], "time": DAX_list_tradingTimes[inc],
                                                    "close": df.close.loc[inx - 1]}, index=[inx])
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                    else:
                        # print(df_incrt.date.loc[inx],df_incrt.time.loc[inx],df_incrt.close.loc[inx])
                        rowToInsert = pd.DataFrame({"date": df.date.loc[inx], "time": DAX_list_tradingTimes[inc], "close": df.close.loc[inx]},index=[inx])
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)

                    # print("new Val " + str(df_incrt.loc[inx]))
                    print('in 2nd loop')
                    # print(df_incrt.loc[inc])

                    print()
                    inc_index = inx + 1
                    inc = 0
                    lengthDataFrame = len(df)
                    break

                inc = inc + 1
                if (inc_index == lengthDataFrame):
                    df = checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df, inx, inc, DAX_list_tradingTimes)

        return df

    @classmethod
    def saveDataFrame(cls, stockData, pathToSave):
        def jobDoneMsg(pathToSave):
            print()
            print()
            print('Job Done')
            print('DataFrame saved under' + pathToSave)
            print()

        stockData.to_csv(str(pathToSave), sep=',',  index=False)

        jobDoneMsg(pathToSave)

def main()
    DAXDataPath = "D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DAX_data/"
    DAXData = "DAX_M1_2018/DAX_M1_2018_04_april_cleanedData.csv"
    cleanedDAXData = "DAX_M1_2018/DAX_M1_2018_04_april_cleanedANDunifiedData.csv"
    dataPath = os.path.join(DAXDataPath, DAXData)

    pathcleanedDataFrameDAX =  os.path.join(DAXDataPath, DAXData)
    savingpathcleanedDataFrameDAX =  os.path.join(DAXDataPath, cleanedDAXData)

    # performance gedanke, Erst columns dann rows deleten oder umgekehert -> timewatch messung
    # JAN performance gedanken, überlegen aus der tehorie heraus warum so einen best. code aufrauf und nciht anders.
    DFtoPrepare = DataPreparationDAX_checkForMissingData(pathcleanedDataFrameDAX)
    cleanedData = DFtoPrepare.seachAndReplaceMissingData(DFtoPrepare.dataFrame)
    print("cleanedData")
    print(cleanedData['time'].value_counts())
    print('rawData')
    print(DFtoPrepare.dataFrame['time'].value_counts())

    #formatedDataFrame = DFtoPrepare.formatDataFrame()
    DFtoPrepare.saveDataFrame(cleanedData, savingpathcleanedDataFrameDAX)

main()
