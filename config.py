import os

MONGODB_USER = os.getenv('MONGODB_USER')
MONGODB_PASSW = os.getenv('MONGODB_PASSW')

MONGODB_SETTINGS = {
    'host': f'mongodb+srv://{MONGODB_USER}:{MONGODB_PASSW}@fuelly.q5vipht.mongodb.net/?retryWrites=true&w=majority&appName=fuelly'
}