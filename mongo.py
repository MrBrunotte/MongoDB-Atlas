import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

""" Add one new record
new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952',
           'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)

documents = coll.find()
"""

""" Add more than one new record 

new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm',
             'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm',
                                                                                            'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

coll.insert_many(new_docs)
"""

""" find data
documents = coll.find({'first': 'douglas'})
"""

""" remove data
coll.remove({'first': 'douglas'})
"""

""" update_one (the first one in the database)
coll.update_one({'nationality': 'american'}, {
                '$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})
"""

""" update_many (update all in the db) """
coll.update_many({'nationality': 'american'}, {
    '$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
