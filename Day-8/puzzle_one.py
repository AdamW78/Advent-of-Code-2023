"""
https://adventofcode.com/2023/day/8#day-desc
"""
from collections import namedtuple
from typing import Tuple

Node = namedtuple('Node', 'label left right')


def read_desert_map(file='example_input_one') -> Tuple[Node, ...]:
    """
    Read in input to a list of nodes that make up the desert map
    :param file: File from which to read input
    :return: Tuple of nodes - desert map
    """
    with open(file, 'rt', encoding='utf8') as inp:
        directions = inp.readline().rstrip('\n')  # pylint: disable=unused-variable
        # Read blank line
        inp.readline()
        # Read nodes in desert map input
        cur_node_raw = inp.readline()
        desert_map = []
        while cur_node_raw:
            cur_node_raw = cur_node_raw.rstrip('\n').split(" = ")
            lr = cur_node_raw[1].strip('(').rstrip(')').split(', ')
            cur_node = Node(cur_node_raw[0], lr[0], lr[1])
            desert_map.append(cur_node)
            cur_node_raw = inp.readline()
        return tuple(desert_map)


print(*read_desert_map(), sep='\n')
