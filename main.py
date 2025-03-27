from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio ke variable
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello bhai! Railway pe chal raha hai bot 🚀',
    to='whatsapp:+919798729776'  # Apna number daal
)

print("Message Sent! SID:", message.sid)
