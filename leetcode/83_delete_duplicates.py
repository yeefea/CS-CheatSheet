"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2

示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：单向链表删除下一个元素
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_duplicates(head: ListNode) -> ListNode:
    cur = head
    while cur is not None and cur.next is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
