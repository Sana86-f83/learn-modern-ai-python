# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4
# 4.0 squared is 16.0

# =================== Start Program =====================

# ANSI escape codes for colors & formatting
BOLD_ITALIC = "\033[1;3m"   # Bold & Italic
GREEN = "\033[92m"          # Green color for results
CYAN = "\033[96m"           # Cyan color for input
RESET = "\033[0m"           # Reset formatting

# ✅ Solution
def main():
    # Asking for user input with color
    num: float = float(input(f"\n\t\t{CYAN}{BOLD_ITALIC}Type a number to see its square: {RESET}"))

    # Calculating square of the number
    square = num * num

    # Printing result with color
    print(f"\n\t\t\t{GREEN}{num} squared is {square}{RESET}\n")

# Calling the main function
if __name__ == "__main__":
    main()

# =================== Program End =====================
