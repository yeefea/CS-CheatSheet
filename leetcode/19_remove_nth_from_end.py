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
            ptr1  ptr2

删除ptr1.next
ptr1.next = ptr1.next.next
返回dummy.next
"""
class Solution:

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        pointer1 = dummy
        pointer2 = dummy

        for _ in range(n):
            pointer1 = pointer1.next

        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer2.next=pointer2.next.next
        return dummy.next

    def removeNthFromEnd_trivial(self, head, n):
        """
        一般解法，需要扫描两次
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        pre = dummy
        while pre.next:
            length += 1
            pre=pre.next
        pre = dummy
        count = 0
        while pre.next:
            cur = pre.next
            if count==length-n:
                pre.next = cur.next
                break
            else:
                count += 1
                pre = pre.next
        return dummy.next