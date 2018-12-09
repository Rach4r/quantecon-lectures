# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:44:42 2018

@author: manma
@purpose:   QuantEcon Python Lectures
            -   Python Essentials
"""

# %% EX 1
"""
Part 1: Given two numeric lists or tuples x_vals and y_vals of equal length,
compute their inner product using zip()

Part 2: In one line, count the number of even numbers in 0,…,99
Hint: x % 2 returns 0 if x is even, 1 otherwise

Part 3: Given pairs = ((2, 5), (4, 2), (9, 8), (12, 10)), count the
number of pairs (a, b) such that both a and b are even
"""


def pt1():
    x_vals = list(range(1, 101))
    y_vals = list(range(101, 201))
    dot = sum([a * b for a, b in zip(x_vals, y_vals)])
    return dot


def pt2(n):
    evens = len([i for i in range(n) if i % 2 == 0])
    return evens


def pt3():
    pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
    count = 0
    for a, b in pairs:
        if (a % 2 == 0) & (b % 2 == 0):
            count += 1
    return count


# %% EX 2
"""
Consider the polynomial

p(x)=a0+a1x+a2x2+⋯anxn=∑i=0naixi(1)
Write a function p such that p(x, coeff) that computes the value in (1)
given a point x and a list of coefficients coeff

Try to use enumerate() in your loop
"""


def p(x, coeff):
    result = sum([coef * x ** idx for idx, coef in enumerate(coeff)])
    return result


# %% EX 3
"""
Write a function that takes a string as an argument and returns the number
of capital letters in the string

Hint: 'foo'.upper() returns 'FOO'
"""


def countcap(string):
    count = sum([letter.isupper() for letter in string])
    return count


# %% EX 4
"""
Write a function that takes two sequences seq_a and seq_b as arguments
and returns True if every element in seq_a is also an element of seq_b,
else False

By “sequence” we mean a list, a tuple or a string
Do the exercise without using sets and set methods
"""


def compare(seq_a, seq_b):
    bools = sum([a in seq_b for a in seq_a])

    if bools == len(seq_a):
        return True
    else:
        return False


# %% EX 5
"""
When we cover the numerical libraries, we will see they include many
alternatives for interpolation and function approximation

Nevertheless, let’s write our own function approximation routine as
an exercise

In particular, without using any imports, write a function linapprox
that takes as arguments

A function f mapping some interval [a,b] into R
two scalars a and b providing the limits of this interval
An integer n determining the number of grid points
A number x satisfying a <= x <= b
and returns the piecewise linear interpolation of f at x, based on
n evenly spaced grid points a = point[0] < point[1] < ... < point[n-1] = b

Aim for clarity, not efficiency
"""
# =============================================================================
# Not my solution :(
# =============================================================================


def linapprox(f, a, b, n, x):
    """
    Evaluates the piecewise linear interpolant of f at x on the interval
    [a, b], with n evenly spaced grid points.

    Parameters
    ===========
        f : function
            The function to approximate

        x, a, b : scalars (floats or integers)
            Evaluation point and endpoints, with a <= x <= b

        n : integer
            Number of grid points

    Returns
    =========
        A float. The interpolant evaluated at x

    """
    length_of_interval = b - a
    num_subintervals = n - 1
    step = length_of_interval / num_subintervals

    # === find first grid point larger than x === #
    point = a
    while point <= x:
        point += step

    # === x must lie between the gridpoints (point - step) and point === #
    u, v = point - step, point

    return f(u) + (x - u) * (f(v) - f(u)) / (v - u)
