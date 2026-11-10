<<<<<<< HEAD

=======
# Quiz data storage
QUIZ_DATA = [
    {
        "question": "Question 1: Is the blockchain centralized or decentralized?\n",
        "answer": "decentralized",
    },
    {
        "question": "Question 2: What was the first cryptocurrency ever created?\n",
        "answer": "bitcoin",
    },
    {
        "question": "Question 3: What is an automated program that runs on a blockchain?\n",
        "answer": "smart contract",
    },
]


# Function that runs the quiz logic
def run_quiz():
    # Your initial virtual wallet balance
    token_balance = 0

    # Welcome message
    print("---WELCOME TO THE BLOCKCHAIN QUIZ---")
    print("Answer the questions correctly to earn Tokens!💰")

    # Run the quiz loop
    for item in QUIZ_DATA:
        # Get and clean user input
        user_answer = input(item["question"]).lower().strip()

        # Check answer
        if item["answer"] in user_answer:
            token_balance += 10
            print("Correct!✔️  +10 Tokens 💰\n")
        else:
            print(f"Wrong!❌ The correct answer was: {item['answer']}.\n")

    # Display final result
    print("-" * 50)
    print(f"QUIZ FINISHED! Your final balance is: {token_balance} Tokens 💰")
    print("-" * 50)


# Start the quiz
if __name__ == "__main__":
    run_quiz()
>>>>>>> d9c8bc0c7878ee91a40acf78b5c93529b7731060
