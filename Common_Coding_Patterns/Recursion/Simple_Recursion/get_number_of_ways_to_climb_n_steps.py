class ClimbingStairs:
    def __init__(self):
        self._cache = {}

    def get_number_of_ways_to_climb_n_steps(self, current_step, n):
        if current_step > n:
            return 0

        if current_step == n:
            return 1

        if current_step in self._cache:
            return self._cache[current_step]

        self._cache[current_step] = self.get_number_of_ways_to_climb_n_steps(current_step + 1, n) + self.get_number_of_ways_to_climb_n_steps(current_step + 2, n)

        return self._cache[current_step]


climbing_stairs = ClimbingStairs()

print(climbing_stairs.get_number_of_ways_to_climb_n_steps(0, 5))




