import pymongo
from bson import ObjectId
from scape_mars import scrape



def getLatest():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
    db = client.marsDb
    #data = db.scrapes.find()
    data = db.scrapes2.find().sort('_id', -1)
    print(data[0])
    return data[0]



def update():
        # Create connection variable
    conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
    db = client.marsDb
    #data = db.scrapes.find()

    mars_data = scrape()
    #print(mars_data)

    data = db.scrapes2
    post_id = data.insert_one(mars_data).inserted_id
    print(post_id)




