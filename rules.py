class Rules(object):

    def __init__(self):
        self.rules_map = {
            1: self.aces,
            2: self.twos,
            3: self.threes,
            4: self.fours,
            5: self.fives,
            6: self.sixes,
            7: self.three_of_a_kind,
            8: self.four_of_a_kind,
            9: self.full_house,
            10: self.small_straight,
            11: self.large_straight,
            12: self.yahtzee,
            13: self.chance,
        }

    def aces(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 1):
            sum += face
        return sum

    def twos(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 2):
            sum += face
        return sum

    def threes(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 3):
            sum += face
        return sum

    def fours(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 4):
            sum += face
        return sum

    def fives(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 5):
            sum += face
        return sum

    def sixes(self, hand):
        sum = 0
        for face in (x for x in hand.get_hand() if x == 6):
            sum += face
        return sum

    def three_of_a_kind(self, hand):
        for i in hand.get_hand():
            if hand.get_hand().count(i) >= 3:
                return sum(hand.get_hand())
        return 0

    def four_of_a_kind(self, hand):
        for i in hand.get_hand():
            if hand.get_hand().count(i) >= 4:
                return sum(hand.get_hand())
        return 0

    def full_house(self, hand):
        for i in hand.get_hand():
            x = hand.get_hand().count(i)
            if x == 3:
                for i in hand.get_hand():
                    y = hand.get_hand().count(i)
                    if y == 2 and x != y:
                        return 25
        return 0

    def small_straight(self, hand):
        hand = list(set(sorted(hand.get_hand())))
        try:
            if len(hand) >= 4:
                for idx, val in enumerate(hand):
                    if hand[idx+1] == val+1 and \
                       hand[idx+2] == val+2 and \
                       hand[idx+3] == val+3:
                        return 30
        except IndexError:
            pass
        return 0

    def large_straight(self, hand):
        hand = list(set(sorted(hand.get_hand())))
        try:
            if len(hand) >= 5:
                for idx, val in enumerate(hand):
                    if hand[idx+1] == val+1 and \
                       hand[idx+2] == val+2 and \
                       hand[idx+3] == val+3 and \
                       hand[idx+4] == val+4:
                        return 40
        except IndexError:
            pass
        return 0

    def yahtzee(self, hand):
        if len(set(hand.get_hand())) == 1:
            return 50
        return 0

    def chance(self, hand):
        return sum(hand.get_hand())
