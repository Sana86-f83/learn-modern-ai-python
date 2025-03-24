
# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

# ==============Start Program======================

# ANSI escape codes for bold and italic
BOLD_ITALIC = "\033[1;3m"   # Bold & Italic
GREEN = "\033[92m"          # Green color for results
RESET = "\033[0m"           # Reset formatting
BLUE = "\033[34m"

# ✅ Solution
def main():
  
    # Asking the user for their favorite animal
    animal = input(f"\n\t\t{BLUE}{BOLD_ITALIC} What's your favourite animal? ")

    # Responding with the user's favorite animal
    print(f"\n\t\t{GREEN} My favorite animal is also {BOLD_ITALIC}{animal}{RESET} !\n ")

# This calls the main function
if __name__ == "__main__":
    main()    

# ============Program end===========================