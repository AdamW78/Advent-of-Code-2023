"""
https://adventofcode.com/2023/day/6
"""
import re
from collections import namedtuple

import read_input

Race = namedtuple('Race', 'duration record')


def read_races(file=None, kern=False):
    """
    Read all races from the input file and return tuple of namedtuple Races
    :return:
    """
    if file == 'input':
        races = read_input.read()
    else:
        races = read_input.example_read()
    # Puzzle 1
    if not kern:
        races[0] = tuple(int(n) for n in re.findall(r'\d+', races[0]))
        races[1] = tuple(int(m) for m in re.findall(r'\d+', races[1]))
        return tuple(Race(x, y) for x, y in zip(races[0], races[1]))
    # Puzzle 2
    races[0] = int("".join(re.findall(r'\d+', races[0])))
    races[1] = int("".join(re.findall(r'\d+', races[1])))
    return Race(races[0], races[1])
