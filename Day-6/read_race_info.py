"""
https://adventofcode.com/2023/day/6
"""
import re
from collections import namedtuple
from typing import Tuple

import read_input

Race = namedtuple('Race', 'duration record')


def read_races(file=None) -> Tuple[Race, ...]:
    """
    Read all races from the input file and return tuple of namedtuple Races
    :return:
    """
    if file == 'input':
        races = read_input.read()
    else:
        races = read_input.example_read()
    races[0] = tuple(int(n) for n in re.findall(r'\d+', races[0]))
    races[1] = tuple(int(m) for m in re.findall(r'\d+', races[1]))
    races = zip(races[0], races[1])
    races = tuple(Race(x, y) for x, y in races)
    return races