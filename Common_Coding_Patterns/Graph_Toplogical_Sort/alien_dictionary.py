"""
Problem:
-------
There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. Write a method to find the correct order of the alphabets in the alien language. 
It is given that the input is a valid dictionary and there exists an ordering among its alphabets.


Example:
-------
Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points, we can conclude that the correct character order is: "bac"

Approach:
--------
Topological sort:

1. Compare characters in successive words. Take the length of the minimum word while comparing
2. Use topological sort to compute the order. 

Complexity:
---------
1. Time: O(V + E) Where V is the total number of characters and E is the number of rules. Each successive word combination forms one rule and so the 
complexity becomes O(V + N)
2. Space: O(V + N)  


"""

from collections import deque


def find_order(words):
    if len(words) == 0:
        return ""

    in_degree = {}
    graph = {}

    for word in words:
        for character in word:
            graph[character] = []
            in_degree[character] = 0

    for i in range(len(words) - 1):
        word_one, word_two = words[i], words[i + 1]
        for j in range(0, min(len(word_one), len(word_two))):
            parent = word_one[j]
            child = word_two[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    queue = deque()
    for character in in_degree:
        if in_degree[character] == 0:
            queue.append(character)

    sorted_order = []

    while queue:
        character = queue.popleft()
        sorted_order.append(character)
        for adjacent_char in graph[character]:
            in_degree[adjacent_char] -= 1
            if in_degree[adjacent_char] == 0:
                queue.append(adjacent_char)

    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
