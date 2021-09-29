import random


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 0

    def get_random_node(self):
        left_size = 0 if (self.left is None) else self.left.size()
        index = random.randint(left_size)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert_in_order(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert_in_order(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert_in_order(value)
        self.size += 1

    def find(self, d):
        if d == self.value:
            return self
        elif d <= self.value:
            return self.left.find(d) if self.left is not None else None
        else:
            return self.right.find(d) if self.right is not None else None

        return None

    def size(self):
        return self.size

    def data(self):
        return self.value


def main():
    root = BinarySearchTree(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    root.insert_in_order(3)
    root.insert_in_order(7)
    root.insert_in_order(15)
    root.insert_in_order(17)
    root.insert_in_order(30)
    root.insert_in_order(35)
    print(root.get_random_node())


main()
