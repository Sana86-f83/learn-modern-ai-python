# Problem Statement
# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

# In the Gregorian calendar, three criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."

# ===========================================================================
def main():
    # ANSI color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    MAGENTA = "\033[35m"



    print(f"\n\t\t\t\t{BOLD}{MAGENTA}{UNDERLINE}{ITALIC}Leap Year Checker: Determine if a Year is a Leap Year or Not{RESET}")
    # Get the year to check from the user
    year = int(input(f'\n\t\t\t\t\t\t{CYAN}{BOLD}{ITALIC}Please input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisible by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisible by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisible by 400
                print(f"\n\t\t\t\t\t\t\t{GREEN}{BOLD}{ITALIC}That's a leap year!{RESET}\n")
            else:  # (Not divisible by 400)
                print(f"\n\t\t\t\t\t\t\t{RED}{BOLD}{ITALIC}That's not a leap year.{RESET}\n")
        else:  # (Not divisible by 100)
            print(f"\n\t\t\t\t\t\t\t{GREEN}{BOLD}{ITALIC}That's a leap year!{RESET}\n")
    else:  # (Not divisible by 4)
        print(f"\n\t\t\t\t\t\t\t{RED}{BOLD}{ITALIC}That's not a leap year.{RESET}\n")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

# =================================================================