var allowedFormats = ['oai_dc','simple_dublin_core','qualified_dublin_core','oai_etdms'];
if(allowedFormats.indexOf(process.argv[2]) >= 0){
    var http = require('http');
    var parseString = require('xml2js').parseString;
    var records = [];
    http.get('http://scholarship.law.berkeley.edu/do/oai/?verb=ListRecords&metadataPrefix=' + process.argv[2], function(res){
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
                    console.log(resumptionToken);
                    console.log(records.length);
                }
            })
        });
    });
} else {
    console.log('usage: node harvest (' + allowedFormats.join('|') + ')')
}

function addRecords(){
    
}