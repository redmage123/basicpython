#!/usr/bin/python

import re

mystr = "foo bar baz"

re_obj = re.search("([a-z]+) ([a-z]+) ([a-z]+)",mystr)

print (re_obj.group(1))
print (re_obj.group(2))
print (re_obj.group(3))
