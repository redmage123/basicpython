#!/usr/bin/python3

import re
import datetime

class eBook(object):

    ''' A wrapper around an ebook record
    '''
    def __init__(self,ebookrecord):
            self.ebrecord = ebookrecord

class eBooks(object):

    ''' The ebooks class contains a dictionary of ebooks

    addEBook(self,key,value) - Adds an Ebook object to the dictionary
    resetSearchResults(self) - Clears the search dictionary
    QueryByStatus(self) - Queries the ebook dictionary.  If the ebook status field 
                          is 'active', then add that ebook to the search results
                          dictionary

    QueryByDate(self,querydate) - Queries the ebooks by the query date and returns
                                  all active ebooks with a date greater than the
                                  query date.

    QueryBySubject(self,subjecttoquery) - Queries the ebooks by the subject. Note
                                          that although we use a regular expression
                                          to do this, an RE is not required. 



    '''

# Thee searchresults list is a static variable.
    searchresults = []

# The init method only creates the empty ebook dictionary.
    def __init__(self):
        self.ebookDict = {}

# add an Ebook to the ebooks dictionary.
    def addEBook(self,key,value):

# If the ebook is already in the dictionary, raise an error.
        if key in self.ebookDict:
            raise KeyError("Error:  Key exists in database")

# Otherwise, add the ebook to the ebooks dictionary
        self.ebookDict[key] = value


# Clear the searchresults list.
    def resetSearchResults(self):
        eBooks.searchresults = []

# Query the ebooks by the status field
    def QueryByStatus(self):
    
        self.resetSearchResults()
        for key in self.ebookDict.keys():
            if 'active' in self.ebookDict[key][12]:
                eBooks.searchresults.append(self.ebookDict[key])

                

# Query the books by the query date.  Return active books published after the query date. 
    def QueryByDate(self,querydate):
        self.resetSearchResults()
        querydate = datetime.datetime.strptime(querydate,'%d-%b-%Y').date()
        for key in self.ebookDict.keys():
            try:
                if 'active' in self.ebookDict[key][12].lower() and querydate > datetime.datetime.strptime(record[11],'%d-%b-%Y').date():
                    eBooks.searchresults.append(self.ebookDict[key])
            except ValueError:
                continue

        return eBooks.searchresults

# Query the books by the subject.  Note that although we use a regular expression here, 
# We could have just as easily used the 'in' operation. 

    def QueryBySubject(self,subjecttoquery):
       self.resetSearchResults()
       for key in self.ebookDict.keys():
           if re.search('eBook - ([a-zA-Z]+).*',ebookDict[key][1]):
               eBooks.searchresults.append(self.ebookDict[key])

            

# We'd really just import the class into our own python code, but here's
# a testing platform if we want to test the methods. 

if __name__ == '__main__':
# Instantiate our ebooks class
    ebd = eBooks()

# Read all the data in the data source and add th e3ebooks to the ebooks object.
    with open('data/ebook2016.csv') as ebookdata:
        ebookdata.readline()
        for eb in ebookdata:
            record = eb.strip().split(',')
            try:
     #           ebd.addEBook(record[4],eBook(record))
                ebd.addEBook(record[4],record)
            except KeyError:
                continue

# More testing code can be done here.

#ebd.QueryByStatus()
#print (ebd.searchresults)
ebd.QueryByDate('01-Jan-2010')
print (ebd.searchresults)
