"""
Complexity:
----------
Solution1
---------
Time: O(log(N)) Each time we are modulo N to get the digit to sum it for each digit. 
Space: O(log(N))

Solution2
---------
Time: O(log(N)) Each time we are modulo N to get the digit to sum it for each digit. 
Space: O(1)


"""

class Solution1:
    def get_next_n(self, n: int) -> int:
        sum_of_digits = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum_of_digits += (digit * digit)

        return sum_of_digits

    def isHappy(self, n: int) -> bool:
        seen_square_sums = set()
        while n != 1 and n not in seen_square_sums:
            seen_square_sums.add(n)
            n = self.get_next_n(n)

        return n == 1

class Solution2:
    def get_next(self, n: int) -> int:
        sum_of_digits = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum_of_digits += (digit ** 2)

        return sum_of_digits

    def isHappy(self, n: int) -> bool:
        fast_runner = self.get_next(n)
        slow_runner = n
        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))

        return fast_runner == 1