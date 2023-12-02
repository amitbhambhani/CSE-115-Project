import milestone1 as m1
import milestone2 as m2
import os
import urllib.request as url
import json
import matplotlib.pyplot as plt
import csv


keys = ['title', 'category', 'type', 'medium',
        'frame', 'photo_url_link', 'artist',
        'site', 'street_address', 'city', 'zip_code',
        'state', 'latitude', 'longitude']


def cacheAndLoadData(file):
    if not os.path.isfile(file):
        requestURL = url.urlopen(
            'https://data.buffalony.gov/resource/6xz2-syui.json')
        data = json.loads(requestURL.read().decode('utf-8'))
        dataList = m2.convertToLists(keys, data)
        with open(file, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(keys)
        m2.writeRecords(file, dataList)
    load = m2.loadRecords(file)
    out = m2.convertToDictionaries(keys, load)
    return out


def cleanData(data):
    for ad in data:
        if ad['category'] == 'PAINTINGS':
            ad['category'] = 'PAINTING'
        elif ad['category'] == 'DECORATIVE OBJECTS':
            ad['category'] = 'DECORATIVE OBJECT'
        elif ad['category'] == 'GRAPHICS' or \
                ad['category'] == 'GRAPHIC' or \
                ad['category'] == 'GRAPHICS ARTS':
            ad['category'] = 'GRAPHIC ARTS'
    return None


def plotPieForKey(key, data):
    counted = m1.computeFrequency(key, data)
    labels = list(counted.keys())
    sizes = list(counted.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.show()
    return None


def plotBarForKey(key, data):
    counted = m1.computeFrequency(key, data)
    labels = list(counted.keys())
    values = list(counted.values())
    plt.figure(figsize=(14, 4))
    plt.barh(labels, values)
    plt.show()
    return None


def plotFilteredBarForKey(key, fkey, fval, data):
    filter = m1.filterByKey(fkey, fval, data)
    counted = m1.computeFrequency(key, filter)
    labels = list(counted.keys())
    values = list(counted.values())
    plt.figure(figsize=(14, 4))
    plt.barh(labels, values)
    plt.show()
    return None
