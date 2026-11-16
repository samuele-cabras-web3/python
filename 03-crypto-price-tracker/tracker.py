import requests

# Alias map to improve user experience with common tickers
COIN_ALIASES = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana",
    "ada": "cardano",
    "xrp": "ripple",
    "doge": "dogecoin",
    "bnb": "binancecoin",
    "usdt": "tether",
}


def get_crypto_price(coin_id: str) -> tuple[float, float | None] | None:
    """Fetches the current price and 24h change of a cryptocurrency from CoinGeko."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_24hr_change": "true",
    }

    try:
        # Request handling with timeout to prevent hanging
        response = requests.get(url, params=params, timeout=10)

        # Handle CoinGecko free tier rate limiting
        if response.status_code == 429:
            print("Too many requests. Please wait a moment and try again.")
            return None

        response.raise_for_status()
        data = response.json()

        # Data validation: check if the coin exists in the JSON payload
        if coin_id in data:
            price = data[coin_id].get("usd")
            change_24h = data[coin_id].get("usd_24h_change")
           
            if price is not None:
                return price, change_24h

        print(f"Could not find data for '{coin_id}'. Make sure you used the full name(e.g., 'bitcoin').")    

    except requests.exceptions.RequestException as e:
        # Error handling for connection drops, DNS failures, or HTTP errors
        print(f"Network error: {e}")
        return None


def main() -> None:
    print("--- LIVE CRYPTO PRICE TRACKER ---")
    print("Type a coin name (e.g., bitcoin, ethereum, solana)) or 'exit' to quit.")

    # Main application loop
    while True:
        user_input = input("\nEnter cryptocurrency name: ").lower().strip()

        # Exit condition
        if user_input == "exit":
            print("Closing tracker. Goodbye!")
            break

        # Input sanitization skip empty strings
        if not user_input:
            print("Please enter a valid name.")
            continue

        # Normalize spaces to hiphens (e.g., "shiba inu" -> "shiba-inu")
        normalized_input = user_input.replace(" ", "-")
        coin = COIN_ALIASES.get(normalized_input, normalized_input)

        print(f"Fetching data for {coin}...")
        result = get_crypto_price(coin)

        # Output formatting
        if result:
            price, change = result
            price_str = f"${price:,.2f}" if price >= 1 else f"${price:,.6f}"
            print(f"Price: {price_str} USD")

            # Handle cases where 24h change might be missing for new coins
            if change is not None:
                print(f"24h Change: {change:+.2f}%")
            else:
                print("24h Change: N/A")
        
# Entry point guard
if __name__ == "__main__":
    main()
