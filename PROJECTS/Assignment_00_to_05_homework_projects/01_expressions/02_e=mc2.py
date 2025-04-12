# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# =============Start Program==================================

# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
RED = "\033[1;31m"  # Bold Red
BLUE = "\033[1;34m"  # Bold Blue
GREEN = "\033[1;32m"  # Bold Green
PURPLE = "\033[1;35m"  # Bold Purple
YELLOW = "\033[1;33m"  # Bold Yellow
UNDERLINE = "\033[4m"  # Underline

# Constant value:
C = 299792458  # Speed of light in m/s

def calculate_energy(mass):
    """
    Calculate the energy using Einstein's formula: E = m * C^2
    """
    return mass * (C ** 2)

def main():
    # User Input
    value = float(input(f"\n\t\t\t{BOLD_ITALIC}{BLUE}🔹 Enter mass in kg: {RESET}"))  

    if value < 0:
        print(f"\n\t\t\t{RED}❌ Invalid input! Mass cannot be negative.{RESET}")  
        return

    # Calculate Energy
    energy = calculate_energy(value)

    # Output Results
    print(f"\n\t\t{BOLD_ITALIC}{UNDERLINE}{GREEN}🔬 Energy Calculation 🔬{RESET}\n")  
    print(f"\t\t{BLUE}📌 Mass (m): {value} kg{RESET}")  
    print(f"\t\t{PURPLE}📌 Speed of Light (C): {C} m/s{RESET}")  
    print(f"\t\t{YELLOW}📌 Energy (E): {energy:.2e} joules{RESET}\n")  

if __name__ == "__main__":
    main()

# =============Program End==================================


