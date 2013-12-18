201312

model
=====
+ whole process runs on aws instance
+ citations are stored in document database
+ statistics and authors are stored in relational database

processes
=========
+ node harvest.js -[seed|update]
++ creates datestamped json files of citation objects
+ fillDB filestem
++ inserts citations from json files into document db
+ ingestStatsMySQL.py [dataWithHeader|-h=dataWithHeader data]

workflow
========
+ use harvest.js to grab xml from bepress of all citations, in all four formats
+ use fillDB.py to insert them into the database. citations are keyed on header:identifier and are "upserted" (inserted if new, updated if existing)
+ use authors.py to associate authors with institutions
+ get statistics locally
+ use ingestStats.py to get statistics into mongo
 
misc
====

keys.py
-------
`python keys.py file`

enumerates the metadata keys for the given docType
