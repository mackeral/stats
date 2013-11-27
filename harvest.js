var allowedFormats = ['oai_dc','simple-dublin-core','qualified-dublin-core','oai_etdms'];
var baseURL = 'http://scholarship.law.berkeley.edu/do/oai/?verb=ListRecords&';
var http = require('http');
var fs = require('fs');
var parseString = require('xml2js').parseString;
today = new Date();
var curr_date = ("0" + today.getDate()).slice(-2);
var curr_month = ("0" + (today.getMonth() + 1)).slice(-2);
var curr_year = today.getFullYear();
var records = {};
var maxRecords = 10000;

allowedFormats.forEach(function(format) {
	harvestURL = baseURL + 'metadataPrefix=' + format;
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
                    var resumptionToken = result['OAI-PMH']['ListRecords'][0]['resumptionToken'][0]['_'];
                    recordSet.forEach(function(recordItem){ records[format].push(recordItem); });
                    if(resumptionToken){ getMoreRecords(format, resumptionToken); }
                    else finish();
                }
            })
        });
    });
});

function getMoreRecords(format, token){
    console.log(records[format].length + ': ' + token );
    http.get(baseURL + 'resumptionToken=' + token, function(res){
        var record;
        res.on('data', function(chunk){ record = record + chunk; });
        res.on('end', function(){
            var trimmedRecord = record.substring(record.indexOf('<'));
            parseString(trimmedRecord, { trim: true }, function(err, result){
                if(err) console.log(err + ":" + result);
                else {
                    var recordSet = result['OAI-PMH']['ListRecords'][0]['record'];
                    var resumptionToken = result['OAI-PMH']['ListRecords'][0]['resumptionToken'][0]['_'];
                    recordSet.forEach(function(recordItem){ records[format].push(recordItem); });
                    if(resumptionToken && (records[format].length < maxRecords)){ getMoreRecords(format, resumptionToken); } 
                    else finish(format);
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
    });
}