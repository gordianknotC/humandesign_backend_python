#!D:\Python34\python
# -*- coding: utf-8 -*-
__author__ = 'gordianknot'
import os, ephem
from ephem.cities import lookup as googleLookup, _city_data
from typing import *
from utils.utils import TCity
from humandesign.cities.csvToJson import readJSON
from hd_database.database import geoDB, TObserver
from humandesign.cities.worldcities_db import MAJOR_CITY_PAIRS, CITY_DB

import unittest
from utils.logger import Logger, LEVELS


log = Logger('server', colorize = True)
log.allowed_flag = LEVELS[2]

CONFIG = os.path.join (os.path.abspath (os.path.curdir), "./cities.json")
isAddress = lambda x:',' in x
last = lambda x:x [-1]
COUNTRY_SEP = '$country:'
OBSERVER_SEP = '$observer:'
encodeCityRawData = lambda countryname, observer_data:'{}{}{}{}'.format (COUNTRY_SEP, countryname, OBSERVER_SEP,
                                                                         observer_data)
IS = lambda a, b:isinstance (a, b)


def getCitiesByCountry (country):
    return MAJOR_CITY_PAIRS.get (country)


def processAddress (key: str) -> TCity:
    if isAddress (key):
        prefix = 'address:'
        codes = list (map (lambda x:x.strip (), key.split (',')))
        if last (codes).isdigit ():
            zip = codes [-1]
            country = codes [-2]
            city = codes [-3]
        else:
            country = codes [-1]
            city = codes [-2]
        return TCity (country, city)
    return TCity ('UnKnown', key)


# FIXME: tested but may run into problems?
def lookupCity (address: str) -> Optional [ephem.Observer]:
    cityobj = processAddress (address)
    googleNotFound = lambda x:IS (x, str)
    log.debug("lookup address:", address, "cityobj", cityobj, 'is in geoDB', address in geoDB)
    if not address in geoDB:
        try:
            observer = googleLookup (address)
            log.debug('lookup city:', address, 'from google map,', 'observer:', observer, 'cityobj:', cityobj)
            if googleNotFound (observer):
                raise Exception('google cannot found city for :', address, 'is address in geoDB?', address in geoDB)
            else:
                geoDB [address] = TObserver (observer.lat, observer.lon, observer.pressure, cityobj.city,
                                                  cityobj.country)
            log.debug (geoDB [address])
        except Exception as e:
            raise Exception(e)
    else:
        observer = ephem.Observer ()
        citydata = list(geoDB.search(cityobj))[0]
        observer.lat = citydata.lat
        observer.lon = citydata.lon
        observer.pressure = float(citydata.pressure)
        observer.name = citydata.city
        log.debug('get data from geoDB:', citydata)
    return observer


def readJSONintoDB ():
    j = readJSON ()
    for key in j:
        value = j [key]
        print (key, value, value [0])
        city = processAddress (key)
        geoDB [key] = TObserver (lat=value [0], lon=value [1], pressure=1010, city=city.city, country=city.country)



def dumpCityDB_toDatabase():
    for key in CITY_DB:
        value = CITY_DB[key]
        cityobj = processAddress(key)
        pressure = _city_data.get(cityobj.city, 1010)
        geoDB[key.strip()] = TObserver(lat = value[0], lon=value[1], city=cityobj.city, country=cityobj.country, pressure='1010')



class Test (unittest.TestCase):
    def setUp (self):
        pass

    def test_getCityByCountry (self):
        print(getCitiesByCountry('Taiwan'))
        self.assertEqual(len(getCitiesByCountry('Taiwan')), 20)

    def test_lookupCity(self):
        o = lookupCity('Zhongli, Taiwan')
        self.assertAlmostEqual(o.lat, 0.4357218884560205)

    def test_lookupCity2(self):
        o = lookupCity('Taipei, Taiwan')
        self.assertAlmostEqual(o.lat, 0.43695772258903604)

