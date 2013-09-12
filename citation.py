from pprint import pprint
class Citation:
    """A class to represent a citation in a repository"""
    def __init__(self, jsonCitation):
        print jsonCitation
        self.datestamp = jsonCitation['header'][0]['datestamp'][0]
        self.identifier = jsonCitation['header'][0]['identifier'][0]
        self.setSpec = jsonCitation['header'][0]['setSpec'][0]
        self.dcSource = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:source'][0]
        try:
            self.dcCreator = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:creator'][0]
        except KeyError:
            print self.identifier + " has no dc:creator"
        try:
            self.dcType = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:type'][0]
        except KeyError:
            print self.identifier + " has no dc:type"
        try:
            self.dcTitle = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:title'][0]
        except:
            print self.identifier + " has no dc:title"
        try:
            self.dcFormat = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:format'][0]
        except:
            print self.identifier + " has no dc:format"
        try:
            self.dcDate = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:date'][0]
        except:
            print self.identifier + " has no dc:date"
        try:
            self.dcIdentifier = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:identifier']
        except:
            print self.identifier + " has no dc:identifier"
        try:
            self.dcPublisher = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:publisher'][0]
        except:
            print self.identifier + " has no dc:publisher"
        try:
            self.dcDescription = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:description'][0]
        except:
            print self.identifier + " has no dc:description"
        try:
            self.dcSubject = jsonCitation['metadata'][0]['oai_dc:dc'][0]['dc:subject']
        except:
            print self.identifier + " has no dc:subject"
        pprint(vars(self))
