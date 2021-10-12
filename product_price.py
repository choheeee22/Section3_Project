
import requests
from bs4 import BeautifulSoup  

#농산물 가격 가져오기 - 갈치, 배추, 사과, 돼지고기,

p_cert_key='a3acde6f-14b9-48c9-98a6-74ec4b6ee0a7'
p_cert_id='2083'
start_date='2020-01-01'
end_date='2020-12-31'
p_productclscode='01' #구분 ( 01:소매, 02:도매, default:02 )
item='613'#부류/품목/품종 갈치 600-613-01, 배추 200-213-01, 사과400-413-01, 돼지고기 500-514-01(국산냉장)
category='600'#부류코드
p_countrycode='1101' # 소매가격 선택 1101 서울
p_convert_kg_yn='Y' #kg단위 환산여부(Y : 1kg 단위표시

#URL=f'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode={p_productclscode}&p_startday={start_date}&p_endday={end_date}&p_itemcategorycode={p_itemcategorycode}&p_itemcode={p_itemcode}&p_kindcode=00&p_productrankcode=04&p_countrycode={p_countrycode}&p_convert_kg_yn={p_convert_kg_yn}&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype=xml'

#갈치 (p_kindcode=01,&p_productrankcode=05)
URL=f'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday={start_date}&p_endday={end_date}&p_itemcategorycode={category}&p_itemcode={item}&p_countrycode=1101&p_convert_kg_yn=Y&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype=xml'
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
#items=soup.find_all("item")

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

COLLECTION='pricecollection'
collection=db[COLLECTION]
print(collection)
print("mongo collection 생성")

#제품 가격 칼럼 & 정보 뽑기
key_list=['itemname','yyyy','regday','price']
def product():
    for i in key_list:
        dic_={}
        list=[]
        i=soup.find_all(i)
        for j in i:
            list.append(j.get_text())
        dic_[j.name]=list
        db.pricecollection.insert_one(dic_)

print("갈치가격")
print(URL)
print(soup.find('itemname'))
hairtail=product()

#배추
item='211'#부류/품목/품종 갈치 600-613-01, 배추 200-211-01, 사과400-411-01, 돼지고기 500-514-01(국산냉장)
category='200'#부류코드
URL=f'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday={start_date}&p_endday={end_date}&p_itemcategorycode={category}&p_itemcode={item}&p_countrycode=1101&p_convert_kg_yn=Y&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype=xml'
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
print("배추가격")
print(URL)
print(soup.find('itemname'))
cabbage=product()

#배

item='412'#부류/품목/품종 갈치 600-613-01, 배추 200-211-01, 사과400-411-01, 돼지고기 500-514-01(국산냉장)
category='400'#부류코드
URL=f'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday={start_date}&p_endday={end_date}&p_itemcategorycode={category}&p_itemcode={item}&p_countrycode=1101&p_convert_kg_yn=Y&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype=xml'
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
print("배가격")
print(URL)
print(soup.find("itemname"))
apple=product()

#돼지고기 

item='514'#부류/품목/품종 갈치 600-613-01, 배추 200-213-01, 사과400-413-01, 돼지고기 500-514-01(국산냉장)
category='500'#부류코드
URL=f'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday={start_date}&p_endday={end_date}&p_itemcategorycode={category}&p_itemcode={item}&p_countrycode=1101&p_convert_kg_yn=Y&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype=xml'
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
print("돼지고기 가격")
print(URL)
print(soup.find("itemname"))
pork=product()