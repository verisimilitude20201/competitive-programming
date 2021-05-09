"""
Problem
-------
Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. 
Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects
We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

Example:
-------
Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
Output: 6

Approach:
--------
Two Heaps

1. At each step, we will keep track of available capital and extract those many entries from min_capital_heap for the projects that can be done.
2. min_capital_heap is a min_heap that's already initialized with the available capitals and project number.
3. Once a project that's doable is found, we extract the profit for it and add it to the max_profit heap.
4. If a project is foumd, we add it to the available capital and continue the process.
5. If with the given capital, no project is doable, we simply break out of the loop 

Complexity:
----------
Time: O(N log N + K log N) 
    We store N capital entries initialy in the min_capital_heap, each entry has log N insertion time.
    We store K max_profite entries in the max_profile array, each entry has log N insertion time.
Space: O(N)
"""

from heapq import *


def find_maximum_capital(capitals, profits, number_of_projects, initial_capital):
    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(capitals)):
        heappush(min_capital_heap, (i, capitals[i]))

    available_capital = initial_capital
    for j in range(number_of_projects):
        while min_capital_heap and min_capital_heap[0][1] <= available_capital:
            project_no, capital = heappop(min_capital_heap)
            heappush(max_profit_heap, -profits[project_no])
        if not max_profit_heap:
            break
        available_capital += (-heappop(max_profit_heap))

    return available_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))


main()
