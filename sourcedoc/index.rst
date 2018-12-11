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

.. list-table:: Timings
   :widths: 25 50
   :header-rows: 1

   * - Width and height
     - Time to generate 10 mazes (in seconds)
   * - 10 x 10
     - 0.038097507999964364
   * - 20 x 20
     - 0.22399029899997913
   * - 30 x 30
     - 0.5100063020000221
   * - 40 x 40
     - 1.3165600109999787
   * - 50 x 50
     - 1.4434121799999957
   * - 60 x 60
     - 2.5921263440000075
   * - 70 x 70
     - 4.555961325999988
   * - 80 x 80
     - 5.949108254000009
   * - 90 x 90
     - 5.2760409919999915
   * - 100 x 100
     - 19.35612800299998

Commit order
============

2018-12-11 15:45 Finished the doc
2018-12-11 15:38 Added the table with timings
2018-12-11 15:17 added timings
2018-12-11 15:17 added timings
2018-12-11 15:00 few more things
2018-12-10 15:07 Added some fussy details
2018-12-10 14:58 Generated sphinx doc
2018-12-10 14:09 Made a separate file
2018-12-10 13:47 Added some argparse
2018-12-08 17:47 TOTALLY FINISHED
2018-12-08 17:40 clean doctests
2018-12-08 17:19 Added the examples for the maze
2018-12-08 16:56 Ended rst of maze
2018-12-08 15:12 Added doc
2018-12-08 15:07 PEP correct for maze + docstring
2018-12-08 14:38 Pause
2018-12-08 13:54 Working now ?
2018-12-08 13:49 Added the documentation for the graphical maze
2018-12-08 13:31 maze is now PEP correct
2018-12-08 13:14 graphical maze is now OK with PEP
2018-12-08 13:12 cell is now ok with PEP
2018-12-07 10:07 La DOOOOOOOOOOOOOOOOOOOOOC
2018-12-07 09:51 I hate documenting (cell)
2018-12-07 00:12 Some renaming
2018-12-05 14:23 Need to start the doc
2018-12-05 14:17 reorganisation
2018-12-04 18:28 Added a structure from another Practical
2018-11-05 09:33 Added save_desc_to_file method in the Maze class but atm it is the same as save_to_file, awaiting for more information about this method
2018-11-05 09:23 Renamed generate_text_file by save_to_file in Maze class
2018-11-05 09:19 Replaced the Method class name by MAZE
2018-11-04 14:52 Finished graphical module for mazes
2018-11-04 14:51 Merge branch 'master' of https://bitbucket.org/Etilawin/maze
2018-11-04 14:50 Revert "Revert "Created the graphical module for maze""
2018-11-04 14:50 Revert "Revert "Revert "Created the graphical module for maze"""
2018-11-04 14:50 Revert "Revert "Created the graphical module for maze""
2018-11-04 14:50 Revert "Created the graphical module for maze"
2018-11-04 14:46 Created the graphical module for maze Started documenting the modules
2018-11-04 14:46 Started documenting the modules
2018-11-02 16:58 Modified so it works perfectly
2018-11-02 16:21 Same as last but for method generate_by_algorithm
2018-11-02 16:19 Adapted the generate_by_hand method
2018-11-02 16:11 Added flags and remade the generate_by_file method
2018-11-02 15:49 Added solution finder
2018-10-30 18:24 Adding the algorithm to generate maze
2018-10-30 12:53 Removed the __pycache__ folder
2018-10-30 12:52 Added generation of a maze by text, and corrected mistakes
2018-10-28 14:00 Ended theorical implementation for hand made mazes
2018-10-28 13:59 Ended theorical implementation for hand made mazes
2018-10-27 11:36 First commit

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
