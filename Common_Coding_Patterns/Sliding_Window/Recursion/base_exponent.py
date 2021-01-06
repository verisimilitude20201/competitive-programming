"""
Problem
-------
3 different ways to compute the power of a number raised to an exponent using recursion.

Complexity:
Time: O(N)
Space: O(exponent) for fpower and fpower_optimized amnd O(1) for the tail optimized version
"""


def fpower(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * fpower(number, exponent - 1)


def fpower_tail_recursive(number, exponent, result=1):
    if exponent == 0:
        return result
    else:
        result = result * number
        exponent -= 1
        return fpower_tail_recursive(number, exponent, result)


def fpower_optimized(number, exponent):
    if exponent == 0:
        return 1
    else:
        half = fpower(number, exponent // 2)
        if exponent % 2 == 0:
            return half * half
        else:
            return number * half * half


print(fpower(2, 4))
print(fpower_tail_recursive(2, 0))
print(fpower_optimized(2, 4))
