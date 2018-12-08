===================
:mod: `cell` module
===================

Module description
------------------

This module defines a class to represent the cells of a maze, each cell has
4 walls or less and might be visited if needed by the algorithms. Each cell
has a position, which allows to determine its neighbors.

One cell may

* Be visited or not
* Have a certain amount of walls
* Have a certain amount of neighbors
* Have a position with a line and a col, which avoid recalculing the neighbors
  everytime

Class description
-----------------

.. autoclass:: cell.Cell

Methods
-------

.. automethod:: cell.Cell.make_visited

.. automethod:: cell.Cell.make_unvisited

.. automethod:: cell.Cell.get_column

.. automethod:: cell.Cell.get_row

.. automethod:: cell.Cell.is_visited

.. automethod:: cell.Cell.get_neighbors

.. automethod:: cell.Cell.get_accessible_neighbors

.. automethod:: cell.Cell.set_walls

.. automethod:: cell.Cell.remove_wall

.. automethod:: cell.Cell.get_walls

.. automethod:: cell.Cell.remove_wall_between_cell


Special methods
---------------

.. automethod:: cell.Cell.__init__

.. automethod:: cell.Cell.__str__

.. automethod:: cell.Cell.__repr__
