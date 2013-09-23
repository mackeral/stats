import csv, re
from citation import Citation
from pymongo import MongoClient

client = MongoClient()
db = client.repos

maxI = 50

grid = list(csv.reader(open('monthlies.txt', 'r'), delimiter='\t'))
grid.pop(0);
cols = grid.pop(0)
for i, row in enumerate(grid):

    identifier = row[1]
    ingestDate = row[2]

    # ignore selected works citations
    if re.match('oai:works.bepress.com:', identifier):
        continue
    
    print 'update db: id {} ingested on {}'.format(identifier, ingestDate)
    result = db.citations.update({ "dcIdentifier" : identifier}, {"$set": { 'ingestDate': ingestDate }}, True)
    print result

    j = 3

    for col in row[3:]:
        print 'stat: {1} downloads on {0}'.format(cols[j], col)
        j += 1
    if i > maxI:
        break

    