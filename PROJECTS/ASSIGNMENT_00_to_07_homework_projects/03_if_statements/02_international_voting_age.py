# Problem Statement
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

# ==============================================================================

# 🎨 ANSI color codes
BOLD = "\033[1m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[36m"
RESET = "\033[0m"

# 🏛️ Voting ages for different countries (fictional)

voting_ages = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48    #✅ Mayengua (48 years) → Ye fictional hai, kyunki kisi   bhi real country me voting age 48 nahi hoti.
}


def main():
    print(f"\n\t\t\t\t\t\t{BOLD}{CYAN}🌍 Welcome to the Voting Eligibility Checker!{RESET}\n")
    
    # User se age input lena
    user_age = int(input(f"\t\t\t\t{BOLD}📝 How old are you? {RESET}"))

    # Har country ke liye eligibility check karna
    for country, age in voting_ages.items():
        if user_age >= age:
            print(f"\n\t\t\t\t\t{GREEN}✅ You can vote in {country} where the voting age is {age}.{RESET}")
        else:
            print(f"\n\t\t\t\t\t\t{RED}❌ You cannot vote in {country} where the voting age is {age}.{RESET}\n")

# Program start hone ka point
if __name__ == '__main__':
    main()

# =========================================================================