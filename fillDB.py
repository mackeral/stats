# fill db
import sys, json, re

if len(sys.argv) < 2:
    sys.exit('usage: python fillDB.py fileToIngest.json')
else:
    jsonFile = sys.argv[1]
    m = re.search('\d([a-z\-_]+)\.', jsonFile);
    if not m:
        sys.exit('fileName in wrong format')
    docType = m.group(1)
    
    from pymongo import MongoClient
    client = MongoClient();
    db = client.repos
    
    jsonCitations = open(jsonFile)
    citations = json.load(jsonCitations)
    
    for citation in citations:
        if docType in ('oai_dc', 'simple-dublin-core', 'qualified-dublin-core'):
            del citation["metadata"][0]["oai_dc:dc"][0]["$"]
        elif docType in ('oai_etdms'):
            del citation["metadata"][0]["thesis"][0]["$"]
        db.citations.insert(citation)
    
    jsonCitations.close()
    client.disconnect()    
    #sys.exit("done. ingested " + str(len(citations)) + " entries")