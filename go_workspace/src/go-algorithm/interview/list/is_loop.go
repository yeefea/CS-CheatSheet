package list

import (
	. "github.com/isdamir/gotype"
)

func IsLoop(head *LNode) bool {
	meetPoint := FindMeetPoint(head)
	if meetPoint == nil {
		return false
	}
	return true
}

func FindLoopNode(head *LNode) *LNode {
	meetPoint := FindMeetPoint(head)
	if meetPoint == nil {
		return nil
	}
	ptr1 := head.Next
	for ptr1 != meetPoint {
		ptr1 = ptr1.Next
		meetPoint = meetPoint.Next
	}
	return ptr1
}

func FindMeetPoint(head *LNode) *LNode {
	if head == nil || head.Next == nil {
		// 空链表
		return nil
	}
	slow := head.Next
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if fast == slow {
			return slow
		}
	}
	// fast走到底也没有和slow重合 说明链表无环
	return nil
}
