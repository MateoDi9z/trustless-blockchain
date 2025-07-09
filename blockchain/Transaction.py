import hashlib
from datetime import datetime
from typing import Optional


class Transaction:
    def __init__(
            self,
            sender: str,
            receiver: str,
            amount: float,
            timestamp: Optional[int] = None
    ):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = timestamp if timestamp is not None else int(datetime.now().timestamp())

    def serialize(self) -> str:
        """Devuelve un string único y determinista representando esta transacción"""
        serialized = self.sender + self.receiver + str(self.amount) + str(self.timestamp)
        return serialized

    def hash(self) -> str:
        """Devuelve el SHA-256 del string serializado"""
        serialized = self.serialize()
        hashed = hashlib.sha256(serialized.encode()).hexdigest()
        return hashed

    @staticmethod
    def generateHash(text: str) -> str:
        """Devuelve el SHA-256 de un string"""
        return hashlib.sha256(text.encode()).hexdigest()

    def __repr__(self):
        return f"({self.sender} -> {self.receiver} ${self.amount})"