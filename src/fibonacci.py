#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`fibonacci`

:author: `Kim Vallée`

:date: 2017, september. Lasr revised: 2018, september

Fibonnaci recursion
"""

from ap2_decorators import *

@trace
@count
def fibo(n):
    """
    Computes the nth number of the fibonacci sequence
    using recursitivity

    :param n: A natural number
    :return: The nth number in the fibonacci sequence
    :UC: n >= 0

    Examples:

    >>> fibo(3)
     -> fibo((3,), {})
    ... -> fibo((2,), {})
    ...... -> fibo((1,), {})
    ...... <- 1
    ...... -> fibo((0,), {})
    ...... <- 0
    ... <- 1
    ... -> fibo((1,), {})
    ... <- 1
     <- 2
    2

    >>> fibo(4)
     -> fibo((4,), {})
    ... -> fibo((3,), {})
    ...... -> fibo((2,), {})
    ......... -> fibo((1,), {})
    ......... <- 1
    ......... -> fibo((0,), {})
    ......... <- 0
    ...... <- 1
    ...... -> fibo((1,), {})
    ...... <- 1
    ... <- 2
    ... -> fibo((2,), {})
    ...... -> fibo((1,), {})
    ...... <- 1
    ...... -> fibo((0,), {})
    ...... <- 0
    ... <- 1
     <- 3
    3
    """

    assert isinstance(n, int) and n >= 0,\
        "n must be a natural number"

    if n in (0, 1):
        res = n
    else:
        res = fibo(n - 1)\
            + fibo(n - 2)

    return res


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod()

    n = int(sys.argv[1])
    print(fibo(n))

## n = 3
## 7 appels
## 15 lignes

## n = 4
## 9 appels
## 19 lignes

## n = 5
## 15 appels
## 31 lignes

## Donc pour n appels on a 2n + 1 lignes
