"""
Explanation
-----------
Row 1                 0
                     (1)
Row 2              0       1
                  (1)      (2) 
Row 3             0   1    1   0
                (1)  (2)  (3) (4) 

Row 4         0   1  1  0  1 0 0 1    
             (1) (2)(3)(4)(5)(6)(7)(8) 
             
             
             
             K % 2 + K // 2, N = 4, K = 3

Complexity:
----------
Time: O(N)
Space: O(N)

"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent = self.kthGrammar(n - 1, (k // 2) + (k % 2))
        isOdd = (k % 2 == 1)
        if parent == 1:
            return 1 if isOdd else 0
        else:~
            return 0 if isOdd else 1