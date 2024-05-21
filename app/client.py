import requests
from flask import current_app as app, jsonify

@app.route('/consume', methods=['GET'])
def consume():
    response = requests.get('https://api.github.com/repos/spring-guides/gs-consuming-rest')
    data = response.json()
    return jsonify(data)

@app.route('/quote', methods=['GET'])
def quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    return jsonify(data)
