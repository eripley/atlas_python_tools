import pymongo
from pymongo import MongoClient
import uuid
import json
from bson.objectid import ObjectId



#uri = "mongodb://docQa:passw0rd@10.10.122.15/documentsQa"
uri = "mongodb://docDemo:passw0rd@10.10.122.15/documentsDemo"
#uri = "mongodb://docDemo:passw0rd@10.10.122.15/documentsDemo"
client = MongoClient(uri)
#db = client.documentsDev
db= client["documentsDemo"]
#db = client.documentsDemo
cl = db["Order"]
x = cl.delete_Many({})
print(x, "Orders Deleted")


#coll4 = db.TrackAndTrace
#coll4.deleteMany({})
#for men in coll.find({'Order.LocationInfo' : None }):
# #     #print(men)
#      print (men['Order']['OrderInfo']['Number'])