## FEATURES

1. Add a New Transaction: Users can initiate transactions between a sender and a recipient.
2. Mine a New Block: A new block can be mined to add pending transactions to the blockchain.
3. Validate the Blockchain: The integrity of the blockchain can be validated to ensure it hasn't been tampered with.
4. Get the Full Blockchain: Retrieve the entire blockchain to view all the recorded transactions.

## ROUTES

1 Add a New Transaction (pending block)
Request:
curl -X POST -H "Content-Type: application/json" -d '{"sender": "Alice", "recipient": "Bob", "amount": 50}' http://127.0.0.1:5000/transactions

2 Mine a New Block
Request:
curl http://127.0.0.1:5000/mine

3 Validate the Blockchain
Request:
curl http://127.0.0.1:5000/validate

4 Get the Full Blockchain
Request:
curl http://127.0.0.1:5000/chain
