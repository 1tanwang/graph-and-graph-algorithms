#!/usr/bin/env python

class Graph():
    _vertices = []
    _adj_list = {}
    _edges = []

    def __init__(self, adj_list, undirected=True):
        """build graph object from a dict type adjacent list"""
        self._adj_list = adj_list
        for node in adj_list.keys():
             self._vertices.append(node)
             for adj in adj_list[node]:
                 if undirected and int(adj) < int(node):
                        continue
                 self._edges.append((node, adj))

    def get_vertices(self):
        return self._vertices

    def get_neighbors(self, node):
        return self._adj_list[node]


def read_adj_list(file_name):
    """read adjacent list from file to dict

    RETURN
    ------
    adj_list: dict
        the dict type adjacent list of the graph
    """
    adj_list = {}
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            line = line.split(":")
            node, adj = line[0], line[1]
            adj = adj.strip().split(",")
            adj_list[node] = adj

    return adj_list
