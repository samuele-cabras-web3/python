import requests

# Alias map to improve user experience with short inputs or synonyms
CATEGORY_ALIASES = {
    "all": "Any",
    "random": "Any",
    "prog": "Programming",
    "code": "Programming",
    "coding": "Programming",
    "dev": "Programming",
    "misc": "Misc",
    "other": "Misc",
    "pun": "Pun",
    "puns": "Pun",
    "wordplay": "Pun",
    "spooky": "Spooky",
    "scary": "Spooky",
    "halloween": "Spooky",
    "xmas": "Christmas",
    "christmas": "Christmas",
}

VALID_CATEGORIES = ["Any", "Programming", "Pun", "Misc", "Spooky", "Christmas"]



def get_joke(category: str) -> tuple[str, str | None] | None:
    """Fetches a random joke from JokeAPI based on the selected category."""
    url = f"https://v2.jokeapi.dev/joke/{category}?safe-mode"

    try:
        # Request handling with timeout to prevent hanging
        response = requests.get(url, timeout=10)

        # Handle JokeAPI rate limiting
        if response.status_code == 429:
            print("Too many requests. Please wait a moment and try again.")
            return None

        response.raise_for_status()
        data = response.json()

        # API-level error check (e.g., invalid category)
        if data.get("error"):
            print(f"Could not find category '{category}'. Please choose from the listed categories.")
            return None

        # Extract joke based on its structure ('single' vs 'twopart')
        joke_type = data.get("type")
        if joke_type == "single":
            return data.get("joke", None)
        elif joke_type == "twopart":
            return data.get("setup", ""), data.get("delivery", "")

        return None

    except (requests.exceptions.RequestException, ValueError) as e:
        # Error handling for connection drops, DNS failures, or HTTP errors
        print(f"Network error: {e}")
        return None

def main() -> None:
    print("--- RANDOM JOKE GENERATOR ---")
    print("Categories: any, programming, pun, misc, spooky, christmas")
    print("Type a category or 'exit' to quit.")

    # Main application loop
    while True:
        user_input = input("\nChoose a category (press Enter for 'any'): ").lower().strip()

        # Exit condition
        if user_input == "exit":
            print("Closing joke generator. Goodbye!")
            break

        # Default to 'Any' if the user just presses Enter
        if not user_input:
            user_input = "any"

        # Normalize input using aliases, fall back to capitalized user input
        category = CATEGORY_ALIASES.get(user_input, user_input.capitalize())

        if category not in VALID_CATEGORIES:
            print(f"`{category}` is not a valid category. Please choose from the list above.")
            continue
        
        print(f"Fetching a '{category}' joke...")
        result = get_joke(category)

        # Output formatting
        if result:
            setup, delivery = result
            print(f"\n> {setup}")
            if delivery:
                print(f"> {delivery}")


# Entry point guard
if __name__ == "__main__":
    main()
