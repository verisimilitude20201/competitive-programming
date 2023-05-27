"""
Complexity:
----------
Time: O(N log N)
Space: O(N)
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for number_of_boxes, unit_per_box in boxTypes:
            heapq.heappush(heap, (-unit_per_box, -number_of_boxes))
        
        max_units = 0
        while len(heap):
            unit_per_box, number_of_boxes = heapq.heappop(heap)
            box_count = min(truckSize, -number_of_boxes)
            max_units += (box_count * -unit_per_box)
            truckSize -= box_count
            if truckSize == 0:
                break
        
        return max_units