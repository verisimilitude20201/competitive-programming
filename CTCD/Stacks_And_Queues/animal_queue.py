"""
Complexity:
Time: O(1)
Space: O(M + N) Because we use two different lists of size M and N.
"""
class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._n = 0

    def __len(self):
        return self._n

    def enqueue(self, data):
        new_node = self.Node(data)
        if self._tail is None:
            self._tail = new_node
            self._head = self._tail
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        first_node = self._head

        self._head = self._head.next
        self._n -= 1

        return first_node.data

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self._head.data

    def is_empty(self):
        return self._head is None


class Animal:
    def __init__(self, name):
        self._name = name
        self._order = 0

    def get_order(self):
        return self._order

    def set_order(self, order):
        self._order = order

    def get_name(self):
        return self._name

    def is_older_than(self, a):
        return self._order < a._order


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalQueue:
    def __init__(self):
        self._order = 0
        self._dogs = Queue()
        self._cats = Queue()

    def enqueue(self, animal: Animal):
        animal.set_order(self._order)
        self._order += 1
        if isinstance(animal, Dog):
            self._dogs.enqueue(animal)
        elif isinstance(animal, Cat):
            self._cats.enqueue(animal)

    def dequeue_any(self):
        if self._dogs.is_empty():
            return self._cats.dequeue()
        if self._cats.is_empty():
            return self._dogs.dequeue()

        cat = self._cats.peek()
        dog = self._dogs.peek()
        if cat.is_older_than(dog):
            return self._cats.dequeue()
        else:
            return self._dogs.dequeue()

    def dequeue_cat(self):
        return self._cats.dequeue()

    def dequeue_dog(self):
        return self._dogs.dequeue()


def main():
    aq = AnimalQueue()
    dog1 = Dog("Moti 0")
    cat1 = Cat("Mni 0")
    aq.enqueue(dog1)
    aq.enqueue(cat1)
    dog2 = Dog("Moti 1")
    cat2 = Cat("Mni 1")
    aq.enqueue(cat2)
    aq.enqueue(dog2)
    dog3 = Dog("Moti 2")
    cat3 = Cat("Mni 3")
    aq.enqueue(dog3)
    aq.enqueue(cat3)
    dog4 = Dog("Moti 3")
    cat4 = Cat("Mni 4")
    aq.enqueue(cat4)
    aq.enqueue(dog4)

    cat = aq.dequeue_cat()
    dog = aq.dequeue_dog()
    print(cat.get_name())
    print(dog.get_name())
    animal = aq.dequeue_any()
    print(animal.get_name())


main()
