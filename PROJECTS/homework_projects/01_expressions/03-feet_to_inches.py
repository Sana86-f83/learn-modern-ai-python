# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

# """
# An example program with constants
# """
# =============Start Program==================================

# ANSI color codes
BOLD_ITALIC = "\033[1;3m"  # Bold + Italic
RESET = "\033[0m"  # Reset formatting
PURPLE = "\033[1;35m"  # Bold Purple
BGRED = "\033[1;41m"  # Bold bgRED
GREEN = "\033[1;32m"  # Bold Green
YELLOW = "\033[1;33m"  # Bold Yellow
UNDERLINE = "\033[4m"  # Underline

# Constant value:
INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def convert_feet_to_inches(feet: float) -> float:
    """
    Converts feet to inches using the formula: inches = feet * 12
    """
    return feet * INCHES_IN_FOOT

def main():
    # User Input
    feet = float(input(f"\n\t\t{BOLD_ITALIC}{GREEN}🔹 Enter number of feet: {RESET}"))  
    # Perform Conversion
    inches = convert_feet_to_inches(feet)
    
    # Output Results
    print(f"\n\t\t\t{BOLD_ITALIC}{UNDERLINE}{BGRED}📏 Feet to Inches Conversion📏{RESET}\n")  
    print(f"\t\t\t\t{PURPLE}📌 Feet (ft): {feet}{RESET}")  
    print(f"\t\t\t\t{YELLOW}📌 Inches (in): {inches}{RESET}\n")  

if __name__ == "__main__":
    main()

# =============Program End==================================
