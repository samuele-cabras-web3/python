# GAS FEE TRACKER

Developed by samuele-cabras-web3

A terminal-based Ethereum gas fee tracker that monitors real-time network transaction costs using the Etherscan V2 API and alerts when fees drop below a target threshold.

## Features

* **Real-Time Etherscan V2 Integration:** Connects to the Etherscan V2 Gas Oracle endpoint using the `requests` library to fetch live Safe, Proposed, and Fast gas prices (in Gwei) on Ethereum Mainnet.
* **Automated Threshold Alerts:** Parses the proposed gas price into a floating-point value and notifies the user whenever fees drop below the configured threshold (`1.0` Gwei).
* **Secure API Key Management:** Uses `python-dotenv` and `os.getenv` to load the `GasTracker` API key securely from a local `.env` file, raising a `ValueError` if missing.
* **Continuous Polling Loop:** Runs an automated `while True` loop with a 15-second interval (`time.sleep(15)`) to keep gas data continuously updated.
* **Graceful Error & Exit Handling:** Uses `try-except` blocks, request timeouts, HTTP status validation (`raise_for_status`), and `KeyboardInterrupt` handling to prevent crashes and allow safe termination via `Ctrl+C`.

## Technologies Used

* Python 3.15
* `requests` library (for HTTP API calls)
* `python-dotenv` library (for loading environment variables)
* Core concepts used: REST APIs, JSON parsing, environment variables, type hinting, functions, `while` loops, `try-except` error handling, and f-strings.

## How to Run It

1. Make sure you have Python installed on your computer.
2. Download the `tracker.py` and `requirements.txt` files into the same folder.
3. Create a `.env` file in the same folder and add your Etherscan API key:

```env
GasTracker=your_etherscan_api_key_here
```

4. Open your terminal in that folder and install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

5. Run the tracker with the following command:

```bash
python tracker.py
```

*Note: `pip` is included with standard Python installations. If `pip` is missing on your system, you can enable it by running `python -m ensurepip --upgrade` in your terminal.*
