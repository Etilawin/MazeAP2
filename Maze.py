"""
Module for the Maze class
"""

from Cell import Cell
from random import choice
import os.path

BOOL_CONVERTER = {"true": True, "false": False}

# IDEA: Do it by flags (to generate the maze, avoiding to check everytime if it is generated successfully !)

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

		assert self.__width > 0 and self.__width > 0, "Wrong values for width and height (must be greater than 0)"

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

		assert self.__width > 0 and self.__width > 0, "Wrong values for width and height (must be greater than 0)"

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

	def generate_by_algorithm(self, w, h):
		"""
		The depth-first search algorithm of maze generation is frequently implemented using backtracking:

		Make the initial cell the current cell and mark it as visited
		While there are unvisited cells
			If the current cell has any neighbours which have not been visited
				Choose randomly one of the unvisited neighbours
				Push the current cell to the stack
				Remove the wall between the current cell and the chosen cell
				Make the chosen cell the current cell and mark it as visited
			Else if stack is not empty
				Pop a cell from the stack
				Make it the current cell
		"""

		self.__width = w
		self.__height = h

		self.__board = [[Cell(col, line, self.__width, self.__height) for col in range(self.__width)] for line in range(self.__height)]

		stack = []

		current_cell = self.__board[0][0]
		current_cell.make_visited()

		while not all(self.__board[i][j].is_visited() for i in range(self.__height) for j in range(self.__width)):
			if not all(self.__board[i][j].is_visited() for (i,j) in current_cell.get_neighbors()):
				unvisited = choice([self.__board[i][j] for (i,j) in current_cell.get_neighbors() if not self.__board[i][j].is_visited()])
				stack.append(current_cell)
				current_cell.remove_wall_between_cell(unvisited)
				current_cell = unvisited
				current_cell.make_visited()
			elif stack:
				current_cell = stack.pop()

	def generate_text_file(self, file_dest):
		assert self.__width > 0 and self.__height > 0,\
			"You first need to generate a maze"

		# The file has to be readable from the program so I need to write the width and height

		with open(file_dest, "wt+") as file:

			file.write(str(self.__width) + '\n')
			file.write(str(self.__height) + '\n')

			# First doing the up walls
			up_walls = [self.__board[0][col].get_walls()[0] for col in range(self.__width)]
			up_walls = list(map(lambda wall: '-' if wall else ' ', up_walls))
			file.write('+' + '+'.join(up_walls) + '+\n')

			for line in range(self.__height):
				# side walls <=> all left walls + last right wall
				side_walls = [self.__board[line][col].get_walls()[3] for col in range(self.__width)] + [self.__board[line][-1].get_walls()[1]]
				bottom_walls = [self.__board[line][col].get_walls()[2] for col in range(self.__width)]

				# Now converting
				side_walls = list(map(lambda wall: '|' if wall else ' ', side_walls))
				bottom_walls = list(map(lambda wall: '-' if wall else ' ', bottom_walls))

				# print(' '.join(side_walls) + '\n')
				# print((' '.join(side_walls) + '\n').encode('utf-8'))

				file.write(' '.join(side_walls) + '\n')
				file.write('+' + '+'.join(bottom_walls) + '+\n')






