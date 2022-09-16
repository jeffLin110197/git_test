import pymongo
from pymongo import MongoClient #引入pymongo
client = MongoClient(host="localhost", port=27017)
# #指定資料庫
db = client.admin
# #指定Collection
collections = db['RT-Mart']
print('collection:', collections)
counts = collections.count_documents({})
print(counts)