# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']

# ANSI color codes for formatting
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
MAGENTA = "\033[35m"  # Magenta
UNDERLINE = "\033[4m"  # Underline


# =============Start Program================================

# ✅SOLUTION:

def main():
    lst = []  # Make an empty list to store things in
    print(f"{MAGENTA}{UNDERLINE}{BOLD}{ITALIC}\n\t\t\t\t\t Welcome to the List Entry Program!{RESET}\n")

    val = input(f"\n\t\t\t\t{BOLD}{GREEN}{ITALIC}Enter a value: {BLUE}")  # Get an initial value
    print(RESET, end="")  # Reset color after input

    while val != "":  # While the user input isn't an empty value
        lst.append(val)  # Add val to list
        val = input(f"\n\t\t\t\t{BOLD}{ITALIC}{GREEN}Enter a next value: {BLUE}")  # Get the next value to add
        print(RESET, end="")  # Reset color after input


    # Convert list elements to Blue color
    colored_list = ", ".join(f"{BLUE}{BOLD}{ITALIC}{item}{RESET}" for item in lst)

    # Print the final list
    print(f"\n\t\t\t\t\t{BOLD}{YELLOW}{ITALIC}Here's the list: {colored_list}{RESET}\n")



if __name__ == '__main__':
    main()

# ==================Program End========================