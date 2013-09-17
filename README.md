stats
=====

harvest.js
----------
`node harvest (oai_dc|simple-dublin-core|qualified-dublin-core|oai_etdms)`

creates a timestamped JSON file of citation objects

fillDB.py
-----
`python fillDB.py file`

inserts the objects in file into the database

keys.py
-------
`python keys.py file`

enumerates the metadata keys for the given docType


workflow
--------
+ use harvest.js to grab xml from bepress of all citations, in all four formats
+ use fillDB.py to insert them into the database. citations are keyed on header:identifier and are "upserted" (inserted if new, updated if existing)
+ use authors.py to associate authors with institutions
 

