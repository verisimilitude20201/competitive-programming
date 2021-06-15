class Fibonacci:
    def __init__(self):
        self._cache = {}

    def get_nth_fibonacci(self, n):
        if n in self._cache:
            return self._cache[n]
        if n == 0 or n == 1:
            return n

        return self.get_nth_fibonacci(n - 1) + self.get_nth_fibonacci(n - 2)


fibonacci = Fibonacci()
print(fibonacci.get_nth_fibonacci(6))

