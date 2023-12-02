import csv


# create a dictionary from a list of keys and list of values
def singleListToDict(keys, values):
    ad = {}
    for key in keys:
        ad[key] = 0
    for i in range(len(keys)):
        ad[keys[i]] = values[i]
    return ad


# take a list of keys and a nested list of values
# and turn them into a list of dictionaries
def convertToDictionaries(keys, values):
    dictList = []
    for i in range(len(values)):
        ad = singleListToDict(keys, values[i])
        dictList.append(ad)
    return dictList


# import lines from a csv into a list
def loadRecords(filename):
    csvLines = []
    with open(filename, 'r') as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            csvLines.append(row)
    return csvLines


# add the values of the passed in keys to a list
def singleDictToList(keys, ad):
    listAssign = []
    for key in ad.keys():
        if key in keys:
            listAssign.append(ad[key])
    for k in keys:
        if k not in ad.keys():
            listAssign.append("")
    return listAssign


# use singleDictToList for multiple dictionaries;
# the list of values for each dictionary will be
# contained within a list
def convertToLists(keys, lod):
    commonList = []
    for i in range(len(lod)):
        singleList = singleDictToList(keys, lod[i])
        commonList.append(singleList)
    return commonList


# write each list of values to a new line in a csv file
def writeRecords(filename, records):
    with open(filename, 'a') as fp:
        writer = csv.writer(fp)
        for list in records:
            writer.writerow(list)
