"""
Module for the Maze class
"""

from Cell import Cell
from enum import Enum
from random import choice
import os.path

# IDEA: Do it by flags (to generate the maze, avoiding to check everytime if it is generated successfully !)

class Method(Enum):
	hand = 1
	file = 2
	algorithm = 3

class Maze:
	def __init__(self, width = 0, height = 0, method = Method.algorithm, path = False):
		assert isinstance(method, Method), "The method given is not supported"
		if method == Method.file:
			assert isinstance(path, str), "The path should be a string"
			self.__generate_by_file(path)
		else:
			assert isinstance(width, int) and width > 0, "You must provide a valid width"
			assert isinstance(height, int) and height > 0, "You must provide a valid height"
			self.__width = width
			self.__height = height
			self.__board = [[Cell(row, col, width, height) for col in range(width)] for row in range(height)] # Empty board

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_board(self):
		return self.__board

	def __generate_by_hand(self):
		print("""
			You are going to generate your maze by hand !
			So you will chose the walls for each cell.
			This will be of the form:
			```
			4 50
			Chose walls for this cell: True,False,True,False
			```
			Where 4 is the column number
			Where 50 is the row number
			Walls may be given in the following order TOP, RIGHT, BOTTOM, LEFT
			When True there is a wall (You may also put 1 and 0 for a faster way like this : `Chose walls for this cell: 1,0,1,0`)
			Otherwise there is not (Be careful to miswriting)
			Be careful that both cells do not have walls !
			""")

		for col in range(self.__width):
			for row in range(self.__height):
				print(col, row)
				walls = input("Chose walls for this cell: ").split(",")

				while len(walls) != 4:
					print("Error during spliting, please retry")
					print(col, row)
					walls = input("Chose walls for this cell: ").split(",")

				self.__board[row][col].set_walls([v.strip().lower() in ("1", "true") for v in walls])

	def __generate_by_file(self, path):
		assert os.path.exists(path), "The path may not exist or you don't have access to it"
		with open(path, 'rb') as file:
			try:
				self.__width = int(file.readline())
				self.__height = int(file.readline())
				the_maze = file.read().decode().split('\n')
			except ValueError:
				print("Could no convert the first rows to integer, aborting")
				exit(1)
			except EOFError:
				print("Wrong file structure")
				exit(1)

		assert self.__width > 0 and self.__width > 0, "Wrong values for width and height (must be greater than 0)"

		self.__board = [[Cell(row, col, self.__width, self.__height) for col in range(self.__width)] for row in range(self.__height)]

		# stripping
		the_maze = list(map(lambda x: x.strip(), the_maze))

		# Now converting textual maze to a 2 dimensional array cells
		for row in range(self.__height):
			for col in range(self.__width):

				# Splitted by row then :
				up_wall = the_maze[2*row][2*col + 1]
				right_wall = the_maze[2*row + 1][2*col + 2]
				bottom_wall = the_maze[2*row + 2][2*col + 1]
				left_wall = the_maze[2*row + 1][2*col]

				assert all(v in (' ', '-') for v in (up_wall, bottom_wall)),\
					"The values for bottom and top walls should be either a '-'(hyphen) or a ' '(space) " 
				assert all(v in (' ', '|') for v in (right_wall, left_wall)),\
					"The values for right and left walls should be either ' '(space) or '|'(pipe)"

				# Converts to boolean
				up_wall     = (up_wall     == '-')
				bottom_wall = (bottom_wall == '-')
				right_wall  = (right_wall  == '|')
				left_wall   = (left_wall   == '|')

				self.__board[row][col].set_walls([up_wall, right_wall, bottom_wall, left_wall])

	def __generate_by_algorithm(self):
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

		self.__board = [[Cell(row, col, self.__width, self.__height) for col in range(self.__width)] for row in range(self.__height)]

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

		# Now reset cell state :
		for row in range(self.__height):
			for col in range(self.__width):
				self.__board[row][col].make_unvisited()

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

			for row in range(self.__height):
				# side walls <=> all left walls + last right wall
				side_walls = [self.__board[row][col].get_walls()[3] for col in range(self.__width)] + [self.__board[row][-1].get_walls()[1]]
				bottom_walls = [self.__board[row][col].get_walls()[2] for col in range(self.__width)]

				# Now converting
				side_walls = list(map(lambda wall: '|' if wall else ' ', side_walls))
				bottom_walls = list(map(lambda wall: '-' if wall else ' ', bottom_walls))

				# print(' '.join(side_walls) + '\n')
				# print((' '.join(side_walls) + '\n').encode('utf-8'))

				file.write(' '.join(side_walls) + '\n')
				file.write('+' + '+'.join(bottom_walls) + '+\n')

	def find_path(self, from_row, from_col, to_row, to_col):
		"""
		variables:
			track stack
			visited cells
			current path

		Make first cell as current cell and append it to the current path
		while the current cell is not the destination cell and not all cells have been visited:
			if there are unvisited cells in the neighborhood of the current cell:
				chose one unvisited cell randomly
				append 


		The depth-first search algorithm of maze generation is frequently implemented using backtracking:

		Make the initial cell the current cell and mark it as visited
		While the current cell is not the destination cell and not all cells have been visited
			If the current cell has any neighbours which have not been visited (where there is no wall between them)
				Choose randomly one of the unvisited neighbours
				Push the current cell to the stack
				Append the chosen cell to the path
				Make the chosen cell the current cell and mark it as visited
			Else if stack is not empty
				Pop a cell from the stack
				While the last item of the current path is not this cell
					Remove it from the current path
				Make it the current cell

		"""
		track_stack = []
		path = []

		current_cell = self.__board[from_row][from_col]

		path.append(current_cell)

		destination_cell = self.__board[to_row][to_col]
		while current_cell != destination_cell and not all(self.__board[i][j].is_visited() for i in range(self.__height) for j in range(self.__width)):
			if not all(self.__board[i][j].is_visited() for (i,j) in current_cell.get_accessible_neighbors()):
				unvisited = choice([self.__board[i][j] for (i,j) in current_cell.get_accessible_neighbors() if not self.__board[i][j].is_visited()])
				track_stack.append(current_cell)
				path.append(unvisited)
				current_cell = unvisited
				current_cell.make_visited()
			elif track_stack:
				current_cell = track_stack.pop()
				while path[-1] != current_cell:
					path.pop()

		for row in range(self.__height):
			for col in range(self.__width):
				self.__board[row][col].make_unvisited()

		return path





