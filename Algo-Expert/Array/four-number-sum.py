"""
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