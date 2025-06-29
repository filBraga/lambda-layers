import os
import boto3
from botocore.exceptions import ClientError

from src.utils.logger import logger


class DynamoAdapter:
    def __init__(self):
        self.table_name = os.getenv("DYNAMO_TABLE_NAME")
        if not self.table_name:
            raise ValueError("DYNAMO_TABLE_NAME environment variable is not set")

    def save_sms(self, message_body):
        try:
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(self.table_name)
            response = table.put_item(Item=message_body)
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