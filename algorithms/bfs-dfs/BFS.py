#!/usr/bin/env python

from graph import Graph, read_adj_list

def bfs_shortest_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.get_neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

    return "no path from {} to {}".format(start, goal)


def bfs_connected_components(graph, start):
    queue, visited = [start], set()
    while queue:
        vertex = stack.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            stack += set(graph.get_neighbors(vertex)) - visited

    return visited
