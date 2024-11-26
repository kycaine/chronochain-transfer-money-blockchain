from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now, you can access the environment variable
TRANSACTION_FEE = float(os.getenv('TRANSACTION_FEE', 0.01))
DEBUGGING_MODE = float(os.getenv('DEBUGGING_MODE', 0))