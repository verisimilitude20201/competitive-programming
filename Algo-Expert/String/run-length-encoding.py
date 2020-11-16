"""
Input: 
------
AAAAAAAAAAAAABBCCCCDD

RunLength Encoding 9A4A2B4C2D

Approach
---------

1. Retain a counter of run lengths and an encoded chars list to store run lengths and characters.
2. Start from the 1st character and compare with previous character. 
3. If previous character != first character
3.1    Add the runlength and previous character to encoded chars list
3.2    Reset runlength to 0
4. Increment run length.
5. Add the last run length and last character to encoded chars.
6. Join the encoded chars list to a string and return it

Complexity
----------
1. Time O(N): We loop through N characters in the string
2. Space O(N): We create an auxillary encodedChars which can hold N characters of the string at max.


"""


def runLengthEncoding(string):
    encodedChars = []
    runlength = 1
    for i in range(1, len(string)):
        previousCharacter = string[i - 1]
        currentCharacter = string[i]
        if runlength == 9 or previousCharacter != currentCharacter:
            encodedChars.append(str(runlength))
            encodedChars.append(previousCharacter)
            runlength = 0 
        runlength += 1

    encodedChars.append(str(runlength))
    encodedChars.append(string[len(string) - 1])
        
    return "".join(encodedChars)
