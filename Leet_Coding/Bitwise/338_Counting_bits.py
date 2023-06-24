class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]
        for i in range(1, n + 1):
            counts.append(self.count_one_bit(i))
        
        return counts
    
    def count_one_bit(self, n: int) -> int:
        count = 0
        while n != 0:
            n &= n - 1 
            count += 1
        
        return count 