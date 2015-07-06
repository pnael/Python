#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo

mongocon = pymongo.MongoClient("192.168.1.15",49153)

db = mongocon.stockdb
coll = db.stockcollection
stock = {'name':'NASDAQ' , 'value':4630.60 , 'change':'+6.06' , 'time' : 1}

#coll.insert(stock)   #Insert document
coll.find({ 'name' : 'NASDAQ'}) #Query for all records of ‘NASDAQ’
