import random
import re


class Die(object):

    def __init__(self, sides=6):
        self.sides = sides
        # Make __face private to prevent cheating
        self.__face = None

    def roll(self):
        self.__face = random.randint(1, 6)

    def clear(self):
        self.__face = None

    def get_face(self):
        return self.__face

    def __str__(self):
        if self.__face:
            return "Value: " + str(self.__face)
        else:
            return "Die has not been thrown"


class Hand(object):

    def __init__(self, dice=5, sides=6):
        self.dice = dice
        self.hand = []
        for x in range(dice):
            self.hand.append(Die(sides))
        # x = 0
        # while x < self.dice:
        #     self.hand.append(Die(sides))
        #     x += 1

    def throw(self):
        print("\nRolling dice...")
        for die in self.hand:
            die.roll()

    def clear(self):
        for die in self.hand:
            die.clear()

    def re_roll(self):
        rolls = 0
        while rolls < 2:
            try:
                reroll = input("\nChoose which dice to re-roll "
                               "(comma-separated or 'all'), or 0 to continue: ")

                if reroll.lower() == "all":
                    reroll = list(range(1, 6))
                else:
                    # Perform some clean-up of input
                    reroll = reroll.replace(" ", "")  # Remove spaces
                    reroll = re.sub('[^0-9,]', '', reroll)  # Remove non-numerals
                    reroll = reroll.split(",")  # Turn string into list
                    reroll = list(map(int, reroll))  # Turn strings in list to int
            except ValueError:
                print("You entered something other than a number.")
                print("Please try again")
                continue

            if [x for x in reroll if x > self.dice]:
                print("You only have 5 dice!")
                continue

            if not reroll or 0 in reroll:
                break
            else:
                for i in reroll:
                    self.hand[i-1].roll()
                self.show_hand()
                rolls += 1

    def get_hand(self):
        faces = []
        for face in self.hand:
            faces.append(face.get_face())
        return faces

    def show_hand(self):
        for idx, val in enumerate(self.hand):
            print("die " + str(idx + 1) + " has value " + str(val.get_face()))
