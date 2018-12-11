------
 Maze
------

Description
===========

This project has many features to build and solve a maze. To achieve that it
uses an itarative algorithm called 'Recursive backtracker' to generate the maze.
It is also possible to generate it by hand, or by file.
Then you can either use the graphical interface implemented to show it on your
screen, or save it in a file.

Getting Started
===============

Before starting this project you need to be sure to have python3 or higher and
optionnally tkinter to have a graphical interface.

QuickStart
----------

* From the console

.. code::

    $ cd maze
    $ python3 src/main.py
    $ python3 src/main.py -h # Gives help
    ...

* From python

  >>> from maze import *
  >>> a_maze = Maze(width = 50, height = 50, method = MAZE.algorithm)
  >>> solution = a_maze.find_path(0,0,49,49)
  >>> a_maze.save_to_file('temporary_file.txt')
  >>> from graphicalmaze import *
  >>> show(a_maze)
  >>> show_path(a_maze, solution)


Generate by algorithm
---------------------


  >>> a_maze = Maze(width = 50, height = 50, method = MAZE.algorithm)


Generate by file
----------------


  >>> a_maze = Maze(method = MAZE.file, path = "PathToMyFile.txt")


Generate by hand
----------------


  >>> a_maze = Maze(width = 50, height = 50, method = MAZE.hand)


Find a solution
---------------


  >>> solution = a_maze.find_path(0,0,49,49)


Save to a file
--------------


  >>> a_maze.save_to_file('temporary_file.txt')

Using graphical interface
-------------------------

  >>> import graphicalmaze
  >>> from maze import *
  >>> some_maze = Maze(width = 50, height = 50, method = MAZE.algorithm)
  >>> graphicalmaze.show(some_maze)
  >>> a_path = a_maze.find_path(0,0,49,49)
  >>> graphicalmaze.show_path(some_maze, a_path)

Timings
=======

To generate a maze of 50 by 50 it takes approximately 0.1 seconds.

Project tree
============

.. toctree::
   :maxdepth: 1

   cell
   graphicalmaze
   maze
   main



Indices and tables
==================

* :ref:`search`
