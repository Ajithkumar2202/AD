from config import ACCIDENT_THRESHOLD, TILT_THRESHOLD

def detect_accident(acceleration, tilt):
    if acceleration > ACCIDENT_THRESHOLD or tilt > TILT_THRESHOLD:
        return True
    return False
