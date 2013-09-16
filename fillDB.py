import ast, sys, json, re
from citation import Citation
from pymongo import MongoClient
from pprint import pprint

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
    jsonContent.close()
    
    citations = []
    
    for jsonCitation in jsonCitations:
        if docType in ('oai_dc', 'simple-dublin-core', 'qualified-dublin-core'):
            del jsonCitation["metadata"][0]["oai_dc:dc"][0]["$"]
        elif docType in ('oai_etdms'):
            del jsonCitation["metadata"][0]["thesis"][0]["$"]
        citations.append(Citation(jsonCitation, docType))
    
    client.disconnect()    
    for citation in citations:
        #print citation.__dict__
        result = db.citations.update({ "identifier" : citation.identifier}, {"$set": citation.__dict__}, True)
        #mongoID = db.citations.insert(citation.__dict__, { 'upsert': True })
        print result
    
    sys.exit("done. ingested " + str(len(jsonCitations)) + " entries")