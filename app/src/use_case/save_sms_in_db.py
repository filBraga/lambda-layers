from src.integration.dynamo_adapter import DynamoAdapter
from src.utils.logger import logger

def save_sms_in_db(message_body):
    try:
        db_client = DynamoAdapter()
        response = db_client. save_sms(message_body)
        logger. info(f"SMS saved in DB: {response}") 
        return response
    except Exception as e:
        logger.error(f"Error saving SMS in DB: {e}")
        raise Exception(f"Error saving SMS in DB: {e}")