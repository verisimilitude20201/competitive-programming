"""
Complexity:
-----------
check_permutation1
------------------
Time: O(N log N)
Space: O(N)

check_permutations2
-------------------
Assumes ASCII chars

Time: O(N)
Space: O(1/128)
"""
from typing import List


def check_permutation1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    return l1 == l2


def check_permutations2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    alpha = [0] * 128
    for c in s1:
        c = ord(c.lower())
        alpha[c] += 1

    for c in s2:
        c = ord(c.lower())
        alpha[c] -= 1
        if alpha[c] < 0:
            return False

    return True


print(check_permutation1("abhi", "bhik"))
print(check_permutations2("abhi", "bhia"))

