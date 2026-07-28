



# from twilio.rest import Client
# import smtplib
# from email.message import EmailMessage
# from dotenv import load_dotenv





# def send_alert(location):
    
#     # Create Google Maps link
#     maps_link = f"https://www.google.com/maps?q={location['latitude']},{location['longitude']}"
    
#     # ---------------- SEND SMS ----------------
#     try:
#         client = Client(ACCOUNT_SID, AUTH_TOKEN)

#         message = client.messages.create(
#             body=f"🚨 Accident Detected!\nLocation: {maps_link}",
#             from_=TWILIO_NUMBER,
#             to=USER_NUMBER
#         )

#         print("SMS sent!")
#     except Exception as e:
#         print("SMS Error:", e)

#     # ---------------- SEND EMAIL ----------------
#     try:
#         msg = EmailMessage()
#         msg['Subject'] = "🚨 Accident Alert!"
#         msg['From'] = EMAIL_SENDER
#         msg['To'] = EMAIL_RECEIVER

#         msg.set_content(f"""
# Accident Detected!

# Live Location:
# {maps_link}

# Please take immediate action.
# """)

#         # Attach Image
#         with open("accident.jpg", "rb") as f:
#             img_data = f.read()
#             msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename="accident.jpg")

#         # Send Email
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
#             smtp.send_message(msg)

#         print("Email sent!")
#     except Exception as e:
#         print("Email Error:", e)


from twilio.rest import Client
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# ---------------- TWILIO CONFIG ----------------
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
USER_NUMBER = os.getenv("USER_NUMBER")


# ---------------- EMAIL CONFIG ----------------
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


# ---------------- SEND ALERT FUNCTION ----------------
def send_alert(location):

    # Create Google Maps link
    maps_link = (
        f"https://www.google.com/maps?"
        f"q={location['latitude']},{location['longitude']}"
    )

    # ---------------- SEND SMS ----------------
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body=f"🚨 Accident Detected!\nLocation: {maps_link}",
            from_=TWILIO_NUMBER,
            to=USER_NUMBER
        )

        print("SMS sent!")

    except Exception as e:
        print("SMS Error:", e)


    # ---------------- SEND EMAIL ----------------
    try:
        msg = EmailMessage()

        msg["Subject"] = "🚨 Accident Alert!"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        msg.set_content(f"""
Accident Detected!

Live Location:
{maps_link}

Please take immediate action.
""")

        # Attach accident image
        with open("accident.jpg", "rb") as f:
            img_data = f.read()

            msg.add_attachment(
                img_data,
                maintype="image",
                subtype="jpeg",
                filename="accident.jpg"
            )

        # Send Email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email sent!")

    except Exception as e:
        print("Email Error:", e)

