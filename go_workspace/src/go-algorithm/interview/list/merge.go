package list

import (
	. "github.com/isdamir/gotype"
)

/*
合并两个有序链表
*/
func Merge(head1, head2 *LNode) *LNode {
	if head1 == nil || head1.Next == nil {
		// 链表1为空，返回链表2
		return head2
	}
	if head2 == nil || head2.Next == nil {
		// 链表2为空，返回链表1
		return head1
	}
	// next指针
	next1 := head1.Next
	next2 := head2.Next
	// 当前指针
	var cur *LNode
	// 新头部节点
	var head *LNode

	if next1.Data.(int) < next2.Data.(int) {
		head = head1 // 新的头部节点=两个链表中较小的头部节点
		cur = next1
		next1 = next1.Next
	} else {
		head = head2
		cur = next2
		next2 = next2.Next
	}

	for next1 != nil && next2 != nil {
		// 比较大小，小的链表进一格
		if next1.Data.(int) < next2.Data.(int) {
			cur.Next = next1
			cur = next1
			next1 = next1.Next
		} else {
			cur.Next = next2
			cur = next2
			next2 = next2.Next
		}
	}
	if next1 != nil {
		cur.Next = next1
	}
	if next2 != nil {
		cur.Next = next2
	}
	return head
}
