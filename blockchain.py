import hashlib
import json
import time
from config import TRANSACTION_FEE

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash="0")  # new genesis block

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': None,  
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def hash_block(self, block):
        block_copy = block.copy()
        block_copy.pop('hash', None) 
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def generate_transaction_id(self, sender, recipient, time_now):
        transaction_data = f"{sender}{recipient}{time_now}"
        return hashlib.sha256(transaction_data.encode()).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        time_now = time.time()
        
        fee = amount * TRANSACTION_FEE
        amount_received = amount - fee

        transaction = {
            'id': self.generate_transaction_id(sender, recipient, time_now),
            'sender_public_key': sender + '-pubkey',
            'recipient_public_key': recipient + '-pubkey',
            'amount': amount,
            'fee': fee,
            'amount_received': amount_received,
            'timestamp': time_now,
        }

        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1 

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None 
    
    def validate_chain(self):
        validation_messages = []
        is_valid = True

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # check current hasg block
            if current_block['hash'] != self.hash_block(current_block):
                validation_messages.append(f"Block {current_block['index']} has an invalid hash!")
                is_valid = False
                
            # check previous hash block
            if current_block['previous_hash'] != previous_block['hash']:
                validation_messages.append(f"Block {current_block['index']} has an invalid previous hash!")
                is_valid = False

        # check genesiss block
        genesis_block = self.chain[0]
        if genesis_block['index'] != 1 or genesis_block['previous_hash'] != "0":
            validation_messages.append("Genesis block is invalid!")
            is_valid = False

        if is_valid:
            validation_messages.append("Blockchain is valid!")

        return is_valid, validation_messages



