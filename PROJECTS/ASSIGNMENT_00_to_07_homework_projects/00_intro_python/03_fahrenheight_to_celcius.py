# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C


# ===================Start Program=====================

# ANSI escape codes for bold & italic text
BOLD_ITALIC = "\033[1;3m"   # Bold & Italic
RESET = "\033[0m"           # Reset formatting
GREEN = "\033[92m"          # Green color for results
CYAN = "\033[96m"           # Cyan color for input

# ✅ Solution
def main():
    # User input with formatting
    degrees_fahrenheit = float(input(f"\n\t\t{CYAN}{BOLD_ITALIC}Enter temperature in Fahrenheit: {RESET}"))

    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print output with bold & italic
    print(f"\n\t\t{GREEN}{BOLD_ITALIC}Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.2f}C{RESET}\n")

# Calling the main function
if __name__ == "__main__":
    main()


# ============Program end===========================
