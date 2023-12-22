"""
https://adventofcode.com/2023/day/6
"""
import re
from collections import namedtuple

import read_input

Race = namedtuple('Race', 'duration record')


def find_ways_to_win(race: Race):
    num_ways_to_win = 0
    t_charge = race.duration // 2
    t_go = race.duration - t_charge
    init_vals = tuple((t_charge, t_go))
    while t_charge * t_go > race.record:
        num_ways_to_win += 1
        t_charge -= 1
        t_go += 1
    t_go = race.duration // 2
    t_charge = race.duration - t_go
    while t_charge * t_go > race.record:
        if (t_charge, t_go) == init_vals:
            num_ways_to_win -= 1
        num_ways_to_win += 1
        t_charge += 1
        t_go -= 1
    return num_ways_to_win


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
