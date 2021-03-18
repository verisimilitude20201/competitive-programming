"""
Problem
-------
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Approach
--------
Two pointers
1. Slow pointer = application of the function to compute the sum of squares of digits of a number once
2. Fast pointer = application of the function to compute the sum of squares of digits of a number twice

if slow == 1, its a Happy number 
if slow == fast cycle repeated and its a non-happy number

Caveat: 
 A temptation here is to use a Hash table to store the series of squares and return False if a sum_of_squares_of_digits exists in the Hash table. 
 However, this is a False positive. For larger numbers this will slow things off.

Time complexity
--------------
1. Time: O(log   N)
              10

"""
def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = get_sum_of_squares_of_digits(slow)
        fast = get_sum_of_squares_of_digits(get_sum_of_squares_of_digits(fast))
        if slow == 1:
            return True
        if slow == fast:
            return False


def get_sum_of_squares_of_digits(num):
    sum_of_squares = 0
    while num > 0:
        digit = num % 10
        sum_of_squares += (digit * digit)
        num //= 10

    return sum_of_squares


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))
  print(find_happy_number(7))
  print(find_happy_number(940))


main()