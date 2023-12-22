"""
https://adventofcode.com/2023/day/6#part2
"""

from races import read_races, find_ways_to_win


def find_num_ways_to_win() -> int:
    """
    Find the number of ways to win the single, larger race described in part 2
    :return: the number of ways to win the race
    """
    race = read_races('input', kern=True)
    return find_ways_to_win(race)


print(find_num_ways_to_win())
