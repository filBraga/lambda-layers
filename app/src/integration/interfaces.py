from abc import ABC, abstractmethod

class ISMSClient(ABC):
    @abstractmethod
    def send_sms(self, payload: dict) -> dict:
        pass

class IDBClient(ABC):
    @abstractmethod
    def save_sms(self, message_body: dict, status: str) -> dict:
        pass