#!/usr/bin/env python


import httplib


y = httplib.HTTPConnection('rate-exchange.appspot.com')
y.connect()
y.request('GET','http://rate-exchange.appspot.com/currency?from=USD&to=EUR&q=1')
response = y.getresponse()
print response.read()
y.request('GET','http://rate-exchange.appspot.com/currency?from=GBP&to=EUR&q=1')
response = y.getresponse()
print response.read()


