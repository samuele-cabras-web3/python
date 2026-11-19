# LIVE CRYPTO PRICE TRACKER
Developed by samuele-cabras-web3

A terminal-based cryptocurrency price tracker that fetches real-time market prices and 24-hour percentage changes using the CoinGecko API.

## Features
- **Real-Time API Integration:** Connects to the CoinGecko Rest API using the `requests` library to retrieve live USD prices and 24h market variations.

- **Smart Input Normalization & Aliases:** Supports common ticker shortcuts (e.g., `btc`, `eth`, `sol`) via a dictionary mapping and automatically formats multi-word names (e.g., `shiba inu` to `shiba-inu`).

- **Dynamic Price Formatting:** Displays prices with two decimal places for values `$1` and above, and six decimal places for values under `$1`.

- **Robust Error & Rate-Limit Handling:** Uses `try-except` blocks, requests timeouts, and HTTP status checks (`429`) to prevent crashes from network drops, invalid coin names, or API rate limits.

- **Interactive CLI Loop:** Runs on a continuous `while` loop allowing users to check multiple cryptocurrencies sequentially until typing `exit`.

## Technologies Used
  - **Python 3.15**

  - `requests` library (for HTTP API calls)

  - Core concepts used: **Rest APIs**, JSON parsing, dictionaries, functions, type hinting, `while` loops, `try-except` error handling, and f-strings.

   ## How to Run It
  1. Make sure you have Python installed on your computer.
 
  2. Download the `tracker.py` and `requirements.txt` files into the same folder.
 
  3. Open your terminal in that folder and install the required dependency:
 ```bash
 python -m pip install -r requirements.txt
 ```

  4. Run the tracker with the following command:
 ```bash
 python tracker.py
 ```
>**Note:**`pip` is included with standard Python installations. If `pip` is missing on your system, you can enable it by running `python -m ensurepip --upgrade` in your terminal
