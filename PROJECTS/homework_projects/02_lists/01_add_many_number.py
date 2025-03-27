# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

# ANSI color codes
BOLD = "\033[1m"  # Bold
UNDERLINE = "\033[4m"  # Underline
RESET = "\033[0m"  # Reset formatting
BLACK = "\033[30m"  # BG BLACK
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
RED = "\033[1;31m"  # Bold Red
ITALIC = "\033[3m"  # Italic text
BGRED = "\033[41m"  #BG RED
MAGENTA	="\033[35m"

# =============Start Program================================

# ✅SOLUTION:
def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers
    """
    total_so_far: int = 0  # Initialize value to start from 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    print(f"\n\t\t\t\t{BOLD}{UNDERLINE}{BGRED}{ITALIC}🌟 Welcome to the Number Adder!{RESET}\n")

    user_input: str = input(f"\t\t\t{YELLOW}{ITALIC} 👉 Enter a list of numbers separated by spaces: {RESET}")
    
    try:
        number_list: list[int] = list(map(int, user_input.split()))  # Convert input to a list of integers
        print(f"\n\t\t\t{BOLD}{GREEN}{ITALIC}✅ You entered the numbers:{RESET} {number_list}\n")

        sum_of_numbers: int = add_many_numbers(number_list)

        print(f"\t\t\t\t\t{BOLD}{UNDERLINE}{MAGENTA}{ITALIC}🧮 ✔ The total sum is : {RESET} {sum_of_numbers}\n")
    
    except ValueError:
        print(f"\n\t\t\t{RED}{BOLD}{ITALIC}❌ Error: Please enter valid numbers separated by spaces!{RESET}\n")

if __name__ == "__main__":
    main()

# ==================Program End========================