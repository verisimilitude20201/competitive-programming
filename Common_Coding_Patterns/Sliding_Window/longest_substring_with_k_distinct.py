"""
Problem:
--------
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Approach
--------
Sliding Window - Variable Window Size with HashMap keeping track of distinct characters

1. Given String = araaci,   Distinct characters = 2 


0	1	2	3	4	5
a	r	a	a	c	i				Hash = {}
									Maxlength = 1

WS
WE


2. Add a in hAsh map and increment WE	

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 1}
									Maxlength = 2

WS
    WE


3. Add r in HashMap and increment WE

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 1, r: 1}
                                    Maxlength = 3

WS
        WE
		
		
4. Increment the counter of a in HashMap and increment WE

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 2, r: 1}
									Maxlength = 4

WS
            WE
			
5. Increment the counter of a in HashMap and increment WE

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 3, r: 1}
									Maxlength = 4

WS
                WE
				
8. Add c to HashMap, But number of distinct characters in HashMap > 2

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 3, r: 1, c: 1}

WS
                WE
				
				
9. Increment WS and decrement the count of a from map. Still number of distinct characters in HashMap > 2

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 3, r: 1, c: 1}

    WS
                WE
				
10. Increment WS and decrement the count of r from map. Still number of distinct characters in HashMap > 2

0	1	2	3	4	5
a	r	a	a	c	i				Hash = {a: 2, r: 0, c: 1}

        WS
                WE


Time complexity
--------------
Time: O(N) Where N is the number of characters in string.
Space: O(C) Where C is the number of distinct characters in the string

"""

import math


def longest_substring_with_k_distinct(str1, k):
    max_length = 0
    char_frequency = {}
    window_start = 0

    for window_end in range(len(str1)):
        ending_character = str1[window_end]
        if ending_character not in char_frequency:
            char_frequency[ending_character] = 0
        char_frequency[ending_character] += 1

        while len(char_frequency) > k:
            starting_character = str1[window_start]
            char_frequency[starting_character] -= 1
            if char_frequency[starting_character] == 0:
                del char_frequency[starting_character]

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print("Maximum sum of a subarray of size K: " + str(longest_substring_with_k_distinct("araaci", 2)))
print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
