"""
https://adventofcode.com/2023/day/5#day-desc
"""
from collections import namedtuple
from io import TextIOWrapper
from typing import List


NUM_MAPPINGS = 7
Mapping = namedtuple('Mapping', 'start end mapping')


def read_mappings(mapping_int: int, mappings: List[List[Mapping]], inp: TextIOWrapper):
    """
    Read all the mappings for a given category, e.g., Seed-to-Soil, Soil-to-Fertilizer, etc.
    :param mapping_int: The integer index for a list of mappings in mappings
    :param mappings: List made up of seven (NUM_MAPPINGS) lists
    Each list contains a set of mappings for a given category, or it can be empty
    :param inp: File from which to read the mappings
    """
    mapping = inp.readline()
    while mapping and mapping != '\n':
        mappings[mapping_int].append(Mapping(*[int(x) for x in mapping.rstrip('\n').split(' ')]))
        mapping = inp.readline()


def parse_category_mapping(inp: TextIOWrapper, category_mappings: List[List[Mapping]]):
    """
    Reads a mapping category
    :param inp: File from which to read the input
    :param category_mappings: mapped conversion guides from input
    """
    inp.readline()
    for mapping_num in range(NUM_MAPPINGS):
        read_mappings(mapping_num, category_mappings, inp)
        inp.readline()


def line_by_line_read():
    """
    Reads the input file, one line at a time
    """
    with open('example_input', 'rt', encoding='utf8') as file_input:
        line = file_input.readline()
        file_input.readline()
        seeds = line.strip('seeds: ').rstrip('\n').split(' ')
        seeds = tuple(int(seed) for seed in seeds)
        category_mappings = [[] for _ in range(NUM_MAPPINGS)]
        parse_category_mapping(file_input, category_mappings)
        print(category_mappings)


line_by_line_read()
