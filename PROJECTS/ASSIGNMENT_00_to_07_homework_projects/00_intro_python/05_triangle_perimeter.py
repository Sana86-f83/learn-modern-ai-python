# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

# ===================Start Program=====================

# ✅ Solution
# ANSI escape codes for bold & italic text
BOLD_ITALIC = "\033[1;3m"  # Bold & Italic
RESET = "\033[0m"  # Reset formatting
GREEN="\033[32m"
YELLOW = "\033[43m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
def main():

    # Get the 3 side lengths of the triangle
    side1 = float(input(f"\n\t\t{GREEN}{BOLD_ITALIC}What is the length of side 1 ? {RESET}"))
    side2 = float(input(f"\t\t{CYAN}{BOLD_ITALIC}What is the length of side 2 ? {RESET}"))
    side3 = float(input(f"\t\t{MAGENTA}{BOLD_ITALIC}What is the length of side 3 ? {RESET}"))
    total = side1 + side2 + side3

    # Print out the perimeter (sum of the sides) of the triangle.
    print(f"\n\t\t\t{YELLOW}{BOLD_ITALIC}The perimeter of the triangle is {total} !{RESET}\n")

if __name__ == "__main__":
    main()

# ============Program end===========================

