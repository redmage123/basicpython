#!/usr/bin/env python

import sys



class Book(object):
    def __init__(self, isbn,author,title,quantity):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.quantity = quantity


    def getISBN(self):
        return self.isbn

    def getAuthor(self):
        return self.author

    def getTitle(self):
        return self.title

    def getQuantity(self):
        return self.quantity

    def __str__(self):
        returnString = "ISBN: " + self.isbn + " Author " + self.author + " Title: " + self.title + " Quantity: " + self.quantity
        return(returnString)

bookdict = {}
try:
    f = open("bookstore.dat")
except IOError:
    sys.stderr.write("ERROR: Unable to open file")
    sys.exit(1)



try:
    header = f.readline()
except IOError:
    sys.stderr.write("ERROR: Unable to read from file")
    f.close()
    sys.exit(1)
    

try: 
    for record in  f:
        (key,author,title,quantity) = record.strip().split(',')
        bookdict[key.split()[1]] =   Book(key,author,title,quantity)
except IOError:
    sys.stderr.write("ERROR: Unable to read from file")
    sys.exit(1)
finally:
    f.close()


isbnsearch = raw_input("Please enter an ISBN: ") 
 
if not bookdict.has_key(isbnsearch):
    print "Invalid isbn number"
else:
    print bookdict[isbnsearch]
