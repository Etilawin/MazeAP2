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

  >>> from maze import *
  >>> a_maze = Maze(width = 50, height = 50, method = MAZE.algorithm)
  >>> solution = a_maze.find_path(0,0,49,49)
  >>> a_maze.save_to_file('temporary_file.txt')
  >>> from graphicalmaze import *
  >>> show(a_maze)
  >>> show_path(solution)


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


Project tree
============

.. toctree::
   :maxdepth: 1

   cell
   graphicalmaze
   maze



Indices and tables
==================

* :ref:`search`
