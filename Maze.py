"""
Module for the Maze class
"""

from Cell import Cell

class Maze:
	def __init__(self, width, height):
		self.__width = width
		self.__height = height
		self.__board = [[Cell(col, line, width, height) for col in range(width)] for line in range(height)] # Empty board

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def generate_by_hand(self):
		print("""
			You are going to generate your maze by hand !
			So you will chose the walls for each cell.
			This will be of the form:
			```
			4 50 [True,True,True,False]
			Chose walls for this cell: True,False,True,False
			```
			Where 4 is the column number
			Where 50 is the line number
			Where [True,True,True,False] is the actual configuration with respectively TOP, RIGHT, BOTTOM, LEFT
			When True there is a wall
			Otherwise there is not
			Be careful that both cells do not have walls !
			""")
		for col in range(width):
			for line in range(height):
				pass