#!/usr/bin/env python


import sys
import json

teamdict = {}
recordlist = []

def usage():
    sys.stderr.write("Usage:  baseball.py <year>\n")
    return

if len(sys.argv) < 2:
    usage()
    sys.exit(0)


filename = "ALbb.salaries." + sys.argv[1] + ".formattted.csv"

try:
    f = open (filename)
except IOError:
    sys.stderr.write("Invalid file!")
    sys.exit(0)


# Read each line.  For each team, add up the players salary. The dictionary
# key is going to be the team name. The value is going to be the sum of the 
# salaries for each team. 

try:
    for line in f:
        recordlist = line.strip().split(",");
        if len(recordlist) < 5:
            break
        if (not teamdict.has_key(recordlist[0])):
            try:
                teamdict[recordlist[0].lower()] = int(recordlist[3])
            except ValueError:
                continue
        else:
            try:
                teamdict[recordlist[0].lower()] += int(recordlist[3])
            except ValueError:
                continue

except IOError as ex:
    sys.stderr.write("Read Error!" + str(ex))
    sys.exit(1)
finally:
    f.close()
        

# Once the dictionary is built, allow the user to search on the dictionary
# to find the desired team's total salary. 

while (True):
    teamname =  raw_input("Team Name (type 'x' to quit): ")
    if teamname.lower() == "x":
        break
    if (not teamdict.has_key(teamname.lower())):
        print "Error!  No such team ",teamname
    else:
        print "Team: ",teamname.title(),"Total salary: ",teamdict[teamname.lower()]

# dump the dictionary to a file in json format

of = open("baseballoutput.json","w")
json.dump(teamdict,of)
of.close()
sys.exit(0)
