from blockchain.Transaction import Transaction
from data_structures.Queue import Queue


class MerkleTree:
    def __init__(self, transactions: list[Transaction]):
        # Empty list
        if len(transactions) == 0:
            self.root_hash = ""
            return

        tx_queue = Queue()

        for transaction in transactions:
            tx_queue.enqueue(transaction.hash())

        # odd list => even list
        if len(transactions) == 1:
            tx_queue.enqueue(transactions[-1].hash())

        while len(tx_queue) > 1:
            tx1: str = tx_queue.dequeue()
            tx2: str = tx_queue.dequeue()
            combined_hash = Transaction.generateHash(f"{tx1 + tx2}")
            tx_queue.enqueue(combined_hash)

        self.root_hash = tx_queue.dequeue()

    def get_root_hash(self) -> str:
        """Devuelve el Merkle Root de las transacciones"""
        return self.root_hash
