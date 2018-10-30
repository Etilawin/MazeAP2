"""
Module for the Maze class
"""

from Cell import Cell
import os.path

BOOL_CONVERTER = {"true": True, "false": False}

class Maze:
	def __init__(self):
		self.__width = 0
		self.__height = 0
		# self.__board = [[Cell(col, line, width, height) for col in range(width)] for line in range(height)] # Empty board

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_board(self):
		return self.__board

	def generate_by_hand(self):
		print("""
			You are going to generate your maze by hand !
			So you will chose the walls for each cell.
			This will be of the form:
			```
			4 50
			Chose walls for this cell: True,False,True,False
			```
			Where 4 is the column number
			Where 50 is the line number
			Walls may be given in the following order TOP, RIGHT, BOTTOM, LEFT
			When True there is a wall
			Otherwise there is not (Be careful to miswriting)
			Be careful that both cells do not have walls !
			""")
		try:
			self.__width = int(input("Please enter the width of the board : "))
			self.__height = int(input("Please enter the height of the board : "))
		except ValueError:
			print('You probably miswrote the values, they could not be converted to integers')
			exit(1)

		self.__board = [[0 for x in range(self.__width)] for y in range(self.__height)]

		for col in range(self.__width):
			for line in range(self.__height):
				print(col, line)
				walls = input("Chose walls for this cell: ").split(",")

				while len(walls) != 4:
					print("Error during spliting, please retry")
					print(col, line)
					walls = input("Chose walls for this cell: ").split(",")

				cell = Cell(col, line, self.__width, self.__height)
				cell.set_walls([BOOL_CONVERTER.get(v.strip().lower(), False) for v in walls])
				self.__board[line][col] = cell

	def generate_by_file(self, path):
		assert os.path.exists(path), "The path may not exist or you don't have access to it"
		with open(path, 'rb') as file:
			try:
				self.__width = int(file.readline())
				self.__height = int(file.readline())
				the_maze = file.read().decode().split('\n')
			except ValueError:
				print("Could no convert the first lines to integer, aborting")
				exit(1)
			except EOFError:
				print("Wrong file structure")
				exit(1)

		self.__board = [[0 for x in range(self.__width)] for y in range(self.__height)]

		# stripping
		the_maze = [v.strip() for v in the_maze]

		# Now converting textual maze to a 2 dimensional array cells
		for col in range(self.__width):
			for line in range(self.__height):

				# Splitted by line then :
				up_wall = the_maze[2*line][2*col + 1]
				right_wall = the_maze[2*line + 1][2*col + 2]
				bottom_wall = the_maze[2*line + 2][2*col + 1]
				left_wall = the_maze[2*line + 1][2*col]

				if (col, line) == (0, 0):
					print(up_wall, right_wall, bottom_wall, left_wall)

				assert all(v in (' ', '-') for v in (up_wall, bottom_wall)),\
					"The values for bottom and top walls should be either a '-'(hyphen) or a ' '(space) " 
				assert all(v in (' ', '|') for v in (right_wall, left_wall)),\
					"The values for right and left walls should be either ' '(space) or '|'(pipe)"

				# Converts to boolean
				up_wall     = (up_wall     == '-')
				bottom_wall = (bottom_wall == '-')
				right_wall  = (right_wall  == '|')
				left_wall   = (left_wall   == '|')

				cell = Cell(col, line, self.__width, self.__height)
				cell.set_walls([up_wall, right_wall, bottom_wall, left_wall])
				self.__board[line][col] = cell


