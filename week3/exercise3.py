"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    lowerBound = not_number_rejector("Enter a low number")
    upperBound = not_number_rejector("Enter a high number")
    while upperBound <= lowerBound:
        print("Sorry, please enter a number higher than {}".format(lowerBound))
        upperBound = not_number_rejector("Enter a high number")

    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = int(raw_input("Guess a number: "))
            print("you guessed {}".format(guessedNumber))
            if guessedNumber == actualNumber:
                print("you got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < lowerBound:
                print("Number out of bounds")
            elif guessedNumber > upperBound:
                print("Number out of bounds")
            elif guessedNumber < actualNumber:
                print("too small, try again")
            else:
                print("too big, try again")
        except Exception as e:
            print ("Error, try again!", e)
    return "You got it!"


"""
    message = ("Please give me a number between {} and {}: "
               .format(low, high))

    while True:
        try:
            guessed_number = int(raw_input(message))
            if low < guessed_number < high:
                print ("That's it, nice work!")
                return guessed_number
            else:
                print ("Sorry, that's not a number between {} and {}"
                       .format(low, high))
        except Exception as e:
            print ("Sorry, that's not an actual number, try again!" + "\n", e)
"""

if __name__ == "__main__":
    advancedGuessingGame()
