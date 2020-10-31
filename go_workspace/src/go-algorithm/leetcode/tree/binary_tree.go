package tree

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func BuildTree(values []int) *TreeNode {
	var root *TreeNode
	if len(values) == 0 {
		return root
	}
	root = &TreeNode{Val: values[0]}
	q := []**TreeNode{&(root.Left), &(root.Right)}
	for i := 1; i < len(values); i++ {
		tmp := q[0]
		newNode := TreeNode{Val: values[i]}
		*tmp = &newNode
		q = q[1:]
		q = append(q, &newNode.Left, &newNode.Right)
	}
	return root
}

func PrintTree(root *TreeNode) {
	if root == nil {
		return
	}
	current, next := 1, 0
	for q := []*TreeNode{root}; len(q) > 0; {
		current--
		fmt.Printf("%d ", q[0].Val)
		if q[0].Left != nil {
			q = append(q, q[0].Left)
			next++
		}
		if q[0].Right != nil {
			q = append(q, q[0].Right)
			next++
		}
		q = q[1:]
		if current == 0 {
			fmt.Println()
			current = next
			next = 0
		}
	}
}
