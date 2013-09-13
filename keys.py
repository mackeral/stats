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


"""
keys for dataType qualified-dublin-core:
[
u'dc:creator', 
u'dc:date.created', 
u'dc:description', 
u'dc:description.abstract', 
u'dc:identifier', 
u'dc:source'
u'dc:subject', 
u'dc:title', 
u'dc:type', 
]

keys for dataType simple-dublin-core:
[
u'dc:creator', 
u'dc:date', 
u'dc:description', 
u'dc:identifier', 
u'dc:source'
u'dc:subject', 
u'dc:title', 
u'dc:type', 
]

keys for dataType oai_etdms:
[
u'creator', 
u'date.created', 
u'description', 
u'description.abstract', 
u'identifier', 
u'source'
u'subject', 
u'title', 
u'type', 
]

keys for dataType oai_dc:
[
u'dc:creator', 
u'dc:date', 
u'dc:description'
u'dc:format', 
u'dc:identifier', 
u'dc:publisher', 
u'dc:source', 
u'dc:subject', 
u'dc:title', 
u'dc:type', 
]
"""