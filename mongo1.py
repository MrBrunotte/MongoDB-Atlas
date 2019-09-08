# MongoClient is used to connect to MongoBD server
from pymongo import MongoClient

# create a reference for this client.
# Mongodb = Protocol,
# localhost = Hostname or IP Adress,
# 27017 = portnumber
# check that it connects with: print(client)
client = MongoClient('mongodb://localhost:27017')
print(client)
# store myTestDB in db. You can use: client.myTestDB or client['myTestDB']
db = client.myTestDB
print(db)
