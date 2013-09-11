stats
=====

harvest.js
----------
`node harvest (oai_dc|simple-dublin-core|qualified-dublin-core|oai_etdms)`

creates a timestamped JSON file of citation objects

db.js
-----
`node db file [flush=true|false]`

inserts the objects in file into the database

flush=true will delete from the table before running the insert