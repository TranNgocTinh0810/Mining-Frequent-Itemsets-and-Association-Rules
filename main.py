import sys
import csv
import numpy as np
from csv import reader
import pandas as pd


def pre_process(df):
  '''
  :param dataset: List
  :return: List
  '''
  a=['State','Area Code','Phone','Day Charge','Eve Charge','Night Charge','Intl Charge']  #Xóa các cột dữ liệu không tác động tới Churn
  df.drop(a,axis=1,inplace=True)
  return df

file='churn.csv'
df=pd.read_csv(file, nrows=1000)   #Xử lí trên chuỗi con của dữ liệu(1000 Hàng đầu tiên)
print(df.shape)
pre_process(df)
print(df.shape)
print(df.dtypes)
print(df)