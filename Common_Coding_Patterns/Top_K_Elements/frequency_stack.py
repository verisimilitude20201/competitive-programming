"""
Problem:
-------
Design a class that simulates a Stack data structure, implementing the following two operations:

    1. push(int num): Pushes the number ‘num’ on the stack.
    2. pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.


Example:
-------
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2

Approach:
--------
1. Keep the sequence number with each number once it's pushed.
2. The resulting max_heap Element class simply compares first the frequency and then the sequence.

Complexity:
----------
Time: O(log N)
Space: O(N)
"""

from heapq import *


class Element:
    def __init__(self, sequence_number, number, frequency):
        self.sequence_number = sequence_number
        self.number = number
        self.frequency = frequency

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        return self.sequence_number > other.sequence_number


class FrequencyStack:
    def __init__(self):
        self.num_freq = {}
        self.max_heap = []
        self.sequence_number = 0

    def push(self, num):
        self.num_freq[num] = self.num_freq.get(num, 0) + 1
        heappush(self.max_heap, Element(self.sequence_number, num, self.num_freq[num]))
        self.sequence_number += 1
        
    def pop(self):
        if not self.max_heap:
            return None
        element = heappop(self.max_heap)
        num = element.number
        if self.num_freq[num] > 1:
            self.num_freq[num] -= 1
        else:
            del self.num_freq[num]

        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
