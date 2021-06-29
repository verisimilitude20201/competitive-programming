"""
Explanation:
-----------
x & ~(x - 1) isolates the least bit from the LSB that is set to 1. If it equals x, it's a power of 2. Because remainining all bits will be 0.

Complexity:
----------
Time: O(1)
Space: O(1)

"""
def check_if_a_number_is_a_power_of_two(num):
    if num == num & (~ (num - 1)):
        return True
    return False


print(check_if_a_number_is_a_power_of_two(2))
print(check_if_a_number_is_a_power_of_two(4))
print(check_if_a_number_is_a_power_of_two(1))
print(check_if_a_number_is_a_power_of_two(0))
print(check_if_a_number_is_a_power_of_two(6))