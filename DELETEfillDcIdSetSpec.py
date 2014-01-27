from pymongo import MongoClient
import MySQLdb as mdb
import sys

client = MongoClient()
mongoDB = client.repos
db = mdb.connect('localhost', 'statsW', 'zeb', 'repo')
cur = db.cursor()

with db:
	for citation in mongoDB.citations.find({}, {"dcIdentifier": 1, "setSpec": 1}):
		#print citation['dcIdentifier'][0], citation['setSpec']
		cur.execute("INSERT INTO dcID_setSpec (dcID,setSpec) VALUES(%s,%s)",(citation['dcIdentifier'][0], citation['setSpec']))
	
sys.exit(0)
