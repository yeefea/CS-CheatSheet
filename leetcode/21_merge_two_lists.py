"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
解题思路：链表构建，假节点

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(None)
        last = dummy
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                last.next = l2
                l2 = l2.next
            elif l2 is None:
                last.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        return dummy.next
            