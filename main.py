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
  a=['Phone','Area Code','Day Charge','Eve Charge','Night Charge','Intl Charge']  #Xóa các cột dữ liệu không tác động tới Churn
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
  grade_rank = pd.cut(df['Account Length'], bins, right=False,labels=['Short','Middle_Length','Long'])
  df['Account Length'] = grade_rank

  range=[0,9,41,51]             #0->13 None 13->23 Middle 23->51 Large
  grade_rank = pd.cut(df['VMail Message'], range, right=False, labels=['None','Middle(13->23)','Large(23->51)'],duplicates='drop')
  df['VMail Message'] = grade_rank

  range=[0,100,200,300,400]
  grade_rank = pd.cut(df['Day Mins'], range, right=False,labels=['0->100','100->200','200->300','300->400'],duplicates='drop')
  df['Day Mins'] = grade_rank

  range = [0, 50,100, 150,200]
  grade_rank = pd.cut(df['Day Calls'], range, right=False, labels=['0->50', '50->100','100->150', '150->200'],duplicates='drop')
  df['Day Calls'] = grade_rank

  range = [0, 100, 200, 300, 400]
  grade_rank = pd.cut(df['Eve Mins'], range, right=False, labels=['0->100', '100->200', '200->300', '300->400'],
                      duplicates='drop')
  df['Eve Mins'] = grade_rank

  range = [0, 50, 100, 150, 200]
  grade_rank = pd.cut(df['Eve Calls'], range, right=False, labels=['0->50', '50->100', '100->150', '150->200'],
                      duplicates='drop')
  df['Eve Calls'] = grade_rank

  range = [0, 100, 200, 300, 400]
  grade_rank = pd.cut(df['Night Mins'], range, right=False, labels=['0->100', '100->200', '200->300', '300->400'],
                      duplicates='drop')
  df['Night Mins'] = grade_rank

  range = [0, 50, 100, 150, 201]
  grade_rank = pd.cut(df['Night Calls'], range, right=False, labels=['0->50', '50->100', '100->150', '150->200'],
                      duplicates='drop')
  df['Night Calls'] = grade_rank

  range = [0, 100, 200, 300, 400]
  grade_rank = pd.cut(df['Intl Mins'], range, right=False, labels=['0->100', '100->200', '200->300', '300->400'],
                      duplicates='drop')
  df['Intl Mins'] = grade_rank

  range = [0, 5, 10, 15, 20.1]
  grade_rank = pd.cut(df['Intl Calls'], range, right=False, labels=['0->5', '5->10', '10->15', '15->20'],
                      duplicates='drop')
  df['Intl Calls'] = grade_rank

  range = [0, 5, 10]
  grade_rank = pd.cut(df['CustServ Calls'], range, right=False, labels=['0->5','5->10'],duplicates='drop')
  df['CustServ Calls'] = grade_rank

  #df['Area Code'] = df['Area Code'].astype('category')


  return df



file='churn.txt'
df=pd.read_csv(file, nrows=1000)   #Xử lí trên chuỗi con của dữ liệu(1000 Hàng đầu tiên)
#print(df.shape)
pre_process(df)
#print(df.shape)

#print(df)
Output="data.txt"

#print(df.mean(axis = 0, skipna = True)['Eve Calls'])
#print(df.mean(axis = 0, skipna = True))
#print(df.columns)
df=hierarchies(df)
print(df.dtypes)
df.to_csv(Output,index=False)