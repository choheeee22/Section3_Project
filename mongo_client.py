#install pymongo,dns python
from pymongo import MongoClient
username='chohee'
password='chohee22'
URI=f'mongodb+srv://chohee:{password}@cluster0.ghxbe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client=MongoClient({URI})
#print(client) 로 연결여부 확인 완료 

#database 와 연결 
DATABASE='myFirstDatabase'
database=client[DATABASE]
print(database)

#table (= collection) 생성 및 확인 

COLLECTION='weather-collection'
collection=database[COLLECTION]

#print(collection)로 생성 확인 완료 

#collection.insert_one(document={"hello":"weather"})
#connection security 관련 - allow access from anywhere 체크 

from DataBase import asos

database.collection.insert_many(asos)