"""
Approach
--------
quadruplets = []
pairs_of_sums = {}

1. From i in 1st element of array to second last element
1.1     From j in i + 1th element to last element of the array
1.2.            current_sum = array[i] + array[j]
1.3              difference = targetSum - currentSum
1.4              if difference in hashtable pairs_of_sums
1.4.1                   append array[i] and array[j] and pair to quadruplets
1.5    From k in 0 to i
1.5.1           current_sum = array[i] + array[k]
1.5.2           If current_sum in pairs_of_sums hash table
1.5.3                 Append the list [array[i], array[k]] to pairs_of_sums[current_sum]
1.5.4           Else
1.5.5                 Set pairs_of_sums[current_sum] = [[array[i], array[k]]]

Complexity
---------
O(N^2) Average time complexity
O(N^2) Space Complexity

"""
def fourNumberSum(array, targetSum):
    quadruplets = []
    pairs_of_sums = {}
    for i in range(1, len(array)-1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            difference = targetSum - current_sum
            if difference in pairs_of_sums:
                for pair in pairs_of_sums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pairs_of_sums:
                pairs_of_sums[current_sum] = [[array[i], array[k]]]
            else:
                pairs_of_sums[current_sum].append([array[i], array[k]])
				
	return quadruplets