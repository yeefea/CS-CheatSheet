// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/*
117. 填充每个节点的下一个右侧节点指针 II

给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
进阶：
    你只能使用常量级额外空间。
	使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

思路:用队列层序遍历和116题一样

进阶:因为是不完全二叉树,需要考虑的情况比116题复杂
遍历每一层时要记录下一层的leftmost节点,pre记录前驱节点
下一层从leftmost开始遍历
*/
// connect 使用Next指针
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	leftmost := root
	for leftmost != nil {
		// current layer
		cur := leftmost
		var pre *Node

		// leftmost node in next layer
		leftmost = nil

		// iterate over current layer
		for ; cur != nil; cur = cur.Next {
			pre, leftmost = processChild(cur.Left, pre, leftmost)
			pre, leftmost = processChild(cur.Right, pre, leftmost)
		}
	}
	return root
}

// processChild return (previous, leftmost)
func processChild(node, pre, leftmost *Node) (*Node, *Node) {
	// node是空的 跳过
	if node == nil {
		return pre, leftmost
	}
	// 这里开始node 非空
	// pre是空的, 说明是第一个节点
	if pre == nil {
		// 记录leftmost
		leftmost = node
	} else {
		// 不是leftmost,pre指向node
		pre.Next = node
	}
	// pre向前走1步
	pre = node
	return pre, leftmost
}

// connectNaive 层序遍历
func connectNaive(root *Node) *Node {
	if root == nil {
		return nil
	}
	queue := make([]*Node, 1)
	queue[0] = root
	current, next := 1, 0
	var pre *Node // previous node in a certain layer
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:] // queue pop left
		if pre != nil {
			pre.Next = node // connect previous node
		}
		pre = node // pre move forward
		if node.Left != nil {
			queue = append(queue, node.Left)
			next++
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
			next++
		}
		current--
		// prepare for the next layer
		if current == 0 {
			pre = nil
			current = next
			next = 0
		}
	}

	return root
}

func main() {

}
