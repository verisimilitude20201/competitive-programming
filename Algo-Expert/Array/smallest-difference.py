"""
Concept
-------
Consider the two arrays
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

1. Sort both arrays
arrayOne = [-1, 3, 5, 10, 20, 28]
arrayTwo = [15, 17, 26, 134, 135]

2. Two pointers to first elements of both arrays
arrayOne = [-1, 3, 5, 10, 20, 28]
            IDx1

arrayTwo = [15, 17, 26, 134, 135]
            IDx2


3. -1 < 15 and current difference = 16. Move IDx1, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                IDx1

arrayTwo = [15, 17, 26, 134, 135]
            IDx2

4. 5 < 15 and current difference = 10. Move IDx1, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                   IDx1

arrayTwo = [15, 17, 26, 134, 135]
            IDx2

5. 10 < 15 and current difference = 5. Move IDx1, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                      IDx1

arrayTwo = [15, 17, 26, 134, 135]
            IDx2

6. 20 > 15 and current difference = 5. Move IDx2, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                          IDx1

arrayTwo = [15, 17, 26, 134, 135]
            IDx2


6. 20 > 17 and current difference = 3. Move IDx2, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                          IDx1

arrayTwo = [15, 17, 26, 134, 135]
                IDx2


7. 20 < 26 and current difference = 6. Move IDx1, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                          IDx1

arrayTwo = [15, 17, 26, 134, 135]
                    IDx2


8. 28 > 26 and current difference = 2. Move IDx2, since we have to make difference between them smaller.
arrayOne = [-1, 3, 5, 10, 20, 28]
                              IDx1

arrayTwo = [15, 17, 26, 134, 135]
                        IDx2


9. 28 < 134 and current difference = 106. Move IDx1, since we have to make difference between them smaller. But we cannot move
IDx1 since its past its end of the array. Therefore, we just note the smallest difference till now that is 2 and return [28, 26]


Complexity:
-----------
Time: O(N log N + M log M) ~ O (N + M) = Because we are iterating through two arrays simulateously. Sorting time complexity is O(n log n)
Space: O(1)


"""
def smallestDifference(arrayOne, arrayTwo):
    idx1 = 0
    idx2 = 0
	arrayOne.sort()
	arrayTwo.sort()
    smallest_difference = float("inf")
    current_difference = float("inf")
    smallest_pairs = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
       first_num = arrayOne[idx1]
       second_num = arrayTwo[idx2]
       if first_num == second_num:
           return [first_num, second_num]
       elif first_num < second_num:
           current_difference = second_num - first_num
           idx1 += 1
       elif second_num < first_num:
           current_difference = first_num - second_num
           idx2 += 1
       if current_difference < smallest_difference:
           smallest_difference = current_difference
           smallest_pairs = [first_num, second_num]

    return smallest_pairs
