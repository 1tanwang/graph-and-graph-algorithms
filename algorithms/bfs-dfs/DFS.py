#!/usr/bin/env python

from graph import Graph, read_adj_list

def dfs_connected_components(graph, start):
    stack, visited = [start], set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack += set(graph.get_neighbors(vertex)) - visited

    return visited


def dfs_find_all_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.get_neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

    yield "no path from {} to {}".format(start, goal)
