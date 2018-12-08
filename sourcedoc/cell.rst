===================
:mod: `cell` module
===================

Module description
------------------

Ce module définit une classe pour représenter les cellules d'un labyrinthe,
ces cellules ont 4 murs ou moins et peuvent-être 'visitées' au besoin des
algorithmes. Chaque cellule a une position, ce qui permet de déterminer ses
voisins.

Une cellule peut

* Etre visitée ou non
* Avoir un certain nombre de murs
* Avoir un certain nombre de voisins
* Avoir une ligne et une colonne ce qui permet de la détecter et éviter de
  recalculer les voisins à chaque fois

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
