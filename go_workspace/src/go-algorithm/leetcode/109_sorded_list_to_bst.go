// +build ignore

package main

import (
	. "go-algorithm/list"
	. "go-algorithm/tree"
)

/*
109. 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

思路:单向链表找中间元素,用快慢双指针
递归构造二叉搜索树
边界情况
*/

func sortedListToBST(head *ListNode) *TreeNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return &TreeNode{Val: head.Val}
	}
	slow, fast := head, head
	var preSlow *ListNode
	for fast != nil && fast.Next != nil {
		preSlow = slow
		slow = slow.Next
		fast = fast.Next.Next
	}
	preSlow.Next = nil
	root := new(TreeNode)
	root.Val = slow.Val
	root.Left = sortedListToBST(head)
	root.Right = sortedListToBST(slow.Next)
	return root
}
func main() {

}
