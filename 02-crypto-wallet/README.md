# Bitcoin Wallet Simulator

**Developed by samuele-cabras-web3**

A terminal-based cryptocurrency wallet simulator that allows users to manage a virtual Bitcoin balance.

## Features
- **Input Validation & Error Handling:** Uses a dedicated helper function with `try-except` blocks to prevent crashes from invalid inputs or negative numbers.

- **Balance Management:** Start with an Initial balace of `100.0 BTC` and updates it in real time after every transaction.

- **Simulated Transaction:** Allows sending BTC to a recipient address or username while automatically checking for sufficent funds.

- **Interactive CLI Menu:** Runs on a continuous `while` loop until the user chooses to exit.

## Technologies Used
- **Python 3.15**
- Core concepts used: functions, type hinting, `while` loops, `try-except` error handling, conditional statements, and f-strings.

## How to Run It
1. Make sure you have Python installed on your computer.
2. Download the `crypto.wallet.py` file.
3. Open your terminal in the folder containing the file and run the following command:
   ```bash
   python crypto.wallet.py
   ```
   
