#!/usr/bin/python3


from collections import namedtuple
import re

class eBook(object):

    def __init__(self,ebookrecord):
            self.ebrecord = ebookrecord

class eBooks(object):

    searchresults = []
    def __init__(self):
        self.ebookDict = {}

    def addEBook(self,key,value):
        if key in self.ebookDict:
            raise KeyError("Error:  Key exists in database")

        self.ebookDict[key] = value

    def resetSearchResults(self):
        eBooks.searchresults = []

    def QueryByStatus(self):
    
        self.resetSearchResults()
        for key in ebookDict.keys():
            if 'active' in ebookDict[key[12]]:
                eBooks.searchresults.append(ebookDict[key])

                

    def QueryByDate(self,querydate):

        self.resetSearchResults()
        querydate = datetime.strptime(querytime,'%d-%b-%Y').date()
        for key in ebookDict.keys():
            if 'active' in ebookDict[key][12].lower() and querydate > datetime.strptime(record[11],'%d-%b-%Y').date():
                searchResults.append(ebookDict[key])

        return searchResults

    def QueryBySubject(self,subjecttoquery):
       self.resetSearchResults()
       for key in ebookDict.keys():
           if re.search('eBook - ([a-zA-Z]+).*',ebookDict[key][1]):
               searchResults.append(ebookDict[key])

            

ebd = eBooks()

with open('data/ebook2016.csv') as ebookdata:

    ebookdata.readline()

    for eb in ebookdata:
        record = eb.strip().split(',')
        try:
            ebd.addEBook(record[4],eBook(record))
        except KeyError:
            continue

