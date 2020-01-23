from random import randint

# x = randint(1, 6)

# print(x)

class Die():
    """Simulates dice. Can be any sided"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        """Simulates rolling of dice using randint"""
        dice_num = randint(1, self.sides)
        print(dice_num)

    def set_die_faces(self, faces):
        """Sets number of faces/sides die has"""
        self.sides = faces

my_dice = Die()
my_dice.roll_dice()

dice_10 = Die()
dice_10.set_die_faces(10)
dice_10.roll_dice()

dice_20 = Die(20)
dice_20.roll_dice()