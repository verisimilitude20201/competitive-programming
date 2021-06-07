"""
Problem:
-------
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices

Example:
-------
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0


Approach:
---------

A. Topological order is the traversal from the source nodes to the sink nodes of a graph. Source nodes have incoming edges 0 and sink nodes have outgoing edges 0.

B. Topological ordering is not possible in case Graph has a cycle.

1. We first represent the graph as an adjacency list which is a dictionary with the key equal to the vertex and value is the list of edges
2. We then find the in-degree of each vertex of the graph. 
3. Those whose in-degree is 0, we add to a queue. These are the sources/
4. We pop out the sources one-by-one and add them to a sorted list. 
5. We then visit the child nodes and begin decrementing their in-degrees one-by-one. When their in-degree is 0, we add them to the queue. Process continues

Complexity:
---------
Time: O(V + E). Each vertex will become a source only once and each edge will be accessed and removed once.
Space: O(V + E)
"""

from collections import deque


def topological_order(vertices, edges):
    sorted_order = []
    if len(edges) == 0 or vertices <= 0:
        return []

    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            sources.append(vertex)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return []

    return sorted_order


def main():
    print("Topological sort: " +
          str(topological_order(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_order(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_order(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
