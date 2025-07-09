from blockchain.Transaction import Transaction
from blockchain.Block import Block
from data_structures.ImmutableLinkedList import ImmutableLinkedList


class Blockchain:
    def __init__(self):
        self.chain = ImmutableLinkedList()
        genesis = Block(0, [], "0" * 64)
        self.chain.append(genesis)

    def add_block(self, transactions: list[Transaction]):
        """Crea un nuevo bloque, lo conecta y lo agrega"""
        last_block = self.get_last_block()
        new_block = Block(last_block.block_number + 1, transactions, last_block.block_hash)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Verifica que todos los bloques estén encadenados y con hashes válidos"""

        for node in self.chain:
            if node.next is None:
                break

            this_data: Block = node.data
            next_data: Block = node.next.data

            if this_data.previous_hash != next_data.block_hash:
                return False
            if this_data.compute_hash() != this_data.block_hash:
                return False
        return True

    def get_last_block(self) -> Block | None:
        last = self.chain.getLast()
        if last is None:
            return None
        return last.data
