# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Begin the countdown.

    If 'start' is greater than 'stop', count down from 'start'.
    When countdown reaches 'stop', print completion_message
    """
    countdown_list = []
    step = start

    while True:
        try:
            if start > stop:
                step -= 1
                countdown_list.append(message + "{}".format(step))
                return (countdown_list)
            elif start == stop:
                countdown_list.append(completion_message)
                return (countdown_list)
            else:
                return countdown_list
        except Exception as e:
            print ("Error!", e)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Docstring for hypotenuse.

    Calculate the hypotenuse using a given base and height.
    """
    pass


def calculate_area(base, height):
    """Docstring for area.

    Calculate the area using a given base and height.
    """
    pass


def calculate_perimeter(base, height):
    """Docstring for perimeter.

    Calculate the perimeter using a given base and height.
    """
    pass


def calculate_aspect(base, height):
    """Docstring for aspect.

    Calculate the aspect using a given base and height.
    """
    pass


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Docstring for triangle.

    Return the triangle facts using a given base, height and unit(mm) value.
    """
    return {"area": None,
            "perimeter": None,
            "height": None,
            "base": None,
            "hypotenuse": None,
            "aspect": None,
            "units": None}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Docstring for right triangle.

    Give description of right triangle using facts_dictionary.
    """
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Docstring for triangle master.

    Triangle_master.
    """
    if return_diagram and return_dictionary:
        return None
    elif return_diagram:
        return None
    elif return_dictionary:
        return None
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Docstring for wordy_pyramid.

    Creat a pyramid from words using a list of random words from the internet.
    """
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    for i in range(20, 3, -2):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    return pyramid_list


def get_a_word_of_length_n(length):
    """Docstring for word of length (n).

    Get a word of length (n) when length (n) is given.
    """
    pass


def list_of_words_with_lengths(list_of_lengths):
    """Docstring for lists of words with lengths.

    Create a list of words with lengths from a given list of lengths.
    """
    pass


if __name__ == "__main__":
    do_bunch_of_bad_things()
