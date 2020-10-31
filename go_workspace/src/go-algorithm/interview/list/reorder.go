package list

/*
重新排列链表
将链表从中间分为两部分，后半部分逆序，然后合并两部分，两部分的节点交替排列
*/

import (
	. "github.com/isdamir/gotype"
)

func Reorder(head *LNode) {
	if head == nil || head.Next == nil {
		return
	}

	/*
		1 -> 2 -> 3 -> 4 -> nil
		|
		ptr1


		9 -> 8 -> 7 -> 6 -> 5 -> nil
		|
		ptr2

		nil
		|
		tmp
	*/
	ptr1 := head.Next
	// 获取中间节点前一个节点
	preMid := FindNodeBeforeMiddle(ptr1)
	// 中间节点
	mid := preMid.Next
	// 从中间切断链表
	preMid.Next = nil
	// 后半部分倒序
	ptr2 := ReverseHeadless(mid)
	var tmp *LNode
	// 重新排列，合并链表
	for ptr1.Next != nil {
		tmp = ptr1.Next
		ptr1.Next = ptr2
		ptr1 = tmp

		tmp = ptr2.Next
		ptr2.Next = ptr1
		ptr2 = tmp
	}
	ptr1.Next = ptr2
}
