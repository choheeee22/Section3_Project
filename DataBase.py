import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

##기상청 API 정보 가져오기 ##

num_of_row=500
start_page_no=1
end_page_no=50
service_key='y4oCiBgOJKdw%2FnBw%2FPiQj5jq4XwmFrwOtmdGUxo3%2BRnaHxom20HSK2M072wsGXhR8oCHwsb8nBlVIkTChvJyDA%3D%3D'
start_date='20200101' #yyyymmddex 20100102
end_date='20201231'
stnId=108 #지점 번호 default 108 =  서울

keys_list=['tm','stnid','stnnm','avgta','maxta','minta','sumrn']

url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={service_key}&numOfRows={num_of_row}&pageNo={start_page_no}&dataCd=ASOS&dateCd=DAY&startDt={start_date}&endDt={end_date}&stnIds={stnId}&dataType=XML'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
items=soup.find_all("item")



from pymongo import MongoClient
username='chohee'
password='chohee22'
URI=f'mongodb+srv://chohee:{password}@cluster0.ghxbe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client=MongoClient({URI})
#print(client) 로 연결여부 확인 완료 

#database 와 연결 
DATABASE='myFirstDatabase'
db=client[DATABASE]

#table (= collection) 생성 및 확인 

COLLECTION='weather-collection'
collection=db[COLLECTION]
print(collection)

#print(collection)로 생성 확인 완료 

#collection.insert_one(document={"hello":"weather"})
#connection security 관련 - allow access from anywhere 체크

#컬럼명당 하나씩 데이터 딕셔너리로 저장 
for i in keys_list:
    i=soup.find_all(i)
    list=[]
    dic_={}
    for j in i:
        list.append(j.get_text())
    dic_[j.name]=list
    db.collection.insert_one(dic_)

print("update done")

"""
처음 parsing 참고 코드 
asos = pd.DataFrame()
for i in items:
    dic_ = {}
    for k in keys_list:
        for j in i.find_all(k):
            dic_[j.name] = [j.text]
        asos2 = pd.concat([asos,pd.DataFrame(dic_)],axis=0)
#이거는 왜 안 되는지 모르겠다.. key _list에 있는 항목만 빼오기 
"""
