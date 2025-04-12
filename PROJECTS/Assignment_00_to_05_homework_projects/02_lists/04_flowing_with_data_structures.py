# Problem Statement
# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)


RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"


# =============Start Program================================

def add_many_copies(my_list, add_data):
    print(f"\n\t\t{CYAN}{BOLD}{ITALIC}Starting the loop to add data multiple times...{RESET}")
    for i in range(5):
        my_list.append(add_data)
        print(f"\t\t\t{YELLOW}Iteration {i+1}: {my_list}{RESET}")
    print(f"\t\t\t\t\t\t{CYAN}{BOLD}{ITALIC}Loop execution completed.{RESET}")

def main():
    user = input(f"\n\t\t\t{MAGENTA}{BOLD}{ITALIC}{UNDERLINE}Enter a value to be added multiple times: {RESET}")
    empty_list = []
    print(f"\n\t{GREEN}{BOLD}{ITALIC}Initial List (Empty): {empty_list}{RESET}")
    add_many_copies(empty_list, user)
    print(f"\n\t\t{GREEN}{BOLD}{ITALIC}Final Modified List: {empty_list}{RESET}")
    print(f"\n\t\t\t\t\t{BLUE}{BOLD}{ITALIC}Process completed successfully!{RESET}\n")

if __name__ == "__main__":
    main()

# ==================Program End========================