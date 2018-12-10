================
:app: `main` app
================

Application description
=======================

This little console application allows you to generate a maze directly from the
console. It will then show you the result with tkinter and optionnally the
path from one cell to another if you feed it one.
It is also able to save the maze generated to a given location.

Getting started
===============

From the console
----------------
    $ cd maze
    $ python3 src/main.py -h # Prints help
    ...
    $ python3 src/main.py --size 50 50 # Generates a 50 by 50 maze
    $ python3 src/main.py --method file --input somefile.txt --path 0 0 1 1
