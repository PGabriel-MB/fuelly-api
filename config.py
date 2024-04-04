import os

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

MONGODB_SETTINGS = {
    'host': f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@fuelly.q5vipht.mongodb.net/',#?retryWrites=true&w=majority&appName=fuelly',
    'db': MONGODB_DATABASE,
    'username': MONGODB_USERNAME,
    'password': MONGODB_PASSWORD
}