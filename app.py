# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:56:12 2022

@author: Mahesh
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os

app = Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Revenue = int(request.form['Revenue'])
        bookingcancelled =request.form['bookingcancelled']
        if(bookingcancelled =='Yes'):
            bookingcancelled=1
        elif(bookingcancelled =='No'):
            bookingcancelled=0	
        bookingnoshowed = request.form['bookingnoshowed']
        if(bookingnoshowed =='Yes'):
            bookingnoshowed=1
        elif(bookingnoshowed =='No'):
            bookingnoshowed=0	
        PersonsNights=int(request.form['PersonsNights'])
        RoomNights=int(request.form['RoomNights'])
        DaysSinceLastStay=int(request.form['DaysSinceLastStay'])
        DaysSinceFirstStay=int(request.form['DaysSinceFirstStay'])
        DistributionChannel=request.form['DistributionChannel']
        if(DistributionChannel =='Electronic Distribution'):
            DistributionChannel_Electronic_Distribution = 1
            DistributionChannel_Travel_Agent_Operator = 0            
        elif(DistributionChannel=='Travel Agent/Operator'):
            DistributionChannel_Electronic_Distribution = 0
            DistributionChannel_Travel_Agent_Operator = 1
        MarketSegment =request.form['MarketSegment']
        if(MarketSegment =='Aviation'):
            MarketSegment_Aviation = 1
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 0
            MarketSegment_Direct=0
            MarketSegment_Groups=0
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =0           
        elif(MarketSegment =='Complementary'):
            MarketSegment_Aviation = 0
            MarketSegment_Complementary = 1
            MarketSegment_Corporate = 0
            MarketSegment_Direct=0
            MarketSegment_Groups=0
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =0    
        elif(MarketSegment =='Corporate'):
            MarketSegment_Aviation = 0
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 1
            MarketSegment_Direct=0
            MarketSegment_Groups=0
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =0
        elif(MarketSegment =='Direct'):
            MarketSegment_Aviation = 0
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 0
            MarketSegment_Direct=1
            MarketSegment_Groups=0
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =0
        elif(MarketSegment =='Groups'):
            MarketSegment_Aviation = 1
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 0
            MarketSegment_Direct=0
            MarketSegment_Groups=1
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =0
        elif(MarketSegment =='Other'):
            MarketSegment_Aviation = 0
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 0
            MarketSegment_Direct=0
            MarketSegment_Groups=0
            MarketSegment_Other=1
            MarketSegment_Travel_Agent_Operator =0
        elif(MarketSegment =='Travel_Agent_Operator'):
            MarketSegment_Aviation = 0
            MarketSegment_Complementary = 0
            MarketSegment_Corporate = 0
            MarketSegment_Direct=0
            MarketSegment_Groups=0
            MarketSegment_Other=0
            MarketSegment_Travel_Agent_Operator =1
        prediction=model.predict([[Revenue,bookingcancelled,bookingnoshowed,PersonsNights,RoomNights,DaysSinceLastStay,DaysSinceFirstStay,DistributionChannel_Electronic_Distribution,DistributionChannel_Travel_Agent_Operator,MarketSegment_Aviation,MarketSegment_Complementary,MarketSegment_Corporate, MarketSegment_Direct,MarketSegment_Groups, MarketSegment_Other, MarketSegment_Travel_Agent_Operator]])
        output=round(prediction[0],2)
        if output == 0:
            return render_template('index.html',prediction_texts="Customer will not Check IN")
        else:
            return render_template('index.html',prediction_text="Customer will  Check IN")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)