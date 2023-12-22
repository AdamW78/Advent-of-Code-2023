"""
https://adventofcode.com/2023/day/6#day-desc
"""
from functools import reduce

from read_race_info import read_races


def find_num_ways_to_win() -> int:
    """
    Finds the number of ways to win each race (by beating the race's record)
    :return: Product of number of ways to win each race
    """
    races = read_races('input')
    race_win_counts = [0 for _ in range(len(races))]
    for i, race in enumerate(races):
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
        race_win_counts[i] = num_ways_to_win
    print(race_win_counts)
    return reduce(lambda x, y: x * y, race_win_counts)


print(find_num_ways_to_win())
