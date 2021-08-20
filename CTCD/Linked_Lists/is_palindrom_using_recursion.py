"""
Complexity:
----------
Time: O(N)
Space: O(N/2)

"""
from base.base_linked_list import SingleLinkedList


class Result:
    def __init__(self, node, is_equal):
        self.node = node
        self.is_equal = is_equal

    def __str__(self):
        return "Hey: " + str(self.is_equal)


def is_palindrome(head, length):
    p = is_palindrome_recurse(head, length)
    return p.is_equal


def is_palindrome_recurse(head, length):
    if length <= 0 or head is None:
        return Result(head, True)
    elif length == 1:
        return Result(head.next, True)

    res = is_palindrome_recurse(head.next, length - 2)
    res.is_equal = (head.data == res.node.data)
    res.node = res.node.next

    return res


if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(2)
    l1.append(3)
    l1.append(1)
    

    print(is_palindrome(l1.head, l1.length))
