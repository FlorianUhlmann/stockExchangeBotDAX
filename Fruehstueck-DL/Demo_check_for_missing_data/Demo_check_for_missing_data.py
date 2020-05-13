from datetime import time
import pandas as pd
# Set ipython's max row display
pd.set_option('display.max_row', 10)

class DemoCheckForMissingData:

    def __init__(self):
        pass

    def seachAndReplaceMissingData(self,inputDataFrame,DAX_list_tradingTimes):

        df = inputDataFrame
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
                    if (inx % 10 == 0 and inx != 0):
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
