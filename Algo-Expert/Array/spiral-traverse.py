"""
Spiral Traverse
--------------

Concept:
-------
Input Array: Easier to imagine the array as below

1,  2,  3,  4
12, 13, 14, 5
11, 16, 15, 6
10, 9,  8  7 

Result = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


1. Initialize SR = Start Row, ER = End Row, SC = Start Col, EC = End Col

    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5
    11, 16, 15, 6
ER  10,  9,  8  7


2. Traverse from SC to EC and add all elements to result
    Col 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5
    11, 16, 15, 6
ER  10,  9,  8  7

[1]

3. Traverse from SC to EC and add all elements to result


       Col 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5
    11, 16, 15, 6
ER  10,  9,  8  7

[1, 2]


4. Traverse from SC to EC and add all elements to result

           Col 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5
    11, 16, 15, 6
ER  10,  9,  8  7

[1, 2, 3]


5. Traverse from SC to EC and add all elements to result
                 
                Col 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 Row
    11, 16, 15, 6
ER  10,  9,  8  7

[1, 2, 3, 4]


6. Traverse the end column from EC + 1 to ER


                 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 Row
ER  10,  9,  8  7

[1, 2, 3, 4, 5]


6. Traverse the end column from EC + 1 to ER


                 
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7 Row

[1, 2, 3, 4, 5, 6]


7. Traverse in reverse end column from EC - 1 to SC

               
    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7 
               Col

[1, 2, 3, 4, 5, 6, 7]



8. Traverse in reverse end column from EC - 1 to SC

    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7 
             Row 

[1, 2, 3, 4, 5, 6, 7, 8]


9. Traverse in reverse end column from EC - 1 to SC

    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7 
         Row 

[1, 2, 3, 4, 5, 6, 7, 8, 9]

10.Traverse in reverse end column from EC - 1 to SC

    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7 
         Row 


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

11. Traverse in reverse end column from EC - 1 to SC

    SC          EC 
SR  1,  2,  3,  4
    12, 13, 14, 5 
Row 11, 16, 15, 6 
ER  10,  9,  8  7
    Row
    
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


12. Traverse back in reverse from ER - 1 to SR + 1 On SC

    SC          EC 
SR  1,  2,  3,  4
Row 12, 13, 14, 5 
    11, 16, 15, 6 
ER  10,  9,  8  7

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


13. One perimeter complete. Increment SR and SC to move inwards. Decrement ER and EC to move inwards.

14. If SC <= EC and SR <= ER continue from 1 through 13 else break out and return the result

Complexity
---------
O(N) Space: We are creating auxillary array containing all N elements of the 2-D array.
O(N) Time: We are iterating through N-elements of the 2-D array.

"""



def spiralTraverse(array):
	startRow    = 0
	startColumn = 0
	endColumn = len(array[0]) - 1
	endRow = len(array) - 1
	result = []
	while startRow <= endRow and startColumn <= endColumn:
		for col in range(startCol, endColumn + 1):
			result.append(array[startRow][col])

		for row in range(startRow + 1, endRow + 1):
			result.append(array[row][endColumn])

		for col in reversed(range(startCol, endCol))
			result.append(array[endRow][col])

		for row in reversed(range(startRow + 1, endRow)):
			result.append(array[row][startColumn])



		startRow += 1
		startColumn += 1
		endRow -= 1
		endColumn -= 1


	return result
