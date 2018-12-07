#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: `Kim Vallée <kim.vallee.etu@univ-lille.fr>`_

:date:  2018, november

This module implements the Cell class used to represent a cell in the maze.

"""

class Cell:
	""" Cell class to generate a Maze """

	def __init__(self, row, column, width, height):
		"""
		Init function to create a cell

		:param row: the row position of the cell
		:type row: int
		:param column: the column position of the cell
		:type column: int
		:param width: the width of the maze
		:type width: int
		:param height: the height of the maze
		:type height: int

		:examples:

		>>> cell = Cell(1, 0, 5, 5)
		>>> cell.get_neighbors()
		[(0, 0), (1, 1), (2, 0)]
		>>> cell.is_visited()
		False
		>>> cell.make_visited()
		>>> cell.is_visited()
		True
		>>> cell.get_row()
		1
		>>> cell.get_column()
		0
		>>> cell.set_walls([True, False, True, False])
		>>> cell.get_accessible_neighbors()
		[(1, 1)]
		>>> print(cell)
		(1, 0)
		>>> near_cell = Cell(0, 0, 5, 5)
		>>> near_cell.get_walls()
		[True, True, True, True]
		>>> cell.get_walls()
		[True, False, True, False]
		>>> cell.remove_wall_between_cell(near_cell)
		>>> cell.get_walls()
		[False, False, True, False]
		>>> near_cell.get_walls()
		[True, True, False, True]
		"""
		self.__col = column
		self.__row = row
		self.__neighbors = [(row + y, column + x) for y,x in [(-1, 0), (0, 1), (1, 0), (0, -1)] if 0 <= column + x < width  and 0 <= row + y < height]
		self.__visited = False
		self.__walls = [True, True, True, True]

	def make_visited(self):
		"""
		Mark the cell as visited
		"""
		self.__visited = True

	def make_unvisited(self):
		"""
		Mark the cell as unvisited
		"""
		self.__visited = False

	def get_column(self):
		"""
		Get the column of a cell
		:return: The column of this cell
		:rtype: int
		"""
		return self.__col

	def get_row(self):
		"""
		Get the row of a cell
		:return: The row of this cell
		:rtype: int
		"""
		return self.__row

	def is_visited(self):
		"""
		Return the status of the cell
		:return: The visited status of this cell
		:rtype: bool
		"""
		return self.__visited

	def get_neighbors(self):
		"""
		Get the neighbors of the cell
		:return: The neighbors of this cell
		:rtype: list
		"""
		return self.__neighbors

	def get_accessible_neighbors(self):
		"""
		Get the neighbors only if there is no wall on this side
		:return: The accessible neighbors only
		:rtype: list
		"""
		accessibles = []
		i = 0
		for y,x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
			if (self.__row + y, self.__col + x) in self.__neighbors:
				if not self.__walls[i]:
					accessibles.append((self.__row + y, self.__col + x))
			i += 1

		return accessibles

	def __repr__(self):
		"""
		Reinvocking the str function
		:return: a 'tuple' of the form (self.__row, self.__column)
		:rtype: str
		"""
		return self.__str__()

	def __str__(self):
		"""
		Allows to see it only with its position
		:return: a 'tuple' of the form (self.__row, self.__column)
		:rtype: str
		"""
		return "({}, {})".format(self.__row, self.__col)

	def set_walls(self, l):
		"""
		Set the walls of this cell
		:param l: A list containing all the new walls status
		:type l: list
		:CU: len(l) == 4 and all the elements are booleans
		"""
		assert len(l) == 4, "The list should have 4 elements"
		assert all(isinstance(x, bool) for x in l),\
			"Only booleans should be inside"
		self.__walls = l

	def remove_wall(self, i):
		"""
		Remove the walls of this cell
		"""
		self.__walls[i] = False

	def get_walls(self):
		"""
		Get the walls of this cell
		:return: The walls of this cell
		:rtype: list
		"""
		return self.__walls

	def remove_wall_between_cell(self, another_cell):
		"""
		Removes the wall between this cell and another cell
		(setting its value from True to False)
		:CU: The two cells must be neighbors,
			 and another cell should be an instance of Cell
		"""
		assert isinstance(another_cell, Cell), "The cell given should be a Cell object"
		assert self is not another_cell, "The given cell should be another cell"
		assert (another_cell.get_row(), another_cell.get_column()) in self.__neighbors, "The two cells are not neighbors"

		col_diff  = self.__col  - another_cell.get_column()
		row_diff = self.__row - another_cell.get_row()

		if col_diff:
			self.remove_wall(2 + col_diff)
			another_cell.remove_wall(2 - col_diff)
		else:
			self.remove_wall(1 - row_diff)
			another_cell.remove_wall(1 + row_diff)

if __name__ == "__main__":
	import doctest
	doctest.testmod()
