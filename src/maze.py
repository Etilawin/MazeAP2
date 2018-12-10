#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Maze Module.

:mod:`maze` module

:author: `Kim Vallée <kim.vallee.etu@univ-lille.fr>`_

:date:  2018, november

This module implements the class to create a maze. The maze may be built
    - by hand
    - by file
    - by algorithm.
Every choice is referenced in the MAZE class that allows specific flags.
It is also able to find the path one point to another if it exists.
The maze can be then saved into a file
or printed on screen using the module `graphicalmaze`.

This module uses from :mod:`Cell`:

* :method:`Cell.make_visited`
* :method:`Cell.get_neighbors`
* :method:`Cell.remove_wall_between_cell`
* :method:`Cell.get_accessible_neighbors`
"""


from cell import Cell
from enum import Enum
from random import choice
import os.path


class MAZE(Enum):
    """Class provided to have method of implementing the maze."""

    hand = 1
    file = 2
    algorithm = 3


class Maze:
    """
    This class provides a way to build a maze from different methods.

    It also permits to find a path between two points if it exists.
    And finally it is capable of creating a textual representation of the maze.

    :examples:

    >>> mymaze = Maze(width=50, height=50)
    >>> mymaze.get_width()
    50
    >>> mymaze.get_height()
    50
    >>> type(mymaze.get_cell(0, 0)) == type(Cell(0,0,5,5))
    True
    """

    def __init__(self, width=10, height=10, method=MAZE.algorithm, path=False):
        """
        Init a Maze.

        :param width: The width of the maze, optional if generated by file
                      (default = 10)
        :type width: int
        :param height: The height of the maze, optional if generated by file
                      (default = 10)
        :type height: int
        :param method: The method to generate the maze
                       (default = MAZE.algorithm)
        :type method: MAZE
        :param path: The path to the file,
                     only to use if the method is MAZE.file (default = False)
        :UC: if generated by file a path must be provided
             otherwise a width and height must be provided
        """
        assert isinstance(method, MAZE), "The method given is not supported"
        if method == MAZE.file:
            assert isinstance(path, str), "The path should be a string"
            self.__generate_by_file(path)
        else:
            assert isinstance(width, int) and width > 0,\
                "You must provide a valid width"
            assert isinstance(height, int) and height > 0,\
                "You must provide a valid height"
            self.__width = width
            self.__height = height
            self.__board = [[Cell(row, col, width, height)
                            for col in range(width)] for row in range(height)]
            if method == MAZE.algorithm:
                self.__generate_by_algorithm()
            elif method == MAZE.hand:
                self.__generate_by_hand()

    def get_width(self):
        """
        Getter method for the width.

        :return: The width of the board
        :rtype: int

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> mymaze.get_width()
        50
        """
        return self.__width

    def get_height(self):
        """
        Getter method for the height.

        :return: The height of the board
        :rtype: int

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> mymaze.get_height()
        50
        """
        return self.__height

    def get_board(self):
        """
        Getter method for the board.

        :return: The board itself
        :rtype: list

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> len(mymaze.get_board()) == 50
        True
        >>> sum(len(x) for x in mymaze.get_board()) == 50*50
        True
        """
        return self.__board

    def get_cell(self, row, col):
        """
        Getter method for the cell at row `row` and column `col`.

        :param row: The row of the cell
        :type row: int
        :param col: The col of the cell
        :type col: int
        :return: The cell at position (row, col)
        :rtype: Cell
        :UC: 0 <= row <= self.__height and 0 <= col < self.__width

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> cell1 = mymaze.get_cell(0, 0)
        >>> cell2 = mymaze.get_cell(51, 23)
        Traceback (most recent call last):
        ...
        AssertionError: The row should be between 0 and the height
        >>> type(cell1)
        <class 'cell.Cell'>
        """
        assert 0 <= row < self.__height,\
            "The row should be between 0 and the height"
        assert 0 <= col < self.__width,\
            "The column should be between 0 and the width"
        return self.__board[row][col]

    def __generate_by_hand(self):
        """
        Private method to generate the maze by hand.

        This method allows to generate the maze with the console cell by cell
        """
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
            When True there is a wall (You may also put 1 and 0 for a faster
            way like this : `Chose walls for this cell: 1,0,1,0`)
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

                self.__board[row][col].set_walls(
                    [v.strip().lower() in ("1", "true") for v in walls]
                )

    def __generate_by_file(self, path):
        """
        Private method to generate the maze with a file.

        :param path: The path to the file
        :type path: str
        :UC: The file exists...
        """
        assert os.path.exists(path),\
            "The path may not exist or you don't have access to it"
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

        assert self.__width > 0 and self.__width > 0,\
            "Wrong values for width and height (must be greater than 0)"

        self.__board = [
            [Cell(row, col, self.__width, self.__height)
             for col in range(self.__width)]
            for row in range(self.__height)]

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
                    "The values for bottom and top walls should\
                     be either a '-'(hyphen) or a ' '(space) "
                assert all(v in (' ', '|') for v in (right_wall, left_wall)),\
                    "The values for right and left walls should be either\
                     ' '(space) or '|'(pipe)"

                # Converts to boolean
                up_wall = (up_wall == '-')
                bottom_wall = (bottom_wall == '-')
                right_wall = (right_wall == '|')
                left_wall = (left_wall == '|')

                self.__board[row][col].set_walls(
                    [up_wall, right_wall, bottom_wall, left_wall]
                )

    def __generate_by_algorithm(self):
        """
        Private method to generate the maze by algorithm.

        The algorithm used can be found here :
        https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
        """
        stack = []

        current_cell = self.__board[0][0]
        current_cell.make_visited()

        while not all(
                      self.__board[i][j].is_visited()
                      for i in range(self.__height)
                      for j in range(self.__width)
                      ):
            if not all(
                       self.__board[i][j].is_visited()
                       for (i, j) in current_cell.get_neighbors()
                       ):
                unvisited = choice(
                    [self.__board[i][j]
                     for (i, j) in current_cell.get_neighbors()
                     if not self.__board[i][j].is_visited()])
                stack.append(current_cell)
                current_cell.remove_wall_between_cell(unvisited)
                current_cell = unvisited
                current_cell.make_visited()
            elif stack:
                current_cell = stack.pop()

        # Now reset cell state :
        self.__unvisit_all_cells()

    def __unvisit_all_cells(self):
        """Private method to unvisit all cells of the maze."""
        for row in range(self.__height):
            for col in range(self.__width):
                self.__board[row][col].make_unvisited()

    def __repr__(self):
        """
        Representation of the maze uses str method.

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> mymaze.__repr__() == str(mymaze)
        True
        """
        return self.__str__()

    def __str__(self):
        """Convert to a string."""
        string = ""

        string += str(self.__width) + '\n'
        string += str(self.__height) + '\n'

        # First doing the up walls
        up_walls = [self.__board[0][col].get_walls()[0]
                    for col in range(self.__width)]
        up_walls = list(map(lambda wall: '-' if wall else ' ', up_walls))
        string += '+' + '+'.join(up_walls) + '+\n'

        for row in range(self.__height):
            # side walls <=> all left walls + last right wall
            side_walls = [self.__board[row][col].get_walls()[3]
                          for col in range(self.__width)]
            side_walls += [self.__board[row][-1].get_walls()[1]]
            bottom_walls = [self.__board[row][col].get_walls()[2]
                            for col in range(self.__width)]

            # Now converting
            side_walls = list(
                          map(
                            lambda wall: '|' if wall else ' ', side_walls
                             )
                          )
            bottom_walls = list(
                            map(
                                lambda wall: '-' if wall else ' ', bottom_walls
                                )
                            )

            string += ' '.join(side_walls) + '\n'
            string += '+' + '+'.join(bottom_walls) + '+\n'

        return string

    def save_to_file(self, file_dest):
        """
        Save the maze to a file (that can be used afterward).

        :param file_dest: The file destination
        :type file_dest: str
        """
        with open(file_dest, "wt+") as file:
            file.write(self.__str__())

    def find_path(self, from_row, from_col, to_row, to_col):
        """
        Find the path from one cell to another.

        Using a kind of backtracking algorithm find the path from one cell to
        another.
        :param from_row: Row of the origin cell
        :type from_row: int
        :param from_col: Column of the origin cell
        :type from_col: int
        :param to_row: Row of the final cell
        :type to_row: int
        :param to_col: Column of the final cell
        :type to_col: int
        :return: The path if it exists from one cell to another
        :rtype: list

        :examples:

        >>> mymaze = Maze(width=50, height=50)
        >>> path = mymaze.find_path(0, 0, 49, 49)
        >>> 1 <= len(path) < 50*50
        True
        >>> isinstance(path, list)
        True
        >>> all(isinstance(x, Cell) for x in path)
        True
        """
        track_stack = []
        path = []

        current_cell = self.__board[from_row][from_col]

        path.append(current_cell)

        destination_cell = self.__board[to_row][to_col]
        while current_cell != destination_cell and\
                not all(
                        self.__board[i][j].is_visited()
                        for i in range(self.__height)
                        for j in range(self.__width)
                        ):
            if not all(self.__board[i][j].is_visited()
                       for (i, j) in current_cell.get_accessible_neighbors()):
                unvisited = choice(
                        [self.__board[i][j]
                         for (i, j) in current_cell.get_accessible_neighbors()
                         if not self.__board[i][j].is_visited()]
                        )
                track_stack.append(current_cell)
                path.append(unvisited)
                current_cell = unvisited
                current_cell.make_visited()
            elif track_stack:
                current_cell = track_stack.pop()
                while path[-1] != current_cell:
                    try:
                        path.pop()
                    except IndexError:
                        self.__unvisit_all_cells()
                        return []

        self.__unvisit_all_cells()

        return path


if __name__ == "__main__":
    import doctest
    doctest.testmod()
