# Problem Statement
# Use Python to calculate the number of seconds in a year,
#  and tell the user what the result is in a nice print statement that looks like this 
# (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year,
#  24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# =============Start Program==================================
# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
GREEN = "\033[1;32m"  # Bold Green
UNDERLINE = "\033[4m"  # Underline

# Constant Value:
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # We can get the number of seconds per year by multiplying the handy constants above!
    print(f"\n\t\t\t{BOLD_ITALIC}{GREEN}{UNDERLINE}There are {DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN} seconds in a year!{RESET}\n")



if __name__ == '__main__':
    main()

# ====================Program End=========================
