import hashlib
import json
import time
from time import time


class Block:

    def __init__(self, index, previous_hash, reward_address):
        self.timestamp = time()
        self.nonce = 0
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = [{'amount': 50, 'recipient': reward_address, 'sender': None}]  # coinbase

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    def as_dict(self):
        """

        :return:
        """
        return self.__dict__

    def json(self):
        return json.dumps(self.as_dict())

    def hash(self):
        return hashlib.sha256(self.json().encode('utf-8')).hexdigest()


class Blockchain:

    def __init__(self, difficulty_prefix='000'):
        self.chain = []
        self.difficulty_prefix = difficulty_prefix

    def add_block(self, block):
        """

        :param block:
        :return:
        """
        if len(self.chain) == 0:
            self.chain.append(block)
            return True
        last_block = self.chain[-1]

        if last_block.hash() == block.previous_hash:
            if block.hash().startswith(self.difficulty_prefix):
                self.chain.append(block)
                return True
        return False

    def proof_of_work(self, block):
        """

        :param block:
        :return:
        """
        while True:
            if not self.validate_proof(block):
                block.nonce += 1
                continue
            break
        return block.nonce

    def validate_proof(self, block):
        """

        :return:
        """
        return block.hash().startswith(self.difficulty_prefix)

    def mine(self, block):
        while True:
            if not self.validate_proof(block):
                block.nonce += 1
                continue
            break
        self.chain.append(block)
        return block

    def new_block(self, reward_address):
        """

        :param reward_address:
        :return:
        """
        if len(self.chain) == 0:
            return Block(0, '0', reward_address)
        last_block = self.chain[-1]
        return Block(last_block.index + 1, last_block.hash(), reward_address)

    def print(self):
        """

        :return:
        """
        for block in self.chain:
            print(block.json(), block.hash())


if __name__ == '__main__':
    chain = Blockchain('00')

    block = chain.new_block('0x123123123')
    chain.proof_of_work(block)
    chain.add_block(block)
    block = chain.new_block('0x123123123')
    chain.proof_of_work(block)
    chain.add_block(block)
    block = chain.new_block('0x123123123')
    chain.proof_of_work(block)
    chain.add_block(block)
    chain.print()
