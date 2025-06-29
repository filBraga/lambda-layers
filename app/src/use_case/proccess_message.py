from pydantic import ValidationError
from requests.exceptions import RequestException

from src.utils.logger import logger
from src.model.sqs import SMSRequest
from src.use_case.send_sms import send_sms
from src.use_case.save_sms_in_db import save_sms_in_db

def process_message(message_body)->None:
    validate_message(message_body)
    try:
        send_sms_request (message_body)
    except Exception as e:
        logger. error (f"Failed to process message: {e}") 
        raise Exception(f"Failed to process message: {e}")
    
def validate_message(message_body):
    try:
        return SMSRequest.model_validate(message_body)
    except ValidationError as e:
        logger.error (f"Validation failed: {e}")
        # save_sms_in_db (message_body, status="error")
        raise Exception(f"Error validating SMS: {e}")
        
def save_sms_in_db(message_body, status):
    try:
        return save_sms_in_db(message_body=message_body, status=status)
    except Exception as e:
        logger.error(f"Error saving SMS in DB: {e}")
        raise Exception(f"Error saving SMS in DB: {e}")
                
def send_sms_request(message_body):
    try:
        send_sms(message_body)
        save_sms_in_db(message_body, status="success")
    except RequestException as e:
        logger.error(f"Error sending SMS: {e}")
        save_sms_in_db (message_body, status="error")
        raise Exception(f"Error sending SMS: {e}")