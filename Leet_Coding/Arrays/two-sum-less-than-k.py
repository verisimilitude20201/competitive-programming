"""
Solution 1:
-----------
Time complexity: O(N), space complexity O(N)

1. We compare each elemenent with every other element in the array and compute the sum.
2. If sum is less than K
    2.1 We compare it with a max_sum
    2.2 Assign sum to max_sum if its greater than current value of max_sum




Solution 2:
----------
Time complexity: O(N log (N)), space complexity O(log(N))

1. We first sort the array
2. low := 0, high := 1, S := -1
3. while low < high
    3.1 if sum of A[low] and A[high] < K:
    3.1.1       S = max(S, A[low] + A[high])
    3.1.3       low -= 1
    3.1.4 else
    3.1.4       high += 1

4. Return the last S.

"""

class Solution1:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_sum_less_than_k = -1
        for first_loop_ctr in range(0, len(A)):
            for second_loop_ctr in range(first_loop_ctr + 1, len(A)):
                sum = A[first_loop_ctr] + A[second_loop_ctr]
                if sum < K:
                    if sum > max_sum_less_than_k:
                        max_sum_less_than_k = sum

        return max_sum_less_than_k


class Solution2:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_sum_less_than_k = -1
        A.sort()
        low = 0
        high = len(A) - 1
        while low < high:
            sum1 = A[low] + A[high]
            if sum1 < K:
                if sum1 > max_sum_less_than_k:
                    max_sum_less_than_k = sum1
                low += 1
            else:
                high -= 1

        return max_sum_less_than_k