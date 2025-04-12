# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
# ============= Start Program ==================================

# Import the random library which lets us simulate random things like dice!
import random

# ANSI color codes
BOLD = "\033[1m"  # Bold
ITALIC = "\033[3m"  # Italic
RESET = "\033[0m"  # Reset formatting
BGRED = "\033[1;41m"  # Bold bgRED
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
BGPURPLE = "\033[1;45m"  # PURPLE

# Number of sides on each die to roll
# CONSTANT VALUE :
NUM_SIDES: int = 6

def main():
    # Roll dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Get their total
    total: int = die1 + die2

    # Print out the results
    print(f"\n\t\t{BOLD}{BGRED}🎲 Dice have {NUM_SIDES} sides each.{RESET}\n")
    print(f"\t\t\t{YELLOW}🎲 First die: {BOLD}{die1}{RESET}")
    print(f"\t\t\t{GREEN}🎲 Second die: {BOLD}{die2}{RESET}")
    print(f"\n\t\t\t\t{BGPURPLE}✨ Total of two dice: {BOLD}{ITALIC}{total}{RESET}\n")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

# ==================== End Program ==================================
