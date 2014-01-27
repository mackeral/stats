from pymongo import MongoClient
client = MongoClient('mongodb://lawlibrary:unclezeb@ds063287.mongolab.com:63287/repos')
db = client.repos
cursor = db.citations.find({}, {"dcIdentifier": 1, "setSpec": 1})
citations = {}
for citation in cursor:
    citations[citation['dcIdentifier'][0]] = citation['setSpec']
    
for dcID, setSpec in citations.items():
    #print("change {} to {}").format(dcID, setSpec)
    db.statistics.update({'dcIdentifier': dcID}, {'$set': { 'setSpec': setSpec }}, multi=True)