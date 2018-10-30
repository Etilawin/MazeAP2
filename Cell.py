"""
Module for the Cell class
"""

class Cell:
	def __init__(self, column, line, width, height):
		self.__col = column
		self.__line = line
		self.__neighbors = [(line + y, column + x) for x,y in [(0, +1), (+1, 0), (0, -1), (-1, 0)] if 0 <= column + x < width  and 0 <= line + y < height]
		self.__visited = False
		self.__walls = [True, True, True, True]

	def make_visited(self):
		self.__visited = True

	def get_column(self):
		return self.__col

	def get_line(self):
		return self.__line

	def is_visited(self):
		return self.__visited

	def get_neighbors(self):
		return self.__neighbors

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
		assert (another_cell.get_line(), another_cell.get_column()) in self.__neighbors, "The two cells are not neighbors"

		col_diff  = self.__col  - another_cell.get_column()
		line_diff = self.__line - another_cell.get_line()

		if col_diff:
			self.remove_wall(2 + col_diff)
			another_cell.remove_wall(2 - col_diff)
		else:
			self.remove_wall(1 - line_diff)
			another_cell.remove_wall(1 + line_diff)



