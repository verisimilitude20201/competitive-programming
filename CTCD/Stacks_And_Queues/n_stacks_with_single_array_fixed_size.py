"""
Explanation
----------
0 1 2 3 4 5 6 7 8 9 10 11
------- ------- ---------
1 2     3 4 5
Stack 0 Stack 1  Stack 2

size[2, 3, 0]

Complexity:
----------
Time: O(1)
Space: O(Capacity per stack * Number of Stacks)
"""
class NStacksWithSingleArray:
    def __init__(self, capacity, n):
        self._n = n
        self._capacity = capacity
        self._array = [None] * (self._capacity * self._n)
        self._sizes = [0] * self._n

    def push(self, stack_no, element):
        if self.is_full(stack_no):
            raise Exception("Stack %d is full " % stack_no)
        top_index = self.get_top_index(stack_no)
        self._array[top_index] = element
        self._sizes[stack_no] += 1

    def pop(self, stack_no):
        if self.is_empty(stack_no):
            raise Exception("Stack %d is empty " % stack_no)
        top_index = self.get_top_index(stack_no)
        data = self._array[top_index]
        self._array[top_index] = None
        self._sizes[stack_no] -= 1

        return data

    def get_top_index(self, stack_no):
        offset = stack_no * self._capacity
        size = self._sizes[stack_no]

        return offset + size

    def is_full(self, stack_no):
        return self._sizes[stack_no] == self._capacity

    def is_empty(self, stack_no):
        return self._sizes[stack_no] == 0


n_stacks = NStacksWithSingleArray(4, 3)

n_stacks.push(0, 1)
n_stacks.push(0, 2)
n_stacks.push(0, 3)
n_stacks.push(0, 4)

n_stacks.push(1, 10)
n_stacks.push(1, 20)
n_stacks.push(1, 30)
n_stacks.push(1, 40)

n_stacks.push(2, 100)
n_stacks.push(2, 200)
n_stacks.push(2, 300)
n_stacks.push(2, 400)