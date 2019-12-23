"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：双指针

边界情况 [1] 1 -> []
        [1,2] 1 -> [1]
        [1,2] 2 -> [2]
"""
from data_structure.linked_list import Node


def print_linked_list(head):
    lst = []
    while head:
        lst.append(str(head))
        head = head.next
    print('->'.join(lst))


class Solution:

    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        left = head
        right = head
        for i in range(n):
            right = right.next
        if not right:  # right已经走到尽头 => n=length of list => remove first node
            # 考虑边界情况[1] head.next -> None
            return head.next
        while right.next:
            right = right.next
            left = left.next
        self._rm_next(left)
        return head

    def _rm_next(self, node):
        if not node.next:
            return
        nxt_nxt = node.next.next
        node.next.next = None
        node.next = nxt_nxt


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
