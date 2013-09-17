import re
from pymongo import MongoClient

lines = open('./authorsUCB.txt')
authors = []
for line in lines:
    chunks = line.strip().split()
    authors.append(chunks[1] + ', ' + chunks[0][0])
print authors

client = MongoClient()
db = client.repos

authorRE = re.compile("^" + authors[2])
citations = db.citations.find({ "dcCreator" : authorRE })
print citations.count()
#print citation 