import OfficeFurniture
import Desk


def main():
    table = OfficeFurniture.OfficeFurniture('Table', 'Wood', 8, 3, 3, 15.43)
    desk = Desk.Desk('Desk', 'Wood/Plastic', 6, 4, 5, 50.42, 'Right', 3)
    table.__str__()
    print('\n')
    desk.__str__()


main()
