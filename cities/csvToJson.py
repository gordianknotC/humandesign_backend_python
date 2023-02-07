#!D:\Python34\python
# -*- coding: utf-8 -*-
__author__ = 'gordianknot'
import os
import json
import csv
import codecs

CSV:str     = os.path.join(os.path.abspath(os.path.curdir), "./simplemaps-worldcities-basic.csv")
JSON:str    = os.path.join(os.path.abspath(os.path.curdir), "./simplemaps-worldcities-basic.json")
types_of_encoding = ["utf8", "cp1252"]

def readCSV():
    """read geo csv into dict"""
    data = {}
    for encoding_type in types_of_encoding:
        with codecs.open(CSV, encoding = encoding_type, errors ='replace') as f:
            f_csv = csv.DictReader(f)
            print(f_csv)
            for row in f_csv:
              print(row['city'], row['lat'], row['lng'], row['country'])
              data[row['city']+', ' + row['country']] = (row['lat'], row['lng'])
    return data

def dumpJSON(data):
    """dump data into geo json"""
    with open (JSON, 'w') as fp:
        json.dump (data, fp)


def readJSON():
    """read geo json"""
    with open(JSON, 'r') as f:
        data = f.read()
    return json.loads(data)



if __name__ == '__main__':
    dumpJSON(readCSV())