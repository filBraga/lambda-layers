from pydantic import BaseModel, Field, validator

class CallbackData(BaseModel):
    id_cliente: str
    id_externo: str
    fluxo: str

class SMSRequest(BaseModel):
    sender: str
    destination: str
    message: str = Field(
        ...,
        min_length=1,
        max_length=160,
        description="Message must be between 1 and 160 characters."
    )
    correlation_id: str
    customer_id: str
    callback_data: CallbackData
    save_sms_in: bool = False

    @validator("destination")
    def validate_destination(cls, value):
        if not value.startswith("55"):
            raise ValueError("Destination must start with country code '55'.")
        return value