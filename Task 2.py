#i = int(1)
#j = int(1)
def calculating():

    magenta = "\033[35m"
    reset = "\033[0m"

    for i in range (1, 11):

        for j in range (1, 11):
            print(f"{magenta}{i}{reset}*{magenta}{j}{reset}={magenta}{i * j}{reset}", end=" | ")

        print()
        print("." * 101)

calculating()