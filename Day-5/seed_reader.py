"""
Shared code by both puzzles in https://adventofcode.com/2023/day/5
"""

from collections import namedtuple
from io import TextIOWrapper
from typing import List, Tuple

NUM_MAPPINGS = 7
Mapping = namedtuple('Mapping', 'start end mapping ')


def read_mappings(mapping_int: int, mappings: Tuple[List[Mapping], ...], inp: TextIOWrapper):
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


def parse_category_mapping(inp: TextIOWrapper, category_mappings: Tuple[List[Mapping], ...]):
    """
    Reads a mapping category
    :param inp: File from which to read the input
    :param category_mappings: mapped conversion guides from input
    """
    inp.readline()
    for mapping_num in range(NUM_MAPPINGS):
        read_mappings(mapping_num, category_mappings, inp)
        inp.readline()


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


def find_min_location_mapping(category_mappings: Tuple[List[Mapping], ...]) -> int:
    final_mapping = category_mappings[len(category_mappings) - 1]
    min_mapping = final_mapping[0].mapping
    for mapping in final_mapping:
        min_mapping


def find_min_mapped_seed(file: TextIOWrapper, seeds: tuple) -> int:
    """
    Reads the input file line-by-line, creating mappings according it
    :return: Seeds to map, and the mappings to use
    """

    category_mappings = tuple([] for _ in range(NUM_MAPPINGS))
    # READ NEWLINE
    file.readline()
    parse_category_mapping(file, category_mappings)
    return min(convert_seeds_to_locations(seeds, category_mappings))
