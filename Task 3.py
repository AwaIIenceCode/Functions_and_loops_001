magenta = "\033[35m"
reset = "\033[0m"

def multiplication_table(num_1, num_2):
    print()
    for i in range (num_1, num_2 + 1):

        for j in range (1, 11):
            print(f"{magenta}{i}{reset}*{magenta}{j}{reset}= {magenta}{i*j}{reset}", end = " | ")

        print()
        print("." * 100)

num_1 = int(input("Введите начало диапазона\n>"))
num_2 = int(input("Введите конец диапазона\n>"))

multiplication_table(num_1, num_2)