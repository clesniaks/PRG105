"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

import random
# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)


class Dice:  # note class names are capitalized
    def __init__(self):  # class constructor initializes attributes of the class
        # TODO change side_up to '1'
        self.side_up = '1'

        # TODO change toss() to roll()
    def roll(self):  # class methods
        # TODO get a random value and set side_up for the 6 sides of the dice
        dice_num = random.randint(0, 6)
        if dice_num == 0:
            self.side_up = '0'
        elif dice_num == 1:
            self.side_up = '1'
        elif dice_num == 2:
            self.side_up = '2'
        elif dice_num == 3:
            self.side_up = '3'
        elif dice_num == 4:
            self.side_up = '4'
        elif dice_num == 5:
            self.side_up = '5'
        else:
            self.side_up = '6'
            
    def get_side_up(self):
        return self.side_up
    

def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())
    
    print('I am rolling the dice...')
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())


main()
