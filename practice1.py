from bs4.element import TemplateString
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
#stnId=items.find_all('stnId')
stnId=soup.find("stnid")
#print(stnId.text) #name은 tag 명, text 는 tag속 내용 
n=0
#for i in items:
    #dic_ = {}
# for column in keys_list:
#     dic_={}
#     column=soup.find_all()
#     dic_[column]=dic_[soup.column.get_text()] # 열 한 개 씩 완성 
#     print(dic_)

#컬럼명당 하나씩 데이터 딕셔너리로 저장 
for i in keys_list:
    dic_={}
    i=soup.find_all(i)
    for j in i:
        dic_[j.name]=j.get_text()

"""처음 parsing 참고 코드

for i in items:
    dic_ = {}
    for j in i.find_all():
      dic_[j.name] = [j.text]
    asos = pd.concat([asos,pd.DataFrame(dic_)],axis=0)
    """
    

