"""
Complexity:
----------
Time: O(1)
Space: O(N) Where N is the number of calls to next()
"""
class StockSpanner:

    def __init__(self):
        self._stack = []
    
    def next(self, price: int) -> int:
        ans = 1
        while self._stack and self._stack[-1][0] <= price:
            previous_price, previous_ans = self._stack.pop()
            ans += previous_ans
        self._stack.append((price, ans))
        
        return ans