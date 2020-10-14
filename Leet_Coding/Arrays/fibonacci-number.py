"""
Algorithm fib1 -> 
Time Complexity: O(N)
Space Complexity: O(1)

Iteration    0 1 1 2 3 5 8
1            a b c
2              a b c
3                a b c

Basically, at each step, c denotes the sum of previous two numbers a and b.

------------------------------------------------------------------------------

Algorithm fib2

Second algorithm follows from the mathematical definition of fibonacci numbers. 

Fib(0) = 0
Fib(1) = 1
Fib(2) = Fib(1) + Fib(0)
Fib(3) = Fib(2) + Fib(1) + Fib(0)
Fib(4) = Fib(3) + Fib(2) + Fib(1) + Fib(0)

We can plot a tree. For each level of the tree, the number of computations is 2 ^ N.

                        Fib(4)


        Fib(2)                          Fib(3)

Fib(1)          Fib(0)          Fib(2)          Fib(1)

                            Fib(1)      Fib(0)

Time Complexity:  O(2^N)
Space Complexity: O(N)
------------------------------------------------------------------------------
Algorithm fib3

We maintain a cache in fib3. The cache stores the value of the ith fibonacci number at index i. This avoids doing repeated calculations.

Time Complexity: O(N)
Space Complexity: O(N)



"""



class Solution:
    def fib1(self, N: int) -> int:
        a = 0
        b = 1
        loop_ctr = 1
        if N == 0:
            return 0
        while loop_ctr < N:
            c = a + b
            a = b
            b = c
            loop_ctr += 1
        return b
    
    
    def fib2(self, N: int) -> int:
        if N < 2:
            return N
        return fib2(N - 2) + fib2(N - 1)
    
    
    def fib3(self, N: int) -> int
        cache = {0: 0, 1: 1}
        if N < 2:
            return cache[N]

        for loop_ctr in range(2, N+1):
            cache[loop_ctr] = cache[loop_ctr - 1] + cache[loop_ctr - 2]

        return cache[N]