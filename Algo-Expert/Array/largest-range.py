"""
Approach
--------
1. Initialize a hash table with all numbers in array as keys and values as boolean True.
2. Loop through each number in array.
2.1    If the value is False, continue the iteration
3. Make the value at the number in hash-table False.
4.1 Explore the numbers to the left of the current num while they are in the hash table.
4.2 Make the value at the left in hash tale false.
4.3 Increment currentLength
5.1 Explore the numbers to the right of the current num while they are in  hash table
5.2 Make the value at the right in hash tale false.
5.3 Increment currentLength
5. Check current length with longestLength, if big update longestRange.

Complexity
----------
O(N)/O(N) Space/Time

"""

def largestRange(array):
    nums = {}
    longest_range = []
    
    longest_length = 0
    for num in array:
        nums[num] = True
    for num in array:
        if nums[num] == False:
            continue
        nums[num] = False
		range_length = 1
        left = num - 1
        right = num + 1
        while left in nums:
            range_length += 1
            nums[left] = False
            left -= 1
		while right in nums:
			range_length += 1
			nums[right] = False
			right += 1
		if range_length > longest_length:
			longest_length = range_length
			longest_range = [left + 1, right - 1]

    return longest_range 

