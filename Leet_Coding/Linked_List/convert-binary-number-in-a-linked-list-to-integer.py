"""
Complexity:
----------

1. Time: O(N) Space: O(N)
2 and 3: Time: O(N), Space: O(1)
"""
class Solution:
    def getDecimalValue1(self, head: ListNode) -> int:
        bin_values = []
        while head:
            bin_values.append(head.val)
            head = head.next

        value = 0
        last_element_index = len(bin_values) - 1
        for i in range(last_element_index, -1, -1):
            bit = bin_values[i]
            value += (bit * pow(2, abs(last_element_index - i)))

        return value

    def getDecimalValue2(self, head: ListNode) -> int:
        value = head.val
        while head.next:
            value = value * 2 + head.next.val
            head = head.next
        return value

    def getDecimalValue3(self, head: ListNode) -> int:
        value = head.value
        while head.next is not None:
            value = (value << 1) | head.next.val
            head = head.next

        return value