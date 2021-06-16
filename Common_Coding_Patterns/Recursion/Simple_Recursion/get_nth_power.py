class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = self.get_nth_power_recursive(x, abs(n))
        if n < 0:
            return 1 / pow
        return pow


    def get_nth_power_recursive(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        else:
            return x * self.get_nth_power_recursive(x, n - 1)