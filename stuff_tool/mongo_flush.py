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
db= client.documentsDemo
#db = client.documentsDemo

coll = db.Order
coll.remove({})

coll2 = db.EstimatedTimeOfArrival
coll2.remove({})

coll1 = db.Route
coll1.remove({})

coll3 = db.DeletedOrder
coll3.remove({})

coll4 = db.MobileUserFootprints
coll4.remove({})

coll5 = db.Bookings
coll5.remove({})

coll6 = db.LastPosition
coll6.remove({})

coll7 = db.TrackAndTrace
coll7.remove({})

#coll4 = db.TrackAndTrace
#coll4.remove({})
#for men in coll.find({'Order.LocationInfo' : None }):
# #     #print(men)
#      print (men['Order']['OrderInfo']['Number'])