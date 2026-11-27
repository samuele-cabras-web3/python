import os
import json
import requests
import time
from dotenv import load_dotenv

# Load enviroment variables from .env file
load_dotenv()

# Retrieve Etherscan API key securely from environment variables
def get_api_key() -> str:
    api_key: str | None = os.getenv ("GasTracker")
    if api_key is None:
        raise ValueError("Missing GasTracker .env file")
    return api_key

# Convert proposed gas price string to float for threshold comparison
def format_ProposeGasPrice (ProposeGasPrice: str) -> float:
        return float(ProposeGasPrice)

# Configure Etherscan Gas Oracle API endpoint, query parametres, and headers
url = "https://api.etherscan.io/v2/api"
params = {
    "chainid": "1",
    "module": "gastracker",
    "action": "gasoracle",
    "apikey": get_api_key()
}

headers = {"User-Agent": "GasTracker/1.0"}

try:
    # Start continuous polling loop to  monitor Ethereum gas prices
    while True:
        print("Fetching latest blockchain data...")
        

        try:
            # Fetch gas price data with timeout and HTTP status validation
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = json.loads(response.text)

            # Parse JSON response and display Safe, Proposed, and Fast gas prices
            result = data["result"]
            SafeGasPrice = result["SafeGasPrice"]
            ProposeGasPrice = result["ProposeGasPrice"]
            FastGasPrice = result["FastGasPrice"]
            print(f"Safe Gas Price: {SafeGasPrice} Gwei")
            print(f"Propose Gas Price: {ProposeGasPrice} Gwei")
            print(f"Fast Gas Price: {FastGasPrice} Gwei")

            # Alert user when proposed gas price drops below the target threshold
            gas_price_num = format_ProposeGasPrice(ProposeGasPrice)
            max_gas_threshold = 1.0
            if gas_price_num < max_gas_threshold:
                print("Low gas fee detected! Ready to transact.")

        # Handle network or HTTP errors without crashing the polling loop
        except requests.exceptions.RequestException as e:
            print(f"Connection or HTTP error: {e}")

        print("-" * 40)
        # Wait 15 seconds before the next API request to respect rate limits
        time.sleep(15)

# Gracefully exit the loop when interrupted by the user (Ctrl+C)
except KeyboardInterrupt:
    print("\nPolling stopped safely by user.")


