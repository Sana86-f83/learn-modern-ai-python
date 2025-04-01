# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)
# 🚀 \033[1;4mMinimum Height Ride Checker\033[0m 🎢

# ANSI Formatting Codes
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
MAGENTA = "\033[35m"
CYAN = "\033[96m"



# Define Minimum Height
MINIMUM_HEIGHT: int = 50  # Arbitrary units (e.g., inches or cm)

def main():
    print(f"\n\t\t\t\t{BOLD}{MAGENTA}🚀 Ride Eligibility Checker: Are You Tall Enough to Ride? 🎢")

    # Prompt User for Height
    height = float(input(f"\n\t\t\t\t\t{YELLOW}{BOLD}How tall are you? {RESET}"))


    # Check Height Against Minimum Requirement
    if height >= MINIMUM_HEIGHT:
        print(f"\n\t\t\t\t\t\t\t{GREEN}{BOLD}You're tall enough to ride! 🎉{RESET}\n")
    else:
        print(f"\n\t\t\t\t\t\t{RED}{ITALIC}{BOLD}You're not tall enough to ride, but maybe next year! ⏳{RESET}\n")

# Ensuring Main Execution
if __name__ == '__main__':
    main()
