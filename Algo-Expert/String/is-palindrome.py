"""
Approach
-------
Let N be the length of the string. 

1. Compare ith and (N-i-1)th character from the string.
2. Break out and return false if they are not equal
3. Break out from the loop if half the list has been traversed.
4. Default the is_palindrom flag to True.

Complexity
---------
1. Time O(N): We loop through N-characters of the string
2. Space O(1): No auxillary space reserved.

"""

def isPalindrome(string):
    is_palindrom = True

    for i in range(len(string)):
        first_index = i
        last_index  = len(string) - i - 1
        if first_index >= last_index:
            break

        if string[first_index] != string[last_index]:
            is_palindrom = False
			break
        
    return is_palindrom
