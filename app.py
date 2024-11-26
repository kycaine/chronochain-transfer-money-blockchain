from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields: sender, recipient, amount'}), 400

    index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': f'Transaction will be added to block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.last_block
    previous_hash = last_block['hash']
    block = blockchain.create_block(previous_hash)

    response = {
        'message': 'New block mined!',
        'block': block
    }
    return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid, messages = blockchain.validate_chain()
    
    if is_valid:
        response = {'message': 'eureekaa!!! all blocks are clear.'}
    else:
        response = {'message': 'invalid blocks', 'detail': messages}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
