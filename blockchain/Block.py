import hashlib
from datetime import datetime

from data_structures.MerkleTree import MerkleTree
from blockchain.Transaction import Transaction


class Block:
    def __init__(self, index: int, transactions: list[Transaction], previous_hash: str):
        self.block_number = index
        self.timestamp = datetime.now().timestamp()
        self.transactions = transactions
        self.previous_hash = previous_hash

        self.merkle_root = MerkleTree(transactions).get_root_hash()
        self.block_hash = self.compute_hash()

    def compute_hash(self) -> str:
        """Calcula el hash del bloque entero, usando el merkle root, index, previous_hash, timestamp..."""
        serialize = self.serialize()
        block_hash = hashlib.sha256(serialize.encode()).hexdigest()
        return block_hash

    def get_merkle_root(self) -> str:
        """Devuelve el Merkle Root de las transacciones"""
        return self.merkle_root

    def serialize(self) -> str:
        return (str(self.block_number) + str(self.timestamp) + self.previous_hash
                + self.merkle_root + str(self.transactions))

    def __repr__(self):
        return "#" + str(self.block_number)