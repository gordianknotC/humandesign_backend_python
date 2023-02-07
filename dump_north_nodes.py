# -*- coding: utf-8 -*-
import sys
import os
import json
import ephem
import math
import calendar
import datetime
import json
from ephem import *


CONFIG = os.path.join(os.path.abspath(os.path.curdir), "./nodes.json")


def processSeconds(d, sign, last_lon, result, year, month):
    moon = ephem.Moon()
    for s in range(60):
        d = d.replace(second=s)
        moon.compute(d, epoch=d)
        lon = math.degrees(Ecliptic(moon).lat)
        if last_lon > 0 and lon < 0:
            result[year].append(str(d).replace('-', '/'))
        elif last_lon < 0 and lon > 0:
            result[year].append(str(d).replace('-', '/'))
        last_lon = lon


def processMinutes(d, sign, last_lon, result, year, month):
    moon = ephem.Moon()
    for m in range(60):
        d = d.replace(minute=m)
        moon.compute(d, epoch=d)
        lon = math.degrees(Ecliptic(moon).lat)
        if last_lon > 0 and lon < 0:
            processSeconds(last_d, sign, last_lon, result, year, month)
        elif last_lon < 0 and lon > 0:
            processSeconds(last_d, sign, last_lon, result, year, month)
        last_lon = lon
        last_d = d


def processHours(d, sign, last_lon, result, year, month):
    moon = ephem.Moon()
    for h in range(24):
        d = d.replace(hour=h)
        moon.compute(d, epoch=d)
        lon = math.degrees(Ecliptic(moon).lat)
        if last_lon > 0 and lon < 0:
            print(d)
            processMinutes(last_d, sign, last_lon, result, year, month)
        elif last_lon < 0 and lon > 0:
            print(d)
            processMinutes(last_d, sign, last_lon, result, year, month)
        last_lon = lon
        last_d = d


def find_nodes_dates_by_year(year=2001):
    moon = ephem.Moon()
    result = {str(year): {}}
    lat = 0
    lon = 0
    next_node_day = 1
    last_lon = None
    last_d = None
    last_m = None
    last_y = None
    break_h = False
    break_m = False
    acc = 0
    for month in range(1, 13):
        result[str(year)] = []

    for month in range(1, 13):
        acc = 12 if month == 2 else 13
        i = next_node_day
        mon_len = calendar.monthrange(year, month)[1]
        while i <= mon_len:
            # for i in range( next_node_day, calendar.monthrange(year,
            # month)[1]):
            break_h = False
            for h in range(24):
                if break_h:
                    break
                break_m = False
                for m in range(60):
                    if break_m:
                        break
                    # for s in range(60):
                    d = datetime.datetime(year, month, i, h, m)
                    moon.compute(d, epoch=d)
                    lon = math.degrees(Ecliptic(moon).lat)
                    if last_lon != None:
                        if last_lon >= 0 and lon <= 0:
                            next_node_day = (i + acc) % mon_len or 1
                            i += acc - 1
                            print('\t', str(d).replace('-', '/'), last_lon, lon, 'dec')
                            if len(result[str(year)]) == 0:  result[str(year)].append([None,  str(d).replace('-', '/')])
                            else:                            result[str(year)][-1][1] = str(d).replace('-', '/')
                            break_h = break_m = True
                            last_lon = lon
                            break
                        elif last_lon <= 0 and lon >= 0:
                            next_node_day = (i + acc) % mon_len or 1
                            i += acc - 1
                            print('\t', str(d).replace( '-', '/'), last_lon, lon, 'acc')
                            
                            if len(result[str(year)]) == 0:  result[str(year)].append([str(d).replace('-', '/'), None  ])
                            else :                           result[str(year)].append([str(d).replace('-', '/'), None  ])
                            break_h = break_m = True
                            last_lon = lon
                            break
                        

                    last_lon = lon
            i += 1

    return result


from pprint import pprint


def main():
    ret = {}
    empty = {'+': '', '-': ''}
    _from = 1901
    _to = 2027
    for year in range(_from, _to):
        ret[str(year)] = find_nodes_dates_by_year(year)[str(year)]

    # ret[str(_to)] = []

    # for year in range(_from, _to):
    #     tmp = []
    #     year_data = ret[str(year)]
    #     for i in range(0, len(year_data), 2):
    #         if year_data[i] is not None:
    #             if year_data[i + 1] is None:
    #                 # print('None', year, year_data[i])
    #                 # print('before insert:', ret[str(year + 1)] )
    #                 ret[str(year + 1)].insert(0, None)
    #                 # print('after insert:', ret[str(year + 1)] )
    #             tmp.append([year_data[i], year_data[i + 1]])
    #         elif year_data[i] is None and i == 0:
    #             tmp.append([year_data[i], year_data[i + 1]])

    #     ret[str(year)] = tmp

    pprint(ret)
    with open(CONFIG, 'w') as fp:
        json.dump(ret, fp)

# main()


def show():
    with open(CONFIG, 'r') as fp:
        data = json.load(fp)
        print(data['1981']['12'])


main()
