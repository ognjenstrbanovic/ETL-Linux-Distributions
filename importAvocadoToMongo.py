import csv
import json
import pandas as pd
import sys, getopt, pprint

import pymongo
from pymongo import MongoClient
#CSV to JSON Conversion

conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    # thid creates a schema called etlProject
db = client.etlProject

coll = db.avocado
#data = pd.read_csv(csv_path)
data = pd.read_csv('./data/avocado.csv',encoding = 'ISO-8859-1')
payload = json.loads(data.to_json(orient='records'))
coll.remove()
coll.insert(payload)
print(coll.count())

#db.avocado.update({}, {$rename:{"yourOldFieldName":"yourNewFieldName"}}, false, true);
#coll.update({}, {$rename:{"Unnamed: 0":"index"}}, false, true)

coll.update_many({}, {"$rename": {"Unnamed: 0":"id"}})


returnedData = db.avocado.find().sort('_id', -1)
for i in range(10):
    print(returnedData[i])


