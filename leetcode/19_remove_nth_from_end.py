"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
解题思路：假节点+双指针扫描一趟

dummy->1->2->3->4->5, n=2
             |     |
            ptr2  ptr1

删除ptr2.next
ptr2.next = ptr2.next.next
返回dummy.next
"""
from data_structure.linked_list import Node


def print_linked_list(head):
    lst = []
    while head:
        lst.append(str(head))
        head = head.next
    print('->'.join(lst))


class Solution:

    def removeNthFromEnd(self, head, n):
        """
        1 2 3 4 5 6 7 8 9, n=1
                        |
                        ptr1
        :param head:
        :param n:
        :return:
        """
        if n < 1:
            return head
        dummy = Node(0)
        dummy.next = head
        pointer1 = dummy
        pointer2 = dummy
        for i in range(n):
            pointer1 = pointer1.next
            if pointer1 is None:
                return head
        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer2.next = pointer2.next.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    root = Node(1)
    node = root
    for i in range(2, 10, 1):
        node.next = Node(i)
        node = node.next
    print_linked_list(root)
    ret = sol.removeNthFromEnd(root, 9)
    print_linked_list(ret)
