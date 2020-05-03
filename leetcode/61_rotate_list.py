"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def rotateRight(self, head, k: int):
        if k < 1 or not head:
            return head
        # 获取链表长度，尾节点引用
        n = 1
        end_node = head
        while end_node.next:
            n += 1
            end_node = end_node.next
        # 长度为1直接返回
        if n == 1:
            return head
        # k取模，减少rotate次数
        k %= n
        if k == 0:
            return head
        # rotate
        ptr = head
        for _ in range(n-k-1):
            ptr = ptr.next
        new_head = ptr.next
        ptr.next = None
        end_node.next = head
        return new_head


if __name__ == '__main__':
    from util import print_linked_list, build_linked_list
    sol = Solution()
    res = sol.rotateRight(build_linked_list([]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2]), 1)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3,4,5]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3]), 20000000)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3,4,5]), 5)
    print_linked_list(res)