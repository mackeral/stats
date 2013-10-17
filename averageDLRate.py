import math, datetime
from Bucket import Bucket
from pymongo import MongoClient
from pprint import pprint


client = MongoClient('mongodb://lawlibrary:unclezeb@ds063287.mongolab.com:63287/repos')
db = client.repos

# populate article:ingestDate dictionary
ingestDates = {}
citations = db.citations.find()
for citation in citations:
    ingestDates[citation['dcIdentifier'][0]] = citation['ingestDate']
# initialize empty age:Bucket dictionary
ageBuckets = {}

# get cursor for all statistics
# for each statistic:
#   if(statistic:dcIdentifier is in our article:ingestDate dictionary):
#       determine the correct bucket depending on article:ingestDate and statistic:dlDate
#       addDownloads to that bucket for this statistic (make a bucket if necessary)

statistics = db.statistics.find().limit(1000)
for statistic in statistics:
    if(statistic['dcIdentifier'] in ingestDates):
        ingestDateChunks = ingestDates[statistic['dcIdentifier']].split('/')
        ingestDate = datetime.date(int(ingestDateChunks[2]), int(ingestDateChunks[0]), int(ingestDateChunks[1]))
        dlDate = statistic['dlDate'].date()
        age = int(math.ceil(float((dlDate - ingestDate).days) / (356/12)))
        #print "ingested {}, dlDate {}, age of {} mo".format(ingestDate, dlDate, age)
        if(ageBuckets.get(age) == None):
            ageBuckets[age] = Bucket(age)
        ageBuckets[age].addDownloads(statistic['downloads'])


# now we have full buckets
for bucket in ageBuckets.keys():
    print bO

client.disconnect()