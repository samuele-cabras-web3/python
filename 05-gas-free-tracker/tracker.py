import os
import json
import requests
import time
from dotenv import load_dotenv

load_dotenv()

def get_api_key() -> str:
    api_key: str | None = os.getenv ("GasTracker")
    if api_key is None:
        raise ValueError("Missing GasTracker .env file")
    return api_key

def format_ProposeGasPrice (ProposeGasPrice: str) -> float:
        return float(ProposeGasPrice)


url = "https://api.etherscan.io/v2/api"
params = {
    "chainid": "1",
    "module": "gastracker",
    "action": "gasoracle",
    "apikey": get_api_key()
}

headers = {"User-Agent": "GasTracker/1.0"}

try:
    while True:
        print("Fetching latest blockchain data...")
        

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = json.loads(response.text)

            result = data["result"]
            SafeGasPrice = result["SafeGasPrice"]
            ProposeGasPrice = result["ProposeGasPrice"]
            FastGasPrice = result["FastGasPrice"]
            print(f"Safe Gas Price: {SafeGasPrice} Gwei")
            print(f"Propose Gas Price: {ProposeGasPrice} Gwei")
            print(f"Fast Gas Price: {FastGasPrice} Gwei")

            gas_price_num = format_ProposeGasPrice(ProposeGasPrice)
            max_gas_threshold = 1.0
            if gas_price_num < max_gas_threshold:
                print("Low gas fee detected! Ready to transact.")

        except requests.exceptions.RequestException as e:
            print(f"Connection or HTTP error: {e}")

        print("-" * 40)
        time.sleep(15)

except KeyboardInterrupt:
    print("\nPolling stopped safely by user.")


