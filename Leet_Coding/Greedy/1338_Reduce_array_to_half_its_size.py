"""
Complexity:
----------
Time: O(N log N)
Space: O(N)
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (-freq, -num))
        
        removed_cnt = 0
        ans = set()
        while len(heap):
            frequency, number = heapq.heappop(heap)
            removed_cnt += (-frequency)
            ans.add(-number)
            if removed_cnt >= (len(arr) // 2):
                break
        
        return len(ans)