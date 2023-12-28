"""
https://adventofcode.com/2023/day/8#part2
"""
from typing import Tuple, List
from desert import Node, read_desert_map, dirs


def end_nodes(nodes: List[Node]):
    """
    Check if all the nodes in nodes are end nodes, meaning the last char of their label is 'Z'
    :param nodes: Nodes to check if all are end nodes
    :return: True if all nodes are end nodes, False otherwise
    """
    for node in nodes:
        if node.label[2] != 'Z':
            return False
    return True


def nav_desert_ghost(dir_str: str, d_map: Tuple[Node, ...], start: List[Node]) -> int:
    """
    Navigate a desert, starting from all the nodes contained in start.
    :param dir_str: Directions, in the form of a string, which will be followed by ALL nodes.
    :param d_map: Desert map, containing Nodes, each of which has a label, a left, and a right node.
    :param start: Tuple of nodes from which navigation will begin (in parallel)
    :return: Number of steps necessary for ALL start nodes in start to become end nodes
    """
    steps_taken = 0
    dir_index = 0
    while not end_nodes(start):
        for i, node in enumerate(start):
            if dirs.get(dir_str[dir_index]):  # RIGHT
                start[i] = d_map[node.right]
            else:  # LEFT
                start[i] = d_map[node.left]
        if dir_index == len(dir_str) - 1:
            dir_index = -1
        dir_index += 1
        steps_taken += 1
    return steps_taken


desert_map = read_desert_map('input')
directions = desert_map[0]
s = desert_map[2]
desert_map = desert_map[1]
STEPS = nav_desert_ghost(directions, desert_map, s)
