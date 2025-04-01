# Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

# ================================================================

import random

# ANSI Formatting Codes
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
GREEN = "\033[1;32m" 
RED = "\033[1;31m"


# Constants
N_NUMBERS = 11  # Number of random numbers to generate
MIN_VALUE = 1   # Minimum value
MAX_VALUE = 100 # Maximum value

def main():
    print(f"\n\t\t\t{BOLD}{CYAN}Generating 10 random numbers between {MIN_VALUE} and {MAX_VALUE}:{RESET}\n")

    # Generate and print 10 random numbers in the range 1 to 100
    for numbers in range(1,N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"\t{GREEN}{numbers}{CYAN}==>{RED}{ITALIC}{value}{RESET}", end=" ") 

    print("\n")  
if __name__ == '__main__':
    main()

# ==============================================================