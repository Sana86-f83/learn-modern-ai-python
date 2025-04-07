# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def main():

    try:
        number = random.randint(0, 99)
        guess = int(input(f"\n\t\t{CYAN}{BOLD}I'm thinking of a number between 0 and 99... Enter your guess: {RESET}"))

        while guess != number:
            if guess > number:
                print(f"\t\t\t{YELLOW}{BOLD}Your guess is too high.{RESET}")
            elif guess < number:
                print(f"\t\t\t{GREEN}{BOLD}Your guess is too low.{RESET}")

            guess = int(input(f"\t\t{CYAN}{BOLD}Enter a new number: {RESET}"))

        print(f"\n\t\t\t\t{GREEN}{BOLD}🎉 Congrats! The number was: {number}{RESET}\n")
    except ValueError:
        print(f"\n\t\t\t{RED}❌ Please enter a valid number only!{RESET}\n")
        
if __name__ == "__main__":
    main()
