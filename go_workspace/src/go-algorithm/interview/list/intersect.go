package list

/*
检查两个链表是否相交
*/

import (
	. "github.com/isdamir/gotype"
)

// IsIntersect 检查是否有相同的尾节点
func IsIntersect(head1, head2 *LNode) bool {
	if head1 == nil || head2 == nil {
		return false
	}
	cur1 := head1.Next
	cur2 := head2.Next
	if cur1 == nil || cur2 == nil {
		return false
	}
	for cur1.Next != nil {
		cur1 = cur1.Next
	}
	for cur2.Next != nil {
		cur2 = cur2.Next
	}
	return cur1 == cur2
}

func FindIntersectNode(head1, head2 *LNode) *LNode {
	if head1 == nil || head2 == nil {
		return nil
	}
	length1 := 0
	length2 := 0
	cur1 := head1.Next
	cur2 := head2.Next
	if cur1 == nil || cur2 == nil {
		return nil
	}
	for cur1 != nil {
		cur1 = cur1.Next
		length1++
	}
	for cur2 != nil {
		cur2 = cur2.Next
		length2++
	}

	if cur1 == cur2 {
		cur1 = head1
		cur2 = head2
		diff := length1 - length2
		if diff > 0 {
			length1 -= diff
			for i := 0; i < diff; i++ {
				cur1 = cur1.Next
			}
		} else if diff < 0 {
			diff = -diff
			for i := 0; i < diff; i++ {
				cur2 = cur2.Next
			}
		}
		for cur1 != cur2 {
			cur1 = cur1.Next
			cur2 = cur2.Next
		}
		return cur1
	}
	return nil
}
