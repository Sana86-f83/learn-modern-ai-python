# Problem Statement
# Write a function that takes two numbers and finds the average between the two.


# 🔷🔷🔷 Program to Calculate Average of Two Numbers 🔷🔷🔷

def average(a: float, b: float) -> float:
    """
    Ye function do numbers (a aur b) ka average nikaalta hai.
    Average ka matlab hota hai dono numbers ka beech ka number.
    """
    sum = a + b              # Dono numbers ka total
    return sum / 2           # Total ko 2 se divide karke average return karo


def main():
    # Pehla average: 0 aur 10 ka beech ka number
    avg_1 = average(0, 10)   # avg_1 = 5.0

    # Dusra average: 8 aur 10 ka beech ka number
    avg_2 = average(8, 10)   # avg_2 = 9.0

    # Final average: avg_1 aur avg_2 ka beech ka number
    final = average(avg_1, avg_2)  # final = average(5.0, 9.0) = 7.0

    # 🔸 ANSI Color Codes 🔸
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Heading
    print(f"\n\t\t\t{YELLOW}{'='*50}")
    print(f"\t\t\t{CYAN}{' '*10}📌 AVERAGE CALCULATOR 📌")
    print(f"\t\t\t{YELLOW}{'='*50}{RESET}")

    # Results with color
    print(f"\n\t\t\t\t\t🔹 avg_1: {GREEN}{avg_1}{RESET}")
    print(f"\t\t\t\t\t🔹 avg_2: {GREEN}{avg_2}{RESET}")
    print(f"\t\t\t\t\t🔹 final: {GREEN}{final}{RESET}\n")


# Ye ensure karta hai ke jab file direct run ho, tab hi main() function chale
if __name__ == '__main__':
    main()
