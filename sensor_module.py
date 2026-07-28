import random

def get_acceleration():
    # Simulate acceleration
    return random.randint(0, 20)

def get_tilt():
    # Simulate tilt angle
    return random.randint(0, 90)

def get_location():
    # Simulated GPS
    return {
        "latitude": 10.7905,
        "longitude": 78.7047
    }

