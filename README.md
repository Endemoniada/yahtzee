# Yahtzee
A simple 1-player console Yahtzee game.

The object of the game is to roll five dice in order to get the highest possible score.

# Usage
./yahtzee.py

# Requirements
Python 3.7

# Rules

The player rolls five dice, and has the option to re-roll any or all of the dice two times. When the player is satisfied, or they have rolled a maximum of three times, they choose the most appropriate scoring rule and get awarded the corresponding points.

## Scoring

*Aces*
Dice:   Any combination
Score:  The sum of dice with the number 1

*Twos*
Dice    Any combination
Score:  The sum of dice with the number 2

*Threes*
Dice    Any combination
Score:  The sum of dice with the number 3

*Fours*
Dice    Any combination
Score:  The sum of dice with the number 4

*Fives*
Dice    Any combination
Score:  The sum of dice with the number 5

*Sixes*
Dice    Any combination
Score:  The sum of dice with the number 6

*Three Of A Kind*
Dice:   At least three dice the same
Score:  Sum of all dice

*Four Of A Kind*
Dice:   At least four dice the same
Score:  Sum of all dice

*Full House*
Dice:   Three of one number and two of another
Score:  25

*Small Straight*
Dice:   Four sequential dice
Score:  (1-2-3-4, 2-3-4-5, or 3-4-5-6)
30

*Large Straight*
Dice:   Five sequential dice (1-2-3-4-5 or 2-3-4-5-6)
Score:  40

*Yahtzee*
Dice:   All five dice the same
Score:  50

*Chance*
Dice:   Any combination
Score:  Sum of all dice
