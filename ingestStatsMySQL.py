import csv, re, sys
from citation import Citation
from pymongo import MongoClient
import MySQLdb as mdb
import math, datetime
from Bucket import Bucket
from pprint import pprint


if len(sys.argv) < 2:
    sys.exit('usage: ./ingestStatsMySQL.py dataWithHeader OR ./ingestStatsMySQL.py -h=dataWithHeader data')
else:
	
	"""
    client = MongoClient()
    mongoDB = client.repos
    db = mdb.connect('localhost', 'statsW', 'zeb', 'repo')
    dataFile = sys.argv[1]
    cur = db.cursor()

    if len(sys.argv) == 2:  # called ingestStatsMySQL.py dataWithHeader
        headerFile = sys.argv[1]
        dataFile = sys.argv[1]
        popDataRows = True
    else:                   # called ingestStatsMySQL.py -h=dataWithHeader data
        headerFlag,headerFile = sys.argv[1].split('=')
        dataFile = sys.argv[2]
        popDataRows = False
        
    headerGrid = list(csv.reader(open(headerFile, 'r'), delimiter='\t'))
    headerGrid.pop(0)
    cols = headerGrid.pop(0)
    
    grid = list(csv.reader(open(dataFile, 'r'), delimiter='\t'))
    if popDataRows:
        grid = grid[2:]

    totalStats = 0

    with db:
        for i, row in enumerate(grid):
    
            identifier = row[1]
            ingestDate = row[2]
    
            # ignore selected works citations
            if re.match('http://works.bepress.com', identifier):
                continue
        
            chunks = ingestDate.split('/')
            ingestDateD = datetime.datetime(int(chunks[2]), int(chunks[0]), int(chunks[1]))
            result = mongoDB.citations.update({ "dcIdentifier": identifier }, {"$set": { 'ingestDate': ingestDateD }}, True)
            
            j = 3
            for col in row[3:]:
                m,d,y = cols[j].split('/');
                if int(col) > 0:
                    cur.execute("INSERT INTO stats(dcID,dlDate,dlN,file,repo) VALUES(%s,%s,%s,%s,'Berkeley Law Scholarship Repository')",(identifier, datetime.date(int(y), int(m), 1), col, dataFile))
                    totalStats += 1
                else:
                    pass #print 'zero, not statting {} for {}'.format(identifier, cols[j])
                j += 1

    print "ingested " + str(totalStats) + " entries"
"""	
	#refresh summary files: avgDownloads.txt, structuresData.txt, structuresDownloads.txt
	#find which stats records have no setSpec attribute
	#select all of the above from citations
	#populate them in stats
	sys.exit("done")


