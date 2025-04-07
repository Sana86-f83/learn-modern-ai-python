# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

# You should use the three constants:

# PROMPT JOKE SORRY

# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

# Your program will need to use an if statement which checks if the user input is Joke:

# if user_input == "Joke":

# Recall that == is a comparison which tests if two values are equal to one another.

# Here is a full run of the program (user input is in blue):

# What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# =====================================================================
# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"

# Constants
PROMPT = f"\n\t\t\t{GREEN}{BOLD}What do you want?{RESET}"
JOKE = f"""\n\t\t{YELLOW}{BOLD}Here is a joke for you!{RESET}
{CYAN}\t\tTeacher ne student se poocha: Agar tumhare paas 4 aam hain,
\t\taur main tumse 1 aam le loon, to tumhare paas kitne aam rahenge?
\t\tStudent bola: 4! 😎
\t\tTeacher ne hairan ho kar poocha: Kaise?
\t\tStudent bola: Kyunke aap aam le toh sakte hain, par main dunga nahi! 😁{RESET}\n"""

SORRY = f"\n\t\t\t{RED}{BOLD}Sorry I only tell jokes{RESET}"

def main():
    user_input = input(PROMPT)  # User se input lena

    if user_input == "Joke":  # Agar user ne "Joke" type kiya
        print(JOKE)  # Joke print hoga
    else:
        print(SORRY)  # Agar kuch aur input kiya ho toh sorry message print hoga

if __name__ == "__main__":
    main()
# ======================================================