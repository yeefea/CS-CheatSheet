"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
解题思路：K路归并
"""
import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = ListNode(0)
        ptr = dummy_head
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                lists[i] = node.next

        while heap:
            val, i = heapq.heappop(heap)
            ptr.next = ListNode(val)
            ptr = ptr.next
            node = lists[i]
            if node:
                lists[i] = node.next
                heapq.heappush(heap, (node.val, i))

        return dummy_head.next


def print_list(list_node):
    print('[', end='')
    while list_node:
        print(list_node.val, end=', ')
        list_node = list_node.next
    print(']')


def build_linked_list(lst):
    head = ListNode(0)
    ptr = head
    for x in lst:
        ptr.next = ListNode(x)
        ptr = ptr.next
    return head.next


if __name__ == '__main__':
    sol = Solution()
    res = sol.mergeKLists([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])])
    print_list(res)
