import os
import requests
import logging

from src.utils.logger import logger
from src.integration.interfaces import ISMSClient


class InfobipClient(ISMSClient):
    def __init__(self):
        base_url = os.getenv("BASE_URL_INFOBIP")
        api_key = os.getenv("API_KEY_INFOBIP")
        if not base_url or not api_key:
            raise ValueError("BASE_URL_INFOBIP and API_KEY_INFOBIP must be set in environment variables")
        self.sms_url = f"{base_url}/sms/3/messages"
        self.headers = {
            "Authorization": f"App {api_key}",
            "Content-Type": "application/json"
        }

    def _build_payload(self, payload):
        return {
            "messages": [
                {
                    "from": payload["sender"],
                    "destinations": [{"to": payload["destination"]}],
                    "text": payload["message"],
                    "callbackData": payload.get("callback_data")
                }
            ]
        }

    def send_sms(self, payload):
        try:
            logger.info(f"Sending SMS with payload: {payload}")
            response = requests.post(
                self.sms_url,
                headers=self.headers,
                json=self._build_payload(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending SMS: {e}")
            raise