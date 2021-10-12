import flask 
from flask import Flask, request
from flask.templating import render_template
import joblib
import numpy as np
import pandas as pd

#플라스크 어플리케이션 객체
app=Flask(__name__)

#메인페이지 라우팅
@app.route("/")
def index():
    return print("오늘 장 볼까 말까 앱 입니다.")

#데이터 예측 처리 
@app.route("/")
def input():
    return render_template('questions.html')
@app.route('/predict',method=['POST'])
def make_prediction():
     #user 에게 정보 입력 받기 
    avgtemp=float(input("오늘 평균기온"))
    maxtemp=float(input("오늘 최고 기온"))
    mintemp=float(input("오늘 최저기온"))
    precipitation=float(("오늘 강수량"))
        #장바구니 가격 변수 선언
    total=0

        #입력된 파라미터를 배열로 준비 
    x_data=pd.DataFrame(columns=["avgtemp","maxtemp","mintemp","precipitation"])
    columns=["avgtemp","maxtemp","mintemp","precipitation"]
    data=[avgtemp,maxtemp,mintemp,precipitation]

        #입력값 토대로 예측 값 찾기 
    x_data.loc[0]=data
    total=loaded_model.predict(x_data)
    if total > float("64581"): 
        result= "expensive"
    else:
        result= "ok"
        return result
        #결과를 저장 
    
    return result
        
if __name__=='__main__':
    #model load
    loaded_model=joblib.load('/Users/chohee/Section3_Project/Flask_Web_Server/model/rf.pkl')
    #flask 서비스 시작 
    app.run(debug=True)