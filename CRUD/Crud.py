import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        inputfile = open("customer_file.dat", 'rb')
        customers = pickle.load(inputfile)
    except(IOError, FileNotFoundError):
        print("file not found!")
        customers = {}
    user_choice = 0
    while user_choice != QUIT:
        user_choice = menu()

        if user_choice == LOOK_UP:
            look_up(customers)
        elif user_choice == ADD:
            add(customers)
        elif user_choice == CHANGE:
            change(customers)
        elif user_choice == DELETE:
            delete(customers)
        elif user_choice == QUIT:
            save(customers)


def menu():
    print("Customer Address Lookup")
    print("1.   Look-up a Customer")
    print("2.   Add a new Customer")
    print("3.   Change a current Customer")
    print("4.   Delete a Customer")
    print("5.   Quit")
    choice = int(input("Enter the menu number above: "))
    while choice < 1 or choice > 5:
        choice - int(input("Please enter a valid choice (1-5): "))
    return choice


def look_up(customers):
    name = input("Enter the name of the Customer: ")
    print(customers.get(name, 'Not Found'))


def add(customers):
    name = input("Enter the name of the Customer: ")
    address = input("Enter the address of the Customer: ")
    if name in customers:
        print("That person is already a Customer!")
    else:
        customers[name] = address


def change(customers):
    name = input("Enter the name of the Customer: ")
    if name in customers:
        address = input("Enter the new address of the Customer: ")
        customers[name] = address
    else:
        print("Customer not found!")


def delete(customers):
    name = input("Enter the name of the Customer: ")
    if name in customers:
        del customers[name]
    else:
        print("Customer not found!")


def save(customers):
    outputfile = open("customer_file.dat", 'wb')
    pickle.dump(customers, outputfile)
    outputfile.close()


main()
