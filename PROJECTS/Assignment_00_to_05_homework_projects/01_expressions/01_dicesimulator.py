"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

# =============Start Program==================================
# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
BGRED = "\033[1;41m"  # Bold bgRED
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
UNDERLINE = "\033[4m"  # Underline


# Import the random library to simulate random dice rolls
import random

# Number of sides on each die to roll (Global Variable)
NUM_SIDES = 6  # Global Scope

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Demonstrates **Local Scope** of variables inside this function.
    """
    die1: int = random.randint(1, NUM_SIDES)  # Local Scope (only exists inside roll_dice)
    die2: int = random.randint(1, NUM_SIDES)  # Local Scope (only exists inside roll_dice)
    total: int = die1 + die2  # Local Scope (only exists inside roll_dice)

    print(f"\n\t\t\t{GREEN} {BOLD_ITALIC}🎲 Rolling Dice: die1 = {die1}, die2 = {die2} → Total: {total} {RESET}")

def main():
    """
    The main function demonstrates variable scope.
    """
    die1: int = 10  # Local Scope (only exists inside main)
    print(f"\n\t\t{BGRED}{BOLD_ITALIC}🔹 die1 in main() starts as: {die1} {RESET}")

    print(f"\n\t\t\t{YELLOW}{BOLD_ITALIC}{UNDERLINE}Function Calls 3 Time (does not effect die1 in main){RESET}")
    roll_dice()  
    roll_dice()  
    roll_dice()  

    # The value of die1 in main remains unchanged
    print(f"\n\t\t{BGRED}{BOLD_ITALIC}🔹 die1 in main() is still: {die1} {RESET}\n")

# This line ensures the script runs only when executed directly
if __name__ == '__main__':
    main()

# ====================Program End=========================
