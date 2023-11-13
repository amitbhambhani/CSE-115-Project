import csv


# returns a list of all values stored in the list
# of dictionaries associated with the given key
def getValuesForKey(key, records):
    searchList = []
    for i in range(len(records)):
        if key in records[i] and records[i][key] not in searchList:
            searchList.append(records[i][key])
    return searchList


# returns the number of records whose value associated with
# the passed-in key matches the passed-in value
def countMatchesByKey(key, value, records):
    counter = 0
    for i in range(len(records)):
        if key in records[i]:
            if records[i][key] == value:
                counter += 1
    return counter


# returns the number of records whose value associated with the key1
# matches value1 AND whose value associated with key2 matches the value2
def countMatchesByKeys(key1, value1, key2, value2, records):
    counter = 0
    for i in range(len(records)):
        if key1 in records[i] and key2 in records[i]:
            if records[i][key1] == value1 and records[i][key2] == value2:
                counter += 1
    return counter


# returns a new list of dictionaries corresponding to the records
# whose value associated with the passed-in key matches the passed-
# in value
def filterByKey(key, value, records):
    dictList = []
    for i in range(len(records)):
        if key in records[i]:
            if records[i][key] == value:
                dictList.append(records[i])
    return dictList


# returns a dictionary where the keys are all of the values
# in records associated with key, and the values are the number
# of times that the value appears in records
def computeFrequency(key, records):
    countDict = {}
    valueList = getValuesForKey(key, records)
    for value in valueList:
        countDict[value] = countMatchesByKey(key, value, records)
    return countDict


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
    print(dictList)


# import lines from a csv into a list
def loadRecords(filename):
    csvLines = []
    with open(filename, 'r') as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            csvLines.append(row)
    print(csvLines)


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
