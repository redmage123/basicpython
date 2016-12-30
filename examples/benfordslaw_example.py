#!/usr/bin/python3 

import re
def getData(fileName):
    data = []
    f = open(fileName,'r')
    for line in f:
        data.append(line)

    f.close()
    return data

def getLeadDigitCounts(data):
    counts = [0,0,0,0,0,0,0,0,0]
    for i in data:
        pop = list(filter(lambda elem: elem.isspace() is False and len(elem)>0,i.strip().split(' ')))
        digits = pop[2]
        digits = int(digits[0])
        counts[digits-1] += 1
    return counts

def showResults(counts):
    percentage=0
    sum=0
    num=0
    total=0
    index=0
    for i in counts:
        total += i

    for i in counts:
        index += 1
        sum += index
        percentage = i/float(sum)
        print("%d %d %f" % (index,i,percentage))


def showLeadingDigits(digit,data):
    print("Showing data with a leading",digit)
    for i in data:
        if digit == i[i][1]:
            print (i)

def processFile(name):
    data = getData(name)
    counts = getLeadDigitCounts(data)
    showResults(counts)
    digit = input('Enter leading digit: ')
    showLeadingDigits(digit, data)

def main():
    processFile('TexasCountyPop2010.txt')
    processFile('MilesofTexasRoad.txt')

main()
