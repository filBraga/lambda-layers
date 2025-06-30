import os
import boto3
from botocore.exceptions import ClientError

from src.utils.logger import logger
from src.integration.interfaces import IDBClient

class DynamoClient(IDBClient):
    def __init__(self):
        self.table_name = os.getenv("DYNAMO_TABLE_NAME")
        if not self.table_name:
            raise ValueError("DYNAMO_TABLE_NAME environment variable is not set")
        self.dynamodb = boto3.resource("dynamodb")  # Initialize once here

    def save_sms(self, message_body, status):
        try:
            table = self.dynamodb.Table(self.table_name)
            item = {
                # to be defined based on your DynamoDB schema
                "body": message_body.get("body"),
                "status": status,
                "timestamp": message_body.get("timestamp", None),  # Optional timestamp
            }
            response = table.put_item(Item=item)
            logger.info(f"SMS saved in DynamoDB: {response}")
            return response
        except ClientError as e:
            logger.error(
                f"Error saving SMS in DynamoDB: {e.response['Error']['Message']}"
            )
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise