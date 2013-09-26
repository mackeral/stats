import operator
from pymongo import MongoClient

client = MongoClient()
db = client.repos

ucbAuthors = []

for author in db.authors.find({ 'institution': 'Berkeley Law' }):
    ucbAuthors.append(author['lname'] + ', ' + author['fname'][0])

nonUCBAuthors = {}
for citation in db.citations.find():
    if 'dcCreator' in citation:
        for dcCreator in citation['dcCreator']:
            if dcCreator.find(',') != -1:
                fInit = dcCreator.index(',') + 3
            else:
                fInit = None
            dcCreatorTrunc = dcCreator[0:fInit]
            if not dcCreatorTrunc in ucbAuthors:
                if dcCreator in nonUCBAuthors.keys():
                    nonUCBAuthors[dcCreator] += 1
                else:
                    nonUCBAuthors[dcCreator] = 1
    else:
        print "identifier " + citation['identifier'] + " lacks dcCreator"

nonUCBAuthorsSorted = sorted(nonUCBAuthors.iteritems(), key=operator.itemgetter(1))
print nonUCBAuthorsSorted[-30:]
for (nam,num) in nonUCBAuthorsSorted[-30:]:
    print '{}: {}'.format(nam,num)


client.disconnect()
