201311

model
=====
harvester runs locally on Mike's machine
+ works with mongolab db
+ initial harvest
++ OAI_PMH grab of entire db, saved as json
++ 
+ selective harvest (additions to, modifications of, deletions from initial harvest)

webserver runs on webdev
+ queries mongolab db


stats
=====

sysprep/install
-------
node
python
pymongo
+ make sure you use the location of the python that has the modules installed. E.g. my local /usr/bin/python doesn't have pymongo but /usr/local/bin/python does



workflow
--------
+ use harvest.js to grab xml from bepress of all citations, in all four formats
+ use fillDB.py to insert them into the database. citations are keyed on header:identifier and are "upserted" (inserted if new, updated if existing)
+ use authors.py to associate authors with institutions
+ get statistics locally
+ use ingestStats.py to get statistics into mongo
 
harvest.js
----------
`node harvest`

creates timestamped JSON files of citation objects

fillDB.py
---------
`python fillDB.py fileNameRoot`

inserts the objects in json files into mongodb

keys.py
-------
`python keys.py file`

enumerates the metadata keys for the given docType

todo
====
+ bring in additional authors/affiliations; make designations for California Bar, etc. as institutions

