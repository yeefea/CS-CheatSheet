// +build ignore

package main

// ListNode .
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	if m == n {
		return head
	}
	dummy := new(ListNode)
	dummy.Next = head
	head = dummy
	for i := 0; i < m-1; i++ {
		head = head.Next
	}
	head.Next = reverse(head.Next, n-m) // here m-n must be greater than 0
	return dummy.Next
}

func reverse(head *ListNode, n int) *ListNode {
	h := head
	for i := 0; i < n; i++ {
		tmp := head.Next
		head.Next = tmp.Next
		tmp.Next = h
		h = tmp
	}
	return h
}
