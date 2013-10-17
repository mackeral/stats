class Bucket:
    def __init__(self, age):
        self.age = age
        self.downloads = 0
        self.articles = 0
    def addDownloads(self, downloads):
        self.downloads = self.downloads + downloads
        self.articles = self.articles + 1
    def __str__(self):
        return "{} months: {} articles for a total of {} downloads, or {} downloads per article".format(self.age, self.articles, self.downloads, float(self.downloads)/self.articles)