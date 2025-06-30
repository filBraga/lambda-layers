from pydantic import ValidationError
from requests.exceptions import RequestException

from src.utils.logger import logger
from src.model.sms import SMSRequest
from src.use_case.send_sms import send_sms
from src.use_case.save_sms_in_db import save_sms_in_db
from src.integration.interfaces import ISMSClient, IDBClient

def process_message(message_body: dict, sms_client: ISMSClient, db_client: IDBClient) -> None:
    try:
        send_sms_request(message_body, sms_client, db_client)
    except ValidationError as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        save_sms_in_db(message_body, status="validation_error", db_client=db_client)
        raise
    except RequestException as e:
        logger.error(f"Error sending SMS: {e}", exc_info=True)
        save_sms_in_db(message_body, status="send_error", db_client=db_client)
        raise
    except Exception as e:
        logger.error(f"Failed to process message: {e}", exc_info=True)
        save_sms_in_db(message_body, status="unknown_error", db_client=db_client)
        raise


def send_sms_request(message_body: dict, sms_client: ISMSClient, db_client: IDBClient):
    send_sms(message_body, sms_client)
    save_sms_in_db(message_body, status="success", db_client=db_client)
    