"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2

        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            current_xor = 0
            for bit in num:
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    current_xor = (current_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    current_xor = (current_xor << 1)
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, current_xor)

        return max_xor