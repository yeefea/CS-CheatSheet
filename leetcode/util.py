# Definition for singly-linked list.
class SingleLinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_linked_list(list_node):
    print('[', end='')
    while list_node:
        print(list_node.val, end=', ')
        list_node = list_node.next
    print(']')


def build_linked_list(lst):
    head = SingleLinkedListNode(0)
    ptr = head
    for x in lst:
        ptr.next = SingleLinkedListNode(x)
        ptr = ptr.next
    return head.next
