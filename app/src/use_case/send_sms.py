from src.utils.logger import logger
from src.integration.infobip_adapter import InfobipAdapter

def send_sms(message_body):
    try:
        message_provider = InfobipAdapter()
        response = message_provider.send_sms(message_body)
        logger.info(f"API Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}")
        raise Exception(f"Failed to send SMS: {e}")