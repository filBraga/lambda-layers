from src.utils.logger import logger
from src.integration.interfaces import ISMSClient

def send_sms(message_body: dict, sms_client: ISMSClient) -> dict:
    try:
        response = sms_client.send_sms(message_body)
        logger.info(f"API Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}", exc_info=True)
        raise