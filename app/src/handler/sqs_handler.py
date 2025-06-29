import json

from src.utils.logger import logger
from src.model.sqs import SqsEvent
from src.use_case.proccess_message import process_message

def sqs_handler(event: SqsEvent):
    try:
        logger.info(f"Event: {event}")
        if "Records" not in event:
            raise Exception("No records found in event")
        for message in event["Records"]:
            message_body = json.loads(message["body"])
            process_message(message_body)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Messages processed successfully"}),
        }
    except Exception as e:
        logger.error(f"Unexpected error processing SQS event: {str(e)}")
        raise Exception(f"Error processing SQS event: {str(e)}")