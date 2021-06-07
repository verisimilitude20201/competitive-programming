"""
Problem:
-------
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example:
-------
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2] 

Approach:
--------
Similar to toplogical sort using BFS.

Complexity:
---------
1. Time: O(V + E)
2. Space: O(V + E)
"""

from collections import deque


def is_task_scheduling_possible(tasks, prerequisites):
    sorted_order = []

    if tasks <= 0:
        return False

    if tasks == 1:
        return True

    dependencies = {i: 0 for i in range(tasks)}
    task_graph = {i: [] for i in range(tasks)}

    for prerequisite in prerequisites:
        parent_task, dependent_task = prerequisite[0], prerequisite[1]
        task_graph[parent_task].append(dependent_task)
        dependencies[dependent_task] += 1

    task_queue = deque()
    for vertex in dependencies:
        if dependencies[vertex] == 0:
            task_queue.append(vertex)

    while task_queue:
        vertex = task_queue.popleft()
        sorted_order.append(vertex)
        for child in task_graph[vertex]:
            dependencies[child] -= 1
            if dependencies[child] == 0:
                task_queue.append(child)

    if len(sorted_order) != tasks:
        return False

    return True



def main():
  print("Is scheduling possible: " +
        str(is_task_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_task_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_task_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()