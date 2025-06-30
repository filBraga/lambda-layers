from src.integration.interfaces import IDBClient
from src.utils.logger import logger

def save_sms_in_db(message_body: dict, status: str, db_client: IDBClient) -> dict:
    try:
        response = db_client.save_sms(message_body, status)
        logger.info(f"SMS saved in DB: {response}")
        return response
    except Exception as e:
        logger.error(f"Error saving SMS in DB: {e}", exc_info=True)
        raise