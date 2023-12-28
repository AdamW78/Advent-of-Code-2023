"""
https://adventofcode.com/2023/day/8#part2
"""
from typing import Tuple
from desert import Node


def nav_desert_ghost(dir_str: str, d_map: Tuple[Node, ...], start: Node, dest: Node) -> Tuple[Node, ...]:
    """
    Navigate a desert, starting
    :param dir_str:
    :param d_map:
    :param start:
    :param dest:
    :return:
    """
