from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.preprocessing.text import Tokenizer
import mlflow.keras
import pandas as pd
import numpy as np
# The following import and function call are the only additions to code required
# to automatically log metrics and parameters to MLflow.
import mlflow.keras
mlflow.keras.autolog()
from sklearn.model_selection import train_test_split
# load data
stockData = pd.read_csv('D:/Profiles/fuhlmann/Programmierung/Python/boerse_DataScience_project/Boersendaten/DataFrameTrainingDataForAI_2018_01_january.csv')
##remove index column
stockData = stockData.drop(stockData.columns[0], axis=1)
#get labels and features
Y_label = stockData[['DAX_BUY_DAY','DAX_SELL_DAY','NO_TRADE_DAY']]
X_features = stockData.iloc[:,0:363]
#split training set
X_train, X_test, y_train, y_test = train_test_split(X_features, Y_label, test_size=0.2, random_state=42)

#setup DL model
model = Sequential()
model.add(Dense(units=200, activation='relu', input_dim=363))
model.add(Dense(units=50, activation='relu'))
model.add(Dense(units=3, activation='softmax'))
#configure model learning process
model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])

#train model
model.fit(X_train, y_train, epochs=5, batch_size=3)
#evaluate performance
loss_and_metrics = model.evaluate(X_test, y_test, batch_size=4)
print('____________________________________________________________________________')
print('                  _      _     ___              _ _      _   _       ')
print('  /\/\   ___   __| | ___| |   / _ \_ __ ___  __| (_) ___| |_(_) ___  _ __  ')
print(" /    \ / _ \ / _` |/ _ | |  / /_)| '__/ _ \/ _` | |/ __| __| |/ _ \| '_ \ '")
print('/ /\/\ | (_) | (_| |  __| | / ___/| | |  __| (_| | | (__| |_| | (_) | | | |')
print('\/    \/\___/ \__,_|\___|_| \/    |_|  \___|\__,_|_|\___|\__|_|\___/|_| |_|')
print('-----------------------------------------------------------------------------')
print('| The model has the following values on the test data  |')
print( 'loss: {:.2f} , accurracy: {:.2f}' .format(loss_and_metrics[0], loss_and_metrics[1]))