"""
Complexity:
----------
Time: O(N * K + M) Where N is the length of products, K is the average length of each product string, 
M is the length of the search term
Space: O(N * K)
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:        
        root = TrieNode()
        for product in products:
            node = root
            for c in product:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

                node.suggestions.append(product)
                node.suggestions.sort()
                if len(node.suggestions) > 3:
                    node.suggestions.pop()
        
        ans = []
        node = root
        for c in searchWord:
            if c in node.children:
                node = node.children[c]
                ans.append(node.suggestions)
            else:
                # deadend reached
                node.children = {}
                ans.append([])

        return ans