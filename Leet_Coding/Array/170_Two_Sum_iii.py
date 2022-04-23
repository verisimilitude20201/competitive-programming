"""
TwoSum1
-------
Time:
-----
add: O(1) amortized
find: O(N Log N)

Space: O(N) 

TwoSum2
-------
Time: 
-----
add: O(1)
find: O(N)

Space: O(N)
"""
from collections import defaultdict


class TwoSum1:

    def __init__(self):
        self._list = []
        self._is_sorted = False

    def add(self, number: int) -> None:
        self._list.append(number)

    def find(self, value: int) -> bool:
        if not self._is_sorted:
            self._list.sort()
        low = 0
        high = len(self._list) - 1
        while low < high:
            two_sum = self._list[low] + self._list[high]
            if value == two_sum:
                return True
            elif value < two_sum:
                high -= 1
            else:
                low += 1

        return False

class TwoSum2:

    def __init__(self):
        self._num_freq = {}
        

    def add(self, number: int) -> None:
        self._num_freq[number] = self._num_freq.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for number in self._num_freq:
            complement = value - number
            if complement != number:
                if number in self._num_freq:
                    return True
            elif self._num_freq[number] > 1:
                return True
        
        return False


twoSum = TwoSum();
twoSum.add(1);
twoSum.add(3);
twoSum.add(5);
print(twoSum.find(4))
print(twoSum.find(7))

