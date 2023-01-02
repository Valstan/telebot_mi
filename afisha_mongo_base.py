from pymongo import MongoClient
import config as cfg


def afisha_mongo_base():
    client = MongoClient(cfg.MONGO_CLIENT)
    mongo_base = client['postopus']
    collection = mongo_base["mi"]
    return collection.find_one({'title': 'afisha'}, {'_id': 0})
