import json

class AbstractCitation:
    def __init__(self, statistic):
        self.dcIdentifier = statistic['dcIdentifier']
        self.downloads = {}
        self.downloads[statistic['dlDate']] = statistic['downloads']
    def addDownload(self, statistic):
        if(statistic['dlDate'] in self.downloads):
            self.downloads[statistic['dlDate']] = self.downloads[statistic['dlDate']] + statistic['downloads']
        else:
            self.downloads[statistic['dlDate']] = statistic['downloads']
        print self.downloads
    def __str__(self):
        return json.dumps(self.__dict__)
