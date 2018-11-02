"""
Module for the Cell class
"""

class Cell:
	def __init__(self, column, row, width, height):
		self.__col = column
		self.__row = row
		self.__neighbors = [(row + y, column + x) for y,x in [(-1, 0), (0, 1), (1, 0), (0, -1)] if 0 <= column + x < width  and 0 <= row + y < height]
		self.__visited = False
		self.__walls = [True, True, True, True]

	def make_visited(self):
		self.__visited = True

	def make_unvisited(self):
		self.__visited = False

	def get_column(self):
		return self.__col

	def get_row(self):
		return self.__row

	def is_visited(self):
		return self.__visited

	def get_neighbors(self):
		return self.__neighbors

	def get_accessible_neighbors(self):
		"""
		This depends if there is a wall or not, the function will only return the neighbors which don't have any wall on this side
		"""
		accessibles = []
		# TODO: Improve not to reroll through all the possible neighbors everytime
		i = 0
		for y,x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
			if (self.__row + y, self.__col + x) in self.__neighbors:
				if not self.__walls[i]:
					accessibles.append((self.__row + y, self.__col + x))
			i += 1
		return accessibles


	def set_walls(self, l):
		assert len(l) == 4, "The list should have 4 elements"
		self.__walls = l

	def remove_wall(self, i):
		self.__walls[i] = False

	def get_walls(self):
		return self.__walls

	def remove_wall_between_cell(self, another_cell):
		"""
		Removes the wall between this cell and another cell (setting its value from True to False)
		:CU: The two cells must be neighbors
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



