# Problem Statement
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!
# ============================================================================

# ANSI Color Codes
import random


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

def main():
    correct_affirmation = [ "I believe in myself and my abilities.",

"I am strong, confident, and resilient.",

"I can overcome any challenge that comes my way.",

"I deserve happiness, success, and love.",

"Every day, in every way, I am getting better and better.",

"My potential is limitless.",

"I am focused, persistent, and will never give up.",

"I choose to be positive and grateful today.",

"I have the power to create the life I want.",

"I am enough just as I am.",

]
    
    choice = random.choice(correct_affirmation)
    print(f"\n\t\t\t\t\t{BOLD}{GREEN} 'Positive Mindset Trainer'{RESET}")

    while True:
        print(f"\n\t\t\t{BOLD}{CYAN}Please type the following affirmation exactly as shown:{RESET}\n\t\t\t\t{YELLOW}{choice}{RESET}")
        user_input = input("\n\t\t\t\t > ")

        if user_input == choice:
            print(f"\n\t\t\t\t\t{GREEN}{BOLD}That's right! :){RESET}\n")
            break
        else:
            print(f"\t\t\t\t\t{RED}Hmmm That was not the affirmation. Please try again.\n{RESET}")

if __name__ == "__main__":
    main()
