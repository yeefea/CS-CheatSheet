package list

import (
	. "github.com/isdamir/gotype"
)

func Reverse(node *LNode) {
	/*
		需要左中右三个指针，把向右指的链表变成向左指，最后连上头节点
	*/
	if node == nil || node.Next == nil {
		return
	}
	/*

		1 -> 2 -> 3 -> 4
		^
		|
		node
	*/
	var left *LNode
	var cur *LNode
	var right *LNode
	cur = node.Next
	right = cur.Next
	/*

		nil		1	->	2	->	3	->	4	->	nil
		^		^		^
		|		|		|
		left	cur		right

	*/
	for {
		// 向右指针改成向左指
		cur.Next = left
		/*

			nil	<-	1		2	->	3	->	4	->	nil
			^		^		^
			|		|		|
			left	cur		right

		*/
		left = cur // 最后head要连到left
		if right == nil {
			break
		}
		cur = right
		right = cur.Next
		/*

			nil	<-	1		2	->	3	->	4	->	nil
					^		^		^
					|		|		|
					left	cur		right

		*/
	}
	node.Next = left
}

func RecursiveReverse(node *LNode) {
	/*

		node	-> nil
		node	->	1	-> nil
		node	->	1	->	2	->	3	->	4	->	nil

	*/
	subHead := rReverse(node.Next)
	node.Next = subHead
}

func rReverse(node *LNode) *LNode {
	if node == nil || node.Next == nil {
		return node
	}
	nxt := node.Next
	subHead := rReverse(nxt)
	nxt.Next = node // important!
	node.Next = nil
	return subHead
}

func InsertReverse(node *LNode) *LNode {
	if node == nil || node.Next == nil {
		return node
	}
	var right *LNode
	cur := node.Next.Next
	node.Next.Next = nil
	for cur != nil {
		right = cur.Next
		cur.Next = node.Next
		node.Next = cur
		cur = right
	}
	return node
}

// ReverseHeadless 翻转无头链表
func ReverseHeadless(node *LNode) *LNode {
	if node == nil || node.Next == nil {
		// 只有0或1个元素直接返回
		return node
	}
	// node: 1 -> 2 -> 3 -> 4 -> nil
	// 初始是尾部nil
	var tmp *LNode
	// 新的头部节点
	var new_head *LNode
	for node != nil {
		tmp = node
		node = node.Next
		tmp.Next = new_head
		new_head = tmp
	}
	return new_head
}

func SwapPair(head *LNode) {
	if head == nil || head.Next == nil {
		return
	}
	for cur := head; cur.Next != nil && cur.Next.Next != nil; cur = cur.Next.Next {
		tmp := cur.Next.Next // head -> 1 -> 2 -> 3 -> nil
		cur.Next.Next = tmp.Next
		tmp.Next = cur.Next
		cur.Next = tmp
	}
}

func ReverseKGroup(head *LNode, k int) {
	if k == 1 || head == nil || head.Next == nil {
		return
	}
	subHead := reverseOneGroup(head.Next, k)
	if head.Next == subHead {
		// 最后一组
		return
	}
	firstSubHead := subHead
	// 每一组第一个节点的前一个节点 ptr -> 1 -> 2 -> 3 -> 4
	ptr := head.Next
	for ptr != nil {
		subHead := reverseOneGroup(ptr.Next, k)
		if subHead == ptr.Next {
			//最后一组
			ptr.Next = subHead
			break
		} else {
			//不是最后一组
			tmp := ptr.Next
			ptr.Next = subHead
			ptr = tmp
		}
	}
	head.Next = firstSubHead
}

// reverseOneGroup 类似于翻转无头链表，要处理后续节点
// return new head node
func reverseOneGroup(head *LNode, k int) *LNode {
	if head == nil {
		return head
	}
	ptr := head
	for i := 0; i < k-1; i++ {
		ptr = ptr.Next
		if ptr == nil {
			return head
		}
	}
	newHead := ptr.Next
	for i := 0; i < k; i++ {
		ptr = head
		head = head.Next
		ptr.Next = newHead
		newHead = ptr
	}
	return newHead
}
