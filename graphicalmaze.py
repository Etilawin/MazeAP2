#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`graphicalmaze` module

:author: `Kim Vallée <kim.vallee.etu@univ-lille.fr>`_

:date:  2018, november

This module implements some functions to draw a maze.
The module can be used to show the maze, or to show a path with tkinter.

This module uses from :mod:`Maze`:

* :method:`Maze.get_width`
* :method:`Maze.get_height`
* :method:`Maze.get_cell`

and from :mod:`Cell`:

* :method:`Cell.get_walls`

To show a graphical maze one hase to:

* create a maze with the Maze class
* either apply the `show` function on the created maze
* or the `show_path` function on the created maze with a given path
"""

from Maze import Maze
from Cell import Cell

from tkinter import Tk, Canvas

CAN_WIDTH = 800
CAN_HEIGHT = 600
BG_COLOR = 'black'
GRID_COLOR = 'yellow'

def show(maze):
	assert isinstance(maze, Maze), "The parameter must be a maze"

	win = Tk()
	win.title('Graphical maze')
	canvas = Canvas(win, bg=BG_COLOR, width=CAN_WIDTH, height=CAN_HEIGHT)
	canvas.pack()

	width = maze.get_width()
	height = maze.get_height()

	# Draw maze
	DX = CAN_WIDTH // width
	DY = CAN_HEIGHT // height
	for y in range(height):
		for x in range(width):
			walls = maze.get_cell(y, x).get_walls()

			if walls[0]:
				# Top wall
				canvas.create_line(x * DX, y * DY,
								   (x + 1) * DX, y * DY,
								   fill=GRID_COLOR, width=1)
			if walls[3]:
				# Left wall
				canvas.create_line(x * DX, y * DY,
								   x * DX, (y + 1) * DY,
								   fill=GRID_COLOR, width=1)

	# Bottom line
	canvas.create_line(0,
					   height * DY - 1,
					   width * DX - 1,
					   height * DY - 1,
                       fill=GRID_COLOR, width=1)
	# Right line
	canvas.create_line(width * DX - 1,
					   0,
					   width * DX - 1,
					   height * DY - 1,
                       fill=GRID_COLOR, width=1)
	win.mainloop()

def show_path(maze, path):
	assert isinstance(maze, Maze), "The parameter must be a maze"
	assert isinstance(path, list), "The path must be a list"
	assert all(isinstance(cell, Cell) for cell in path), "The path must be filled with cells"

	win = Tk()
	win.title('Graphical path in the maze')
	canvas = Canvas(win, bg=BG_COLOR, width=CAN_WIDTH, height=CAN_HEIGHT)
	canvas.pack()

	width = maze.get_width()
	height = maze.get_height()

	# Draw maze
	DX = CAN_WIDTH // width
	DY = CAN_HEIGHT // height
	for y in range(height):
		for x in range(width):
			cell = maze.get_cell(y, x)
			walls = cell.get_walls()

			if cell in path:
				canvas.create_oval(x * DX + DX//10, y * DY + DY//10,
								   (x + 1) * DX - DX//10, (y + 1) * DY - DY//10,
								   fill="red")

			if walls[0]:
				# Top wall
				canvas.create_line(x * DX, y * DY,
								   (x + 1) * DX, y * DY,
								   fill=GRID_COLOR, width=1)
			if walls[3]:
				# Left wall
				canvas.create_line(x * DX, y * DY,
								   x * DX, (y + 1) * DY,
								   fill=GRID_COLOR, width=1)

	# Bottom line
	canvas.create_line(0,
					   height * DY - 1,
					   width * DX - 1,
					   height * DY - 1,
                       fill=GRID_COLOR, width=1)
	# Right line
	canvas.create_line(width * DX - 1,
					   0,
					   width * DX - 1,
					   height * DY - 1,
                       fill=GRID_COLOR, width=1)
	win.mainloop()