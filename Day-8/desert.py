"""
Shared code from https://adventofcode.com/2023/day/8
"""
from collections import namedtuple
from typing import Tuple

Node = namedtuple('Node', 'label left right')
dirs = {'L': 0, 'R': 1}


def read_desert_map(file='example_input_one', parallel=False) -> Tuple[str, Tuple[Node, ...], Node]:
    """
    Read in input to a list of nodes that make up the desert map
    :param parallel: Whether the desert map start is from one node or multiple nodes
    :param file: File from which to read input
    :return: Tuple of nodes - desert map
    """
    with open(file, 'rt', encoding='utf8') as inp:
        dir_str = inp.readline().rstrip('\n')
        # Read blank line
        inp.readline()
        # Read nodes in desert map input
        cur_node_raw = inp.readline()
        node_network = []
        while cur_node_raw:
            cur_node_raw = cur_node_raw.rstrip('\n').split(" = ")
            lr = cur_node_raw[1].strip('(').rstrip(')').split(', ')
            cur_node = [cur_node_raw[0], lr[0], lr[1]]
            node_network.append(cur_node)
            cur_node_raw = inp.readline()
        start_node = None
        for i, node in enumerate(node_network):
            if node[1] == node[0]:
                node_network[i][1] = i
            if node[2] == node[0]:
                node_network[i][2] = i
            j = i + 1
            q = i - 1
            while isinstance(node_network[i][1], str) or isinstance(node_network[i][2], str):
                if j < len(node_network) and node_network[j][0] == node[1]:
                    node_network[i][1] = j
                if j < len(node_network) and node_network[j][0] == node[2]:
                    node_network[i][2] = j
                if q >= 0 and node_network[q][0] == node[1]:
                    node_network[i][1] = q
                if q >= 0 and node_network[q][0] == node[2]:
                    node_network[i][2] = q
                j += 1
                q -= 1
            node_network[i] = Node(*node)
            if parallel and node_network[i].label[2] == 'A':
                if start_node is None:
                    start_node = []
                start_node.append(node_network[i])
            elif node_network[i].label == 'AAA':
                start_node = node_network[i]
        return dir_str, tuple(node_network), start_node
