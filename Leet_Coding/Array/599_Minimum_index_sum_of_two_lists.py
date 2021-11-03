"""
Explanation:
-----------
findRestaurant1
---------------
1. Computes the index sum of matching string elements and stores them along with strings in HashMap
2. Computes the minimum index_sum from the HashMap and returns the string list from the map of that.

findRestaurant2
--------------
1. Starts iterating from the ascending order of sum from 0 to l1 + l2 - 11
2. Finds the first match such that it's common to both lists and returns it.

Complexity:
---------
findRestaurant1
--------------
Time: O(l1 * l2 * x) Where x is the average string length
Space: O(l1 * l2 * x) Where x is the average string length

findRestaurant2
---------------
Time: O((l1 + l2)^2 + x) Where x is the average string length
Space: O(r * x) Where r is the length of the result and x is the average string length

"""

import math

class Solution:
    def findRestaurant1(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) == 0 or len(list2) == 0:
            return []
        sum_string = {}
        for i in range(len(list1)):
            string1 = list1[i]
            for j in range(len(list2)):
                string2 = list2[j]
                if string1 == string2:
                    index_sum = i + j
                    if index_sum not in sum_string:
                       sum_string[index_sum] = []
                    sum_string[index_sum].append(string1)

        min_index_sum = math.inf
        for index_sum in sum_string:
            min_index_sum = min(min_index_sum, index_sum)

        return sum_string.get(min_index_sum)

    def find_restaurant2(self, list1, list2):
        l1 = len(list1)
        l2 = len(list2)
        common_restuarants = []
        for total_sum in range(l2 + l1 - 1):
            for i in range(total_sum):
                if i < l1 and total_sum - i < list2.length and list1[i] == list2[total_sum - i]:
                    common_restuarants.add(list1[i])
            if len(common_restuarants) > 0:
                break

        return common_restuarants


