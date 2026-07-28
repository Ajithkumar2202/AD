
from flask import Flask, request, jsonify

app = Flask(__name__)
latest_location = {"latitude": 0, "longitude": 0}

@app.route('/api/update_location', methods=['POST'])
def update_location():
    global latest_location
    latest_location = request.json
    return jsonify({"status": "ok"})

@app.route('/api/get_location')
def get_location():
    return jsonify(latest_location)