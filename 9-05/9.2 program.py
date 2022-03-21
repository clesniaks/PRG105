language = {'Yi1': "one", 'Er4': "two", 'San1': "three", 'Si4': "four", 'Wu3': "five", 'Liu4': "six", 'Qi1': "seven", 'Ba1': "eight", 'Jiu3': "nine", 'Shi2': "ten"}


def main():
    num_correct = 0
    for key in language:
        guess = str(input("What is the equivalent of " + key + "? "))
        print(guess)
        if guess == language[key]:
            print("Correct" + '\n')
            num_correct += 1
        else:
            print("Incorrect" + '\n')
    print("You got " + str(num_correct))
    if num_correct >= 9:
        print("A")
    elif num_correct == 8:
        print("B")
    elif num_correct == 7:
        print("C")
    elif num_correct == 6:
        print("D")
    else:
        print("F")


main()
