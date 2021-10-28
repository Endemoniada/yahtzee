import re
from rules import Rules


class ScoreBoard(object):

    # TODO: Everything
    def __init__(self):
        self.scoreboard_rows = {
            1: "Aces",
            2: "Twos",
            3: "Threes",
            4: "Fours",
            5: "Fives",
            6: "Sixes",
            7: "Three of a Kind",
            8: "Four of a Kind",
            9: "Full House",
            10: "Small Straight",
            11: "Large Straight",
            12: "Yahtzee",
            13: "Chance",
        }
        # Once again, prevent cheating with private variables
        self.__scoreboard_points = {}

    def set_scoreboard_row_value(self, row, value):
        if row not in self.scoreboard_rows.keys():
            print("Bad row index")
            return False
        else:
            if row in self.__scoreboard_points.keys():
                print("ScoreBoard already saved!")
                return False
            else:
                print("Adding {} points to {}".format(
                    value,
                    self.scoreboard_rows[int(row)])
                )
                self.__scoreboard_points[row] = value
                return True

    def get_scoreboard_points(self):
        return self.__scoreboard_points

    def show_scoreboard_rows(self):
        for key, val in self.scoreboard_rows.items():
            print("{}. {}".format(key, val))

    def show_scoreboard_points(self):
        print("\nSCOREBOARD")
        print("===================================")
        for idx, row in self.scoreboard_rows.items():
            try:
                print("{:<2} {:<21}| {:2} points".format(idx,
                      row,
                      self.__scoreboard_points[idx]))
            except KeyError:
                print("{:<2} {:<21}|".format(idx, row))
        print("===================================")

    def select_scoring(self, hand):
        msg = "Choose which scoring to use "\
               "(leave empty to show available rows): "
        scoreboard_row = False
        score_saved = False
        while not scoreboard_row and not score_saved:
            scoreboard_row = input(msg)
            if scoreboard_row.strip() == "":
                self.show_scoreboard_points()
                scoreboard_row = False
                continue
            try:
                scoreboard_row = int(re.sub('[^0-9,]', '', scoreboard_row))
            except ValueError:
                print("You entered something other than a number.")
                print("Please try again")
                scoreboard_row = False
                continue
            if scoreboard_row > len(self.scoreboard_rows):
                print("Please select an existing scoring rule.")
                scoreboard_row = False
                continue
            else:
                score_saved = self.set_scoreboard_row_value(
                    int(scoreboard_row),
                    Rules().rules_map[int(scoreboard_row)](hand)
                )
