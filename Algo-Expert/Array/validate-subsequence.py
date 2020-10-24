"""
Approach
--------
1. Main two pointers in the array and sequence
2. Always increment first pointer in array
3. Increment second pointer only if the corresponding array value equals the sequence value

First few dry-runs
-----------------
1.  Compare current sequence elemenent and array elem
    [5, 1, 22, 25, 6, -1, 8, 10]

   


    [1,     6, -1, 10]
    sequence_index

2.  [5, 1, 22, 25, 6, -1, 8, 10]

        array_index


    [1,     6, -1, 10]
    sequence_index


3.  [5, 1, 22, 25, 6, -1, 8, 10]

           array_index


    [1,     6, -1, 10]
            sequence_index


4.  [5, 1, 22, 25, 6, -1, 8, 10]

               array_index


    [1,     6, -1, 10]
            sequence_index

5.   [5, 1, 22, 25, 6, -1, 8, 10]

                    array_index


    [1,     6, -1, 10]
            sequence_index

Solution 1
-----------
1. This iterates through both the array and the sequence 
2. It stops either when
    a. Array is exhausted
    b. Sub-sequence is exhausted.

3. If sequence_index is equal to the length of the sequence, the sequence is valid sub-sequence of the array

Solution 2
----------
1. This just iterates through the array and keeps track of the current sequence index
2. Current sequence index is incremented if and only if current value in sequence equals that in array'

Complexity:
----------
For both approaches,

Space Complexity = O(1)
Time Complexity = O(N)

"""
def isValidSubsequence1(array, sequence):
 	sequence_index = 0
 	array_index = 0
 	while sequence_index < len(sequence) and array_index < len(array):
 		if sequence[sequence_index] == array[array_index]:
 			sequence_index += 1
 		array_index += 1

 	return sequence_index == len(sequence)



def isValidSubsequence2(array, sequence):
    sequence_index = 0
    
    for value in array:
        if sequence_index == len(sequence):
            break
        if value == sequence[sequence_index]:
            sequence_index += 1

    return sequence_index == len(sequence)