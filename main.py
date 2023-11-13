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
