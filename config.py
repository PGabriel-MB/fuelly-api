import os

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

MONGODB_SETTINGS = {
    'host': f'mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@fuelly.q5vipht.mongodb.net/?retryWrites=true&w=majority&appName=fuelly',
    'db': 'fuelly',
    'username': MONGODB_USERNAME,
    'password': MONGODB_PASSWORD
}