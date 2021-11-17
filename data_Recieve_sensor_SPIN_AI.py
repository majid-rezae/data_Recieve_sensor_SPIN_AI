import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
 
 
value = sys.argv[1]
 
 




    
    ####import all the packages####
import pymongo
import json 
from pandas import read_csv
from pandas import to_datetime
from datetime import datetime
from pandas import DataFrame
import math
import string
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import  Dense,LSTM,Dropout
from tensorflow.keras import backend  
from tensorflow.keras.models import Sequential
from pandas.tseries.offsets import DateOffset
from datetime import datetime,date

####import and read database csv file####
dev_eui=value

myclient = pymongo.MongoClient("mongodb://ibti:ibti@iotibti.ddns.net:27017/admin?tls=true")
mydb = myclient["data"]
#dev_eui='8cf9574000000012'
col_data = mydb[dev_eui]

lista_dados = []

lista_tempo= []
tempo = 0

for item in col_data.find():
    if int(item['ts'])- tempo >= 3600*24:
        tempo=int(item['ts'])
        dado=float(item['temp'])
        lista_tempo.append(datetime.utcfromtimestamp(tempo).strftime('%Y-%m-%d'))
        lista_dados.append(dado)
        
lista_tempo.reverse()
lista_dados.reverse()

del lista_tempo[100:]
del lista_dados[100:]

lista_tempo.reverse()
lista_dados.reverse()

dic={'Date':lista_tempo, 'Temperature':lista_dados}
df=pd.DataFrame(dic) 

####select Data column as index####
df["Date"] =pd.to_datetime(df.Date)
df=df.set_index ('Date')
#dataset=dataset.sort_values(by='Data')

####filter a select column####
df= df.replace(',','.', regex=True)
#df = dataset.filter(["Velocidade do vento (m/s)"])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print('Here is Data recieved by Sensor')
    print(df)
    print( 'End of Data recieved by Sensor')
df.to_csv(r'Forcasting_spincsv', index = True, header=True)

