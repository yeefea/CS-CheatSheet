package list

/*
计算两个链表代数和
*/

import (
	. "github.com/isdamir/gotype"
)

func processNumber(n int) (int, int) {
	c := 0
	if n > 9 {
		n -= 10
		c = 1
	}
	return n, c
}

// Add 时间O(N) 空间O(N)
func Add(h1, h2 *LNode) *LNode {
	if h1 == nil || h1.Next == nil {
		return h2
	}
	if h2 == nil || h2.Next == nil {
		return h1
	}
	n := 0
	c := 0
	res := &LNode{}
	ptr1, ptr2, ptrRes := h1.Next, h2.Next, res

	for ; ptr1 != nil && ptr2 != nil; ptr1, ptr2, ptrRes = ptr1.Next, ptr2.Next, ptrRes.Next {
		n, c = processNumber(ptr1.Data.(int) + ptr2.Data.(int) + c)
		ptrRes.Next = &LNode{Data: n}
	}
	if ptr1 == nil {
		for ; ptr2 != nil; ptr2, ptrRes = ptr2.Next, ptrRes.Next {
			n, c = processNumber(ptr2.Data.(int) + c)
			ptrRes.Next = &LNode{Data: n}
		}
	} else if ptr2 == nil {
		for ; ptr1 != nil; ptr1, ptrRes = ptr1.Next, ptrRes.Next {
			n, c = processNumber(ptr1.Data.(int) + c)
			ptrRes.Next = &LNode{Data: n}
		}
	}

	if c != 0 {
		ptrRes.Next = &LNode{Data: c}
	}

	return res
}
