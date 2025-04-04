# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

# ANSI color codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"


def main():
    print(f"\n\t\t\t\t{BOLD}{CYAN}-------------------------------------------")
    print(f"\t\t\t\t🎯 {BOLD}Welcome to the 'Guess My Number' Game! 🎯")
    print(f"\t\t\t\t-------------------------------------------{RESET}\n")
    
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    while True:
        try:
            guess = int(input(f"\t\t\t\t{BOLD}{YELLOW}Enter your guess (0-99): {RESET}"))
            
            if guess < 0 or guess > 99:
                print(f"\t\t\t\t{RED} ⚠️  Please enter a number between 0 and 99!{RESET}\n")
                continue
            
            if guess > secret_number:
                print(f"\t\t\t\t{CYAN}📉 Your guess is too high! Try again.{RESET}\n")
            elif guess < secret_number:
                print(f"\t\t\t\t{GREEN}📈 Your guess is too low! Try again.{RESET}\n")
            else:
                print(f"\t\t\t\t{GREEN}{BOLD}🎉 Congrats! The number was: {secret_number} 🎉{RESET}\n")
                break
        except ValueError:
            print(f"\t\t\t\t{RED}⚠️  Invalid input! Please enter a valid number.{RESET}\n")

if __name__ == "__main__":
    main()