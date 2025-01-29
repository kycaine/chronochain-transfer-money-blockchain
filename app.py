from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from src.blockchain.blockchain import Blockchain
from config.config import DEBUGGING_MODE, PORT, FLASK_HOST


app = Flask(__name__)
app.debug = DEBUGGING_MODE
socketio = SocketIO(app)

blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/transactions', methods=['POST'])
def new_transaction():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields: sender, recipient, amount'}), 400

    index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])

    socketio.emit('new_transaction', {'sender': data['sender'], 'recipient': data['recipient'], 'amount': data['amount']})

    return jsonify({'message': f'Transaction will be added to block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.last_block
    previous_hash = last_block['hash']
    block = blockchain.create_block(previous_hash)

    socketio.emit('new_block', block)

    response = {
        'message': 'New block mined!',
        'block': block
    }
    return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid, messages = blockchain.validate_chain()
    
    if is_valid:
        response = {'message': 'Blockchain is valid!'}
    else:
        response = {'message': 'Invalid blocks', 'detail': messages}
    
    return jsonify(response), 200

@socketio.on('connect')
def handle_connect():
    print("A new peer has connected!")

@socketio.on('disconnect')
def handle_disconnect():
    print("A peer has disconnected!")

if __name__ == '__main__':
    socketio.run(app, host=FLASK_HOST, port=PORT)
