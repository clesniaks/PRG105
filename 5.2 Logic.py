def validate():
    num = input("Pick a whole number between 20 and 100:")
    while int(num) > 100 or int(num) < 20:
        print("That is not a valid number!")
        num = input("Pick a whole number between 20 and 100:")
    return num


def div_2(number):
    if int(number) % 2 == 0:
        print(number + " is divisible by 2")
    else:
        print(number + " is not divisible by 2")


def div_3(number):
    if int(number) % 3 == 0:
        print(number + " is divisible by 3")
    else:
        print(number + " is not divisible by 3")


def div_5(number):
    if int(number) % 5 == 0:
        print(number + " is divisible by 5")
    else:
        print(number + " is not divisible by 5")


def main():
    good_number = validate()
    div_2(good_number)
    div_3(good_number)
    div_5(good_number)


main()
