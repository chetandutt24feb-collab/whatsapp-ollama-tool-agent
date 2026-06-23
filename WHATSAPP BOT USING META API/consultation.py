import datetime
import json
import random
from typing import Any, Dict, List

from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz
import requests

with open("D:/python/WHATSAPP BOT USING META API/config.json",encoding="utf-8") as f:
    variables=json.load(f)

OWNER=variables["OWNER"]
ACCESS_TOKEN=variables["ACCESS_TOKEN"]
ACCESS_TOKEN=variables["ACCESS_TOKEN"]
PHONE_NUMBER_ID=variables["PHONE_NUMBER_ID"]

def create_event(
    meeting_date: Dict[str, Any],
    meeting_time: Dict[str, Any],
    client_phone: str = "Client",
    meeting_type:Any="Online"
    
):
    print(f"meeting_type is {meeting_type}")
    import requests  # WhatsApp API hit karne ke liye
    

    # 3. Message ko readable format me clean karna
    formatted_date = f"{meeting_date['day']}:{meeting_date['month']}:{meeting_date['year']}"
    formatted_time = f"{meeting_time['hours']}:{meeting_time['minutes']}:{meeting_time['seconds']}"

    # Malik ke liye sunder sa alert message layout
    malik_payload = {
        "messaging_product": "whatsapp",
        "to": OWNER,
        "type": "text",
        "text": {
            "body": f"🚨 New Consultation Booking Alert!*\n\n"
                    f"👤 *Client Number:* {client_phone}\n"
                    f"📅 *Date:* {formatted_date}\n"
                    f"⏰ *Time:* {formatted_time}\n\n"
                    f"meeting_type={meeting_type}\n"
                    f"Please contact the client to confirm the scheduled meeting! ✨"

        }
    }

    # 4. Meta Graph API ko hit marna
    try:
        res = requests.post(
            f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            json=malik_payload
        )
        print(f"📩 Owner has been notified about the meeting!")
        return "Booking done"
        # Ek fake dummy dictionary return kar rahe hain taaki my_ollama.py me chal raha code crash na ho
        return {"status": "success", "message": "Owner notified successfully"}
        
    except Exception as e:
        print(f"An error occurred while sending the WhatsApp message to the owner: {e}")
        return {"status": "error", "message": str(e)}