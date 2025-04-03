# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5
# =====================================================================

def main():
    # ANSI color codes stored in variables
    GREEN = "\033[1;32m"
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    MAGENTA = "\033[35m"


    # Dictionary storing fruit names and their prices
    fruits = {
        'apple': 200,
        'strawberry': 500,
        'peach': 250,
        'grapes': 600,
        'watermelon': 100,
        'mango': 250
    }
    print(f"{BLUE}{BOLD}{ITALIC}\n\t\t\t\tFruit Purchase Tracker{RESET}")

    total_cost = 0  # Total cost initialization



    # Loop through fruits dictionary
    for fruit_name, price in fruits.items():
        while True:
            try:
                # Ask user for the quantity of each fruit
                amount_bought = float(input(f"\n\t\t\t{GREEN}{ITALIC}How many ({fruit_name}) do you want to buy?: {RESET}"))
                
                if amount_bought < 0:
                    print(f"\n\t\t\t\t{RED}❌ Please enter a valid non-negative number.{RESET}")
                    continue
                print(f"{MAGENTA}{BOLD}\t\t\t\t\t Fruit_name -> {RESET}{BLUE}{fruit_name}{MAGENTA} Fruit_price -> {RESET}{BLUE}{price} KG{RESET}")

                amount_bought = int(amount_bought)  # Convert to integer value (rounding down decimals)
                break  # Exit loop if input is valid
            except ValueError:
                print(f"\n\t\t\t\t{RED}❌ Invalid input! Please enter a valid number.{RESET}")

        total_cost += (price * amount_bought)  # Calculate total cost

    # Print the total cost with 2 decimal places
    print(f"{BLUE}{BOLD}{ITALIC}\n\t\t\t\tYour total is: ${total_cost:.2f}{RESET}\n")

# Run the program
if __name__ == '__main__':
    main()

# =============================================================================