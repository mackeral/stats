# fill db
import sys, json, re
from citation import Citation
from pymongo import MongoClient

if len(sys.argv) < 2:
    sys.exit('usage: python fillDB.py fileToIngest.json')
else:
    jsonFile = sys.argv[1]
    m = re.search('\d([a-z\-_]+)\.', jsonFile);
    if not m:
        sys.exit('fileName in wrong format')
    docType = m.group(1)
    
    client = MongoClient();
    db = client.repos
    
    jsonContent = open(jsonFile)
    jsonCitations = json.load(jsonContent)
    
    for jsonCitation in jsonCitations:
        if docType in ('oai_dc', 'simple-dublin-core', 'qualified-dublin-core'):
            del jsonCitation["metadata"][0]["oai_dc:dc"][0]["$"]
        elif docType in ('oai_etdms'):
            del jsonCitation["metadata"][0]["thesis"][0]["$"]
        db.citations.insert(jsonCitation)
        citation = Citation(jsonCitation)
    
    jsonContent.close()
    client.disconnect()    
    sys.exit("done. ingested " + str(len(jsonCitations)) + " entries")