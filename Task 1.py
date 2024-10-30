#ex.1
"""The user enters a number. It is necessary to determine the number of digits in the number, count their sum and the
arithmetic mean. Determine the number of zeros in the number. Communication with the user should be organised through the menu."""

# Version_1

par = int(input("Press \"1\" to find the number of digits in your number, their sum and the arithmetic mean\nPress \"2\" to find the number of zeros in your number\n> "))

# Adding escape sequence to improve code readability
magenta = "\033[35m"
underline = "\033[4m"
reset = "\033[0m"

def cont_sum_mean_number ():
    """Function for counting the number of digits, sum and arithmetic mean"""
    user_input = int(input("\nEnter a number:\n> "))
    number = user_input #Added an additional variable to save the user's number after manipulating it
    count = 0
    total_sum = 0

    while user_input > 0:
        user_input //= 10
        count += 1
    print(f"\nNumber of digits in the number {underline}{number}{reset}: {magenta}{count}{reset}")

    for digit in str(number):
        total_sum += int(digit)

    arithmetic_mean = float(total_sum / count)

    print(f"Sum of digits in a number {underline}{number}{reset} = {magenta}{total_sum}{reset}")
    print(f"Arithmetic mean of digits in a number {number} = {arithmetic_mean}")


def count_zero():
    """Function for counting zeros in a number"""
    user_input = input("Enter a number: ")
    count_of_zero = 0

    for digit_zero in user_input:
        if int(digit_zero) == 0:
            count_of_zero += 1

    print(f"The number of zeros in your number {underline}{user_input}{reset} = {magenta}{count_of_zero}{reset}")

if par == 1:
    cont_sum_mean_number()
elif par == 2:
    count_zero()
else:
    print("This command does not exist, try again...")


# Version_2

# In this variant I wanted to deal with improving the menu and being able to select each item separately:

# Adding escape sequence to improve code readability
magenta = "\033[35m"
underline = "\033[4m"
red = "\033[31m"
reset = "\033[0m"

def count_number(user_number):
    """function for counting digits in a number"""
    count = 0
    number = user_number
    while user_number > 0:
        user_number //= 10
        count += 1
    return count

def sum_count_number(user_number):
    """function for counting the sum of digits in a number"""
    total_sum = 0
    for digit in str(user_number):
        total_sum += int(digit)
    return total_sum

def average_digit_of_number(user_number):
    """function for counting the sum of digits in a number"""
    total_sum = sum_count_number(user_number)
    count = count_number(user_number)
    return total_sum / count

def count_zero(user_number):
    """function for counting the sum of digits in a number"""
    count_of_zero = 0
    for digit_zero in str(user_number):
        if int(digit_zero) == 0:
            count_of_zero += 1
    return count_of_zero

def menu():
    """menu function"""
    print("\nMenu:")
    print(f"{red}1{reset} - Count the number of digits")
    print(f"{red}2{reset} - Count the sum of the digits")
    print(f"{red}3{reset} - Calculate the arithmetic mean of the digits")
    print(f"{red}4{reset} - Count the number of zeros")
    print(f"{red}5{reset} - Get out")

def main():
    """program start function to request a number"""
    user_input = input("\nEnter a number to work with\n> ")

    user_number = int(user_input) # I convert the string to int for further calculations

    menu()
    par = input("\nSelect the menu item (1-5)\n> ")

    if par == "1":
        print(f"\nNumber of digits in the number {underline}{user_number}{reset}: {magenta}{count_number(user_number)}{reset}")
    elif par == "2":
        print(f"\nSum of digits in a number {underline}{user_number}{reset}: {magenta}{sum_count_number(user_number)}{reset}")
    elif par == "3":
        print(f"\nArithmetic mean of digits in a number {underline}{user_number}{reset}: {magenta}{average_digit_of_number(user_number)}{reset}")
    elif par == "4":
        print(f"\nNumber of zeros in the number {underline}{user_number}{reset}: {magenta}{count_zero(user_number)}{reset}")
    elif par == "5":
        print("\nExit from the programme")
        exit()
    else:
        print("\nWrong choice, try again...")

if __name__ == "__main__":
    main()