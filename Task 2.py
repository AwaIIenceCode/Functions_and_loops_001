"""magenta = "\033[35m"
reset = "\033[0m"

size_chess = int(input("Enter cell size\n> "))

def chess_desk():
    print()

    for i in range (3):
        for j in range (4):
            print(f"{size_chess * '*'}{magenta}{size_chess * '_'}{reset}", end = '')
        print()

    for i in range(3):
        for j in range(4):
            print(f"{magenta}{size_chess * '_'}{reset}{size_chess * '*'}", end='')
        print()

chess_desk()"""


# if reduce the number of cycles:


magenta = "\033[35m"
reset = "\033[0m"

size_chess = int(input("Enter cell size\n> "))

def chess_desk():
    print()
    for i in range(6):
        for j in range(4):
            if i < 3:
                print(f"{size_chess * '*'}{magenta}{size_chess * '_'}{reset}", end='')
            else:
                print(f"{magenta}{size_chess * '_'}{reset}{size_chess * '*'}", end='')
        print()

chess_desk()
