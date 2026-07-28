

import requests
from sensor_module import get_acceleration, get_tilt
from detection import detect_accident
from camera_module import capture_image
from alert_module import send_alert
from API import index 

def get_location():
    try:
        res = requests.get("http://10.252.143.103/get_location")
        return res.json()
    except:
        return {"latitude": 0, "longitude": 0}

def main():
    while True:
        acc = get_acceleration()
        tilt = get_tilt()

        print("Acceleration:", acc, "Tilt:", tilt)

        if detect_accident(acc, tilt):
            print("🚨 Accident Detected!")

            location = get_location()
            capture_image()
            send_alert(location)
            break

if __name__ == "__main__":
    main()