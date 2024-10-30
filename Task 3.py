import random

magenta = "\033[35m"
red = "\033[31m"
bold = "\033[1m"
underline = "\033[4m"
invert = "\033[7m"
reset = "\033[0m"

true_answers = 0  #global variable to count responses from each function

print(f"{invert}Welcome to our multiplication table knowledge test! Here you can develop your knowledge!{reset}")
print()

def first_level():
    global true_answers
    initial_true_answers = true_answers  #variable to ensure correct answers count doesn't exceed question count
    user_level = 0

    for i in range(5):
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)

        try:  #check the user input number
            user_number = int(input(f"Enter the result: {magenta}{num_1}{reset} * {magenta}{num_2}{reset} = "))
        except ValueError:
            print(f"{red}{bold}Please, enter only numbers!{reset}")
            continue

        if user_number == num_1 * num_2:
            user_level += 1
            true_answers += 1
        else:
            pass

    if user_level >= 3:
        print(f"\nNumber of correct answers {magenta}{user_level}{reset} out of {magenta}5{reset}")
        print(f"\nYou {magenta}{underline}passed{reset} level one, go to {magenta}the second one!{reset}")
        second_level()
    else:
        true_answers = initial_true_answers
        print(f"\nUnfortunately, you {red}{underline}did not pass{reset} the level. {red}{underline}Try again{reset}")
        first_level()

def second_level():
    global true_answers
    initial_true_answers = true_answers
    user_level = 0

    print()

    for i in range(7):
        num_1 = random.randint(1, 15)
        num_2 = random.randint(1, 15)

        try:
            user_number = int(input(f"Enter the result: {magenta}{num_1}{reset} * {magenta}{num_2}{reset} = "))
        except ValueError:
            print(f"{red}{bold}Please, enter only numbers!{reset}")
            continue

        if user_number == num_1 * num_2:
            user_level += 1
            true_answers += 1
        else:
            pass

    if user_level >= 5:
        print(f"\nNumber of correct answers {magenta}{user_level}{reset} out of {magenta}7{reset}")
        print(f"\nYou {underline}{magenta}passed{reset} the second level, moving to the {magenta}third one!{reset}")
        third_level()
    else:
        true_answers = initial_true_answers
        print(f"\nUnfortunately, you {red}{underline}did not pass{reset} the level. {red}{underline}Try again{reset}")
        second_level()

def third_level():
    global true_answers
    initial_true_answers = true_answers
    user_level = 0

    print()

    for i in range(10):
        num_1 = random.randint(5, 20)
        num_2 = random.randint(5, 20)

        try:
            user_number = int(input(f"Enter the result: {magenta}{num_1}{reset} * {magenta}{num_2}{reset} = "))
        except ValueError:
            print(f"{red}{bold}Please, enter only numbers!{reset}")
            continue

        if user_number == num_1 * num_2:
            user_level += 1
            true_answers += 1
        else:
            pass

    if user_level >= 7:
        print(f"\nNumber of correct answers {magenta}{user_level}{reset} out of {magenta}10{reset}")
        print(f"Total correct answers {magenta}{true_answers}{reset} out of {magenta}22{reset}")
        print(f"{invert}Congratulations, you successfully completed all levels! You mastered the topic well and can move forward with confidence!{reset}")
    else:
        true_answers = initial_true_answers
        print(f"\nUnfortunately, you {red}did not pass{reset} the level. {red}{underline}Try again{reset}")
        third_level()

first_level()
