"""
Module for the Cell class
"""

class Cell:
	def __init__(self, column, line, width, height):
		self.__col = column
		self.__line = line
		self.__neighbors = [(x,y) for x,y in [(0, +1), (+1, 0), (0, -1), (-1, 0)] if 0 <= column + x < width  and 0 <= line + y < height]
		self.__visited = False
		self.__walls = [True, True, True, True]

	def make_visited(self):
		self.__visited = True

	def is_visited(self):
		return self.__visited

	def get_neighboors(self):
		return self.__neighbors

	def set_walls(self, l):
		assert len(l) == 4, "the list should have 4 elements"
		self.__walls = l

	def get_walls(self):
		return self.__walls