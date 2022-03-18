steps = {}


def main():
    print("You will be entering the date and the number of steps taken for each day in a week")
    steps["Sunday"] = int(input("Enter the number of steps on Sunday: "))
    steps["Monday"] = int(input("Enter the number of steps on Monday: "))
    steps["Tuesday"] = int(input("Enter the number of steps on Tuesday: "))
    steps["Wednesday"] = int(input("Enter the number of steps on Wednesday: "))
    steps["Thursday"] = int(input("Enter the number of steps on Thursday: "))
    steps["Friday"] = int(input("Enter the number of steps on Friday: "))
    steps["Saturday"] = int(input("Enter the number of steps on Saturday: "))


def calculate():
    total_steps = 0
    maximum_steps = 0
    minimum_steps = 1000000
    maxday_name = []
    minday_name = []
    for key in steps:
        total_steps += steps[key]
        if steps[key] > maximum_steps:
            maximum_steps = steps[key]
        elif steps[key] < minimum_steps:
            minimum_steps = steps[key]
    for key in steps:  # I may have overcomplicated this a bit I could have taken this loop and put it under each of the (max/min) print statements and replaced the list objects with print(key)#
        if steps[key] == maximum_steps:
            maxday_name.append(key)
        elif steps[key] == minimum_steps:
            minday_name.append(key)
    print("You walked a total of " + str(total_steps) + " steps during the week")
    print("That was an average of " + str(format(int(total_steps/7), ',')) + " steps")
    print("The Maximum steps you took were: " + str(maximum_steps) + " on ")
    for n in maxday_name:
        print(n)
    print("The Minimum steps you took were: " + str(minimum_steps) + " on ")
    for d in minday_name:
        print(d)


main()
calculate()
