# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing 
# the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# ============Start Program=============================
# ✅Solution:

# ANSI color codes
BOLD = "\033[1m"  # Bold
ITALIC = "\033[3m"  # Italic
RESET = "\033[0m"  # Reset formatting
BLUE = "\033[1;34m"  # Bold Blue
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
RED = "\033[1;31m"  # Bold Red


def main():
    # Get the numbers we want to divide
    dividend: int = int(input(f"\n\t\t{BLUE}{BOLD}{ITALIC}🔹 Please enter an integer to be divided: {RESET}"))
    divisor: int = int(input(f"\t\t{YELLOW}{BOLD}{ITALIC}🔹 Please enter an integer to divide by: {RESET}"))

    if divisor == 0:
        print(f"\n\t\t{RED}{BOLD}{ITALIC}❌ Error: Division by zero is not allowed!{RESET}\n")
        return  

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)

    print(f"\n\t\t\t{BOLD}{GREEN}{ITALIC}✔ The result of this division is {quotient} with a remainder of {remainder}{RESET}\n")

if __name__ == '__main__':
    main()


# ============= End Program ==================================

