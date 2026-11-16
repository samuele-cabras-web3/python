# Initial virtual wallet balance
INITIAL_BALANCE = 100.0


# Helper function to prevent crashes if the user not enter a valid number
def get_amount(prompt: str) -> float:
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("The amount must be greater than zero. Please try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input! PLease enter a valid number")


def main():
    balance = INITIAL_BALANCE

    # This loops runs forever until the user chooses to exit (option 4)
    while True:
        print("\n--- BITCOIN WALLET SIMULATOR ---")
        print("1. Check Balance")
        print("2. Deposit Bitcoin")
        print("3. Send Bitcoin")
        print("4. Exit")

        # Get user choice
        choice = input("Choose an option (1-4): ").strip()

        # Option 1: View current balance
        if choice == "1":
            print(f"Your current balance is: {balance} BTC")

        # Option 2: Add tokens to the wallet
        elif choice == "2":
            amount = get_amount("Enter amount to deposit: ")
            balance += amount
            print(f"Successfully deposited: {amount} BTC!")

        # Option 3: Send tokens to another user
        elif choice == "3":
            recipient = input("Enter recipient address or username: ")
            amount = get_amount("Enter amount to send: ")

            # Check if the user have enough tokens in their balance
            if amount <= balance:
                balance -= amount
                print(f"Successfully sent {amount} BTC to {recipient}!")
            else:
                print("Transaction failed: Insufficient funds!")

        # Option 4: Close the application
        elif choice == "4":
            print("\nClosing your wallet. Goodbye!")
            break  # This breaks the while loop and end the program

        else:
            print("Invalid option! Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
