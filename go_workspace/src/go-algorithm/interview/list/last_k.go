package list

/*
查找倒数第K个节点
*/

import (
	. "github.com/isdamir/gotype"
)

func FindLastK(head *LNode, k int) *LNode {
	if head == nil || head.Next == nil || k < 1 {
		return nil
	}
	fast := head
	slow := head
	i := 0
	for ; i < k && fast != nil; i++ {
		fast = fast.Next
	}
	if i < k {
		return nil
	}
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}

	return slow
}
