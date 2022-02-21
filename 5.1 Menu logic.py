def display_menu():
    print("Select one of the menu options below to find out more..")
    print("A. Chicken Alfredo")
    print("B. Chicken Scampi")
    print("C. Herb-Grilled Salmon")
    print("D. 6 oz. Sirloin")
    print("E. Cheese Ravioli")


def get_user_selection():
    select = input("Please enter the letter of your choice: ")
    return select


def display_user_selection(selection):
    if selection == "A":
        print("This homemade sauce combines simple, fresh ingredients like butter, cream and parmesan cheese to make a rich topping to our fettuccine pasta.\nThen it is topped with tender, sliced grilled chicken. Sprinkle some parsley flakes on top and buon appetito!\nOlive Garden's classic Chicken Alfredo is an easy and delicious choice for dinner.")
    elif selection == "B":
        print("Bell peppers and red onions sautéed with chicken tenderloins in a creamy scampi sauce. Served over angel hair pasta.")
    elif selection == "C":
        print("Filet grilled to perfection and topped with garlic herb butter. Served with parmesan garlic broccoli.")
    elif selection == "D":
        print("Grilled 6 oz sirloin topped with garlic herb butter. Served with a side of fettuccine alfredo.")
    elif selection == "E":
        print("Filled with a blend of indulgent Italian cheeses, topped with your choice homemade marinara or meat sauce** and melted mozzarella.")
    else:
        print("Please enter a valid Letter...")
        display_user_selection(get_user_selection())


def main():
    display_menu()
    display_user_selection(get_user_selection())


main()
