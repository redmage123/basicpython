#!/usr/bin/python3

import re

urlschecked = 0
urlsvalid = 0

#"^(https?://)?([0-9a-zA-Z]+\.)+(co\.uk|ac\.uk|com|org|net)$"
def checkvalidURL(x):
    global urlschecked
    global urlsvalid
    urlschecked = urlschecked + 1
                    
   reObj = re.search("^(https?://)?([0-9a-zA-Z]+\.)+(co\.uk|ac\.uk|com|org|net)$",x)
                       #print(x + " - " + reObj)
   if reObj:
       urlsvalid = urlsvalid +1
       return True
   else:
       return False
                                                                
file = open ("urls.txt","r")

for i in range(0):
    try:
        file.readline()
    except IOError:
        print("IO Error")
        file.close()
        sys.exit()

validIPs = list(url for url in file if (checkvalidURL(url.strip())))
file.close()

print(validIPs)
