"""
Approach
-------

Input abaxyzzyxf
Output xyzzyx


1. current_longest = [0, 1]
    0 1 2 3 4 5 6 7 8
	a b a x y z z y x
    -
  
  The first letter is the minimum palindrom

2. Start from b.

0 1 2 3 4 5 6 7 8
a b a x y z z y x
  -

3. Compare for odd

0 1 2 3 4 5 6 7 8
a b a x y z z y x
L - R

L == R, Hence decrement L and Increment R

	0 1 2 3 4 5 6 7 8
	a b a x y z z y x
  L   -   R

L is past the left end of the string so break out

odd = [0, 2]

4. Compare for even

0 1 2 3 4 5 6 7 8
a b a x y z z y x
L R
  -
string[L] != string[R] so break out

even = [0, 1]

5. maximumum of even and odd

odd = [0, 2]
even = [0, 1]

max(2, 1) ==> 2 

Therefore longest = odd

6. maximum of currentLongest and longest

longest = [0, 2]
currentLongest = [0, 1]

max(2, 1) ==> 2

Therefore, currentlongest = [0, 2]

And so on continue till the end of the string.

Complexity:
----------

Time O(N^2): We are walking through each character in string twice, once while looping and second time while comparing for even/odd palindrom checks.
Space O(1): The slice that we are doing can allocate a new string 

"""
def longestPalindromSubstring(string):
	currentLongest = [0, 1]
	for i in range(1, len(string)):
		odd = getLongestPalindromSubstring(string, i - 1, i + 1)
		even = getLongestPalindromSubstring(string, i - 1, i)
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currentLongest = max(currentLongest, longest, key=lambda x: x[1] - x[0])

	return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromSubstring(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1