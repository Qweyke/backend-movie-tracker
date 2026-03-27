import os
from pymongo import MongoClient


def get_db():
    # If we are in Docker, use the service name, otherwise use localhost for dev
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
    client = MongoClient(mongo_url)
    return client["movie_accounting_db"]
