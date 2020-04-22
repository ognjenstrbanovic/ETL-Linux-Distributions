import pymongo
from bson import ObjectId
from scape_mars import scrape



def getLatest():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
    db = client.etlProject
    
    # get the record that was inserted last 
    data = db.myDB.find().sort('_id', -1)
    print(data[0])
    return data[0]



def update():
        # Create connection variable
    conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
    db = client.etlProject
    
    #myData = getData()
    
    # insert mData into DB 
    data = db.myDB
    post_id = data.insert_one(myData).inserted_id
    print(post_id)




