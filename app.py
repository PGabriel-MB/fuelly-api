from flask import Flask, jsonify
from config import MONGODB_SETTINGS
from database.db import initialize_db

app = Flask(__name__)
app.config.update(MONGODB_SETTINGS)

initialize_db(app)

@app.route('/movies')

def hello():
    return jsonify([{ teste: 'ab'}])

app.run()
