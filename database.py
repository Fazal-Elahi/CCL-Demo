from pymongo import MongoClient
from datetime import datetime

class PostcodeDatabase:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.postcode_database
        self.collection = self.db.postcodes

    def find_postcode(self, postcode):
        return self.collection.find_one({"_id": postcode})

    def update_postcode(self, postcode, addresses):
        self.collection.update_one(
            {"_id": postcode},
            {"$set": {"addresses": addresses, "last_accessed": datetime.now()}},
            upsert=True
        )