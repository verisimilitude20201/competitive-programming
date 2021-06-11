"""
Problem:
-------
Given a sequence originalSeq and an array of sequences, 
write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

Example:
-------
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct   
[1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers 
in the 'originalSeq'.

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct 
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]

Approach:
--------
This is similar to topological sort but for the following differences.

1. At each step we check if the current source in queue is equal to the corresponding number at the index in original sequence. If not, we return False
2. If there are more than one sources in queue, then there is more than one way to sequence them that may not match the original sequence. So we return
False

Complexity:
-----------
Time: O(V + N) V is count of distinct numbers and N is the total numbers in all sequences
Space: O(V + N)

"""

from collections import deque


def can_construct_sequence(original_sequence, sequences):
    sorted_order = []
    if len(original_sequence) == 0 or len(sequences) == 0:
        return False

    in_degree = {}
    graph = {}

    for sequence in sequences:
        for num in sequence:
            in_degree[num]  = 0
            graph[num] = []

    for sequence in sequences:
        for i in range(len(sequence) - 1):
            parent, child = sequence[i], sequence[i + 1]
            in_degree[child]  += 1
            graph[parent].append(child)

    sources = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            sources.append(vertex)

    while sources:
        if len(sources) > 1:
            return False
        if original_sequence[len(sorted_order)] != sources[0]:
            return False
        c_vertex = sources.popleft()
        sorted_order.append(c_vertex)
        for child in graph[c_vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_sequence)


def main():
    print("Can construct: " +
          str(can_construct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
       str(can_construct_sequence([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
