#-*-coding:utf-8-*-
import joblib
import numpy as np
import pandas as pd

loaded_model=joblib.load('rf.pkl')

avgtemp=float(input('평균기온:'))
maxtemp=float(input("오늘 최고 기온:"))
mintemp=float(input("오늘 최저기온:"))
precipitation=float(input("오늘 강수량:"))

x_data=pd.DataFrame(columns=["avgtemp","maxtemp","mintemp","precipitation"])
columns=["avgtemp","maxtemp","mintemp","precipitation"]
data=[avgtemp,maxtemp,mintemp,precipitation]
x_data.loc[0]=data
pred=loaded_model.predict(x_data)
print(pred)

if pred > float("64581"): 
    result= "expensive"
else:
    result= "ok"
print(result)
