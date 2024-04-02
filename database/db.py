from pymongo import MongoClient

def initialize_db(mongo_settings):
    """ connect(
        host=mongo_settings['host'],
        db=mongo_settings['db'],
        username=mongo_settings['username'],
        password=mongo_settings['password']
    ) """
    client = MongoClient(mongo_settings['host'])