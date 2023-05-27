"""
Complexity:
----------
Time: O(N + N log N)
Space: O(N)
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        heap = [(-freq, word) for word, freq in word_freq.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)] 
        
        
        