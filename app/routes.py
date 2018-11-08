from app import app
from flask import jsonify
import requests

@app.route('/')
def index():
    res = requests.get(
        'https://api.darksky.net/forecast/{0}/37.8267,-122.4233'
        .format(app.config['API_KEY']))
    
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    apiData = jsonify(res.json())
    return apiData
    