import socketio
from src.blockchain.blockchain import Blockchain

sio = socketio.Client()
blockchain = Blockchain()
sio.connect('http://localhost:5000')

@sio.event
def message(data):
    print(f"Received message: {data}")

@sio.event
def new_transaction(data):
    print(f"New transaction received: {data}")
    blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])

@sio.event
def new_block(block):
    print(f"New block received: {block}")
    blockchain.chain.append(block)

def send_new_transaction(sender, recipient, amount):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    sio.emit('new_transaction', transaction)

sio.wait()
