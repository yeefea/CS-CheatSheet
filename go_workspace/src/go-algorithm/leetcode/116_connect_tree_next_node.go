// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/*
116. 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

		1
  	 /     \
 	2		 3
  /   \    /   \
 4	   5  6     7
=>
        1 -> nil
     /     \
 	2	->	 3 -> nil
  /   \    /   \
 4 ->  5->6  -> 7 -> nil
思路:二叉树层序遍历,记录current层,next层的节点个数,用pre节点记录当前层的前一个节点
需要O(N)的空间复杂度

进阶: 用Next指针
从root开始,用当前层的Left和Right链接从左到右连接下一层的Next
此时下一层已经构造出了一个链表,可以从左到右遍历
然后进入下一层的头节点,用Next指针遍历,继续连接下一层
只需要O(1)的空间复杂度
*/
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	head := root
	for head.Left != nil {
		tmp := head
		for tmp.Next != nil {
			tmp.Left.Next = tmp.Right
			tmp.Right.Next = tmp.Next.Left
			tmp = tmp.Next
		}
		tmp.Left.Next = tmp.Right
		head = head.Left
	}
	return root
}

func connectNaive(root *Node) *Node {
	if root == nil {
		return nil
	}
	queue := make([]*Node, 1)
	queue[0] = root
	var pre *Node
	current, next := 1, 0
	for len(queue) > 0 {
		node := queue[0]
		if pre != nil {
			pre.Next = node
		}
		pre = node
		queue = queue[1:]
		if node.Left != nil {
			queue = append(queue, node.Left)
			next++
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
			next++
		}
		current--
		if current == 0 {
			current = next
			next = 0
			pre = nil
		}
	}
	return root
}

func main() {

}
