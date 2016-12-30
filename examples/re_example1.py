#!/usr/bin/python3


import re


ip = "192.168.100.1"

re_obj = re.match ("^([0-9]{1,3}\.){3}[0-9]{1,3}$",ip)

if re_obj:
    print ("Found a match!")
