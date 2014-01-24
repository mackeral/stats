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
+ python fillDB [filestem]
++ inserts citations from json files into document db
+ ingestStatsMySQL.py [dataWithHeader|-h=dataWithHeader data]

workflow
========
+ use harvest.js to grab xml from bepress of all citations, in all four formats
+ use fillDB.py to insert them into the database. citations are keyed on header:identifier and are "upserted" (inserted if new, updated if existing)
+ use authors.py to associate authors with institutions
+ get statistics from bepress; account for any overlap (may need to delete any partial month stats that are in the db already)
+ use ingestStatsMySQL.py to get statistics into MySQL
 
misc
====

keys.py
-------
`python keys.py file`

enumerates the metadata keys for the given docType


fix:
http://ec2-54-193-44-7.us-west-1.compute.amazonaws.com/statsWeb/personalAuthor.php?q=Asian%20American%20Law%20Journal
