"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 记录重复的值
        dup_set = set()
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                dup_set.add(ptr.val)
            ptr = ptr.next
        dummy_head = ListNode(None)
        newptr = dummy_head
        ptr = head
        # 过滤掉重复的值
        while ptr:
            if ptr.val not in dup_set:
                newptr.next = ptr
                newptr = newptr.next
            ptr = ptr.next
        # 处理尾节点
        newptr.next = None
        # 返回新链表
        return dummy_head.next