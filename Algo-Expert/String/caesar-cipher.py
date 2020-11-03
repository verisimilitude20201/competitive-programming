"""
Below solutions assume we are dealing with only ASCII lowercase alphabets and the key is positive

Solution 1
---------


1. ASCII code for letter 'a' is 97 and letter 'z' is 122.
2. We first compute the newKey by mod with 26. Why is that?
    If key = 54 say (54 > 26), it can be expressed as 54 = 26 + 26 + 2. Effectively its equal to shifting right by 2 characters.
3. We then compute the ASCII value of the shifted alphabet
    shifted_key = ord(letter) + key

4. If that is less than 122, well and good. Return it. 
5. Else we need to wrap back to the beginning of the alphabet 
    96 + shifted_key % 122

Solution 2
---------

Again on similar lines as Solution 1, but we use an auxillary string containing 'a-z' in lowercase.

1. We use the index of the character in the 'alphabets' string to compute the shifted key.
2. We return mod that with 26 and return the character at that index. 

Complexity:
---------
1. Time: O(N) for both. We visit N letters in a string.
2. Space: O(N) for the first and O(1) for the second. 
    O(N): For Solution 1, we are reserving an auxillary array to hold N characters. 
    O(1): For solution 2, we are just reserving an auxillary string 'alphabets' containing 26 ASCII english characters. However, it can be generically expressed as O(m) if 
    we choose to extend this solution for other character sets..

"""
def caesarCipherEncryptor1(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
    	newLetters.append(get_new_letter1(letter, newKey))

    return "".join(newLetters)


def get_new_letter1(letter, key):
	shifted_key = ord(letter) + key
	if shifted_key <= 122:
		return chr(shifted_key)
	else:
		return chr(96 + shifted_key % 122)


def caesarCipherEncryptor2(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
    	newLetters.append(get_new_letters2(letter, key))

    return "".join(newLetters)

def get_new_letters2(letter, key):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	shifted_key = alphabets.index(letter) + key
	if shifted_key <= len(alphabets) - 1:
		return alphabets[shifted_key]
	else:
		return alphabets[shifted_key % len(alphabets)]