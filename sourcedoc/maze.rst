===================
:mod: `maze` module
===================

Module description
------------------

This module is the main module of this project. It allows to create a maze
from the class Maze. It has also a class to provide methods to create the maze.

A maze may

* Have a width and height which almost defines everything
* Have a `board` which is basically the whole maze, composed with cells
* Be saved to a file
* Generate path from one way to another

It requires the mod :mod:`cell`.

MAZE class
==========

Class description
-----------------

.. autoclass:: maze.MAZE

Maze class
==========

Class description
-----------------

.. autoclass:: maze.Maze

Public methods
--------------

.. automethod:: maze.Maze.get_width

.. automethod:: maze.Maze.get_height

.. automethod:: maze.Maze.get_board

.. automethod:: maze.Maze.get_cell

.. automethod:: maze.Maze.save_to_file

.. automethod:: maze.Maze.find_path

Private methods
---------------

.. automethod:: maze.Maze._Maze__generate_by_hand

.. automethod:: maze.Maze._Maze__generate_by_file

.. automethod:: maze.Maze._Maze__generate_by_algorithm

.. automethod:: maze.Maze._Maze__unvisit_all_cells

Special methods
---------------

.. automethod:: maze.Maze.__init__

.. automethod:: maze.Maze.__repr__

.. automethod:: maze.Maze.__str__
