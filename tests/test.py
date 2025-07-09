import time

from blockchain.Block import Block
from blockchain.Blockchain import Blockchain
from blockchain.Transaction import Transaction
from data_structures.MerkleTree import MerkleTree


def test_transaction():
    t1 = Transaction("alice", "bob", 100, 1234567890)
    t2 = Transaction("alice", "bob", 100, 1234567890)
    assert t1.serialize() == t2.serialize()
    assert t1.hash() == t2.hash()
    t3 = Transaction("alice", "bob", 101)
    assert t1.hash() != t3.hash()

def test_merkle_tree():
    txs = [
        Transaction("a", "b", 1),
        Transaction("b", "c", 2),
        Transaction("c", "d", 3)
    ]
    tree1 = MerkleTree(txs)
    root1 = tree1.get_root_hash()

    # Cambiamos una transacción
    txs[0] = Transaction("a", "b", 999)
    tree2 = MerkleTree(txs)
    root2 = tree2.get_root_hash()

    assert root1 != root2

def test_block():
    txs = [
        Transaction("x", "y", 42),
        Transaction("y", "z", 10)
    ]
    previous_hash = "0" * 64
    block = Block(index=1, transactions=txs, previous_hash=previous_hash)

    assert block.block_number == 1
    assert block.previous_hash == previous_hash
    assert block.get_merkle_root() == MerkleTree(txs).get_root_hash()
    assert block.compute_hash() == block.block_hash

def test_blockchain():
    chain = Blockchain()

    assert len(chain.chain) == 1  # Bloque génesis

    t1 = Transaction("a", "b", 10)
    t2 = Transaction("b", "c", 5)
    chain.add_block([t1, t2])

    assert len(chain.chain) == 2
    assert chain.is_chain_valid()

    # Rompemos la cadena manualmente
    chain.chain.at(1).transactions[0] = Transaction("a", "b", 999)
    assert not chain.is_chain_valid()

def run_all_tests():
    test_transaction()
    test_merkle_tree()
    test_block()
    test_blockchain()
    print("✅ Todos los tests pasaron correctamente")

run_all_tests()
