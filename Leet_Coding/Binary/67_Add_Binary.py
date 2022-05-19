"""
Explanation:
-----------
Solution 1 won't work in Java if the Bit string is very large since it will overflow the range of BigInteger, Long. It has low performance for large bit strings.


Complexity:
----------
Solution1:
---------
Time & Space: O(M + N)

Solution 2:
------------
Time: O(MAX(M, N))
Space: O(MAX(M, N))
"""
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        answer = []
        carry  = 0
        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")
            
            carry //= 2
            
        if carry == 1:
            answer.append("1")
        answer.reverse()
        return "".join(answer)