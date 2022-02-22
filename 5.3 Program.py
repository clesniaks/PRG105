import math


def validate():
    display_menu()
    number = get_selection()
    while not number == 5:
        if number > 5:
            print("That is not a valid number!")
            display_menu()
            number = get_selection()
        elif number <= 0:
            print("That is not a valid number!")
            display_menu()
            number = get_selection()
        else:
            return int(number)
    return 5


def get_selection():
    selection = int(input("Pick a menu option: "))
    return selection


def display_menu():
    print(
        "This program will find the area of a shape for you!\n 1. Rectangle\n 2. Triangle\n 3. Square\n 4. Circle\n 5. Quit")


def rectangle(length1, width1):
    return float(length1 * width1)


def triangle(base1, height1):
    return float((1 / 2) * base1 * height1)


def square(side):
    return float(side * side)


def circle(radius):
    return float(math.pi * radius * radius)


def main():
    flag = True
    menu = validate()
    while flag:
        if menu == 1:
            length = int(input("What is the Length in cm?: "))
            width = int(input("What is the Width in cm?: "))
            print("The Area of the Rectangle is: " + str(rectangle(length, width)) + " square cm")
            menu = validate()
        elif menu == 2:
            base = int(input("What is the length of the base in cm?: "))
            height = int(input("What is the Height in cm?: "))
            print("The Area of the Triangle is: " + str(triangle(base, height)) + " square cm")
            menu = validate()
        elif menu == 3:
            side = int(input("What is length of one side in cm?: "))
            print("The Area of the Square is: " + str(square(side)) + " square cm")
            menu = validate()
        elif menu == 4:
            radius = int(input("What is the Radius in cm?: "))
            print("The Area of the Circle is: " + str(circle(radius)) + " square cm")
            menu = validate()
        elif menu == 5:
            flag = False


main()
