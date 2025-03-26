# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

# =============Start Program==================================

# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
RED = "\033[1;31m"  # Bold Red
BLUE = "\033[1;34m"  # Bold Blue
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
PURPLE = "\033[1;35m"  # Bold Purple
UNDERLINE = "\033[4m"  # Underline

# Enhanced Sentence Starter
SENTENCE_START: str = (
    f"{BOLD_ITALIC}{BLUE}Panaversity is fun! 🚀 "
    f"I learned to code, explored new ideas, and used Python to create my {RESET}"
)  

def main():
    # Get user inputs with colored prompts
    adjective: str = input(f"\n\t\t{GREEN}Please type an adjective and press enter: {RESET}")
    noun: str = input(f"\t\t{YELLOW}Please type a noun and press enter: {RESET}")
    verb: str = input(f"\t\t{RED}Please type a verb and press enter: {RESET}")

    # Display the completed sentence with colors
    print(f"\n\t\t{SENTENCE_START}{BOLD_ITALIC}{UNDERLINE}{PURPLE}{adjective} {noun} {verb}!{RESET}\n")

# Function call;
if __name__ == '__main__':
    main()

# ====================Program End=========================  










