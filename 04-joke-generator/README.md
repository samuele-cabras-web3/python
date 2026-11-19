# JOKE GENERATOR
Developed by samuele-cabras-web3

A terminal-based joke generator that fetches jokes by user-selected category or randomly across multiple categories using the JokeAPI.

## Features
- **Real-Time API Integration:** Connects to the JokeAPI Rest endpoint using the `requests` library to retrieve single and two-part jokes with safe-mode filtering enabled. 

- **Smart Input Normalization & Aliases:** Supports common category shortcuts (e.g., `prog`, `code`, `xmas`) via a dictionary mapping, defaults to `Any` on empty input, and validates entries against allowed categories .

- **Dynamic Joke Formatting:** Automatically detects the joke structure (`single` vs. `twopart`) to cleanly separate and display the setup and punchline.

- **Robust Error & Limit Handling:** Uses `try-except` blocks, requests timeouts, and HTTP status checks (`429`) to prevent crashes from network drops, invalid categories, or API rate limits.

- **Interactive CLI Loop:** Runs on a continuous `while` loop allowing users to generate multiple jokes sequentially until typing `exit`.

## Technologies Used
  - **Python 3.15**

  - `requests` library (for HTTP API calls)

  - Core concepts used: **Rest APIs**, JSON parsing, dictionaries, functions, type hinting, `while` loops, `try-except` error handling, and f-strings.

   ## How to Run It
  1. Make sure you have Python installed on your computer.
 
  2. Download the `joke.py` and `requirements.txt` files into the same folder.
 
  3. Open your terminal in that folder and install the required dependency:
 ```bash
 python -m pip install -r requirements.txt
 ```

  4. Run the generator with the following command:
 ```bash
 python joke.py
 ```
>**Note:**`pip` is included with standard Python installations. If `pip` is missing on your system, you can enable it by running `python -m ensurepip --upgrade` in your terminal
