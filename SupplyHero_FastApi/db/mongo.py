from pymongo import MongoClient
import motor.motor_asyncio

class MongoSession:

    def __init__(self, collection=None, database_name="supply-hero"):
        DATABASE_URL = 'mongodb+srv://admin_user:8w5B1e3hz4UcGEs5@supply-hero.isdcn.mongodb.net/supply-hero?retryWrites=true&w=majority'
        self.client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")
        self.db = self.client[database_name]
        self.collection = self.db[collection]

    def insert_json(self, document):
        return self.collection.insert_one(document)

    def find_json(self, document):
        return self.collection.find_one(document)

    def delete_json(self, document):
        return self.collection.remove(document)



class MongoSessionRegular:

    def __init__(self, collection=None, database_name="supply-hero"):
        DATABASE_URL = 'mongodb+srv://admin_user:8w5B1e3hz4UcGEs5@supply-hero.isdcn.mongodb.net/supply-hero?retryWrites=true&w=majority'
        self.client = MongoClient(DATABASE_URL, uuidRepresentation="standard")
        self.db = self.client[database_name]
        self.collection = self.db[collection]

    def insert_json(self, document):
        return self.collection.insert_one(document)

    def find_json(self, document):
        return self.collection.find_one(document)

    def delete_json(self, document):
        return self.collection.remove(document)