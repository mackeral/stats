import math, datetime
#from Bucket import Bucket
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://lawlibrary:unclezeb@ds063287.mongolab.com:63287/repos')
db = client.repos

ingestDates = {}
distinctDates = db.citations.distinct('ingestDate')
for distinctDate in distinctDates:
    chunks = distinctDate.split('/')
    ingestDateD = datetime.datetime(int(chunks[2]), int(chunks[0]), int(chunks[1]))
    #print("{}:{}").format(distinctDate, ingestDateD)
    db.citations.update({ "ingestDate": distinctDate }, { "test1": "helf" })


client.disconnect()
print "done"    
