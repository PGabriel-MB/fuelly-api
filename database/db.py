from mongoengine import connect

def initialize_db(mongo_settings):
    '''connect(
        host=mongo_settings['host'],
        db=mongo_settings['db'],
        username=mongo_settings['username'],
        password=mongo_settings['password']
    )'''
    print("##################################### - Connecting to MongoDB - ################################")
    print(mongo_settings['host'])
    connect(host=mongo_settings['host'])