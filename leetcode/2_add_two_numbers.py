"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
解题思路：递归
"""
from typing import Union


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def print_node(node: ListNode):
    if node:
        buffer = []
        while node:
            buffer.append(str(node.val))
            node = node.next
        print(' -> '.join(buffer))
    else:
        print(node)


def build_number(*n):
    if len(n) == 0:
        return None
    root = ListNode(n[0])
    tmp = root
    for x in n[1:]:
        tmp.next = ListNode(x)
        tmp = tmp.next
    return root


def add_two_numbers(l1: ListNode, l2: ListNode) -> Union[ListNode, None]:
    if not l1 and not l2:
        return None
    elif not (l1 and l2):
        return l1 or l2
    else:
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = add_two_numbers(l1.next, l2.next)
        else:
            l3 = ListNode(l1.val + l2.val - 10)
            l3.next = add_two_numbers(l1.next, add_two_numbers(l2.next, ListNode(1)))  # 进位1
    return l3


n1 = build_number(2, 4, 3)
n2 = build_number(5, 6, 4)
print_node(n1)
print_node(n2)
s = add_two_numbers(n1, n2)
print_node(s)
