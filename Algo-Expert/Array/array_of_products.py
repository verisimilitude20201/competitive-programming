"""
Input [5, 1, 4, 2]
Output [1, 40, 10, 20]

i.e the Product at each ith term of the output is the equal to the product every other number other than input[i]


Approach 1
----------
1. Two loops, inner loop computing a running product whenever the outer loop's index is not equal to the inner 1.


Complexity 1
------------
Time O(N^2) - Because two loops are needed
Space O(N) - Auxillary Products array


Approach 2
----------
array = [5, 1, 4, 2]
leftProducts = [1, 1, 1, 1]
rightProducts = [1, 1, 1, 1]
leftRunningProduct = 1

1. 

array = [5, 1, 4, 2]
         L
leftRunningProduct = 1

leftProducts = [1, 1, 1, 1]
                i 

2. array = [5, 1, 4, 2]
               L
leftRunningProduct = 5

leftProducts = [1, 5, 1, 1]
                   i 


3. array = [5, 1, 4, 2]
                  L
leftRunningProduct = 5

leftProducts = [1, 5, 5, 1]
                      i

4.  array = [5, 1, 4, 2]
                      L

leftRunningProduct = 20

leftProducts = [1, 5, 5, 20]
                         i


5. array = [5, 1, 4, 2]
                     R

leftRunningProduct = 1

rightProducts = [1, 1, 1, 1]
                          i

6. array = [5, 1, 4, 2]
                  R

leftRunningProduct = 2

rightProducts = [1, 1, 2, 1]
                       i

7. array = [5, 1, 4, 2]
               R

leftRunningProduct = 8

rightProducts = [1, 8, 2, 1]
                    i

8. array = [5, 1, 4, 2]
            R

leftRunningProduct = 8

rightProducts = [8, 8, 2, 1]
                 i

9. rightProducts = [8, 8, 2, 1]
   leftProducts = [1, 5, 5, 20]

   products = [1, 40, 10, 20]

Complexity 2
------------
Time O(N) -  Single loop
Space O(3N) - 3 Auxillary arrays needed. If we ignore the constant term, this is O(N) space. 


Approach 3
----------
Save on space, use the same products array to store both left and right running products in place.
Time O(N) -  Single loop
Space O(N) - Single auxillary products array


"""


def arrayOfProducts1(array):
    products = [1 for _ in array]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
		products[i] = runningProduct

    return products


def arrayOfProducts2(array):
    products = [1 for _ in array]
    leftProducts = [1 for _ in array]
    rightProducts = [1 for _ in array]
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
   
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products


def arrayOfProducts3(array):
    products = [1 for _ in array]
    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
   
    return products