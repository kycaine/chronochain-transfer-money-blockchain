import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("connected to blockchain node!")

@sio.event
def disconnect():
    print("disconnected from blockchain node!")

@sio.event
def new_transaction(data):
    print(f"new transaction received: {data}")

@sio.event
def new_block(block):
    print(f"New block mined: {block}")

sio.connect('http://localhost:5000')

import time
while True:
    time.sleep(1)
