import os
import pandas as pd
from datetime import datetime, time
pd.set_option('display.max_rows', None)

class DataPreparationHSI_checkForMissingData:
    dataFrame = None

    def __init__(self, pathInputFile):
        self.inputFile = pathInputFile
        self.dataFrame = pd.read_csv(self.inputFile, sep=',')

    def showDataFrame(self):
        print(self.dataFrame)

    def seachAndReplaceMissingData(self,inputDataFrame):

        df= inputDataFrame

        def GenerateList_tradingTimesHSI(self):

            list_featuresHSI = []
            for h in range(0, 4):
                for m in range(0, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresHSI.append(str(time_convert))
                    if (h == 3 and m >= 29): break
            for h in range(4, 5):
                for m in range(15, 60):

                    t = time(h, m)
                    time_convert = t.strftime("%H:%M")

                    list_featuresHSI.append(str(time_convert))
                    if (h == 5): break

            hsiClose = time(5, 0).strftime("%H:%M")
            list_featuresHSI.append(str(hsiClose))

            return list_featuresHSI

        def resetListIndex(inx, inc):
            # reset list index at end of list len(list) = 257
            if inx % 256 == 0 and inx != 0:
                return 0
            else:
                return inc

        def checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df_incrt, inx, inc, DAX_list_Time):
            print("checkCorrectDataFrameEnding")
            if (df_incrt.time[inx] == "05:00"):
                print("is correct end")
                df_incrt
            elif (df_incrt.time[inx] != "05:00"):
                rowToAppend = pd.DataFrame(
                    {"date": df_incrt.date.loc[inx], "time": DAX_list_Time[inc], "close": df_incrt.close.loc[inx]},
                    index=[inx])
                return df_incrt.append(rowToAppend, ignore_index=True)
            else:
                print("check the last rows of input data. The time column is missing values")
                df_incrt
            return df_incrt

        HSI_list_tradingTimes = GenerateList_tradingTimesHSI(self)

        inc = 0
        inc_index = 0
        lengthDataFrame = len(df)
        while inc_index < lengthDataFrame:
            if(lengthDataFrame >9999):
                break
            print(lengthDataFrame)
            for inx, curTime in enumerate(df.time):
                inc = resetListIndex(inx, inc)

                # if value of df.time as expected
                if curTime == HSI_list_tradingTimes[inc]:
                    inc_index = inx + 1
                # else change value
                else:
                    print("loop  replacing values")
                    # if the value to change is the last value in HSI_list_tradingTimes AND indexvalue for the value is under 10
                    if (inx % 255 == 0 and inx != 0 and HSI_list_tradingTimes[inc] == "05:00"):
                        # create value
                        print('in row 1')
                        rowToInsert = pd.DataFrame(
                            {"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                             "close": df.close.loc[inx - 1]}, index=[inx])
                        # insert value
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        # update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break
                    # if the value to change is the last value in HSI_list_tradingTimes AND indexvalue for the value is over 10
                    elif (inx %  509 == 0 and inx != 0 and HSI_list_tradingTimes[inc] == "05:00"):
                        # create value
                        print('in row 2')
                        rowToInsert = pd.DataFrame(
                            {"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                             "close": df.close.loc[inx - 1]}, index=[inx])
                        # insert value
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        # update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break
                    # if the value is not the last value in     HSI_list_tradingTimes
                    else:
                        print('in else loop')
                        # handle special case -> value looks like last value before row starts again, but is just
                        #  bc of missing data   e.g. 1,2,3,4,5,6,1,2,3,4,5.....(missing7,8,9,10)
                        if (df.date.loc[inx - 1] != df.date.loc[inx] == df.date.loc[inx + 1] and inc != 0):
                            # create missing row
                            rowToInsert = pd.DataFrame(
                                {"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                                 "close": df.close.loc[inx - 1]}, index=[inx])
                        # handle normal case  e.g.  1,2,3,4, 7,8,9,10,1,2,3...... (missing 5,6)
                        else:
                            # create missing row
                            rowToInsert = pd.DataFrame(
                                {"date": df.date.loc[inx], "time": HSI_list_tradingTimes[inc],
                                 "close": df.close.loc[inx]}, index=[inx])
                        # insert missing row
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        # update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break

                inc = inc + 1
                # if end of datalist
                if (inc_index == lengthDataFrame):
                    df = checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df, inx, inc,
                                                     HSI_list_tradingTimes)
                    # update indices
                    inc_index = inx + 1
                    inc = 0
                    lengthDataFrame = len(df)
                    break
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

def main():
    HSIDataPath = "D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/HSI_data/"
    HSIData = "HSI_M1_2018/HSI_M1_2018_02_february_cleanedData.csv"
    cleanedHSIData = "HSI_M1_2018/HSI_M1_2018_02_february_cleanedANDunifiedData.csv"
    dataPath = os.path.join(HSIDataPath, HSIData)

    pathcleanedDataFrameHSI =  os.path.join(HSIDataPath, HSIData)
    savingpathcleanedDataFrameHSI =  os.path.join(HSIDataPath, cleanedHSIData)

    # performance gedanke, Erst columns dann rows deleten oder umgekehert -> timewatch messung
    # JAN performance gedanken, überlegen aus der tehorie heraus warum so einen best. code aufrauf und nciht anders.
    DFtoPrepare = DataPreparationHSI_checkForMissingData(pathcleanedDataFrameHSI)
    cleanedData = DFtoPrepare.seachAndReplaceMissingData(DFtoPrepare.dataFrame)
    print("cleanedData")
    print(cleanedData['time'].value_counts())
    print('rawData')
    print(DFtoPrepare.dataFrame['time'].value_counts())

    #formatedDataFrame = DFtoPrepare.formatDataFrame()
    DFtoPrepare.saveDataFrame(cleanedData, savingpathcleanedDataFrameHSI)

main()
