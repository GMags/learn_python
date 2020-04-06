from random import randint


class Dice:
    """Class to define the sides of a dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Function to define rolling of a dice """

        return randint(1, self.sides)


six_dice = Dice()
ten_dice = Dice(sides=10)

results = []
print(f"You rolled a six sided dice")
for roll in range(10):
    result = six_dice.roll_die()
    results.append(result)

print(results)

print(f"------------------------------------")

results = []
print(f"You rolled a 10 sided dice")
for roll in range(10):
    result = ten_dice.roll_die()
    results.append(result)

print(results)