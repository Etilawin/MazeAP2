=================
Fibonacci numbers
=================

What are Fibonacci numbers?
===========================

Fibonacci numbers are a sequence of numbers defined by the two first terms :

.. math::

   f_0 = 0\\
   f_1 = 1

and for all :math:`n\geq 0` by the following recursion relation :

.. math::

   f_{n+2} = f_{n+1} + f_n

Here are the Fibonacci numbers for :math:`0\leq n \leq 10` :

.. table:: 
   Table of the first Fibonacci numbers

   ===========    ============
   :math:`n`       :math:`f_n`  
   ===========    ============
   0              0
   1              1
   2              1
   3              2
   4              3
   5              5
   6              8
   7              13
   8              21
   9              34
   10             55
   ===========    ============

Limits of the function
======================

The function being recursive, it may take more time for large numbers.

.. table::
   Table that trace the calls of the function in function of :math:`n`

   ==========  ===================
   :math:`n`    :math:`f_n` calls
   ==========  ===================
   0           1
   1           1
   2           3
   3           5
   4           9
   5           15
   6           25
   7           41
   8           67
   9           109
   10          177
   ...         ...
   40          331160280
   ==========  ===================

We can deduce from this table that the numbers of call for n is following the rules:

.. math::
   a_n = a_{n-1} + a_{n-2} + 1
