# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# ANSI color codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

# Number of even numbers to print
NUM_EVEN_NUMBERS = 20

def main():
    """
    Prints the first 20 even numbers in a formatted way.
    """
    print(f"\n\t\t\t{BOLD}{CYAN}--------------------------------------")
    print(f"\t\t\t        🔢 First {NUM_EVEN_NUMBERS} Even Numbers 🔢")
    print(f"\t\t\t--------------------------------------{RESET}\n")

    for i in range(NUM_EVEN_NUMBERS):
        print(f"{GREEN}{i * 2}{RESET}", end=" ")

    print(f"\n\n\t\t{BOLD}{YELLOW}✅ Successfully printed {NUM_EVEN_NUMBERS} even numbers!{RESET}\n")

if __name__ == '__main__':
    main()
