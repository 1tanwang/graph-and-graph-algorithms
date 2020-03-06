## This markdown file contains quick notes for graph types and components mentioned in the book 

<dl>
  <dt>Null Graph</dt>
  <dd>A null graph is a graph where the node set is empty, and, obviously, the edge set is also empty</dd>

  <br>

  <dt>Empty Graph</dt>
  <dd>An empty graph is a graph where the edge set is empty. A null graph is an empty graph but not vice versa. </dd>

  <br>

  <dt>Simple Graph</dt>
  <dd>Simple graphs are graphs where only one edge could exist between any pair of nodes. </dd>

  <br>

  <dt>Multigraph</dt>
  <dd>Multigraphs are graphs where multiple edges between two nodes can exist, in contrary to simple graphs. </dd>

  <br>

  <dt>Adjacent Nodes</dt>
  <dd>Two nodes in a graph are adjacent when they are connected via an edge. </dd>

  <br>

  <dt>Incident Edges</dt>
  <dd>Two edges are incident when they share one endpoint (i.e., are connected via a node). In a directed graph, two edges are incident if the ending of one is the beginning of the other; that is, the edge directions must match for edges to be incident. </dd>

  <br>

  <dt>Walk</dt>
  <dd>A walk is a sequence of incident edges traversed one after another. When a walk does not end where it started then it is called an open walk. When a walk returns to where it was started, it is called a closed walk. </dd>

  <br>

  <dt>Trail</dt>
  <dd>A trail is a walk where no edge is traversed more than once. A closed trail is called a tour or circuit. </dd>

  <br>

  <dt>Path</dt>
  <dd>A walk where nodes and edges are distincct is called a path, and a closed path is called a cycle. </dd>

  <br>

  <dt>Hamiltonian Cycle</dt>
  <dd>A graph has a Hamiltonian cycle if it has a cycle succh that all the nodes in the graph are visited. </dd>

  <br>

  <dt>Eulerian Tour</dt>
  <dd>A graph has an Eulerian tour if all the edges are traversed only once. </dd>

  <br>

  <dt>Connected Graph</dt>
  <dd>A graph is connected if there exists a path between any pair of nodes in it. </dd>

  <br>

  <dt>Diameter</dt>
  <dd>The diameter of a graph is defined as the length of the longest shortest path between any pair of nodes in the graph. It is defined only for connected graphs because the shortest path might ot exist in desconnected graphs. </dd>

  <br>

  <dt>Tree</dt>
  <dd>A tree is a graph structure that has no cycle in it. </dd>

  <br>

  <dt>Spanning Tree</dt>
  <dd>A spanning tree of a connected undirected graph is a tree that includes all the nodes in the original graph and a subset of its edges.</dd>

  <br>

  <dt>Steiner Tree Problem</dt>
  <dd>The Steiner Tree problem is similar to the minimm spanning tree problem but only on a subset of nodes. </dd>

  <br>

  <dt>Complete Graph</dt>
  <dd>A complete graph is a graph where all possible edges for all of its nodes exist in the graph.</dd>

  <br>

  <dt>Planar and Nonplanar Graph</dt>
  <dd>A graph that can be drawn in such a way that no two edges cross each other is called planar. </dd>

  <br>

  <dt>Bipartite Graph</dt>
  <dd>A bipartite graph is a graph where the node set can be partitioned into two sets such that, for all edges, one endpoint is in one set and the other endpoint is the other set. </dd>

  <br>

  <dt>Regular Graph</dt>
  <dd>A regular graph is a graph in which all nodes have the same degree. (e.g. a regular graph where all nodes have degree 2 is called a 2-regular graph. </dd>

  <br>

  <dt>Bridge</dt>
  <dd>Bridges are edges in a graph with several connected components whose removal will increase the number of connected components. The remoal of these edges results in the disconnection of formerly connected components and hence an increase in the number of components. </dd>
</dl>
