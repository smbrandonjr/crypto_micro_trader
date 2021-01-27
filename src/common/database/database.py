import pymongo
import os

__author__ = 'mike.brandon|smbrandonjr@gmail.com'

class Database(object):
    URI = os.environ.get("DB_CONNECTION_STRING")
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['cbt']

    @staticmethod
    def insert(collection, data):
        Database.initialize()
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        Database.initialize()
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def most_recent_order(collection, query):
        Database.initialize()
        return Database.DATABASE[collection].find(query).sort("done_at", pymongo.DESCENDING).limit(1)

    @staticmethod
    def find_one(collection, query):
        Database.initialize()
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def distinct(collection, query, filter=None):
        Database.initialize()
        return Database.DATABASE[collection].distinct(query, filter=filter)

    @staticmethod
    def aggregate(collection, query):
        return Database.DATABASE[collection].aggregate(query)

    @staticmethod
    def update(collection, query, data):
        Database.initialize()
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        Database.initialize()
        return Database.DATABASE[collection].remove(query)

    @staticmethod
    def drop(collection):
        return Database.DATABASE[collection].drop()