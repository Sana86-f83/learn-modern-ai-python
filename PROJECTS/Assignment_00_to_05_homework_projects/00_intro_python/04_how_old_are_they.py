# Problem Statement
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. 
# The autograder is sensitive to capitalization and punctuation, be careful! 
# Your solution should look like this 
# (the below numbers are made up -- your solution should have the correct values!):

# =================== Start Program =====================

# ANSI escape codes for colors & formatting
BOLD_ITALIC = "\033[1;3m"   # Bold & Italic
GREEN = "\033[92m"          # Green color for results
CYAN = "\033[96m"           # Cyan color for labels
RESET = "\033[0m"           # Reset formatting

# ✅ Solution
def main():
    # Defining the ages of Anton, Beth, Chen, Drew, and Ethan
    anton: int = 21
    beth: int = anton + 6
    chen: int = beth + 20
    drew: int = chen + anton
    ethan: int = chen

    # Printing the names and ages with formatting
    print(f"\n\t\t{CYAN}{BOLD_ITALIC}Anton age is {GREEN}{anton}{RESET}")
    print(f"\t\t{CYAN}{BOLD_ITALIC}Beth age is {GREEN}{beth}{RESET}")
    print(f"\t\t{CYAN}{BOLD_ITALIC}Chen age is {GREEN}{chen}{RESET}")
    print(f"\t\t{CYAN}{BOLD_ITALIC}Drew age is {GREEN}{drew}{RESET}")
    print(f"\t\t{CYAN}{BOLD_ITALIC}Ethan age is {GREEN}{ethan}{RESET}\n")

# Calling the main function
if __name__ == "__main__":
    main()

# ============ Program End ==========================
