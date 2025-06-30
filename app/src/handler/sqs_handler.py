import json

from src.utils.logger import logger
from src.use_case.process_message import process_message
from src.integration.infobip_client import InfobipClient
from src.integration.dynamo_client import DynamoClient

def sqs_handler(event: dict):
    sms_client = InfobipClient()
    db_client = DynamoClient()

    try:
        logger.info(f"Event: {event}")
        records = event.get("Records")
        if not records:
            raise Exception("No records found in event")
        for message in records:
            message_body = json.loads(message["body"])
            process_message(message_body, sms_client, db_client)
            logger.info(f"Processed message: {message_body}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing SQS event: {str(e)}", exc_info=True)
        raise Exception(f"Error processing SQS event: {str(e)}")