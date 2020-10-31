package list

/*
展开链接链表
*/

// import (
// 	. "github.com/isdamir/gotype"
// )

type ComplexLNode struct {
	Data  int
	Right *ComplexLNode
	Down  *ComplexLNode
}

// Flatten 二维链表扁平化
func Flatten(head *ComplexLNode) *ComplexLNode {
	if head == nil {
		return head
	}
	var res *ComplexLNode
	res = mergeHeadless(head, head.Right)
	return res
}

// 递归调用，逻辑复杂
func mergeHeadless(h1, h2 *ComplexLNode) *ComplexLNode {
	if h2 == nil {
		return h1
	}
	if h2.Right != nil {
		h2 = mergeHeadless(h2, h2.Right)
	}
	var head *ComplexLNode
	var cur *ComplexLNode
	next1 := h1
	next2 := h2
	if h1.Data < h2.Data {
		head = h1
		cur = h1
		next1 = next1.Down
	} else {
		head = h2
		cur = h2
		next2 = next2.Down
	}

	for next1 != nil && next2 != nil {
		// 接较小的下一个节点
		if next1.Data < next2.Data {
			cur.Down = next1
			// cur向下走一格
			cur = next1
			next1 = next1.Down
		} else {
			cur.Down = next2
			cur = next2
			next2 = next2.Down
		}
	}
	if next1 != nil {
		cur.Down = next1
	}
	if next2 != nil {
		cur.Down = next2
	}
	head.Right = nil
	return head
}
