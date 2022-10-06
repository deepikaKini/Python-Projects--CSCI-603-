__author__ = 'dk1346'



"""
CSCI-603: Recursion (week 3)
Author: Deepika Kini

This is a demo program that draws the fractal antenna using 2 strategies.
Other functionality include checking for float/int inputs (data validation)
using regex 
and clearing screen between strategies.
also using tracer to avoid animation

note:
Output is modeled as present in FractalAntenna.pdf
Please use float value in input for side
"""

import turtle as t
import math
import re


def fractal_strategy1(n, level):
    """
    Draw fractal pattern using strategy 1 ie. using lab
    question as reference.
    :param n: the width of the diagram
    :param level: the level of recursion
    :return: len1: length of sides drawn
    """
    len1 = 0

    if level == 1:
        t.forward(n)
        return n

    else:
        len1 += fractal_strategy1(n / 3, level - 1)
        t.left(90)
        len1 += fractal_strategy1(n / 3, level - 1)
        t.right(90)
        len1 += fractal_strategy1(n / 3, level - 1)
        t.right(90)
        len1 += fractal_strategy1(n / 3, level - 1)
        t.left(90)
        len1 += fractal_strategy1(n / 3, level - 1)
        return len1


def fractal_strategy2(n, level):
    """
    Draw fractal pattern using strategy 2 ie. using squares
    :param n: the width of the diagram
    :param level: the level of recursion
    :return: len2: length of sides drawn
    """
    len2 = 0
    if level == 1:
        t.penup()
        t.forward(n / math.sqrt(2))
        t.pendown()
        t.left(135)
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.right(45)
        t.penup()
        t.backward(n / math.sqrt(2))
        t.pendown()
        return n * 4


    else:
        len2 += fractal_strategy2(n / 3, level - 1)
        i = 0
        while i < 4:
            t.penup()
            t.forward(math.sqrt(2) * n / 3)
            t.pendown()
            len2 += fractal_strategy2(n / 3, level - 1)
            t.penup()
            t.backward(math.sqrt(2) * n / 3)
            t.pendown()
            t.left(90)
            i += 1
        return len2


def data_validation():
    """
    checks the inputs of users using regex expression
    :return: n: user-inputed size
    :return: n: user-inputed level
    """
    check = 0
    n = input("Length of initial side: ")
    if re.fullmatch('[0-9]+\.[0-9]', n) is not None:
        check = 1
    while check == 0:
        n = input("Error! Length of initial side in float: ")
        if re.fullmatch('[0-9]+\.[0-9]', n) is not None:
            check = 1

    check = 0
    level = input("Number of levels: ")
    if re.fullmatch('\d', level) is not None:
        check = 1
    while check == 0:
        level = input("Error! Number of levels in Integer: ")
        if re.fullmatch('\d', level) is not None:
            check = 1
    return n, level


def run_strategy1(n, level):
    """
    initialises the run for strategy 1 by passing inputs and getting length
    :param n: the width of the diagram
    :param level: the level of recursion
    :return: len1: length of sides drawn
    """
    t.left(45)
    len1 = 0
    i = 0
    t.tracer(0, 0)  # avoid animation
    while i < 4:
        len1 += fractal_strategy1(float(n), int(level))
        t.left(90)
        i += 1
    t.update()
    return len1

def run_strategy2(n, level):
    """
    initialises the run for strategy 2 by passing inputs and getting length
    :param n: the width of the diagram
    :param level: the level of recursion
    :return: len2: length of sides drawn
    """
    t.tracer(0, 0)
    len2 = fractal_strategy2(float(n), int(level))
    t.update()
    return len2


def init():
    """
    initialises paramters for turtle screen
    """
    t.setheading(0)
    t.title('Fractal Antenna')
    t.setup(1000, 1200)  # set window size
    t.hideturtle()


def main():
    init()

    # Strategy 1

    # take inputs after validation
    n, level = data_validation()
    # run strategy 1 and get length of lines
    len1 = run_strategy1(n, level)
    print("Strategy 1 - Antenna’s length is ", round(len1, 2), " units.")

    # clear screen for next strategy
    input("Hit enter to continue...")
    t.reset()

    # Strategy 2

    init()

    #taking same values of n and level in this strategy as well
    len2 = run_strategy2(n, level)

    print("Strategy 2 - Antenna’s length is ", round(len2, 2), " units.")

    print("Bye!")

    t.mainloop()


if __name__ == "__main__":
    main()
