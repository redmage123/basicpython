#!/usr/bin/python3



statsfile = open("ALbb.salaries.2003.formatted.csv")

records = statsfile.readlines()

keys = set(record[0] for record in records)
statsdict = {key:0 for key in keys}
for key in statsdict.keys():
     statsdict[key] = sum(int(row.strip().split(",")[3]) for row in records)

print (statsdict)

   

