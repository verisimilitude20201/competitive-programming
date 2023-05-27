"""
Complexity:
----------
Time: O(M log M + N log M)
Space: O(N)
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for spell in spells:
            potion_index = self.search_potion(target / spell, potions)
            ans.append(len(potions) - potion_index)
        return ans
    
    def search_potion(target: float, potions: List[int]) -> int:
        left = 0
        right = len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > potions[mid]:
                left = mid + 1
            elif target < potions[mid]:
                right = mid - 1
        
        return left