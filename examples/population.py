#!/usr/bin/env python



f = open("./Eur.pop.XL.zip.csv")
data_list = []
output_dict = {}

for i in range(0,3):
    f.readline()

for country in f:
    data_list = country.strip().split(",")
    if (data_list[0] == ""):
        continue
    if (data_list[0] == "Sources:" or data_list[0] == "Total Europe"):
        break
    diff = int(data_list[7].replace("\'","")) - int(data_list[1].replace("\'",""))
    output_dict[data_list[0]] = diff


while (True):
    country_input = raw_input("please print the country you want to view: ")
    if not output_dict.has_key(country_input):
        print "Error:  No such key: ",country_input
    else:
        print "Country: ",country_input,"Population differential: ",output_dict[country_input]
        break




    


