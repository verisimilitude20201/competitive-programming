"""
Input = {"array": [5, 2, [7, -1], 3, [6, [-13, 8], 4]]}
Output = Product sum is defined as [x, [y,  z]] = x + 2 * (y + z)

Approach:
--------
Use recursion.

1. If element is a sub-array, call the function recursively by passing it the element and an incremented multiplier.
2. If not, add the element to sum. 
3. At the end, multiple the sum with the multiplier to calculate product sum.

Complexity:
----------
Time: O(n) Where n is the number of elements in all the arrays including sub-arrays
Space: O(d) Where d is the depth of the call stack corresponding to recursive calls for calculating product sums for sub-arrays.

"""
def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element

    return multiplier * sum
