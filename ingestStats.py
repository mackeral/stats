import csv, re, sys
from citation import Citation
from pymongo import MongoClient
import datetime


if len(sys.argv) < 2:
    sys.exit('usage: ./ingestStats.py dataWithHeader OR ./ingestStats.py -h=dataWithHeader data')
else:
    client = MongoClient('mongodb://lawlibrary:unclezeb@ds063287.mongolab.com:63287/repos')
    db = client.repos
    
    dataFile = sys.argv[1]
    
    if len(sys.argv) == 2:  # called ingestStats.py dataWithHeader
        headerFile = sys.argv[1]
        dataFile = sys.argv[1]
        popDataRows = True
    else:                   # called ingestStats.py -h=dataWithHeader data
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

    for i, row in enumerate(grid):
    
        identifier = row[1]
        ingestDate = row[2]
    
        # ignore selected works citations
        if re.match('http://works.bepress.com', identifier):
            continue
        
        chunks = ingestDate.split('/')
        ingestDateD = datetime.datetime(int(chunks[2]), int(chunks[0]), int(chunks[1]))
        #print 'update db: id {} ingested on {}'.format(identifier, ingestDate)
        result = db.citations.update({ "dcIdentifier": identifier }, {"$set": { 'ingestDate': ingestDateD }}, True)
        #print result
    
        j = 3
        for col in row[3:]:
            m,d,y = cols[j].split('/');
            if int(col) > 0 and int(m) > 8: # HERE I'M USING ONLY STATS FROM SEPTEMBER FORWARD (AUG=8TH MONTH)
                #print 'id {}; {} dls on {}/{}/{}'.format(identifier, int(col), m, d, y)
                db.statistics.save({'dcIdentifier': identifier, 'downloads': int(col), 'dlDate': datetime.datetime(int(y), int(m), 1), 'repo': 'Berkeley Law Scholarship Repository', 'file': dataFile})
                totalStats += 1
            else:
                pass #print 'zero, not statting {} for {}'.format(identifier, cols[j])
            j += 1

    client.disconnect()
    sys.exit("done. ingested " + str(totalStats) + " entries")
