# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.


# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"


print(f"{BLUE}{BOLD}{ITALIC}\n\t\t\t📖 Simple Phonebook App' Store, view, and search contacts easily!' ☎️{RESET}")

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input(YELLOW + "\n\t\t\tEnter a Name here: " + RESET)
        if name == "":
            break
        number = input(GREEN + "\t\t\t\tNumber: " + RESET)
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\n" + BLUE + "\t\t\t\t📖 Phonebook Entries:" + RESET)
    for name in phonebook:
        print(f"\n\t\t\t\t\t{YELLOW}{name} -> {GREEN}{phonebook[name]}{RESET}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input(MAGENTA + "\n\t\t\t\tEnter name to lookup: " + RESET)
        if name == "":
            break
        if name not in phonebook:
            print(RED + f"\n\t\t\t\t\t\t❌ {name} is not in the phonebook" + RESET)
        else:
            print(GREEN + f"\n\t\t\t\t\t✅ {name}'s number: {phonebook[name]}" + RESET)

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
