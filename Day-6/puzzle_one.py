"""
https://adventofcode.com/2023/day/6#day-desc
"""
from functools import reduce

from races import read_races, find_ways_to_win


def find_num_ways_to_win() -> int:
    """
    Finds the number of ways to win each race (by beating the race's record)
    :return: Product of number of ways to win each race
    """
    races = read_races('input')
    race_win_counts = [0 for _ in range(len(races))]
    for i, race in enumerate(races):
        race_win_counts[i] = find_ways_to_win(race)
    return reduce(lambda x, y: x * y, race_win_counts)


print(find_num_ways_to_win())
