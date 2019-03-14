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
解题思路：递归和迭代都可以
"""
class Solution:
    def reverseKGroup(self, head, k):

        cur = head
        cnt = 0
        while cur and cnt != k:
            cur = cur.next
            cnt += 1
        if cnt == k:
            nxt = self.reverseKGroup(cur, k) 
            while cnt > 0:
                tmp = head.next
                head.next = nxt
                nxt = head
                head = tmp
                cnt -= 1
            return nxt
        return head