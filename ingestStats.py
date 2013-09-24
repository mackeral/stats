import csv, re
from citation import Citation
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.repos

maxI = 7000

grid = list(csv.reader(open('monthlies.txt', 'r'), delimiter='\t'))
grid.pop(0);
cols = grid.pop(0)
for i, row in enumerate(grid):

    identifier = row[1]
    ingestDate = row[2]

    # ignore selected works citations
    if re.match('http://works.bepress.com', identifier):
        continue
    
    #print 'update db: id {} ingested on {}'.format(identifier, ingestDate)
    #result = db.citations.update({ "dcIdentifier": identifier }, {"$set": { 'ingestDate': ingestDate }}, True)
    #print result

    j = 3

    for col in row[3:]:
        m,d,y = cols[j].split('/');
        #print 'stat: {0} downloads on {1} {2} {3}'.format(col, m, d, y)
        db.statistics.insert({'identifier': identifier, 'downloads': col, 'dlDate': datetime.datetime(int(y), int(m), int(d))})
        j += 1
    if i > maxI:
        break

    