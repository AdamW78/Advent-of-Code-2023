"""
https://adventofcode.com/2023/day/5#part2
"""
from seed_reader import find_mappings


def read_seeds(filename: str) -> int:
    """
    Reads seeds as input and sets off calculation of the min mapped seed
    Reads in a DIFFERENT set of seeds than puzzle one!
    :param filename: A path to file input
    """
    with open(filename, 'rt', encoding='utf8') as file:
        seed_starts = [int(x) for x in file.readline().strip('seeds: ').rstrip('\n').split(' ')]
        seed_ends = seed_starts[1::2]
        seed_starts = seed_starts[::2]
        seed_ends = [((seed_ends[i] + seed_starts[i]) - 1) for i in range(len(seed_ends))]
        seed_ranges = zip(seed_starts, seed_ends)
        return find_mappings(file, seed_ranges)


print(read_seeds('input'))
