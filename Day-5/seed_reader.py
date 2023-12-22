"""
Shared code by both puzzles in https://adventofcode.com/2023/day/5
"""

from collections import namedtuple
from typing import List, Tuple, TextIO

NUM_MAPPINGS = 7
Mapping = namedtuple('Mapping', 'start end mapping ')
SeedRange = namedtuple('SeedRange', 'start stop')


def read_mappings(mapping_int: int, mappings: Tuple[List[Mapping], ...], inp: TextIO):
    """
    Read all the mappings for a given category, e.g., Seed-to-Soil, Soil-to-Fertilizer, etc.
    :param mapping_int: The integer index for a list of mappings in mappings
    :param mappings: List made up of seven (NUM_MAPPINGS) lists
    Each list contains a set of mappings for a given category, or it can be empty
    :param inp: File from which to read the mappings
    """
    mapping = inp.readline()
    while mapping and mapping != '\n':
        mapping = [int(y) for y in mapping.rstrip('\n').split(' ')]
        start = mapping[1]
        end = start + mapping[2]
        dest = mapping[0]
        mappings[mapping_int].append(Mapping(start, end, dest))
        mapping = inp.readline()


def parse_category_mapping(inp: TextIO, category_mappings: Tuple[List[Mapping], ...]):
    """
    Reads a mapping category
    :param inp: File from which to read the input
    :param category_mappings: mapped conversion guides from input
    """
    inp.readline()
    for mapping_num in range(NUM_MAPPINGS):
        read_mappings(mapping_num, category_mappings, inp)
        inp.readline()


def convert_ranges(seed_ranges: List[Tuple], category_mappings: Tuple[List[Mapping], ...]) -> int:
    """
    Iterates through each set of mappings in category_mappings
    It updates seeds to soil, soil to fertilizer, etc.
    :param seed_ranges: Ranges of seeds for which mappings will be performed
    :param category_mappings: sets of mappings used to convert seeds to soil, etc.
    :return: Lowest possible location value mapped using the given RANGES of seeds as inputs
    """
    seed_ranges = [SeedRange(x, y) for (x, y) in seed_ranges]
    for mapping_list in category_mappings:
        for index, seed_range in enumerate(seed_ranges):
            mapped = False
            i = 0
            while not mapped and i < len(mapping_list):
                mapping = mapping_list[i]
                # Seed range is contained completely within 1 mapping
                if seed_range.start >= mapping.start and seed_range.stop <= mapping.end:
                    mapped = True
                    seed_start = mapping.mapping + (seed_range.start - mapping.start)
                    seed_stop = mapping.mapping + (seed_range.stop - mapping.start)
                    seed_ranges[index] = SeedRange(seed_start, seed_stop)
                # Seed range is bi-directionally bigger than mapping range
                # Split into 3 different seed ranges
                elif (seed_range.start < mapping.start < seed_range.stop
                      and seed_range.start < mapping.end < seed_range.stop):
                    mapped = True
                    seed_ranges.append(SeedRange(seed_range.start, mapping.start - 1))
                    seed_ranges.append(SeedRange(mapping.end, seed_range.stop))
                    seed_start = mapping.mapping
                    seed_stop = mapping.mapping + (mapping.end - mapping.start)
                    seed_ranges[index] = SeedRange(seed_start, seed_stop)
                # Seed range is overlapping and to the left of mapping range
                elif seed_range.start < mapping.start < seed_range.stop:
                    mapped = True
                    seed_ranges.append(SeedRange(seed_range.start, mapping.start - 1))
                    seed_start = mapping.mapping
                    seed_stop = mapping.mapping + (seed_range.stop - mapping.start)
                    seed_ranges[index] = SeedRange(seed_start, seed_stop)
                # Seed range is overlapping and to the right of mapping range
                elif seed_range.start < mapping.end < seed_range.stop:
                    mapped = True
                    seed_ranges.append(SeedRange(mapping.end + 1, seed_range.stop))
                    seed_start = mapping.mapping + (seed_range.start - mapping.start)
                    seed_stop = mapping.mapping + (mapping.end - mapping.start)
                    seed_ranges[index] = SeedRange(seed_start, seed_stop)
                i += 1
    return min(x.start for x in seed_ranges)


def convert_seeds_to_locations(seeds, category_mappings) -> List[int]:
    """
    Iterates through each set of mappings in category_mappings
    It updates seeds to soil, soil to fertilizer, etc.
    :param seeds: seeds to update to soil, etc.
    :param category_mappings: sets of mappings used to convert seeds to soil, etc.
    :return: seeds converted to locations, in a list
    """
    seeds = list(seeds)
    mapped_vals = [-1 for _ in range(len(seeds))]
    for mapping_list in category_mappings:
        for seed_num, seed in enumerate(seeds):
            i = 0
            while mapped_vals[seed_num] == -1 and i < len(mapping_list):
                if mapping_list[i].start <= seed < mapping_list[i].end:
                    mapped_vals[seed_num] = mapping_list[i].mapping + (seed - mapping_list[i].start)
                i += 1
        for vi, mapped_val in enumerate(mapped_vals):
            if mapped_val != -1:
                seeds[vi] = mapped_val
                mapped_vals[vi] = -1
    return seeds


def find_mappings(file: TextIO, seeds) -> int:
    """
    Reads the input file line-by-line, creating mappings according it
    :return: Seeds to map, and the mappings to use
    """
    category_mappings = tuple([] for _ in range(NUM_MAPPINGS))
    # READ NEWLINE
    file.readline()
    parse_category_mapping(file, category_mappings)
    if isinstance(seeds, tuple):
        return min(convert_seeds_to_locations(seeds, category_mappings))
    ranges_converted = convert_ranges(seeds, category_mappings)
    return ranges_converted
