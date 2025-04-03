# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# ================================================================

# ANSI Escape Sequences for Text Formatting
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"


def get_user_numbers():
    """
    Ask the user to input numbers and store them in a list.
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input(f"\t\t\t\t{ITALIC}{BOLD}{YELLOW}Enter a number: {BLUE}")
        print(RESET, end="")  # Reset color after input
        
        # If the user enters a blank line, break out of the loop
        if user_input == "":
            break
        
        # Convert input to integer and add to list
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print(f"\n\t\t\t\t\t\t{BOLD}{ITALIC}{RED}Invalid input! Please enter a valid number.{RESET}")
    
    return user_numbers


def count_nums(num_lst):
    """
    Create a dictionary to count occurrences of numbers.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def print_counts(num_dict):
    """
    Print each number with its occurrence count, formatted in color.
    """
    print(f"\n\t\t\t\t\t\t{BOLD}{ITALIC}{GREEN}=== Number Frequency Count ==={RESET}\n")
    for num, count in num_dict.items():
        print(f"\t\t\t\t\t{ITALIC}{BOLD}{MAGENTA}{num}{RESET}{GREEN} appears {BOLD}{count}{RESET}{BLUE}{BOLD} times.{RESET}")


def main():
    """
    Main function to handle input, processing, and output.
    """
    print(f"\n\t\t\t\t\t{BOLD}{ITALIC}{GREEN}Welcome to the Number Frequency Counter!{RESET}\n")
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)
    print(f"\n\t\t\t\t\t\t{BOLD}{ITALIC}{MAGENTA}Thank you for using the program!{RESET}")


if __name__ == '__main__':
    main()
