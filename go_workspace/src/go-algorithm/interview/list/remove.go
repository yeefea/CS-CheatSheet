package list

/*
删除重复元素

单向链表删除元素需要2个指针
*/

import (
	. "github.com/isdamir/gotype"
)

// O(N^2)复杂度，顺序删除
func RemoveDup(head *LNode) {
	if head == nil || head.Next == nil {
		// 链表只有0或1个元素，不需要删除
		return
	}
	// 2层循环删除重复节点
	for node := head.Next; node != nil; node = node.Next {
		innerLeft := node
		for innerNode := node.Next; innerNode != nil; {
			if innerNode.Data == node.Data {
				innerLeft.Next = innerNode.Next
				innerNode = innerNode.Next
			} else {
				innerLeft = innerNode
				innerNode = innerNode.Next
			}
		}
	}
}

// O(N^2)复杂度，递归
func RemoveDupRecursive(head *LNode) {
	if head == nil {
		return
	}
	rRemoveDup(head.Next)

}

func rRemoveDup(node *LNode) {
	if node == nil || node.Next == nil {
		return
	}

	left := node
	rRemoveDup(left.Next)
	right := left.Next

	for right != nil {
		if node.Data == right.Data {
			// duplicated
			left.Next = right.Next
			right = left.Next
		} else {
			left = left.Next
			right = right.Next
		}
	}
}

// O(1)复杂度，用哈希表空间换时间
func RemoveDupHashSet(head *LNode) {
	if head == nil {
		return
	}
	hashSet := make(map[interface{}]interface{})
	left := head.Next
	for node := head.Next; node != nil; node = node.Next {
		if _, ok := hashSet[node.Data]; ok {
			// duplicated
			left.Next = node.Next
		} else {
			hashSet[node.Data] = nil
			left = node
		}
	}

}

// RemoveNode 只给定一个节点的指针，删除节点
func RemoveNode(head, node *LNode) {
	if head == nil || head.Next == nil || node == nil {
		return
	}
	/*
		1. 非尾部节点，把后面的数据向前移，删除尾节点
		2. 尾部节点，从头遍历链表，删除节点
	*/
	// 删除尾部节点
	if node.Next == nil {
		pre := head
		/* head -> 1 -> 2 -> 3 -> nil
		(pre)
		*/
		for pre.Next != nil {
			if pre.Next == node {
				pre.Next = nil
				break
			}
			pre = pre.Next
		}
		return
	}
	/*
		head -> 1 -> 2 -> 3 -> nil,  remove 2
	*/

	pre := node
	cur := node
	for cur.Next != nil {
		// Data向前移
		cur.Data = cur.Next.Data
		/*
			head -> 1 -> 3 -> 3 -> nil
						cur
		*/
		pre = cur
		cur = cur.Next
		/*
			head -> 1 -> 3 -> 3 -> nil
						pre   cur
		*/
	}
	/*

		head -> 1 -> 3 -> nil
					pre
	*/
	pre.Next = nil
}
