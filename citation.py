from pprint import pprint
import json

class Citation:
    """A class to represent a citation in a repository"""
    def __init__(self, jsonCitation, recordType, showMissingKeys=False):
        #print jsonCitation
        if recordType == 'oai_dc':
            self.datestamp = jsonCitation['header'][0]['datestamp'][0]
            self.identifier = jsonCitation['header'][0]['identifier'][0]
            self.setSpec = jsonCitation['header'][0]['setSpec'][0]
            self.dcSource = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:source']
            try:
                self.dcCreator = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:creator']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no dc:creator"
            try:
                self.dcType = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:type'][0]
            except KeyError:    
                if(showMissingKeys):
                    print self.identifier + " has no dc:type"
            try:
                self.dcTitle = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:title'][0]
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:title"
            try:
                self.dcFormat = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:format'][0]
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:format"
            try:
                self.dcDate = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:date'][0]
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:date"
            try:
                self.dcIdentifier = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:identifier']
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:identifier"
            try:
                self.dcPublisher = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:publisher'][0]
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:publisher"
            try:
                self.dcDescription = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:description'][0]
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:description"
            try:
                self.dcSubject = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:subject']
            except:
                if(showMissingKeys):
                    print self.identifier + " has no dc:subject"
        elif recordType == 'oai_etdms':
            self.datestamp = jsonCitation['header'][0]['datestamp'][0]
            self.identifier = jsonCitation['header'][0]['identifier'][0]
            self.setSpec = jsonCitation['header'][0]['setSpec'][0]
            try:
                self.creator = jsonCitation['metadata'][0]['thesis'][0]['creator']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no creator"
            try:
                self.description = jsonCitation['metadata'][0]['thesis'][0]['description']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no description value"
            try:
                self.abstract = jsonCitation['metadata'][0]['thesis'][0]['description.abstract'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no abstract"
            try:
                self.thesisIdentifier = jsonCitation['metadata'][0]['thesis'][0]['identifier']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no thesisIdentifier"
            try:
                self.subject = jsonCitation['metadata'][0]['thesis'][0]['subject']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no subjects"
            try:
                self.title = jsonCitation['metadata'][0]['thesis'][0]['title'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no title"
            try:
                self.type = jsonCitation['metadata'][0]['thesis'][0]['type'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no type"
            try:
                self.dateCreated = jsonCitation['metadata'][0]['thesis'][0]['date.created'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no date.created"
        elif recordType == 'simple-dublin-core':
            self.datestamp = jsonCitation['header'][0]['datestamp'][0]
            self.identifier = jsonCitation['header'][0]['identifier'][0]
            self.setSpec = jsonCitation['header'][0]['setSpec'][0]
            try:
                self.dcSource = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:source']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no source"
            try:
                self.dcCreator = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:creator']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no creator"
            try:
                self.dcType = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:type'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no type"
            try:
                self.dcTitle = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:title'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no title"
            try:
                self.dcIdentifier = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:identifier']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no dc:identifier"
            try:
                self.dcDescription = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:description'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no description value"
            try:
                self.dcSubject = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:subject']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no subjects"
            try:
                self.dcDate = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:date'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no date"
        elif recordType == 'qualified-dublin-core':
            self.datestamp = jsonCitation['header'][0]['datestamp'][0]
            self.identifier = jsonCitation['header'][0]['identifier'][0]
            self.setSpec = jsonCitation['header'][0]['setSpec'][0]
            try:
                self.dcCreator = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:creator']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no creator"
            try:
                self.dcDate = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:date.created'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no date"
            try:
                self.dcDescription = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:description'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no description"
            try:
                self.dcAbstract = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:description.abstract'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no abstract"
            try:
                self.dcIdentifier = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:identifier']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no thesisIdentifier"
            try:
                self.dcSource = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:source']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no source"
            try:
                self.dcSubject = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:subject']
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no subjects"
            try:
                self.dcTitle = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:title'][0]
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no title"
            try:
                self.dcType = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:type'][0]       
            except KeyError:
                if(showMissingKeys):
                    print self.identifier + " has no type"

        #pprint(vars(self))
    def __str__(self):
        return json.dumps(self.__dict__)
