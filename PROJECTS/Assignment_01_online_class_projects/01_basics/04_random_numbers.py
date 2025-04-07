# Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)
import random

# ANSI color codes for styling
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers in the range 1 to 100
    print(f"\n\t\t\t{CYAN}Random Numbers between {MIN_VALUE} and {MAX_VALUE}:{RESET}\n")


    for _ in range(N_NUMBERS):
        # Printing numbers in GREEN color
        print(f"\t{GREEN}{random.randint(MIN_VALUE, MAX_VALUE)}{RESET}", end=' ')
    print("\n")

if __name__ == "__main__":
    main()
