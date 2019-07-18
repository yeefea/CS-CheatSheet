from typing import Iterable


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __str__(self):
        return 'Node({})'.format(self.data)


class SinglyLinkedList:

    def __init__(self, iterable: Iterable = tuple()):
        self._head = Node()
        self._size = 0
        current = self._head
        for x in iterable:
            current.next = Node(x)
            current = current.next
            self._size += 1

    @property
    def left_most(self):
        return self._head.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return str(self.to_list())

    def __str__(self):
        return str(self.to_list())

    def append_left(self, data):
        node = Node(data)
        node.next = self._head.next
        self._head.next = node

    def to_list(self):
        current = self._head
        ret = []
        while current.next is not None:
            ret.append(current.next.data)
            current = current.next
        return ret


if __name__ == '__main__':
    l = SinglyLinkedList([1, 2, 3, 4, 5])
    print(l.to_list())
