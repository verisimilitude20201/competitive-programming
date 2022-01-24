"""
Explanation:
-----------
Beware of taking integer division only while calculating the remainder for finding out the number of digits

Complexity:
----------
Time: O(M * d) M is the number of elements in the array, d is the nmber of digits of the number
Space: O(1)
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if num < 10:
                continue
            if self.is_digits_in_num_even(num):
                even_count += 1

        return even_count

    def is_digits_in_num_even(self, num):
        digit_count = 0
        while num:
            digit_count += 1
            num //= 10

        return digit_count % 2 == 0

solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))
print(solution.findNumbers([555,901,482,1771]))