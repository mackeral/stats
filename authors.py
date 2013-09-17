import re
from pymongo import MongoClient

client = MongoClient()
db = client.repos

lines = open('./authorsUCB.txt')
authors = []
for line in lines:
    chunks = line.strip().split()
    db.authors.save({ 'lname': chunks[1], 'fname': chunks[0], 'institution': 'Berkeley Law' })
    #authors.append(chunks[1] + ', ' + chunks[0][0])
#print authors


#authorRE = re.compile("^" + authors[2])
#for citation in db.citations.find({ "dcCreator" : authorRE }):
#    print citation 