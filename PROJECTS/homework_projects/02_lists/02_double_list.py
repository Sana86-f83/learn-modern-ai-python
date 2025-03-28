# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# ANSI color codes
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
BLUE = "\033[1;34m"   # Bold Blue
GREEN = "\033[1;32m"  # Bold Green
CYAN = "\033[1;36m"   # Bold Cyan
RED = "\033[1;31m"    # Bold Red

# =============Start Program================================

def main():
    # Define a list of numbers
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 8]  
    print(f"\n\t\t\t{BOLD}{BLUE}{ITALIC}Original List:{RESET}", numbers)  

    for i in range(len(numbers)):  
        elem_at_index = numbers[i]  

        # Print index and element being processed
        print(f"\t\t{ITALIC}{GREEN}Processing index {i}:{RESET} {UNDERLINE}{CYAN}{elem_at_index}{RESET}")  
        
        numbers[i] = elem_at_index * 2  

    # Print the final modified list
    print(f"\n\t\t\t\t{BOLD}{RED}{ITALIC}Updated List:{RESET}", numbers)  

if __name__ == '__main__':
    main()
# ==================Program End========================