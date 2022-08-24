# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 08:29:20 2022

@author: Mahesh
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('train_data_evaluation_part_2.csv')
df = df[:3000]
 
df = df[df['Age'] > 0] 
df = df[df['AverageLeadTime'] >= 0] 
df['CheckIn'] = np.where(df['BookingsCheckedIn'] >= 1,1,0)
df = pd.get_dummies(df,columns = ['DistributionChannel'])
df = pd.get_dummies(df,columns = ['MarketSegment'])
df.drop(['Unnamed: 0','ID','Nationality'],axis=1,inplace=True)

#df = df.rename(columns={'DistributionChannel_Electronic Distribution':'DistributionChannel_Electronic_Distribution','DistributionChannel_Travel Agent/Operator':'DistributionChannel_Travel_Agent_Operator', 'MarketSegment_Travel Agent/Operator':'MarketSegment_Travel_Agent_Operator'})

x =df[['OtherRevenue', 'BookingsCanceled', 'BookingsNoShowed', 'PersonsNights', 'RoomNights', 'DaysSinceLastStay','DaysSinceFirstStay','DistributionChannel_Electronic Distribution','DistributionChannel_Travel Agent/Operator', 'MarketSegment_Aviation','MarketSegment_Complementary', 'MarketSegment_Corporate','MarketSegment_Direct', 'MarketSegment_Groups', 'MarketSegment_Other','MarketSegment_Travel Agent/Operator']]
y = df['CheckIn']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

dt = DecisionTreeClassifier(criterion = 'entropy',max_depth = 11,max_features = 7)

dt.fit(x_train,y_train)

pickle.dump(dt,open("model.pkl","wb"))
