"""
Solution 1
----------

Time: O(2^n)
Space: O(n)

Solution 2
-----------

Time: O(n)
Space: O(n)

Solution 3
----------

Time: O(n)
Space: O(1)

"""

def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n - 2)


def getNthFib2(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else
        memoize[n] = getNthFib(n-1) + getNthFib(n - 2)
        return memoize[n]


def getNthFib3(n):
    lastTwoFibs = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwoFibs[0] + lastTwoFibs[1]
        lastTwoFibs[0] = lastTwoFibs[1]
        lastTwoFibs[1] = nextFib
        counter += 1

    return lastTwoFibs[1] if n > 1 else lastTwoFibs[0]