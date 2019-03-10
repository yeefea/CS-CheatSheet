"""
迭代器模式
"""
class LinkedListNode:

    def __init__(self, predecessor, data, successor):
        self.data = data
        self.predecessor = predecessor
        self.successor = successor


class LinkedList:

    def __init__(self):
        """
        初始化链表，头，尾
        """
        self.size = 0
        self._head = LinkedListNode(None, None, None)
        self._tail = LinkedListNode(None, None, None)
        self._head.successor = self._tail
        self._tail.predecessor = self._head
        self._mod_count = 0
        
    def append(self, x):
        self.size += 1
        self._mod_count += 1
        pre = self._tail.predecessor
        node = LinkedListNode(pre, x, self._tail)
        pre.successor = node
        self._tail.predecessor = node

    def is_empty(self):
        return self.size == 0
    
    def __iter__(self):
        return LinkedListIterator(self)


class LinkedListIterator:

    def __init__(self, linked_list):
        self._list = linked_list
        self._head = linked_list._head
        self._tail = linked_list._tail
        self.cursor = self._head
        self._expect_mod_count = linked_list._mod_count
    
    def __next__(self):
        if self._expect_mod_count != self._list._mod_count:
            raise RuntimeError('list changed during iteration')
        if self.cursor.successor is self._tail:
            raise StopIteration
        self.cursor = self.cursor.successor
        return self.cursor.data


if __name__ == '__main__':
    lst = LinkedList()
    lst.append(1)
    lst.append(23)
    lst.append(456)
    for x in lst:
        print(x)
    
    it = iter(lst)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

    # it = iter(lst)
    # lst.append(7)
    # print(next(it))  这一行会抛出异常，因为在迭代过程中不能改变容器
