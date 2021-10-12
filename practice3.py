# -*- conding:utf-8 -*-'
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

num_of_row=100
start_page_no=1
end_page_no=50
service_key='y4oCiBgOJKdw%2FnBw%2FPiQj5jq4XwmFrwOtmdGUxo3%2BRnaHxom20HSK2M072wsGXhR8oCHwsb8nBlVIkTChvJyDA%3D%3D'
start_date='20200101' #yyyymmddex 20100102
end_date='20201231'
stnId=108 #지점 번호 default 108 =  서울

rows = []
keys_list=['tm','stnId','stnName','AvgTa','MaxTa','MinTa','sumRn']

for i in range(end_page_no,start_page_no+1):
    url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={service_key}&numOfRows={num_of_row}&pageNo={page_no}&dataCd=ASOS&dateCd=DAY&startDt={start_date}&endDt={end_date}&stnIds={stnId}&dataType=XML'

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    for j in soup.find_all("item"):
        rows.append({"일자": j.tm.string,
                        "지역 아이디": j.stnId.string,
                        "지역 이름": j.stnName.string,
                        "일 평균 기온": j.AvgTa.string,
                        "일 최고 기온": j.MaxTa.string,
                        "일 최저 기온": j.MinTa.string,
                        "일 강수량":j.sumRn.string
                        })

columns = ["일자", "지역 아이디", "지역 이름", "일 평균 기온","일 최고 기온","일 최저 기온","일 강수량"]
weather_df = pd.DataFrame(rows, columns=columns)

print(weather_df)

# engine = create_engine("mysql+mysqldb://<db id>:"+"<password>" +
#                        "@<ip_address>/<db_name>?charset=utf8", encoding='utf8')
# conn = engine.connect()

# bus_stop_df.to_sql(name='<table_name>', con=engine,
#                    if_exists='replace', index=False)