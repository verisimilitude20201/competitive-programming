"""
Problem
-------
Given a string, find the length of the longest substring, which has no repeating characters.

For example:
Input: aabccbb
Output: 3 viz "abc"

Approach
--------
Sliding Window with Variable Window size

1. Given string

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {}
											 
WS
WE


2. Add a to HashMap and increment max_length and WE

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {a: 0}
											 
WS
    WE
	

3. Now a is already present in the hash_map. Therefore, we increment WE and WS

WS = max(WS, (last index of a + 1)) = max(0, 1) = 1

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {a: 0}
											 
    WS
        WE


4. Add b and c to HashMap

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {a: 0, b: 2, c: 3}
											 
    WS
                WE

5. Now c at index 4 is already present in the HashMap. Therefore, increment WS and WE both

WS = max(WS, (last index of c + 1)) = max(1, 4) = 4

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {a: 0, b: 2, c: 3}
											 
                WS
                    WE

6. Again, Now b at index 5 is already present in the HashMap. Therefore, increment WS and WE both

WS = max(WS, (last index of b + 1)) = max(4, 3) = 4. Hence, we won't change WS since it cannot go behind. That's why the max

0	1	2	3	4	5	6
a	a	b	c	c	b	b                    Hash = {a: 0, b: 2, c: 3}
											 
                WS
                        WE

7. Again same logic as step 6. Program ends and the maximum string length without duplicates is 3
  
Complexity:
---------

Time: O(N)
Space: O(1). At any time, there will be at max 26 letters of the English alphabet in the HashMap.

Tricky Part:
-----------

Increment WS by

WS = max(WS, last index of already seen character + 1)
"""



def non_repeat_substring(string):
    max_length = 0
    window_start = 0
    char_index_map = {}

    for window_end in range(len(string)):
        ending_character = string[window_end]
        if ending_character not in char_index_map:
            char_index_map[ending_character] = window_end
        else:
            # Tricky - Start the next index of WS to an index after the last index of ending_character
            window_start += max(window_start, char_index_map[ending_character] + 1)

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abccde")))



