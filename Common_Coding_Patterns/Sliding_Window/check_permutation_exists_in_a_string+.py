"""
Problem
-------
Given a string and a pattern, find out if the string contains any permutation of the pattern.

For example:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Approach
-------
Sliding Window with Dynamic Window Size: Use of a Hash table to store pattern frequencies. Our goal will be to match all the characters from this HashMap with a sliding window in the given string

Input

0 1 2 3 4 5 6
o i d b c a f,       pattern = abc, char_frequency = {}, matched = 0
WS
WE
1. Add elements of the pattern to char_frequency one by one

char_frequency = {a: 1, b: 1, c: 1}


2.   Skip to b, decrement it's frequency

0 1 2 3 4 5 6
o i d b c a f,       pattern = abc, char_frequency = {a: 1, b: 1, c: 1}, matched = 0
WS
      WE

3. Here, current index 3 >= the length of the pattern (3), increment WS. matched won't be decremented because o is 
not in char_frequency

0 1 2 3 4 5 6
o i d b c a f,       pattern = abc, char_frequency = {a: 1, b: 0, c: 1}, matched = 1
WS
      WE

4. Decrement c and increment matched. current index 3 >= the length of the pattern (3), increment WS. matched won't be decremented

0 1 2 3 4 5 6
o i d b c a f,       pattern = abc, char_frequency = {a: 1, b: 0, c: 0}, matched = 2
  WS
        WE

Complexity
----------
Time: O(M + N) Where M is the number of characters in the pattern, N is the length of the string
Space: O(M) where M is the length of the pattern


Tricky part
----------
We increment matched only when the frequency of the character comes to 0. This is because, we would need to weed out cases such as

Str = bidbcaf, P = abc

matched should not be incremented for the first b.


"""
def check_permutation_exists_in_a_string(str1, pattern):
    matched = 0
    char_frequency = {}
    window_start = 0

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True

        if window_end >= len(char_frequency) - 1:
            left_char = str1[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


print('Permutation exist: ' + str(check_permutation_exists_in_a_string("oidbcaf", "abc")))
print('Permutation exist: ' + str(check_permutation_exists_in_a_string("odicf", "dc")))
print('Permutation exist: ' + str(check_permutation_exists_in_a_string("bcdxabcdy", "bcdyabcdx")))
print('Permutation exist: ' + str(check_permutation_exists_in_a_string("aaacb", "abc")))