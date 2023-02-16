#import random
#define a function to roll the dice
#create a dictionary that will the drawing of the dice

import random

def dice_drawing(dice):
    drawing = {
        1: (
            "-------",
            "|  1  |",
            "|  ●  |",
            "|     |",
            "-------",
        ),
        2: (
            "-------",
            "|●    |",
            "|  2  |",
            "|    ●|",
            "-------",
        ),
        3: (
            "-------",
            "|●    |",
            "|  ●  |",
            "|    ●|",
            "-------",
        ),
        4: (
            "-------",
            "|●   ●|",
            "|     |",
            "|●   ●|",
            "-------",
        ),
        5: (
            "-------",
            "|●   ●|",
            "|  ●  |",
            "|●   ●|",
            "-------",
        ),
        6: (
            "-------",
            "|●   ●|",
            "|●   ●|",
            "|●   ●|",
            "-------",
        )
    }

    return drawing[dice]


def roll_dice():
    roll = input("Roll the dice? (Yes/No) : ")

    while roll.lower() == 'yes':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print(" ")
        print("="*50)
        print(f"Dice rolled: {dice_1} and {dice_2}")
        print("="*50)
        print(" ")

        print("\n".join(dice_drawing(dice_1)))
        print("\n".join(dice_drawing(dice_2)))
        # print(f"{dice_drawing(dice_1)}")

        roll = input("Roll again? (Yes/No): ")

def run():
    roll_dice()

if __name__ == '__main__':
    run()