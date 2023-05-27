"""
Complexity:
----------
Time:
    add()  -> Assume M calls to add(). K is the size of the heap. So M log K
    constructor -> N log K
    Total: O(M log k + N log K)
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k  = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]