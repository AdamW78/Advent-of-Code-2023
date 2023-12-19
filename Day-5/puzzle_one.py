"""
https://adventofcode.com/2023/day/5#day-desc
"""
from collections import namedtuple
from enum import StrEnum
from io import TextIOWrapper
from typing import List


class Categories(StrEnum):
    """
    Enumeration of possible categories
    """
    SEED = 'seed'
    SOIL = 'soil'
    FERTILIZER = 'fertilizer'
    WATER = 'water'
    LIGHT = 'light'
    TEMP = 'temperature'
    HUMIDITY = 'humidity'
    LOCATION = 'location'


NUM_MAPPINGS = len(Categories) - 1
Mapping = namedtuple('Mapping', 'start end mapping')


def read_mappings(category_mapping: int, mappings: List[List[Mapping]], inp: TextIOWrapper):
    f"""
    Read all the mappings for a given category, e.g., Seed-to-Soil, Soil-to-Fertilizer, etc.
    :param category_mapping: The integer representing the list index (in a list of lists) of the mapping
    :param mappings: List made up of {NUM_MAPPINGS} lists, each containing a set of mappings (or empty) 
    :param inp: File from which to read the mappings
    """
    mapping = inp.readline()
    while mapping and mapping != '\n':
        mapping = [int(x) for x in mapping.rstrip('\n').split(' ')]
        mappings[category_mapping].append(Mapping(*mapping))
        mapping = inp.readline()


def parse_category_mapping(inp: TextIOWrapper, category_mappings: List[List[Mapping]]):
    f"""
    """
    line = inp.readline()
    for mapping_num in range(NUM_MAPPINGS):
        line = line.rstrip(' map:\n')
        line = tuple(line.split('-to-'))
        match line:
            case (Categories.SEED, Categories.SOIL):
                read_mappings(0, category_mappings, inp)
            case (Categories.SOIL, Categories.FERTILIZER):
                read_mappings(1, category_mappings, inp)
            case (Categories.FERTILIZER, Categories.WATER):
                read_mappings(2, category_mappings, inp)
            case (Categories.WATER, Categories.LIGHT):
                read_mappings(3, category_mappings, inp)
            case (Categories.LIGHT, Categories.TEMP):
                read_mappings(4, category_mappings, inp)
            case (Categories.TEMP, Categories.HUMIDITY):
                read_mappings(5, category_mappings, inp)
            case (Categories.HUMIDITY, Categories.LOCATION):
                read_mappings(6, category_mappings, inp)
        line = inp.readline()


def line_by_line_read():
    with open('example_input', 'rt', encoding='utf8') as file_input:
        line = file_input.readline()
        file_input.readline()
        seeds = line.strip('seeds: ').rstrip('\n').split(' ')
        seeds = tuple([int(seed) for seed in seeds])
        category_mappings = [[] for _ in range(NUM_MAPPINGS)]
        parse_category_mapping(file_input, category_mappings)


line_by_line_read()
