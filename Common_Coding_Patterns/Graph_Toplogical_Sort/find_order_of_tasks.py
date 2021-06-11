"""
Problem:
-------
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, 
write a method to find the ordering of tasks we should pick to finish all tasks

Example:
--------
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

Approach:
--------
Graph-based topological sort

Complexity:
----------
Time: O(V + E)
Space: O(V + E)
"""

from collections import deque


def find_order_of_tasks(tasks, prerequisites):
    sorted_order = []

    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}
    for prerequisite in prerequisites:
        parent_task, depedent_task = prerequisite[0], prerequisite[1]
        graph[parent_task].append(depedent_task)
        in_degree[depedent_task] += 1

    queue = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            queue.append(task)

    while queue:
        task = queue.popleft()
        sorted_order.append(task)
        for child in graph[task]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)
    if len(sorted_order) != tasks:
        return []

    return sorted_order


def main():
    print("Is scheduling possible: " + str(find_order_of_tasks(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order_of_tasks(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order_of_tasks(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
