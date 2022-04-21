"""
Complexity:
---------

Solution1
---------------

Time: O(l1 * l2 * x)
Space: O(l1 * l2 * x)

Solution2

"""
class Solution1:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        for i, restaurant1 in enumerate(list1):
            for j, restaurant2 in enumerate(list2):
                index_sum = j + i
                if restaurant1 == restaurant2:
                    if index_sum not in index_map:
                        index_map[index_sum] = []
                    index_map[index_sum].append(restaurant1)

        min_index_sum = math.inf
        for key in index_map:
            min_index_sum = min(key, min_index_sum)

        return index_map[min_index_sum]

class Solution2:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        m = len(list1)
        n = len(list2)
        for total in range(m + n - 1):
            for i in range(0, total + 1):
                if i < m and total - i < n and list1[i] == list2[total - i]
                    result.append(list1[i])
            if len(result) > 0:
                break            
        return result