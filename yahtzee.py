#!/usr/bin/env python

"""Yahtzee, the board game!

This python program will simulate a game of Yahtzee
"""

import sys
import os

from hand import Hand
from scoreboard import ScoreBoard


def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
YAHTZEE

Welcome to the game. To begin, simply press [Enter]
and follow the instructions on the screen.

To exit, press [Ctrl+C]
""")

    # Begin by instantiating the hand and scoreboard
    hand = Hand(5, 6)
    scoreboard = ScoreBoard()

    # We keep going until the scoreboard is full
    while len(scoreboard.get_scoreboard_points()) < len(scoreboard.scoreboard_rows):
        hand.throw()
        hand.show_hand()
        hand.re_roll()
        scoreboard.select_scoring(hand)
        scoreboard.show_scoreboard_points()

        input("\nPress any key to continue")
        os.system('cls' if os.name == 'nt' else 'clear')

    print("\nCongratulations! You finished the game!\n")
    scoreboard.show_scoreboard_points()
    print("Total points: {}".format(sum(scoreboard.get_scoreboard_points().values())))


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print("\nExiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
