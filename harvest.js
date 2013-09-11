var allowedFormats = ['oai_dc','simple-dublin-core','qualified-dublin-core','oai_etdms'];
var baseURL = 'http://scholarship.law.berkeley.edu/do/oai/?verb=ListRecords&';
var maxRecords =10000;
var recordType;

if(allowedFormats.indexOf(process.argv[2]) >= 0){
    var http = require('http');
    var parseString = require('xml2js').parseString;
    var records = [];
    recordType = process.argv[2]
    http.get(baseURL + 'metadataPrefix=' + recordType, function(res){
        var record;
        res.on('data', function(chunk){ record = record + chunk; });
        res.on('end', function(){
            var trimmedRecord = record.substring(record.indexOf('<'));
            parseString(trimmedRecord, { trim: true }, function(err, result){
                if(err) console.log(err + ":" + result);
                else {
                    var recordSet = result['OAI-PMH']['ListRecords'][0]['record'];
                    var resumptionToken = result['OAI-PMH']['ListRecords'][0]['resumptionToken'][0]['_'];
                    recordSet.forEach(function(recordItem){ records.push(JSON.stringify(recordItem)); });
                    if(resumptionToken){ getMoreRecords(resumptionToken); }
                    else finish();
                }
            })
        });
    });
} else { console.log('usage: node harvest (' + allowedFormats.join('|') + ')') }

function getMoreRecords(token){
    console.log(records.length + ' records. getting more with ' + token );
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
                    recordSet.forEach(function(recordItem){ records.push(JSON.stringify(recordItem)); });
                    if(resumptionToken && (records.length < maxRecords)){ getMoreRecords(resumptionToken); } 
                    else finish();
                }
            })
        });
    });
}

function finish(){ 
    console.log('done. total of ' + records.length + ' records.');
    fs = require('fs');
    today = new Date();
    var curr_date = ("0" + today.getDate()).slice(-2);
    var curr_month = ("0" + (today.getMonth() + 1)).slice(-2);
    var curr_year = today.getFullYear();
    fs.writeFile('records' + curr_year + curr_month + curr_date + recordType + '.json', JSON.stringify(records), function(err){
        if(err) console.log('problem writing file:' + err);
        else console.log('file written');
    });
}