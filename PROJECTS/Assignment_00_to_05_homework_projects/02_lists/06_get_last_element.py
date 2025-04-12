# roblem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# ANSI color codes
BOLD = "\033[1m"  # Bold
UNDERLINE = "\033[4m"  # Underline
RESET = "\033[0m"  # Reset formatting
BLACK = "\033[30m"  # Black
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
RED = "\033[1;31m"  # Bold Red
ITALIC = "\033[3m"  # Italic text
CYAN = "\033[1;36m"   # Bold Cyan
BGRED = "\033[41m"  # Background Red
MAGENTA = "\033[35m"  # Magenta


# ============= Start Program ================

def get_first_element(lst):
    """Prints the Last element of the list if it's not empty."""
    if lst:
        print(f"\n\t\t\t{GREEN}{BOLD}{ITALIC}📌 Get Last element: {lst[-1]}{RESET}")
    else:
        print(f"\n\t\t\t\t\t{RED}The list is empty.{RESET}")

def get_lst():
    """Takes multiple inputs from the user and returns a list."""
    lst = []
    while True:
        elem = input(f"\t\t\t\t{CYAN}{ITALIC}💥 Enter an element (or press enter to stop): {RESET}")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    print(f"{MAGENTA}{UNDERLINE}{BOLD}{ITALIC}\n\t\t\t\t\tWelcome to the List Input Program!{RESET}")
    print(f"{YELLOW}{UNDERLINE}{BOLD}{ITALIC}\n\t\t\t\t\t\t✅ Access Last Element Program !{RESET}\n")
    lst = get_lst()
    print(f"\n\t\t\t\t\t\t{MAGENTA}{UNDERLINE}{BOLD}{ITALIC}📃 List of elements --> {lst}")
    get_first_element(lst)
    print(f"\n{BGRED}{BLACK}{ITALIC}\t\t\t\t\t\t🌟 Program execution completed!🌟   {RESET}\n")

if __name__ == "__main__":
    main()

# ================= Program End =================
