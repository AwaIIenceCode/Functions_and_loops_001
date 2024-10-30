# escape sequence for better readability
Magenta = "\033[35m"
reset = "\033[0m"

num_1 = int(input("Enter the beginning of the range\n> "))
num_2 = int(input("Enter the end of the range\n> "))
print()

def prime_number(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for number in range(num_1, num_2 + 1):
    if prime_number(number):
        print(f"Number {Magenta}{number}{reset} is {Magenta}prime{reset}")
    else:
        print(f"Number {Magenta}{number}{reset} is {Magenta}not prime{reset}")