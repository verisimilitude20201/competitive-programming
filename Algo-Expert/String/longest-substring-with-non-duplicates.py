"""
Approach:
--------
Input: clementisacap
Output: mentisac

Pointers

S = Abbreviated to startIdx
C = current char

1. lastSeenAt = {}, startIdx = 0, longest = [0:1]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
C

2.  c not in lastSeenAt,

lastSeenAt = {c: 0}, startIdx = 0, 

longest[1] - longest[0] < i + 1 - startIdx ~ 1 < 1 is False 
Therefore, longest = [0: 1]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
C

3. Update C

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
  C

3. l not in lastSeenAt

lastSeenAt = {c: 0, l: 1}, startIdx = 0;
longest[1] - longest[0] < i + 1 - startIdx ~ 1 < 2;
Therefore, longest = [0 : 2]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
  C

4. Update C

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
    C


5. e not in lastSeenAt

lastSeenAt = {c: 0, l: 1, e: 2}, startIdx = 0;
longest[1] - longest[0] < i + 1 - startIdx ~ 2 < 3;
Therefore, longest = [0 : 3]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
    C

6. Update C

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
      C

7. m not in lastSeenAt

lastSeenAt = {c: 0, l: 1, e: 2, m: 3}, startIdx = 0;
longest[1] - longest[0] < i + 1 - startIdx ~ 3 < 4;
Therefore, longest = [0 : 4]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

S
        C

8. But now, e is seen in lastSeenAt, we need to update startIdx.

startIdx = max(startIdx, lastSeenAt[char] + 1) ~ max(0, 3) = 3 ;
longest[1] - longest[0] < i + 1 - startIdx ~ 4 < 1; False
Therefore, longest = [0 : 4]

0 1 2 3 4 5 6 7 8 9 10 11 12
c l e m e n t i s a c  a  p

      S
        C

 And so on

Complexity:
----------
Time: O(N)
Space: O(min(N, a)). 'a' is the number of unique characters in the string. The Hashmap can hold only unique characters in the string.

"""





def longestSubstringWithoutDuplication(string):
    startIdx = 0
    longest = [0 : 1]
    lastSeenAt = {}
    for i, char in enumerate(string):
    	if char in lastSeenAt:
    		startIdx = max(startIdx, lastSeenAt[char] + 1)
    	if longest[1] - longest[0] < i + 1 - startIdx:
    		longest = [startIdx, i + 1]
    	lastSeenAt[char] = i
  	return string[longest[0] : longest[1]]