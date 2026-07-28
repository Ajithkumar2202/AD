from flask import Flask, request

app = Flask(__name__)

latest_location = {"latitude": 0, "longitude": 0}

@app.route('/update_location', methods=['POST'])
def update_location():
    global latest_location
    data = request.json
    latest_location = data
    print("📍 Updated:", latest_location)
    return {"status": "ok"}

@app.route('/get_location')
def get_location():
    return latest_location

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)