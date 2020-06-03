"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
解题思路：链表构建

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            l_new = l1
            l1 = l1.next
        else:
            l_new = l2
            l2 = l2.next
        head = l_new
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    l_new.next = l1
                    l1 = l1.next
                else:
                    l_new.next = l2
                    l2 = l2.next
                l_new = l_new.next
            else:
                break
        if l1:
            l_new.next = l1
        if l2:
            l_new.next = l2
        return head
