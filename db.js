if(process.argv[2]) {
    jsonFile = process.argv[2];
    objects = require('./' + jsonFile);
    objects.forEach(function(objectString){
        object = JSON.parse(objectString);
        console.log(object.header[0].identifier[0]);
    });
} else { console.log('usage: node db fileToParse'); }
