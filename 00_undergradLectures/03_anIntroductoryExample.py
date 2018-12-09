# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 01:52:31 2018

@author:    manma
@purpose:   QuantEcon Python Lectures
            -   Python by Example
"""
# %% EX 1
"""
Recall that n! is read as “n factorial” and defined as n! = n × (n−1)×...×2×1
There are functions to compute this in various modules, but let’s write
our own version as an exercise

In particular, write a function factorial such that factorial(n) returns
n! for any positive integer n
"""


def factorial(n):
    j = 1
    for i in range(2, n + 1):
        j *= i
    return j


# %% EX 2
"""
The binomial random variable Y∼Bin(n,p) represents the number of successes
in n binary trials, where each trial succeeds with probability p

Without any import besides from numpy.random import uniform, write a
function binomial_rv such that binomial_rv(n, p) generates one draw of Y

Hint: If U is uniform on (0,1) and p∈(0,1), then the expression U < p
evaluates to True with probability p
"""
from numpy.random import uniform  # noqa: E402


def binomial_rv(n, p):
    rands = [uniform() for i in range(n)]
    counts = len([i for i in rands if i < p])
    return counts


# %% EX 3
"""
Compute an approximation to π using Monte Carlo. Use no imports besides

import numpy as np
Your hints are as follows:

If U is a bivariate uniform random variable on the unit square (0,1)2,
then the probability that U lies in a subset B of (0,1)2 is equal to the
area of B
If U1,…,Un are iid copies of U, then, as n gets large, the fraction that
fall in B converges to the probability of landing in B

For a circle, area = pi * radius^2
"""
import numpy as np  # noqa: E402


def mc_pi(n_times):
    count = 0
    for i in range(n_times):
        u, b = np.random.uniform(), np.random.uniform()
        if u ** 2 + b ** 2 < 0.5:
            count += 1
    area = count / n_times
    return area / 0.5 ** 2


# %% EX 4
"""
Write a program that prints one realization of the following random device:

Flip an unbiased coin 10 times
If 3 consecutive heads occur one or more times within this sequence,
pay one dollar
If not, pay nothing
Use no import besides from numpy.random import uniform
"""


def payup():
    rands = list(map(lambda x: 1 if x > 0.5 else 0, uniform(size=10)))
    head_counter = 0
    for idx, rand in enumerate(rands):
        if rand == 1:
            head_counter += 1
        else:
            head_counter = 0
        if head_counter >= 3:
            pay = 1
            break
        else:
            pay = 0
    return 'Your payout is ${}'.format(pay)


# %% EX 5
"""
our next task is to simulate and plot the correlated time series

xt+1=αxt+εt+1wherex0=0andt=0,…,T
The sequence of shocks {εt} is assumed to be iid and standard normal

Set T=200 and α=0.9
"""
import matplotlib.pyplot as plt  # noqa E402


def ts():
    a = 0.9
    T = 200
    y = 0
    ys = []
    for i in range(1, T + 1):
        y = y * a + np.random.normal()
        ys.append(y)

    xs = list(range(1, 201))
    _ = plt.plot(xs, ys)
    return _


# %% EX 6
"""
To do the next exercise, you will need to know how to produce a plot legend

The following example should be sufficient to convey the idea

Now, starting with your solution to exercise 5, plot three simulated
time series, one for each of the cases α=0, α=0.8 and α=0.98
"""


def ex6():
    az = [0, 0.8, 0.98]
    T = 200
    y = 0
    xs = list(range(1, 201))
    for alpha in az:
        ys = []
        for i in range(1, T + 1):
            y = y * alpha + np.random.normal()
            ys.append(y)
        _ = plt.plot(xs, ys, label=r'$\alpha$= {}'.format(alpha))
    plt.legend()
    return _
