"""
Complexity:
----------
Time: O(1)
Space: O(1)
"""
from base import SingleLinkedList

def delete_middle_node(slist, middle_node):
    if middle_node is None:
        return None
    middle_node.data = middle_node.next.data
    middle_node.next = middle_node.next.next


if __name__ == '__main__':
    slist = SingleLinkedList()
    slist.append("a")
    slist.append("b")
    slist.append("c")
    slist.append("d")
    slist.append("e")

    delete_middle_node(slist, SingleLinkedList.Node("c"))