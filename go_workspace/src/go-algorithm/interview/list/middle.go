package list

/*
中间节点
*/

import (
	. "github.com/isdamir/gotype"
)

// FindMiddleNode 获取链表中间节点, headless
func FindMiddleNode(node *LNode) *LNode {
	for node == nil || node.Next == nil {
		// empty
		return node
	}
	// 快慢两个指针
	fast := node
	slow := node
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}

// FindNodeBeforeMiddle
func FindNodeBeforeMiddle(node *LNode) *LNode {
	for node == nil || node.Next == nil {
		return node
	}
	preSlow := node
	slow := node
	fast := node

	for fast != nil && fast.Next != nil {
		preSlow = slow
		slow = slow.Next
		fast = fast.Next.Next
	}
	return preSlow
}
