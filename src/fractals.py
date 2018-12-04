#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`fractals`

:author: `Kim Vallée`_

:date: 2017, september. Lasr revised: 2018, september

Examples of recursion tracings.
"""

from turtle import forward, backward, left, right, done, penup, pendown, goto, speed

def draw_vonKoch(l, n):
	"""
	Draws the vonKoch curve on screen using turtle and recursivity

    :param l: (int or float) Length of the wire
    :param n: (int) 		 Order of the curve to draw
    :return: None
    :UC: n >= 0, l >= 0
	"""
	if n==0:
		forward(l)

	else:
		draw_vonKoch(l/3, n-1)
		left(60)
		draw_vonKoch(l/3, n-1)
		right(120)
		draw_vonKoch(l/3, n-1)
		left(60)
		draw_vonKoch(l/3, n-1)

def draw_snowlfakeKoch(l, n):
	"""
	Draw the von Koch snowflake using draw_vonKoch function

	:param l: (int or float) Length of the wire
    :param n: (int) 		 Order of the curve to draw
    :return: None
    :UC: n >= 0, l >= 0
	"""

	draw_vonKoch(l, n)
	right(120)
	draw_vonKoch(l, n)
	right(120)
	draw_vonKoch(l, n)

def draw_cesaro(l, n):
	"""
	Draws the cesaro curve on screen using turtle and recursivity
	It is the same as vonKoch but with 10° angle at top

    :param l: (int or float) Length of the wire
    :param n: (int) 		 Order of the curve to draw
    :return: None
    :UC: n >= 0, l >= 0
	"""
	if n==0:
		forward(l)

	else:
		draw_cesaro(l/3, n-1)
		left(85)
		draw_cesaro(l/3, n-1)
		right(170)
		draw_cesaro(l/3, n-1)
		left(85)
		draw_cesaro(l/3, n-1)

def draw_cesaroSquare(l, n):
	"""
	Draws the cesaro square based on the draw_cesaro function

	:param l: (int or float) Length of the wire
    :param n: (int) 		 Order of the curve to draw

	:return: None
    :UC: n >= 0, l >= 0
    """
	for i in range(4):
		draw_cesaro(l,n)
		left(90)

def draw_Sierpinski(l, n):
	"""
	Draws the Sierpinski triangle

	:param l: (int or float) Length of the wire
    :param n: (int) 		 Order of the curve to draw

	:return: None
    :UC: n >= 0, l >= 0
	"""
	if n == 0:
		for i in range(3):
			forward(l)
			left(120)
	else:
		# pencolor("green") --> That really was a bad idea (really)
		draw_Sierpinski(l/2, n-1)
		forward(l/2)
		# pencolor("blue")
		draw_Sierpinski(l/2, n-1)
		backward(l/2)
		left(60)
		forward(l/2)
		right(60)
		# pencolor("orange")
		draw_Sierpinski(l/2, n-1)
		left(60)
		backward(l/2)
		right(60)

def draw_hexagoneSierpinski(l, n):
	for i in range(6):
		draw_Sierpinski(l, n)
		forward(l)
		left(60)

if __name__ == "__main__":
	speed(0)
	penup()
	goto(-150, -250)
	pendown()
	draw_hexagoneSierpinski(200, 4)
	# penup()
	# goto(0,0)
	done()



