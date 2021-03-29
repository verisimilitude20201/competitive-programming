"""
Problem
------
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example:
-------
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].


Approach:
--------

Merge intervals with a Priority Queue

0) [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 0, current_load = 0, j = None, min_heap = []

   [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 0, current_load = 0, j = [1, 4, 2], min_heap = []

   [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 2, current_load = 2, j = [1, 4, 2], min_heap = [[1, 4, 2]]

1) [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 2, current_load = 2, j = [2, 4, 1], min_heap = [[1, 4, 2]]

      2 >= 4 ? No

  [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 2, current_load = 2, j = [2, 4, 1], min_heap = [[1, 4, 2], [2, 4, 1]]
  
  [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 3, current_load = 3, j = [2, 4, 1], min_heap = [[1, 4, 2], [2, 4, 1]] 

2) [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 3, current_load = 3, j = [3, 6, 5], min_heap = [[1, 4, 2], [2, 4, 1]]
         3 >= 4 ? No

   [[1,4,2], [2,4,1], [3,6, 5]], max_cpu_load = 8, current_load = 8, j = [3, 6, 5], min_heap = [[1, 4, 2], [2, 4, 1], [3, 6, 5]]

Complexity:
----------
Time: O(N log N)
Space: O(N)

"""

from heapq import *


class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    active_jobs = []
    for job in jobs:
        while len(active_jobs) > 0 and job.start >= active_jobs[0].end:
            current_cpu_load -= active_jobs[0].load
            heappop(active_jobs)
        current_cpu_load += job.load
        max_cpu_load = max(current_cpu_load, max_cpu_load)
        heappush(active_jobs, job)

    return max_cpu_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()
