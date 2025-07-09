from blockchain.Transaction import Transaction
from blockchain.Blockchain import Blockchain

# t1 = Transaction("alice", "bob", 50)
# print(t1.serialize())
# print(t1.hash())

txs = [
    Transaction("Alice", "Pepe", 20),
    Transaction("Alice", "Pepe", 10),
    Transaction("Alice", "Pepe", 40)
]
#
# merkle = MerkleTree(txs)
# print("Root Hash:", merkle.get_root_hash())

# t1 = Transaction("alice", "bob", 50)
# t2 = Transaction("bob", "carol", 30)

# block = Block(index=0, transactions=[t1, t2], previous_hash="0"*64)

blockchain = Blockchain()       # Genesis Block
blockchain.add_block(txs)       # Block #1
blockchain.add_block(txs[1:])   # Block #2
blockchain.add_block(txs[:1])   # Block #3

# Rompemos la cadena manualmente
blockchain.chain.at(1).transactions[0] = Transaction("a", "b", 999)

print(blockchain.is_chain_valid())
# print(blockchain.is_chain_valid())

