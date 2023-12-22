"""
https://adventofcode.com/2023/day/6#part2
"""

from read_race_info import read_races


def find_num_ways_to_win() -> int:
    """
    Find the number of ways to win the single, larger race described in part 2
    :return: the number of ways to win the race
    """
    races = read_races()
    print(races)
    return 0
