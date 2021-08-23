class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def prepend(self, data):
        """
        O(1) Space/Time
        :param data:
        :return:
        """
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self._increment_length()

    def append(self, data):
        """
        O(1) Space/Time
        :param data:
        :return:
        """
        new_node = self.Node(data)
        self.append_node(new_node)

    def append_node(self, new_node):
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._increment_length()


    def print_list(self):
        """
        O(n) time
        O(1) Space
        :return:
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data, sep="", end=" --> ")
            current_node = current_node.next

    def insert(self, index, value):
        """
        O(n) Time
        O(1) Space
        :param index:
        :param value:
        :return:
        """
        if index >= self.length:
            self.append(value)
        elif index <= 0:
            self.prepend(value)
        else:
            prev_node, next_node = self._traverse_nodes_till(index)
            new_node = self.Node(value)
            prev_node.next = new_node
            new_node.next = next_node
        self._increment_length()

    def remove(self, index):
        if index <= 0:
            self.head = self.head.next
        elif index <= self.length - 1:
            prev_node, next_node = self._traverse_nodes_till(index)
            if index == self.length - 1:
                self.tail = prev_node
                prev_node.next = None
            else:
                next_node = next_node.next
                prev_node.next = next_node
        else:
            raise Exception("Sorry, index can only be between 0 and %d" % (self.length - 1))

        self._decrement_length()

    def _traverse_nodes_till(self, index):
        prev_node = self.head
        current_index = 1
        next_node = self.head.next
        while current_index != index:
            next_node = next_node.next
            prev_node = prev_node.next
            current_index += 1
        return prev_node, next_node

    def _increment_length(self):
        self.length += 1

    def _decrement_length(self):
        self.length -= 1