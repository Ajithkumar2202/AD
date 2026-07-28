# 🚨 Accident Detection & Alert System

An automated system that detects vehicle accidents using sensor data (acceleration and tilt), captures an image at the moment of impact, and instantly alerts an emergency contact via SMS and email with the live location.

## How It Works

1. **Sensors** continuously report acceleration and tilt values.
2. The **detection engine** compares these readings against configured thresholds.
3. If an accident is detected:
   - The device's **live location** is fetched.
   - A **photo** is captured from the camera at the moment of the incident.
   - An **SMS (via Twilio)** and an **email** are sent to the emergency contact, including a Google Maps link to the location and the captured image.

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — runs the detection loop |
| `sensor_module.py` | Reads/simulates acceleration and tilt data |
| `detection.py` | Compares sensor readings against thresholds to flag an accident |
| `camera_module.py` | Captures an image from the webcam using OpenCV |
| `alert_module.py` | Sends SMS (Twilio) and email alerts with location + image |
| `location_server.py` | Flask server that receives and serves live GPS coordinates |
| `mobile_live_location.py` | Fallback location lookup (IP-based geolocation) |
| `phone_gps.html` | Simple web page to push a phone's GPS coordinates to the location server |
| `config.py` | Threshold values and emergency contact details |
| `utils.py` | Helper functions for displaying sensor data |

## Requirements

- Python 3.10+
- A webcam (for image capture)
- A [Twilio](https://www.twilio.com/) account (for SMS alerts)
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) (for email alerts)

Install dependencies:

```bash
pip install -r requirements.txt
```

> If you don't have a `requirements.txt` yet, create one with:
> ```
> opencv-python
> requests
> flask
> twilio
> python-dotenv
> ```

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Ajithkumar2202/AD.git
   cd AD
   ```

2. **Create a `.env` file** in the project root with your credentials (this file is git-ignored and never committed):

   ```env
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_NUMBER=your_twilio_phone_number
   USER_NUMBER=recipient_phone_number

   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_gmail_app_password
   EMAIL_RECEIVER=receiver_email@gmail.com
   ```

3. **Configure thresholds and contact info** in `config.py`:

   ```python
   ACCIDENT_THRESHOLD = 15   # acceleration limit
   TILT_THRESHOLD = 60       # tilt angle
   ```

## Usage

Start the location server (so live GPS coordinates can be received from a phone):

```bash
python location_server.py
```

Open `phone_gps.html` on a mobile browser to begin streaming GPS coordinates to the server.

Then run the main detection loop:

```bash
python main.py
```

When an accident is detected, the system will print an alert, capture a photo, and send an SMS/email with the location.

## ⚠️ Notes

- `sensor_module.py` currently **simulates** acceleration and tilt with random values for testing/demo purposes. Replace this with real accelerometer/gyroscope sensor input for production use.
- Never commit your `.env` file or hardcode API keys/tokens directly in source files — this repo's `.gitignore` already excludes `.env`, `.venv/`, and `__pycache__/`.
- If you previously exposed Twilio credentials in a commit, rotate them in the Twilio console immediately.

## License

This project is open-source and available for educational and personal use.
