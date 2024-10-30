magenta = "\033[35m"
red = "\033[31m"
italic = "\033[3m"
reset = "\033[0m"

size = int(input(f"Enter the height of the rhombus {italic}{magenta}\"ODD NUMBER FOR SYMMETRY\"{reset}\n>"))

print()

def rhombus_output():
    for i in range(size // 2 + 1):
        print(f"{magenta}{' ' * (size // 2 - i) + '*' * (2 * i + 1)}{reset}")

    for j in range(size // 2 - 1, -1, -1):
        print(f"{magenta}{' ' * (size // 2 - j) + '*' * (2 * j + 1)}{reset}")

if size % 2 != 0:
    rhombus_output()
else:
    print(f"{red}well, you've been told an odd number, but keep it rounded up if you don't know which number is odd ^-^{reset}\n")
    rhombus_output()

#______________________________________________________________________________________________________________________#

size = int(input("Enter the height of the rhombus\n>"))
mid = size // 2

for i in range(size):
    spaces = abs(mid - i) #returns the modulus of a number
    symbols = size - 2 * spaces
    print(' ' * spaces + '*' * symbols)

#______________________________________________________________________________________________________________________#

# and last variant

def easy_romb():

    size = int(input("Enter the height of the rhombus\n>"))
    print()

    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

easy_romb()