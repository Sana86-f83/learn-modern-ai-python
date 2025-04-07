# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

# Note that:

# 2 doubled is 4

# 4 doubled is 8

# 8 doubled is 16

# and so on.

# We stop at 128 because that value is greater than 100.

# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

# while curr_value < 100


# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"

def main():
    print(f"\n\t\t\t{CYAN}{BOLD}⚡ Double Value Program ⚡{RESET}\n")

    # Get input from the user
    user_input = input(f"\t\t{YELLOW}Please enter a number: {RESET}")
    
    try:
        # Convert the input to an integer
        curr_value = int(user_input)
        
        # Double the initial value
        curr_value *= 2
        
        print(f"\n\t\t\t{GREEN}{BOLD}Doubled values:{RESET}", end=" ")

        # Keep doubling and printing until value is 100 or more
        while curr_value < 100:
            print(f"{CYAN}{curr_value}{RESET}", end=" ", flush=True)
            curr_value *= 2  # Double the value

        # Print the last value which is >= 100
        print(f"\n\n\t\t\t\t{GREEN}{BOLD}Last Value ==> {CYAN}{curr_value}{RESET}\n")
    
    except ValueError:
        print(f"\n\t\t\t{RED}❌ Please enter a valid number only!{RESET}\n")

if __name__ == "__main__":
    main()
