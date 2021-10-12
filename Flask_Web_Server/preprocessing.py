#!/usr/bin/env python
# coding: utf-8

# In[1]:


#mongo db에 있는 파일 가져오기 

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

#mongo db 파일 가져오기 
import pandas as pd
data=list(db.collection.find())


# In[2]:


#column마다 분리하기 
keys_list=['tm','stnid','stnnm','avgta','maxta','minta','sumrn']
for i in range(7):
    keys_list[i]


# In[3]:


#list dictionary 화

dictionary = {i : data[i] for i in range(len(data))}


# In[4]:


date=pd.DataFrame(dictionary[0]["tm"])


# In[5]:


weatherdf=pd.DataFrame()
for i in range(7):
    print(i)
    add=pd.DataFrame(dictionary[i][keys_list[i]])
    pd.concat([weatherdf,add],axis=0)


# In[6]:


#keys_list=['tm','stnid','stnnm','avgta','maxta','minta','sumrn']
date=pd.DataFrame(dictionary[0]["tm"])
locationId=pd.DataFrame(dictionary[1]["stnid"])
locationName=pd.DataFrame(dictionary[2]["stnnm"])
avgtemp=pd.DataFrame(dictionary[3]["avgta"])
maxtemp=pd.DataFrame(dictionary[4]["maxta"])
mintemp=pd.DataFrame(dictionary[5]["minta"])
precipitation=pd.DataFrame(dictionary[6]["sumrn"])


# In[7]:


weatherdf=pd.concat([date,locationId,locationName,avgtemp,maxtemp,mintemp,precipitation],axis=1)


# In[8]:


print(weatherdf)


# In[9]:


columns=['date','locationId','locationName','avgtemp','maxtemp','mintemp','precipitation']
weatherdf.columns=columns
print(weatherdf)


# In[10]:


#product price data가져오기 

data=list(db.pricecollection.find())


# In[11]:


#key_list=['itemname','yyyy','regday','price']


# In[12]:


#list dictionary 화
dictionary = {i : data[i] for i in range(len(data))}


# In[13]:


#price date frame 생성 함수
def df(n,name):
    itemname=pd.DataFrame(dictionary[n+0]["itemname"])
    year=pd.DataFrame(dictionary[n+1]["yyyy"])
    date=pd.DataFrame(dictionary[n+2]["regday"])
    price=pd.DataFrame(dictionary[n+3]["price"])
    name=pd.concat([itemname,year,date,price],axis=1)
    name.columns=['item','year','date','price'] #칼럼 명
    name['Date']=pd.to_datetime(name.year+"/"+name.date) #날짜 합치기 
    return name


# In[14]:


#df 생성
hairtail=df(0,'hairtail')
cabbage=df(4,'cabbage')
pear=df(8,'pear')
pork=df(12,'pork')


# In[15]:


#확인완료
print(hairtail)


# In[16]:


#date & year 없애기
def cleaning(df):
    df.drop('year',axis=1,inplace=True)
    df.drop('date',axis=1,inplace=True)
    return df


# In[17]:


cleaning(hairtail)
print(hairtail) #확인 완료


# In[18]:


#나머지 아이템도 year&date 없애기
cleaning(pear)
cleaning(pork)
cleaning(cabbage)


# In[19]:


#각 데이터 날짜 확인해 보기 
def check(df):
    a=df.drop_duplicates(subset='Date',keep="first")
    df=a.set_index('Date')
    return df


# In[20]:


hairtail=check(hairtail)


# In[21]:


cabbage=check(cabbage)
pear=check(pear)
pork=check(pork)


# In[22]:


pear.dtypes, hairtail.dtypes, pork.dtypes, cabbage.dtypes


# In[23]:


#merge 시도 
pricedfraw=hairtail.merge(cabbage,how="outer",on="Date")
print(pricedfraw)


# In[24]:


pricedfraw=pricedfraw.merge(pear,how="outer",on="Date")
pricedfraw=pricedfraw.merge(pork,how="outer",on="Date")
print(pricedfraw)


# In[25]:


pricedfraw.columns=["갈치","갈치가격","배추","배추가격","배","배가격","돼지고기","돼지고기가격"]


# In[106]:


pricedf=pricedfraw.drop(["갈치","배추","배","돼지고기"],axis=1)
print(pricedf)


# In[107]:


#데이터 타입 확인
pricedf.dtypes


# In[108]:


#결측치 확인 하기 
pd.DataFrame(pricedf.isnull().sum(),columns=['결측치 개수'])

# In[109]:


#object 숫자화 하기 
#nan 값 처리 
import numpy as np
pricedf=pricedf.replace(np.nan, '', regex=True)


# In[111]:


#콤마 없애기
pricedf['갈치가격']=pricedf['갈치가격'].str.replace(',','')
pricedf['배추가격']=pricedf['배추가격'].str.replace(',','')
pricedf['배가격']=pricedf['배가격'].str.replace(',','')
pricedf['돼지고기가격']=pricedf['돼지고기가격'].str.replace(',','')


# In[113]:


#numeric으로 바꾸기 
pricedf=pricedf.apply(pd.to_numeric)


# In[115]:


#소수점 1자리까지만 
pd.set_option('display.float_format', '{:,.1f}'.format)


# In[117]:


#데이터 타입 확인 
pricedf.dtypes


# In[30]:


#profiling report
#pricedf.profile_report()


# In[118]:


#결측치 열별 평균값으로 대체 
pricedf=pricedf.fillna(pricedf.mean())


# In[121]:


#total 가격 칼럼 넣기 - 
pricedf['total']=pricedf["갈치가격"]+pricedf['배추가격']+pricedf["배가격"]+pricedf["돼지고기가격"]
print(pricedf)


# In[126]:


#weather df 정리하기 - 결측치 확인 하기 
pd.DataFrame(weatherdf.isnull().sum(),columns=['결측치 개수'])


# In[127]:


weatherdf.dtypes


# In[129]:


#avgtemp, maxtemp,mintemp,precipitation 숫자화
weatherdf=weatherdf.replace(np.nan, '', regex=True)
#콤마 없애고 & nemeric으로 변환
weatherdf['avgtemp']=pd.to_numeric(weatherdf['avgtemp'].str.replace(',',''))
weatherdf['maxtemp']=pd.to_numeric(weatherdf['maxtemp'].str.replace(',',''))
weatherdf['mintemp']=pd.to_numeric(weatherdf['mintemp'].str.replace(',',''))
weatherdf['precipitation']=pd.to_numeric(weatherdf['precipitation'].str.replace(',',''))
#소수점 1자리까지만 
pd.set_option('display.float_format', '{:,.1f}'.format)


# In[130]:


weatherdf.dtypes


# In[131]:


#weather 와 통합 하기 전 weather 처리 , 날짜별로 오름차순 정렬, index reset
weatherdf.rename(columns={'date':'Date'},inplace=True)
weatherdf['Date']=pd.to_datetime(weatherdf['Date'])
Data=pricedf.merge(weatherdf,how="left",on="Date")
Data=Data.sort_values(['Date'],ascending=True)
Data=Data.reset_index(drop=True)


# In[132]:


Data2=Data.drop(["갈치가격","배추가격","배가격","돼지고기가격","locationId","locationName"],axis=1)


# In[138]:


#결측값 평균으로 대체
Data2['precipitation']=Data2['precipitation'].fillna(Data2.mean())


# In[139]:


print(Data2)


# In[ ]:




