var allowedFormats = ['oai_dc','simple-dublin-core','qualified-dublin-core','oai_etdms'];
var baseURL = 'http://scholarship.law.berkeley.edu/do/oai/?verb=ListRecords&';
var http = require('http');
var fs = require('fs');
var mongo = require('mongodb').MongoClient;

var parseString = require('xml2js').parseString;
today = new Date();
var curr_date = ("0" + today.getDate()).slice(-2);
var curr_month = ("0" + (today.getMonth() + 1)).slice(-2);
var curr_year = today.getFullYear();
var records = {};
var maxRecords = 10000;
var finishedFormats = 0;

/*
http://www.openarchives.org/OAI/openarchivesprotocol.html#SelectiveHarvestingandDatestamps
datestamp of most recent: 
	db.citations.find({}, {datestamp: 1, _id: 0}).sort({"datestamp": -1}).limit(1)
	{ "datestamp" : "2013-11-23T23:22:13Z" }
then use this to bring up to date:
http://scholarship.law.berkeley.edu/do/oai/?verb=ListRecords&metadataPrefix=oai_dc&from=2013-11-23T23:22:13Z
upsert to handle edits
but what about deletes?
*/

if(process.argv[2] == '-seed'){
	startHarvest('');
} else if(process.argv[2] == '-update') {
	mongo.connect("mongodb://localhost:27017/repos", function(err, db){
		if(!err){
			citations = db.collection('citations');
			citations.find({}, {datestamp: 1, _id: 0}).sort({"datestamp": -1}).limit(1).toArray(function(err, items){	
				startHarvest('&from=' + items[0].datestamp);
			});
		}
	});
} else console.log('usage: node harvest.js -[seed|update]');

function startHarvest(fromParam){
	allowedFormats.forEach(function(format) {
		harvestURL = baseURL + 'metadataPrefix=' + format + fromParam;
		records[format] = [];
			http.get(harvestURL, function(res){
			var record;
			res.on('data', function(chunk){ record = record + chunk; });
			res.on('end', function(){
				var trimmedRecord = record.substring(record.indexOf('<'));
				parseString(trimmedRecord, { trim: true }, function(err, result){
					if(err) console.log(err + ":" + result);
					else {
						var recordSet = result['OAI-PMH']['ListRecords'][0]['record'];
						recordSet.forEach(function(recordItem){ records[format].push(recordItem); });
						var resumptionToken;
						if(typeof(result['OAI-PMH']['ListRecords'][0]['resumptionToken']) == 'undefined')
							finish(format);
						else {
							resumptionToken = result['OAI-PMH']['ListRecords'][0]['resumptionToken'][0]['_'];
							if(resumptionToken) getMoreRecords(format, resumptionToken);
							else finish(format);
						}
					}
				})
			});
		});
	});
}

function getMoreRecords(format, token){
    http.get(baseURL + 'resumptionToken=' + token, function(res){
        var record;
        res.on('data', function(chunk){ record = record + chunk; });
        res.on('end', function(){
            var trimmedRecord = record.substring(record.indexOf('<'));
            parseString(trimmedRecord, { trim: true }, function(err, result){
                if(err) console.log(err + ":" + result);
                else {
					var recordSet = result['OAI-PMH']['ListRecords'][0]['record'];
					recordSet.forEach(function(recordItem){ records[format].push(recordItem); });
					var resumptionToken;
					if(typeof(result['OAI-PMH']['ListRecords'][0]['resumptionToken']) == 'undefined')
						finish(format);
					else {
						resumptionToken = result['OAI-PMH']['ListRecords'][0]['resumptionToken'][0]['_'];
						if(resumptionToken) getMoreRecords(format, resumptionToken);
						else finish(format);
					}
                }
            })
        });
    });
}

function finish(format){ 
	var fileName = 'records' + curr_year + curr_month + curr_date + format + '.json';
	fs.writeFile(fileName, JSON.stringify(records[format]), function(err){
		if(err) console.log('problem writing file:' + err);
		else console.log(fileName + ' written: ' + records[format].length + ' records');
		finishedFormats++;
		if(finishedFormats >= allowedFormats.length) process.exit(0);
	});
}
