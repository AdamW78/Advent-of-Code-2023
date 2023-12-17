"""
Shared code from https://adventofcode.com/2023/day/2 puzzles
"""
from collections import namedtuple
from typing import List, Tuple


def get_cube_draw(drawn_cube_string: List[str]) -> Tuple[int, int, int]:
    """
    Given a list of three strings, return them in the form of a tuple
    :param drawn_cube_string:
    :return: Tuple[int, int, int] that represents the numbers of red, green
    and blue cubes, respectively.
    """
    return_cube_draw = [0] * 3
    for cube_set in drawn_cube_string:
        red_find = cube_set.rfind("red")
        green_find = cube_set.rfind("green")
        if red_find > 0:
            return_cube_draw[0] = int(cube_set[:cube_set.index(" ")])
        elif green_find > 0:
            return_cube_draw[1] = int(cube_set[:cube_set.index(" ")])
        else:
            return_cube_draw[2] = int(cube_set[:cube_set.index(" ")])
    CubeDraw = namedtuple('CubeDraw', ['red', 'green', 'blue'])
    return_cube_draw = CubeDraw(*return_cube_draw)
    return return_cube_draw
