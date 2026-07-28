import requests

def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()

        loc = data['loc'].split(',')
        latitude = float(loc[0])
        longitude = float(loc[1])

        return {
            "latitude": latitude,
            "longitude": longitude
        }

    except:
        return {"latitude": 0, "longitude": 0}