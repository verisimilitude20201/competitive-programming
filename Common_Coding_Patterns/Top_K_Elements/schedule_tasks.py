"""
Problem
-------
You are given a list of tasks that need to be run, in any order, on a server. 
Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. 
If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

Example:
-------
Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a

Approach:
--------
1. Compute the frequency of execution of each task
2. Add each frequency and task on a max_heap
3. With each iteration, try to process k + 1 tasks
4. For each processed task, decrement the frequency and append to a wait_list
5. Once the max_heap exhausts, add the current pending task count to interval_count.

Complexity:
----------
Time: O(N log N)
Space: O(N)

"""


from heapq import *


def schedule_tasks(tasks, k):
    intervalCount = 0
    taskFrequencyMap = {}
    for char in tasks:
        taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all tasks to the max heap
    for char, frequency in taskFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    while maxHeap:
        waitList = []
        n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
        while n > 0 and maxHeap:
            intervalCount += 1
            frequency, char = heappop(maxHeap)
            if -frequency > 1:
                # decrement the frequency and add to the waitList
                waitList.append((frequency + 1, char))
            n -= 1

        # put all the waiting list back on the heap
        for frequency, char in waitList:
            heappush(maxHeap, (frequency, char))

        if maxHeap:
            intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
