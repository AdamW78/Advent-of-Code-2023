"""
https://adventofcode.com/2023/day/5#part2
"""
from seed_reader import find_min_mapped_seed


def read_seeds(filename: str) -> int:
    """
    Reads seeds as input and sets off calculation of the min mapped seed
    Reads in a DIFFERENT set of seeds than puzzle one!
    :param filename: A path to file input
    """
    with open(filename, 'rt', encoding='utf8') as file:
        seed_ranges = [int(x) for x in file.readline().strip('seeds: ').rstrip('\n').split(' ')]
        all_seeds = []
        for i in range(0, len(seed_ranges), 2):
            for seed_num in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i+1]):
                all_seeds.append(seed_num)
        print(find_min_mapped_seed(file, all_seeds))


read_seeds('example_input')
