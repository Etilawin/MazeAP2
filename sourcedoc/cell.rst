===================
:mod: `cell` module
===================


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

.. autoclass:: Cell.Cell

Methods
-------

.. automethod:: cell.Cell.is_revealed

.. automethod:: cell.Cell.reveal

.. automethod:: cell.Cell.is_bomb

.. automethod:: cell.Cell.set_bomb

.. automethod:: cell.Cell.is_hypothetic

.. automethod:: cell.Cell.set_hypothetic

.. automethod:: cell.Cell.unset_hypothetic

.. automethod:: cell.Cell.number_of_bombs_in_neighborhood

.. automethod:: cell.Cell.incr_number_of_bombs_in_neighborhood


Special method
--------------

Only two special methods for this class.

.. automethod:: cell.Cell.__init__

.. automethod:: cell.Cell.__str__
