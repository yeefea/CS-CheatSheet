"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
解题思路：单向链表逆序
"""

from leetcode.util import print_linked_list, build_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def reverseKGroup(self, head, k: int):
        if k == 1 or (not head):
            return head
        # 1 -> 2 -> 3 -> 4
        new_head = self._reverse_one_group(head, k)
        if new_head == head:
            return head
        # 2 -> 1 -> 3 -> 4
        ptr = head
        while ptr:
            # ptr: 3 -> 4 -> nil
            tmp_head = self._reverse_one_group(ptr.next, k)
            if tmp_head == ptr.next:
                ptr.next = tmp_head
                break
            else:
                tmp = ptr.next
                ptr.next = tmp_head
                ptr = tmp
        return new_head

    def _reverse_one_group(self, head, k):
        """

        :return: new head
        """
        if not head:
            return head
        ptr = head
        for _ in range(k - 1):
            ptr = ptr.next
            if not ptr:
                # 长度不够
                return head
        new_head = ptr.next
        for _ in range(k):
            ptr = head
            head = head.next
            ptr.next = new_head
            new_head = ptr
        return new_head


if __name__ == "__main__":
    sol = Solution()
    res = build_linked_list([1, 2, 3, 4, 5])
    res = sol.reverseKGroup(res, 2)
    print_linked_list(res)
    res = sol.reverseKGroup(res, 3)
    print_linked_list(res)
