import argparse
import graphicalmaze
from maze import Maze, MAZE

parser = argparse.ArgumentParser(description='Create a maze')
parser.add_argument("--method", "-m",
                    choices=['algorithm', 'hand', 'file'],
                    default='algorithm',
                    type=str,
                    dest="method",
                    help="The method to generate the maze")
parser.add_argument("--input", '-i',
                    type=str,
                    dest='input',
                    help='The input file to generate with a file')
parser.add_argument("--size", "-s",
                    nargs=2,
                    type=int,
                    default=[10, 10],
                    metavar=('WIDTH', 'HEIGHT'),
                    dest="size",
                    help="The size of the maze")
parser.add_argument("--output", "-o",
                    type=str,
                    dest="output",
                    help="The output file if you want to save the maze")
parser.add_argument("--path", "-p",
                    nargs=4,
                    type=int,
                    metavar=("ORIGIN_ROW",
                             "ORIGIN_COL",
                             "DESTINATION_ROW",
                             "DESTINATION_COL"),
                    dest="path",
                    help="The path you want to generate through the maze")

args = vars(parser.parse_args())

if args['method'] == 'algorithm':
    method = MAZE.algorithm
elif args['method'] == 'hand':
    method = MAZE.hand
elif args['method'] == 'file':
    method = MAZE.file
    assert args['input'], "No file given, cannot continue"
else:
    assert False, "Logic exception, shouldn't reach that point"

size = args['size']

if method == MAZE.file:
    the_maze = Maze(method=method, path=args['input'])
else:
    the_maze = Maze(method=method, width=size[0], height=size[1])

if args['output']:
    the_maze.save_to_file(args['output'])

graphicalmaze.show(the_maze)
if args['path']:
    path = the_maze.find_path(args['path'][0],
                              args['path'][1],
                              args['path'][2],
                              args['path'][3])
    graphicalmaze.show_path(the_maze, path)
