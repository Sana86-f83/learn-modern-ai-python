import random

# Function to play one round of the game
def play_round():
    # Generate random numbers between 1 and 100
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Display the user's number (computer's number is hidden)
    print(f"Your number: {user_number}")
    
    # Ask for the user's guess
    guess = input("Do you think your number is higher or lower than the computer's number? (Enter 'higher' or 'lower'): ").lower()
    
    # Check if the guess is correct
    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You guessed correctly! Computer's number was: {computer_number}")
        return 1  # Player scores a point
    else:
        print(f"You guessed wrong. Computer's number was: {computer_number}")
        return 0  # No point

# Main function to start the game
def main():
    rounds = 5  # Set number of rounds
    score = 0   # Initialize score
    
    # Play multiple rounds
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        score += play_round()
    
    # Print final score
    print(f"\nGame Over! Your final score: {score}/{rounds}")

if __name__ == "__main__":
    main()
