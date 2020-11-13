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
  a=['Phone','Day Charge','Eve Charge','Night Charge','Intl Charge']  #Xóa các cột dữ liệu không tác động tới Churn
  #'State', 'Area Code',
  df.drop(a,axis=1,inplace=True)
  return df

def hierarchies(df):
  '''
  Định nghĩa các khái niệm phân cấp cho các thuộc tính
  :param df:dataFrame
  :return:DataFrame
  '''
  '''a=['Account Length','VMail Message','Day Mins','Day Calls','Eve Mins','Eve Calls'
      ,'Night Mins','Night Calls','Intl Mins','Intl Calls','CustServ Calls']'''

  bins=df['Account Length'].quantile([0,0.35,0.65,1])
  #bins.iloc[-1] += 0.1
  grade_rank = pd.cut(df['Account Length'], bins, right=False,labels=['Short','Middle_Length','Long'])
  df['Account Length']=grade_rank
  return df

file='churn.txt'
df=pd.read_csv(file, nrows=1000)   #Xử lí trên chuỗi con của dữ liệu(1000 Hàng đầu tiên)
#print(df.shape)
pre_process(df)
#print(df.shape)
#print(df.dtypes)
#print(df)
Output="data.csv"

#print(df.mean(axis = 0, skipna = True)['Eve Calls'])
#print(df.mean(axis = 0, skipna = True))
#print(df.columns)
df=hierarchies(df)
df.to_csv(Output,index=False)