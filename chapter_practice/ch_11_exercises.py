"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors


class Dwelling:

    def __init__(self, num_rooms, sqr_ft, num_floors):
        self.__num_rooms = num_rooms
        self.__sqr_ft = sqr_ft
        self.__num_floors = num_floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_rooms(self, num_rooms):
        self.__num_rooms = num_rooms

    def set_sqr_ft(self, sqr_ft):
        self.__sqr_ft = sqr_ft

    def set_num_floors(self, num_floors):
        self.__num_floors = num_floors

    # 3) Add accessors for all of the data attributes

    def get_rooms(self):
        return self.__num_rooms

    def get_sqr_ft(self):
        return self.__sqr_ft

    def get_num_floors(self):
        return self.__num_floors


# 4) Create the class SingleFamilyHome as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes


class SingleFamilyHome(Dwelling):

    def __init__(self, num_rooms, sqr_ft, num_floors, garage_type, yard_size):
        Dwelling.__init__(self, num_rooms, sqr_ft, num_floors)
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes

    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size

    def get_yard_size(self):
        return self.__yard_size

    def get_garage_type(self):
        return self.__garage_type


# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
# 7) In main, create an object from the Single_family_home class with the following information:
#            6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres

def main():
    new_home = SingleFamilyHome(6, 1200, 1, "Single car garage", 0.25)
    # 8) Display the data using the accessor methods
    print(str(new_home.get_rooms()) + " Rooms")
    print(str(new_home.get_sqr_ft()) + " Square-feet")
    print(str(new_home.get_num_floors()) + " Floor/s ")
    print(new_home.get_garage_type())
    print(str(new_home.get_yard_size()) + " acres")


# 9) Call the main function

main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)
# 1) Type in the mammal class from program 11-9, lines 1 - 22


class Mammal:

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        print('Grrrrr')


# 2) Create a Mouse class as a sub class of the mammal class following the Dog example


class Mouse(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Mouse')

    def make_sound(self):
        print('Squeak Squeak!')
# 3) Create an Sheep class as a sub class of the mammal class following the Cat Example


class Sheep(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Sheep')

    def make_sound(self):
        print('BAAAAAAAAA')
# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created


def main2():
    mammal = Mammal('Mammal')
    mouse = Mouse()
    sheep = Sheep()
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    mammal.show_species()
    mammal.make_sound()
    print('--------------------------')
    mouse.show_species()
    mouse.make_sound()
    print('--------------------------')
    sheep.show_species()
    sheep.make_sound()


main2()
