// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/*
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
思路:层序遍历+翻转
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	res := make([][]int, 0)
	if root == nil {
		return res
	}
	fromLeft := true
	current := 1
	next := 0
	res = append(res, []int{})
	q := make([]*TreeNode, 0)
	q = append(q, root)
	for len(q) > 0 {
		tmp := q[0]
		res[len(res)-1] = append(res[len(res)-1], tmp.Val)
		q = q[1:]
		if tmp.Left != nil {
			q = append(q, tmp.Left)
			next++
		}
		if tmp.Right != nil {
			q = append(q, tmp.Right)
			next++
		}
		current--
		if current == 0 {
			current = next
			next = 0
			if !fromLeft {
				reverse(res[len(res)-1])
			}
			res = append(res, make([]int, 0))
			fromLeft = !fromLeft
		}
	}
	return res[:len(res)-1]
}

func reverse(arr []int) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}
func main() {

}
