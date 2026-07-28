import os
import base64
import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# ---------------- ENV VARS (set these in Vercel dashboard) ----------------
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
USER_NUMBER = os.getenv("USER_NUMBER")

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


@app.route('/')
def home():
    return jsonify({"status": "Accident detection backend is running"})


@app.route('/api/trigger_alert', methods=['POST'])
def trigger_alert():
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    photo_base64 = data.get("photo")

    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

    # ---------------- SMS ----------------
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"🚨 Accident Detected!\nLocation: {maps_link}",
            from_=TWILIO_NUMBER,
            to=USER_NUMBER
        )
    except Exception as e:
        print("SMS Error:", e)

    # ---------------- EMAIL ----------------
    try:
        msg = EmailMessage()
        msg["Subject"] = "🚨 Accident Alert!"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg.set_content(f"Accident Detected!\n\nLive Location:\n{maps_link}")

        if photo_base64:
            # strip "data:image/jpeg;base64," prefix if present
            if "," in photo_base64:
                photo_base64 = photo_base64.split(",")[1]
            img_data = base64.b64decode(photo_base64)
            msg.add_attachment(img_data, maintype="image", subtype="jpeg", filename="accident.jpg")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print("Email Error:", e)

    return jsonify({"status": "alert sent"})


@app.route('/api/update_location', methods=['POST'])
def update_location():
    return jsonify({"status": "ok"})


@app.route('/api/get_location')
def get_location():
    return jsonify({"latitude": 0, "longitude": 0})