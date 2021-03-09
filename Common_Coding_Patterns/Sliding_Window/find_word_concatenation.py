"""
Problem
-------
Given a string and a list of words, find all the starting indices of substrings in the given string 
that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example:
-------
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".


Approach
-------
1. Treat each index as start of a concatenated version of catfox
2. Maintain word_freq and word_seen
3. At each index try to match all words keeping track of all words previously seen. 
4. If all words match, add that index to result.

Assumption
---------
1. Here we assume all words are of same length

Complexity
---------
    Time: O(N * M * L) Where M = length of the string, N = number of words, L = Length of each word
    Space: O(M + N) Where N = total number of words and M is the size of the resultant list.
"""
def find_word_concatenation(string, words):
    if string == "" or len(words) == 0:
        return []
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    word_length = len(words[0])
    word_count = len(words)
    substring_index = []
    for i in range((len(string) - word_length * word_count) + 1):
        word_seen = {}
        for j in range(len(words)):
            next_word_index = i + j * word_length
            word = string[next_word_index: next_word_index + word_length]
            if word not in word_freq:
                break
            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1

            if word_seen[word] > word_freq.get(word, 0):
                break

            if j + 1 == word_count:
                substring_index.append(i)

    return substring_index


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))


main()
