from typing import List
from pydantic import BaseModel, Field

class SQSRecord(BaseModel):
    messageId: str = Field(..., description="Unique identifier for the message.")
    receiptHandle: str = Field(..., description="Identifier for the receipt of the message.")
    body: str = Field(..., description="The content of the message.")
    attributes: dict = Field(..., description="Attributes of the message.")
    messageAttributes: dict = Field(description="Custom message attributes.")
    md5OfBody: str = Field(..., description="MD5 hash of the message body.")
    eventSource: str = Field(..., description="Source of the event.")
    eventSourceARN: str = Field(..., description="ARN of the event source.")
    awsRegion: str = Field(..., description="AWS region.")

class SqsEvent(BaseModel):
    Records: List[SQSRecord] = Field(..., description="List of records in the SQS event.")