"""
Sample Input
["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

Approach
-------
1. For each word,
2. Sort its letters alphabetically.
3. Check if the sorted word is in the hash table.
3.1  If Yes, append the current word to it
3.2 If no, create new list with the sole word in it 
4. Return a list of values in the hash table.

"""

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]

    return list(anagrams.values())