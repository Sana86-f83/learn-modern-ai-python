# Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.


# """
# Program: add2numbers
# --------------------
# Another python program to get some practice with
# variables.  This program asks the user for two
# integers and prints their sum.
# """

# ================ Start Program ====================

# ANSI escape codes for colors & formatting
BOLD_ITALIC = "\033[1;3m"   # Bold & Italic
GREEN = "\033[92m"          # Green color for results
CYAN = "\033[96m"           # Cyan color for input
RESET = "\033[0m"           # Reset formatting
BLUE = "\033[34m"
YELLOW = "\033[43m"
UNDERLINE = "\033[4m"
BLACK = "\033[30m"

# ✅ Solution
def main():
    print(f"\n\t\t{UNDERLINE}{BOLD_ITALIC}{GREEN}This program adds two numbers.{RESET}\n")

    # User se first number input lena
    num1:str = input(f"\t\t\t{CYAN}{BOLD_ITALIC}Enter first number here... {RESET}")
    num1:int = int(num1)
    
    # User se second number input lena
    num2:str = input(f"\t\t\t{BOLD_ITALIC}{CYAN}Enter second number here... {RESET}")
    num2:int = int(num2)

    # Sum Calculate karna
    total:int = num1 + num2

    # Result Print karna
    print(f" \n\t\t{YELLOW}{BOLD_ITALIC}{BLACK} The sum of {num1} and {num2} is {total}.{RESET}\n ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == "__main__":
    main()  

# ============ Program End ==========================
