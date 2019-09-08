# connection string #
import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# END connection string #

# define our show_menu() function


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

# define our main_loop() function


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have seleced option 1")
        elif option == "2":
            print("You have seleced option 2")
        elif option == "3":
            print("You have seleced option 3")
        elif option == "4":
            print("You have seleced option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


# connection object from Mongo
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

# call our main loop
main_loop()
