import random

def high_low_game(rounds):
    score = 0

    print("🎮 Welcome to the High-Low Game!")
    print("You will see your number and guess whether it's higher or lower than the computer's number.")
    print("Let's start!\n")

    for round_number in range(1, rounds + 1):
        print(f"--- Round {round_number} ---")

        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {your_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()

        if guess not in ["higher", "lower"]:
            print("Invalid input! Please enter 'higher' or 'lower'. No points this round.\n")
            continue

        if (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
            print("✅ Correct! You get a point.")
            score += 1
        else:
            print("❌ Wrong guess.")

        print(f"The computer's number was: {computer_number}\n")

    print(f"🏁 Game Over! Your total score: {score}/{rounds}")

# Start the game with 5 rounds
high_low_game(5)
