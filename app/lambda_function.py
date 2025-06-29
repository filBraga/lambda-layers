import json
from src.utils.logger import logger
from src.handler.sqs_handler import sqs_handler

def lambda_handler (event, _context):
    try:
        logger. info("Starting Lambda function")
        response = sqs_handler (event)
        logger. info("Lambda function completed successfully")
        return response
    except Exception as e:
        logger.error(f"Error in lambda_handler: {e}", exc_info=True)
        return {"statuscode": 500, "body": json.dumps ({"error": str(e)})}