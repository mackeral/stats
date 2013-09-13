import json, re, sys
from citation import Citation

if len(sys.argv) < 2:
    sys.exit('usage: python fillDB.py fileToIngest.json')
else:
    jsonFile = sys.argv[1]
    m = re.search('\d([a-z\-_]+)\.', jsonFile);
    if not m:
        sys.exit('fileName in wrong format')
    docType = m.group(1)

    jsonContent = open(jsonFile)
    jsonCitations = json.load(jsonContent)
    jsonContent.close()
    
    
    keys = []
    
    for jsonCitation in jsonCitations:
        if docType in ('oai_dc', 'simple-dublin-core', 'qualified-dublin-core'):
            del jsonCitation["metadata"][0]["oai_dc:dc"][0]["$"]
            for k in jsonCitation["metadata"][0]["oai_dc:dc"][0].keys():
                if k not in keys:
                    keys.append(k)
        elif docType in ('oai_etdms'):
            del jsonCitation["metadata"][0]["thesis"][0]["$"]
            for k in jsonCitation["metadata"][0]["thesis"][0].keys():
                if k not in keys:
                    keys.append(k)
    
    print "keys for dataType " + docType + ":"
    print keys
