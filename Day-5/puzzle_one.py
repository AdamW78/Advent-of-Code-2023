"""
https://adventofcode.com/2023/day/5#day-desc
"""
from seed_reader import find_min_mapped_seed


def read_seeds(filename: str) -> int:
    """
    Function that reads seeds as input and sets off calculation of the min mapped seed
    :param filename: path to file input
    """
    with open(filename, 'rt', encoding='utf8') as file:
        seeds = tuple(int(x) for x in file.readline().strip('seeds: ').rstrip('\n').split(' '))
        print(find_min_mapped_seed(file, seeds))


read_seeds('input')
