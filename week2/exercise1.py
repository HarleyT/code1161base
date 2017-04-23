"""Tidy up this file.

This file runs, but it's a mess!
Go through it and change it until there are no more linter errors or warnings.
Make sure that your code still runs without any errors by pressing
[ctrl]+[shift]+[b] as often as you think you need to.
"""
from __future__ import division
from __future__ import print_function
import os


def useful_function():
    """Get Current Working Directory.

    Uses the getcwd() function to get the current working directory
    and prints it.
    """
    print(os.getcwd())
    print("hello! Let's get started")
    jobs = ['get', 'this',
            'file', 'to', 'pass',
            'the', 'linter']
    In_other_words = "make it show no linter errors"
    print(jobs)
    print(In_other_words)
    print (1+1, "is smaller than", 7*0.5, "is", (1+1) < (7*0.5),
           ", which is a relief!")


if __name__ == "__main__":
    print(useful_function())
