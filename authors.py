from pymongo import MongoClient

client = MongoClient()
db = client.repos

lines = open('./authorsUCB.txt')
authors = []
for line in lines:
    chunks = line.strip().split()
    db.authors.save({ 'lname': chunks[1], 'fname': chunks[0], 'institution': 'Berkeley Law' })
