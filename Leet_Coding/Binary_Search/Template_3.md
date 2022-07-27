```
def binary_search(nums, target)
    if len(nums) == 0:
        return -1
    while left + 1 < right:
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```

Used to search for an element or condition which requires accessing the current index and it's immediate left and right neighbor.

## Key attributes
1. Search Condition needs to access element's immediate left and right neighbors
2. Use element's neighbors to determine if condition is met and decide whether to go left or right
3. Gurantees Search Space is at least 3 in size at each step
4. Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.


## Syntax:

1. Initial Condition: left = 0, right = length-1
2. Termination: left + 1 == right
3. Searching Left: right = mid
4. Searching Right: left = mid
