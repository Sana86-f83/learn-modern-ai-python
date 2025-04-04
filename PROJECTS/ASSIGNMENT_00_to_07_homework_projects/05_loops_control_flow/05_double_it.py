# ANSI Color Codes for styling (optional)
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

def main():
    print(f"{BOLD}{CYAN}\n\t\t\t🔢 Double Until 100 Program\n{RESET}")

    # User input
    user_input = int(input(f"\t\t\t{YELLOW}Enter a number: {RESET}"))
    curr_value = user_input * 2  # Pehla double

    # Print the first doubled value
    print(f"\n\t\t\t{GREEN}Doubled values:{RESET}", end=" ")

    # Loop until value >= 100
    while curr_value < 100:
        print(f"{curr_value}", end=" ")
        curr_value = curr_value * 2  # Double again

    # Print the final value which is >= 100
    print(f"\n\n\t\t\t{BOLD}{CYAN}Final value ==> {GREEN}{curr_value}{RESET}\n")  # This will be >= 100

if __name__ == "__main__":
    main()
