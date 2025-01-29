from dotenv import load_dotenv
import os

load_dotenv()

TRANSACTION_FEE = float(os.getenv('TRANSACTION_FEE', 0.01))
DEBUGGING_MODE = float(os.getenv('DEBUGGING_MODE', 0))
PORT = int(os.getenv('PORT', 5000));
SOCKET_HOST = os.getenv('SOCKET_HOST', 'localhost')
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')