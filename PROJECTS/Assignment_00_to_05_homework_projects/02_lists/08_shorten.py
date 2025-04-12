# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


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
BLUE = "\033[34m"
CYAN = "\033[36m"

# =============Start Program================================

# ✅SOLUTION:
MAX_LENGTH: int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"\t\t\t\t\t{BOLD}{ITALIC}{CYAN}Removing element: {last_elem}{RESET}")


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    print(f"\n\t\t\t\t\t{BOLD}{BGRED}{ITALIC}🌟 Welcome to the List Creator!🌟{RESET}\n")
    elem = input(f"\t\t\t{BOLD}{GREEN}{ITALIC}Enter an element of the list (Press Enter to stop): {BLUE}")
    print(RESET, end="")  # Reset color after input
    
    while elem != "":
        lst.append(elem)
        elem = input(f"\t\t\t{BOLD}{ITALIC}{GREEN}Enter the next element: {BLUE}")
        print(RESET, end="")  # Reset color after input
    
    return lst


def main():
    lst = get_lst()
    # Convert list elements to red color
    colored_list = ", ".join(f"{RED}{BOLD}{ITALIC}{item}{RESET}" for item in lst)
    print(f"\n\t\t{BOLD}{UNDERLINE}{ITALIC}{MAGENTA}Your original list:{RESET} {colored_list}\n")
    shorten(lst)
    colored_list2 = ", ".join(f"{RED}{BOLD}{ITALIC}{item}{RESET}" for item in lst)
    print(f"\n\t\t\t{UNDERLINE}{BOLD}{YELLOW}{ITALIC}Final list after shortening:{RESET} {colored_list2}\n")


if __name__ == '__main__':
    main()

# ==================Program End========================