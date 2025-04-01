# Problem Statement
# Write a program that prints the first 20 even numbers using a loop.
# The first even number is 0.
# Output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# ANSI color codes
BOLD = "\033[1m"   # Bold text
GREEN = "\033[1;32m" # Bold Green
RESET = "\033[0m"   # Reset text color
MAGENTA = "\033[35m"


def main():
    print(f"\n\t\t\t{BOLD}{GREEN}First 20 Even Numbers:{RESET}\n")
    for i in range(20):
        print(f"{MAGENTA}{i * 2}{RESET}", end=" ")
    print()  # New line after printing all numbers


if __name__ == '__main__':
    main()