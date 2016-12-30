#!/usr/bin/env python

#### 
# For windows, use this rather than /usr/bin/env python
#!c:\Python27\python.exe -u
####


import urllib2

response = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?format=json&s=AAPL&f=nab')
for line in response:
    print line


