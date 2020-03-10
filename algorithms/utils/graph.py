#!/usr/bin/env python

class Graph():
    _vertices = []
    _adj_list = {}
    _directed = False
    _weighted = None

    def __init__(self, graph_info,
                    adj_list=False,
                    edge_list=False,
                    file=False,
                    directed=False):
        """build graph object from a dict type adjacent list"""
        self._directed = directed

        if file:
            with open(graph_info, "r") as f:
                graph_info = f.readlines()[1:]

        if edge_list:
            self._generate_graph_edge_list(graph_info)
        elif adj_list:
            self._generate_graph_adj_list(graph_info, file)
        else:
            raise NotImplementedError("Source other than adjacent list and edge list not implemented")


    def _generate_graph_edge_list(self, edge_list):
        edge_content = edge_list[0].strip("()\n").split(",")
        if len(edge_content) == 3:
            self._weighted = True
        elif len(edge_content) == 2:
            self._weighted = False
        else:
            raise ValueError("Edge tuple should be 2- or 3-tuple")

        for edge in edge_list:
            edge = edge.strip("()\n").split(",")
            if self.is_weighted():
                node1, node2, weight = edge
                edge_info = (node2, weight)
                if not self.is_directed():
                    edge_info_2 = (node1, weight)
            else:
                node1, node2 = edge
                edge_info = node2
                if not self.is_directed():
                    edge_info_2 = node1

            if node1 not in self._vertices:
                self._vertices.append(node1)
                self._adj_list[node1] = []
            if node2 not in self._vertices:
                self._vertices.append(node2)
                self._adj_list[node2] = []

            self._adj_list[node1].append(edge_info)
            if not self.is_directed():
                self._adj_list[node2].append(edge_info_2)


    def _generate_graph_adj_list(self, adj_list, is_file):
        if not is_file:
            self._adj_list = adj_list
            self._weighted = is_weighted
            for n in adj_list.keys():
                if len(adj_list[n]) != 0 and self._weighted is not None:
                    if isinstance(adj_list[n][0], tuple):
                        self._weighted = True
                    else:
                        self._weighted = False
                self._vertices.append(n)
        else:
            if adj_list[0].find("(") != -1:
                self._weighted = True
            else:
                self._weighted = False

            for adj in adj_list:
                node, neighor = adj.split(":")
                self._vertices.append(node)
                if node not in self._adj_list:
                    self._adj_list[node] = []
                if self.is_weighted():
                    for next in neighor.split(")"):
                        if next != "":
                            n, w = next.strip("(\n").split(",")
                            self._adj_list[node].append((n, w))
                else:
                    for n in neighor.strip().split(","):
                        self._adj_list[node].append(n)


    def get_vertices(self):
        return self._vertices


    def get_neighbors(self, node):
        return self._adj_list[node]


    def is_directed(self):
        return self._directed

    def is_weighted(self):
        return self._weighted


def read_adj_list_file(file_name):
    with open(file_name, "r") as f:
        is_directed = f.readline().strip()

    if is_directed == "1":
        return read_adj_list(file_name, file=True, directed=True)
    else:
        return read_adj_list(file_name, file=True, directed=False)


def read_adj_list(adj_list, file=False, directed=False):
    return Graph(adj_list, adj_list=True, file=file, directed=directed)


def read_edge_list_file(file_name):
    with open(file_name, "r") as f:
        is_directed = f.readline().strip()

    if is_directed == "1":
        return read_edge_list(file_name, file=True, directed=True)
    else:
        return read_edge_list(file_name, file=True, directed=False)


def read_edge_list(edge_list, file=False, directed=False):
    return Graph(edge_list, edge_list=True, file=file, directed=directed)
