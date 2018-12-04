#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`recursion_tracing`

:author: `Kim Vallée`_

:date: 2017, september. Lasr revised: 2018, september

Examples of recursion tracings.
"""

from ap2_decorators import trace

@trace
def fact(n):
    """
    Computes the factorial of natural number n.
    Tracks recursive calls if optional parameter is set to True.

    :param n: natural number
    :return: factorial of n
    :UC: n >= 0
    :Examples:

    >>> fact(10)
      -> fact((10,), {})
    ... -> fact((9,), {})
    ...... -> fact((8,), {})
    ......... -> fact((7,), {})
    ............ -> fact((6,), {})
    ............... -> fact((5,), {})
    .................. -> fact((4,), {})
    ..................... -> fact((3,), {})
    ........................ -> fact((2,), {})
    ........................... -> fact((1,), {})
    .............................. -> fact((0,), {})
    .............................. <- 1
    ........................... <- 1
    ........................ <- 2
    ..................... <- 6
    .................. <- 24
    ............... <- 120
    ............ <- 720
    ......... <- 5040
    ...... <- 40320
    ... <- 362880
     <- 3628800
    3628800
    >>> fact(5)
      -> fact((5,), {})
    ... -> fact((4,), {})
    ...... -> fact((3,), {})
    ......... -> fact((2,), {})
    ............ -> fact((1,), {})
    ............... -> fact((0,), {})
    ............... <- 1
    ............ <- 1
    ......... <- 2
    ...... <- 6
    ... <- 24
     <- 120
    120


    """
    assert isinstance(n, int) and n >= 0,\
        'parameter n must be a non negative integer'

    if n == 0:
        res = 1
    else:
        res = n * fact(n - 1)

    return res

@trace
def add(a, b):
    """
    Computes a + b in a recursive way.
    Tracks recursive calls if talkative parameter is set to True.

    :param a: natural number
    :param b: natural number
    :return: the addition of a and b
    :UC: a >= 0 b >= 0

    ->Examples:

    >>> add(1, 2)
     -> add((1, 2), {})
    ... -> add((1, 1), {})
    ...... -> add((1, 0), {})
    ...... <- 1
    ... <- 2
     <- 3
    3
    >>> add(8, 3)
     -> add((8, 3), {})
    ... -> add((8, 2), {})
    ...... -> add((8, 1), {})
    ......... -> add((8, 0), {})
    ......... <- 8
    ...... <- 9
    ... <- 10
     <- 11
    11
    """
    assert isinstance(a, int) and a >= 0,\
        "a must be a positive integer"
    assert isinstance(b, int) and b >= 0,\
        "b must be a positive integer"

    if b == 0:
        res = a
    else:
        res = 1 + add(a, b - 1)

    return res

@trace
def is_palindromic(text):
    """
    Predicate that tells if 'text' is palindromic
    Tracks recursive calls if talkative parameter is set to True.

    :param text: (str) A string we want to check
    :return: True if it is palindromic, False otherwise
    :CU: None

    Examples:

    >>> is_palindromic("No lemons no melon")
     -> is_palindromic(('No lemons no melon',), {})
    ... -> is_palindromic(('olemonsnomelo',), {})
    ...... -> is_palindromic(('lemonsnomel',), {})
    ......... -> is_palindromic(('emonsnome',), {})
    ............ -> is_palindromic(('monsnom',), {})
    ............... -> is_palindromic(('onsno',), {})
    .................. -> is_palindromic(('nsn',), {})
    ..................... -> is_palindromic(('s',), {})
    ..................... <- True
    .................. <- True
    ............... <- True
    ............ <- True
    ......... <- True
    ...... <- True
    ... <- True
     <- True
    True
    >>> is_palindromic("No lemons non melon")
     -> is_palindromic(('No lemons non melon',), {})
    ... -> is_palindromic(('olemonsnonmelo',), {})
    ...... -> is_palindromic(('lemonsnonmel',), {})
    ......... -> is_palindromic(('emonsnonme',), {})
    ............ -> is_palindromic(('monsnonm',), {})
    ............... -> is_palindromic(('onsnon',), {})
    .................. -> is_palindromic(('nsno',), {})
    ..................... -> is_palindromic(('sn',), {})
    ........................ -> is_palindromic(('',), {})
    ........................ <- True
    ..................... <- False
    .................. <- False
    ............... <- False
    ............ <- False
    ......... <- False
    ...... <- False
    ... <- False
     <- False
    False
    """

    assert isinstance(text, str),\
        "The text parameter must be a string"

    text = text.lower()
    text = text.replace(" ", "")

    if len(text) in (0, 1):
        res = True
    else:
        res = is_palindromic(text[1:-1])\
            and (text[0] == text[-1])
        # The other way would only consier the first part and therefore...
        # Not really recursive
    return res

@trace
def binomial(n, k):
    """
    Computes the binomial coefficient
    Tracks recursive calls if talkative parameter is set to True.

    :param n: positive integer
    :param k: positive integer
    :return: the binomial coefficient for (n, k)
    :CU: k <= n

    Examples:

    >>> binomial(5, 3)
     -> binomial((5, 3), {})
    ... -> binomial((4, 3), {})
    ...... -> binomial((3, 3), {})
    ...... <- 1
    ...... -> binomial((3, 2), {})
    ......... -> binomial((2, 2), {})
    ......... <- 1
    ......... -> binomial((2, 1), {})
    ............ -> binomial((1, 1), {})
    ............ <- 1
    ............ -> binomial((1, 0), {})
    ............ <- 1
    ......... <- 2
    ...... <- 3
    ... <- 4
    ... -> binomial((4, 2), {})
    ...... -> binomial((3, 2), {})
    ......... -> binomial((2, 2), {})
    ......... <- 1
    ......... -> binomial((2, 1), {})
    ............ -> binomial((1, 1), {})
    ............ <- 1
    ............ -> binomial((1, 0), {})
    ............ <- 1
    ......... <- 2
    ...... <- 3
    ...... -> binomial((3, 1), {})
    ......... -> binomial((2, 1), {})
    ............ -> binomial((1, 1), {})
    ............ <- 1
    ............ -> binomial((1, 0), {})
    ............ <- 1
    ......... <- 2
    ......... -> binomial((2, 0), {})
    ......... <- 1
    ...... <- 3
    ... <- 6
     <- 10
    10
    >>> binomial(2, 1)
     -> binomial((2, 1), {})
    ... -> binomial((1, 1), {})
    ... <- 1
    ... -> binomial((1, 0), {})
    ... <- 1
     <- 2
    2
    """

    assert isinstance(n, int) and n >= 0,\
        "n must be a positive integer"

    assert isinstance(k, int) and k >= 0,\
        "n must be a positive integer"

    assert k <= n,\
        "k must be less or equal to n"

    if n == k or k == 0:
        res = 1
    else:
        # Using the recursion formula
        res = binomial(n - 1, k    )\
            + binomial(n - 1, k - 1)

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
