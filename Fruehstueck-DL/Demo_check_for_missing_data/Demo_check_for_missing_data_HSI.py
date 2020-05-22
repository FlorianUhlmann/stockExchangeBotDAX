from datetime import time
import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)

class DemoCheckForMissingDataHSI:

    def __init__(self):
        pass

    def seachAndReplaceMissingDataHSI(self,inputDataFrame,HSI_list_tradingTimes):

        df = inputDataFrame

        def resetListIndex(inx, inc):
            # reset list index at end of list = 182
            if inx % 10 == 0 and inx != 0:
                return 0
            else:
                return inc

        def checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df_incrt, inx, inc, DAX_list_Time):
            print("checkCorrectDataFrameEnding")
            if (df_incrt.time[inx] == 10):
                print("is correct end")
                df_incrt
            elif (df_incrt.time[inx] != 10):
                rowToAppend = pd.DataFrame(
                    {"date": df_incrt.date.loc[inx], "time": DAX_list_Time[inc], "close": df_incrt.close.loc[inx]},
                    index=[inx])
                return df_incrt.append(rowToAppend, ignore_index=True)
            else:
                print("check the last rows of input data. The time column is missing values")
                df_incrt
            return df_incrt

        inc = 0
        inc_index = 0
        lengthDataFrame = len(df)
        while inc_index < lengthDataFrame:

            for inx, curTime in enumerate(df.time):
                inc = resetListIndex(inx, inc)

                #if value of df.time as expected
                if curTime == HSI_list_tradingTimes[inc]:
                    inc_index = inx + 1
                #else change value
                else:
                    #if the value to change is the last value in HSI_list_tradingTimes AND indexvalue for the value is under 10
                    if (inx % 9 == 0 and inx != 0 and HSI_list_tradingTimes[inc] == 10):
                        # create value
                        print('in row 1')
                        rowToInsert = pd.DataFrame({"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                                                    "close": df.close.loc[inx - 1]}, index=[inx])
                        # insert value
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        #update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break
                    # if the value to change is the last value in HSI_list_tradingTimes AND indexvalue for the value is over 10
                    elif (inx % 19 == 0 and inx != 0 and HSI_list_tradingTimes[inc] == 10):
                        # create value
                        rowToInsert = pd.DataFrame({"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                                                    "close": df.close.loc[inx - 1]}, index=[inx])
                        # insert value
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        #update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break
                    # if the value is not the last value in     HSI_list_tradingTimes
                    else:
                        # handle special case -> value looks like last value before row starts again, but is just
                        #  bc of missing data   e.g. 1,2,3,4,5,6,1,2,3,4,5.....(missing7,8,9,10)
                        if (df.date.loc[inx - 1] != df.date.loc[inx] == df.date.loc[inx + 1] and inc != 0):
                           #create missing row
                            rowToInsert = pd.DataFrame({"date": df.date.loc[inx - 1], "time": HSI_list_tradingTimes[inc],
                                 "close": df.close.loc[inx - 1]}, index=[inx])
                        #handle normal case  e.g.  1,2,3,4, 7,8,9,10,1,2,3...... (missing 5,6)
                        else:
                            #create missing row
                            rowToInsert = pd.DataFrame({"date": df.date.loc[inx], "time": HSI_list_tradingTimes[inc],
                                                        "close": df.close.loc[inx]}, index=[inx])
                        #insert missing row
                        df = pd.concat([df.iloc[:inx], rowToInsert, df.iloc[inx:]]).reset_index(drop=True)
                        #update indices
                        inc_index = inx + 1
                        inc = 0
                        lengthDataFrame = len(df)
                        break

                inc = inc + 1
                #if end of datalist
                if (inc_index == lengthDataFrame):
                    
                    df = checkCorrectDataFrameEnding(inc_index, lengthDataFrame, df, inx, inc, HSI_list_tradingTimes)
                    #update indices
                    inc_index = inx + 1
                    inc = 0
                    lengthDataFrame = len(df)
        return df