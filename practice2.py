# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd

num_of_row=500
page_no=1
service_key='y4oCiBgOJKdw%2FnBw%2FPiQj5jq4XwmFrwOtmdGUxo3%2BRnaHxom20HSK2M072wsGXhR8oCHwsb8nBlVIkTChvJyDA%3D%3D'
start_date='20200101' #yyyymmddex 20100102
end_date='20201231'
stnId=108 #지점 번호 default 108 =  서울

API_URL=f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={service_key}&numOfRows={num_of_row}&pageNo={page_no}&dataCd=ASOS&dateCd=DAY&startDt={start_date}&endDt={end_date}&stnIds={stnId}&dataType=JSON'

raw_data = requests.get(API_URL)
data = json.loads(raw_data.text) 
print(data)

"""
사용 데이터 
tm :연월일
stnId:지역아이디
stnName:지역 이름
AvgTa: 일 평균 기온
MaxTa : 일 최고 기온
MinTa:일 최저 기온
sumRn:일 강수량
"""
bodies=data["response"]["body"]["items"]["item"] # 일별 정보 
keys_list=['tm','stnId','stnName','AvgTa','MaxTa','MinTa','sumRn'] #사용할 data column목록


dates=[]
for body in bodies:
    date=body[keys_list[0]]
    dates.append(date)

print(dates)

# def parsing(key):
#     if keys_list[key] in body:
#             key+"s"=[]
#             key=body[keys_list[key]]
#             key+"s".append(date)
#             return dates



for key in keys_list:
    key=[]
    parsing(key)

#print("def 시도")
#print(parsing(0)) # 됐다! 



