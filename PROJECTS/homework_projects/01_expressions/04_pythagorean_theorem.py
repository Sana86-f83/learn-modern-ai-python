# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0

# =============Start Program==================================

# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
PURPLE = "\033[1;35m"  # Bold Blue
GREEN = "\033[1;32m"  # Bold Green
UNDERLINE = "\033[4m"  # Underline


import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input(f"\n\t\t\t{BOLD_ITALIC}{GREEN}Enter the length of AB: {RESET}"))
    ac: float = float(input(f"\n\t\t\t{BOLD_ITALIC}{GREEN}Enter the length of AC: {RESET}"))

    # Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"\n\t\t\t\t{BOLD_ITALIC}{PURPLE}{UNDERLINE}The length of BC (the hypotenuse) is: {bc}{RESET}\n")



if __name__ == '__main__':
    main()

# ====================Program End=========================    