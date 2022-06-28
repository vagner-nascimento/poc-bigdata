# This connections should be a lib and the strings parametrized
from pymongo import MongoClient

def get_db(name, port):
    CONN_STR = "mongodb://root:rpwd@localhost:" + str(port) + "/admin"
    client = MongoClient(CONN_STR)

    return client[name]

def get_bigdata_db():
    return get_db("reports", 27018)
